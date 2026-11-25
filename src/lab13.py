"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.

Nhóm RICONs · L3B. Mọi số tính từ cột *_simulated được in kèm nhãn [simulated].
"""
import math
import sys
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)

CHI_PHI_CO_DINH = 40_000_000   # đồng / tháng
YEU_CAU_THANG = 45_000         # yêu cầu hoàn phí / tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']   # phạm vi pilot chọn từ A3
SIM = '[simulated]'


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p                      # kỳ vọng của phân phối hình học
    return (1 - (1 - p) ** k) / p         # tổng P(cần lần thứ i) = sum (1-p)^(i-1), i = 1..k


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]   # chỉ lấy lần chạy của các yêu cầu đang xét
    if max_lan_chay is not None:
        # Bỏ lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn giới hạn → chuyển nhân viên, phút xem lại/làm lại = 0
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai     # tử số: MỌI lần chạy
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())        # mẫu số: chỉ việc thành công
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
                so_yc=len(reqs), so_lan_chay=len(runs))


# ---------- Nhiệm vụ D · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (z chính xác, làm tròn lên)."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc):
    return 1 + (m - 1) * icc


def tieu_de(s):
    print('\n' + '=' * 78 + f'\n{s}\n' + '=' * 78)


if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8')   # Windows: in được tiếng Việt khi chuyển hướng output
    except AttributeError:
        pass
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    # ===================== A1 =====================
    tieu_de('A1 · Ba phép thử đáp án biết trước (p = 0,8)')
    kiem_tra_dap_an_biet_truoc()
    print(f'  Tối đa 2 lần, số lần chạy TB      : {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  Chạy đến khi đúng, số lần chạy TB  : {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  Hệ số chi phí/việc TC, tối đa 3 lần: {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    # ===================== A2 =====================
    tieu_de('A2 · Mô hình chi phí từ trace (toàn bộ 1.200 yêu cầu)')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    g = ket_qua
    n_tool = int(runs['tool_calls'].sum())
    phut_xl = int(reqs['phut_xem_lai_simulated'].sum())
    phut_ll = int(reqs['phut_lam_lai_simulated'].sum())
    print(f'\n  Số lần gọi tool: {n_tool:,} · phút xem lại: {phut_xl:,} {SIM} · phút làm lại: {phut_ll:,} {SIM}')
    print(f'  Chi phí mỗi việc TC / hoá đơn mỗi yêu cầu = {g["cps"]:,.0f} / {g["hoa_don_moi_yc"]:,.1f}'
          f' = {g["cps"] / g["hoa_don_moi_yc"]:.1f} lần {SIM}')
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  Tỉ trọng {k:8s}: {g[k] / g["tong"] * 100:5.1f}%' + (f' {SIM}' if k in ('xem_lai', 'lam_lai') else ''))
    print(f'  Giờ nhân viên (xem lại + làm lại) chiếm {(g["xem_lai"] + g["lam_lai"]) / g["tong"] * 100:.1f}% tổng {SIM}')
    khong_tc = g['so_yc'] - g['thanh_cong']
    he_thong_moi_yc = (g['tong'] + khong_tc * BASELINE) / g['so_yc']
    print(f'  Chi phí cả hệ thống mỗi yêu cầu (cộng {khong_tc} ca không TC × 12.000 đ): '
          f'{he_thong_moi_yc:,.0f} đ = {he_thong_moi_yc / BASELINE:.2f}× của 12.000 đ {SIM}')

    # ===================== A3 =====================
    tieu_de('A3 · Tách theo loại yêu cầu')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_TC":>9s} {"lan/yc":>7s} {"cps [sim]":>10s} {"so_12k":>7s}')
    a3 = {}
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        k = mo_hinh(runs, sub)
        a3[loai] = k
        print(f'{loai:10s} {k["so_yc"]:6d} {k["thanh_cong"] / k["so_yc"] * 100:8.1f}% '
              f'{k["so_lan_chay"] / k["so_yc"]:7.2f} {k["cps"]:10,.0f} {k["cps"] / BASELINE:6.2f}×')
    print('\n  Tỉ lệ lần chạy ok theo loại và theo lần thử (chạy lại có giúp không?):')
    ok_theo_lan = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                   .assign(ok=lambda d: (d['status'] == 'ok').astype(float))
                   .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    so_lan_theo = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                   .pivot_table(index='loai', columns='attempt', values='run_id', aggfunc='count'))
    print((ok_theo_lan * 100).round(1).to_string())
    print('  Số lần chạy theo lần thử:')
    print(so_lan_theo.to_string())

    # ===================== A4 =====================
    tieu_de('A4 · Chi phí cố định, phạm vi noi_dia + hang_nang')
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    k_pv = mo_hinh(runs, pv)
    print(f'  Phạm vi: {k_pv["so_yc"]} yêu cầu, {k_pv["thanh_cong"]} việc TC, tổng {k_pv["tong"]:,.0f} đ, '
          f'cps {k_pv["cps"]:,.0f} đ {SIM}')
    for ten, he_so in [('45.000 yc/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        tc_thang = YEU_CAU_THANG * he_so * k_pv['thanh_cong'] / len(reqs)
        cd = CHI_PHI_CO_DINH / tc_thang
        tong_cd = k_pv['cps'] + cd
        print(f'  {ten:20s}: việc TC/tháng {tc_thang:9,.0f} · cố định/việc {cd:6,.0f} đ · '
              f'cps + cố định {tong_cd:6,.0f} đ = {tong_cd / BASELINE:.2f}× {SIM}')
    # Hoà vốn khối lượng: cps + cố định = 12.000 đ
    tc_hoa_von = CHI_PHI_CO_DINH / (BASELINE - k_pv['cps'])
    print(f'  Hoà vốn so với 12.000 đ khi việc TC/tháng ≥ {tc_hoa_von:,.0f} '
          f'(≈ {tc_hoa_von / (YEU_CAU_THANG * k_pv["thanh_cong"] / len(reqs)) * 100:.0f}% khối lượng đầy đủ) {SIM}')

    # ===================== B1 =====================
    tieu_de('B1 · Đổi từng yếu tố (toàn bộ 1.200 yêu cầu)')
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    print(f'{"Gốc (A2)":28s} {goc:8,.0f} đ {SIM}')
    b1 = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        b1[ten] = (cps / goc - 1) * 100
        print(f'{ten:28s} {cps:8,.0f} đ {b1[ten]:+6.1f}% {SIM}')

    # ===================== B2 =====================
    tieu_de('B2 · Đổi một cặp và xếp hạng')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'  Giá token ×2 + xem lại ×2: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%) '
          f'= tổng hai tác động riêng {b1["Giá token gấp đôi"] + b1["Tỉ lệ xem lại gấp đôi"]:+.1f}% {SIM}')
    yeu_to = {'Số ca làm lại (×2)': b1['Số ca làm lại gấp đôi'],
              'Tỉ lệ xem lại (×2)': b1['Tỉ lệ xem lại gấp đôi'],
              'Lương nhân viên (+25%)': b1['Lương nhân viên tăng 25%'],
              'Giá token (×2)': b1['Giá token gấp đôi'],
              'Giới hạn số lần chạy (1 lần)': abs(b1['Chỉ cho chạy 1 lần'])}
    for i, (ten, v) in enumerate(sorted(yeu_to.items(), key=lambda x: -abs(x[1])), 1):
        print(f'  {i}. {ten:30s} |thay đổi| {abs(v):5.1f}%')

    # ===================== B3 =====================
    tieu_de('B3 · Giới hạn chạy lại: chi phí cả hệ thống cho 1.200 yêu cầu')
    print(f'{"gioi_han":>8s} {"tong_tro_ly":>13s} {"khong_TC":>9s} {"ca_he_thong":>13s} {"cps":>7s}')
    for gh in [1, 2, 3]:
        k = mo_hinh(runs, reqs, max_lan_chay=gh)
        khong = k['so_yc'] - k['thanh_cong']
        print(f'{gh:8d} {k["tong"]:13,.0f} {khong:9d} {k["tong"] + khong * BASELINE:13,.0f} {k["cps"]:7,.0f} {SIM}')

    # ===================== B4 =====================
    tieu_de('B4 · Xem lại 100% trong phạm vi noi_dia + hang_nang')
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    token_tool_pv = (runs_pv['tokens_in'] / 1000 * GIA_VAO + runs_pv['tokens_out'] / 1000 * GIA_RA
                     + runs_pv['tool_calls'] * GIA_TOOL).sum()
    tc_pv = int((pv['ket_qua'] == 'thanh_cong').sum())
    phut_ll_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    print(f'  Yêu cầu có ≥1 lần chạy ok: {co_ok} · ca lam_lai: {so_lam_lai} · token+tool: {token_tool_pv:,.0f} đ · việc TC: {tc_pv}')
    print(f'  Phút làm lại TB trên ca lam_lai (toàn mẫu): {phut_ll_tb.mean():.1f} (trung vị {phut_ll_tb.median():.1f}) {SIM}')
    for nhan, phut_ll_ca in [('làm lại 9 phút (đề cho)', 9), ('làm lại theo dữ liệu', phut_ll_tb.mean())]:
        xl = co_ok * 5 * LUONG_PHUT
        ll = so_lam_lai * phut_ll_ca * LUONG_PHUT
        tong = token_tool_pv + xl + ll
        hoa_von = (BASELINE * tc_pv - token_tool_pv - ll) / (co_ok * LUONG_PHUT)
        print(f'  {nhan:26s}: xem lại {xl:,.0f} + làm lại {ll:,.0f} → tổng {tong:,.0f} đ → '
              f'{tong / tc_pv:,.0f} đ/việc = {tong / tc_pv / BASELINE:.2f}× · hoà vốn khi xem lại ≤ {hoa_von:.1f} phút {SIM}')
    print(f'  Tiền xem lại chiếm {co_ok * 5 * LUONG_PHUT / (token_tool_pv + co_ok * 5 * LUONG_PHUT + so_lam_lai * 9 * LUONG_PHUT) * 100:.1f}% tổng (với 9 phút làm lại) {SIM}')

    # ===================== D1 =====================
    tieu_de('D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02)')
    ICC = 0.02
    n_a = co_mau(0.70, 0.75)
    de_b = he_so_thiet_ke(75, ICC)
    n_b = math.ceil(n_a * de_b)
    nv_b = math.ceil(n_b / 75)
    n_6 = co_mau(0.70, 0.76)
    # e: 20·m / (1 + (m−1)·ICC) ≥ n_6  →  m ≥ n_6·(1 − ICC) / (20 − n_6·ICC)
    m_e = math.ceil(n_6 * (1 - ICC) / (20 - n_6 * ICC))
    print(f'  a) Theo yêu cầu: {n_a:,} yêu cầu mỗi nhóm')
    print(f'  b) Theo nhân viên, m = 75: DE = {de_b:.2f}; n = {n_b:,} mỗi nhóm → {nv_b} nhân viên/nhóm, '
          f'tổng {2 * nv_b} > 40: KHÔNG đủ người')
    print(f'  c) 20 nhân viên/nhóm: cỡ mẫu hiệu dụng tối đa < c/ICC = {20 / ICC:,.0f} < {n_a:,}: KHÔNG đạt')
    print(f'  d) 6 depot/nhóm: cỡ mẫu hiệu dụng tối đa < {6 / ICC:,.0f}')
    print(f'  e) Mức chênh 6 điểm: {n_6} mỗi nhóm; 20 nhân viên/nhóm → m ≥ {m_e} yêu cầu/người '
          f'(DE = {he_so_thiet_ke(m_e, ICC):.2f}; n hiệu dụng = {20 * m_e / he_so_thiet_ke(m_e, ICC):.1f})')
    try:
        from statsmodels.stats.proportion import proportion_effectsize
        from statsmodels.stats.power import NormalIndPower
        h5 = proportion_effectsize(0.75, 0.70)
        print(f'  statsmodels kiểm tra câu a: {NormalIndPower().solve_power(h5, alpha=0.05, power=0.8):,.0f} '
              f'(arcsine, gần với {n_a:,})')
        pw = NormalIndPower().power(h5, nobs1=n_6, alpha=0.05)
        print(f'  Nếu tác động thật chỉ 5 điểm mà n hiệu dụng = {n_6}: power ≈ {pw:.2f} (con số bất lợi)')
    except ImportError:
        print('  (thiếu statsmodels: bỏ qua phần kiểm tra power)')
    # Khối lượng thực tế mỗi nhân viên trong phạm vi pilot
    ti_le_pv = len(pv) / len(reqs)
    yc_nv_ngay = YEU_CAU_THANG / 22 / 40 * ti_le_pv
    print(f'  Phạm vi noi_dia + hang_nang = {ti_le_pv * 100:.1f}% yêu cầu → ≈ {yc_nv_ngay:.0f} yc/nhân viên/ngày làm việc '
          f'→ {m_e} yc mất ≈ {m_e / yc_nv_ngay:.0f} ngày làm việc')

    # ===================== D3 · tỉ lệ mở lại hiện tại =====================
    tieu_de('D3 · Tỉ lệ mo_lai_trong_7_ngay hiện tại (trước khi đặt luật an toàn)')
    print(f'  Toàn mẫu: {reqs["mo_lai_trong_7_ngay"].mean() * 100:.2f}% '
          f'({reqs["mo_lai_trong_7_ngay"].sum()}/{len(reqs)})')
    print(f'  Phạm vi noi_dia + hang_nang: {pv["mo_lai_trong_7_ngay"].mean() * 100:.2f}% '
          f'({pv["mo_lai_trong_7_ngay"].sum()}/{len(pv)})')
    theo_nv = reqs.groupby('staff_id')['mo_lai_trong_7_ngay'].mean() * 100
    print(f'  Theo nhân viên: thấp nhất {theo_nv.min():.1f}%, cao nhất {theo_nv.max():.1f}%, '
          f'{(theo_nv > 3).sum()}/{len(theo_nv)} nhân viên đã trên 3%')
    print('  → ngưỡng tuyệt đối 3% sẽ dừng pilot ngay tuần đầu; dùng so với đối chứng (+2 điểm) kèm trần 6%')

    # ===================== E1 · chỉ số =====================
    tieu_de('E1 · Ba chỉ số tính thử (đợt chạy thử, không có đối chứng)')
    for ten_pv, d in [('Toàn mẫu 1.200', reqs), ('Phạm vi noi_dia + hang_nang', pv)]:
        chinh = ((d['dong_trong_24h'] == 1) & (d['mo_lai_trong_7_ngay'] == 0))
        xem = d[d['duoc_xem_lai'] == 1]
        bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
        an_toan = d['mo_lai_trong_7_ngay'] == 1
        print(f'  {ten_pv}:')
        print(f'    Chính  : {chinh.mean() * 100:.2f}% ({chinh.sum()}/{len(d)})')
        print(f'    Dùng   : {bo_qua.mean() * 100:.2f}% ({bo_qua.sum()}/{len(xem)}) bỏ qua gợi ý (sua + bo)')
        print(f'    An toàn: {an_toan.mean() * 100:.2f}% ({an_toan.sum()}/{len(d)}) mở lại trong 7 ngày')
        print(f'    Tỉ lệ được xem lại: {len(xem) / len(d) * 100:.1f}% · tỉ lệ lam_lai: '
              f'{(d["ket_qua"] == "lam_lai").mean() * 100:.1f}% · chuyen_nhan_vien: '
              f'{(d["ket_qua"] == "chuyen_nhan_vien").mean() * 100:.1f}%')
