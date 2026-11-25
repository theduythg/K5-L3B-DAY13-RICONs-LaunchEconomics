# Báo cáo cá nhân — HoangTheDuyet-2A202603980

## 1. Thông tin thành viên

- Họ tên: Hoàng Thế Duyệt
- MSSV: 2A202603980
- Email: ⟨Email⟩
- GitHub: theduythg
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): cả bốn vai (nhóm RICONs chỉ có 1 thành viên)

## 2. Phần việc phụ trách

Toàn bộ năm nhiệm vụ A–E và duyệt chéo: viết và chạy `src/lab13.py`, kiểm số, gắn nhãn 20 ca lỗi (bộ nhãn 1), giữ hồ sơ launch v0, làm hội đồng chấm nhóm n + 1.

## 3. Đóng góp cụ thể

- **A · Chi phí:** ba hàm A1 (đạt 1,20 · 1,25 · 1,25); hàm `mo_hinh` tính tử số trên mọi 1.624 lần chạy, mẫu số chỉ 978 việc thành công → 4.472 đ/việc [simulated], gấp 16,3 lần hoá đơn; A3 theo loại, A4 cộng chi phí cố định cho phạm vi noi_dia + hang_nang (4.599 đ = 0,38× [simulated]).
- **B · Độ nhạy:** 9 kịch bản + 1 cặp; xếp hạng làm lại (+51,8%) · xem lại (+40,7%) · lương (+23,1%) [simulated]; B3 giới hạn 2 lần rẻ nhất cho công ty; B4 xem lại 100% → 0,98× (1,03× với phút làm lại thật) [simulated].
- **C · Lỗi:** bộ nhãn 1, so với bộ nhãn 2, bảng khắc phục 5 ca có event, ngưỡng, vai trò.
- **D · Pilot:** năm câu D1, chọn chia theo nhân viên 20 + 20 với mde 6 điểm (power 0,64 nếu tác động thật 5 điểm), ngưỡng an toàn dựa trên tỉ lệ mở lại hiện tại 3,97% trong phạm vi, 4 luật dừng.
- **E · Hồ sơ:** 5 chỉ số, 10 event có `trace_id`, 4 dòng rủi ro, hồ sơ 7 mục, đề xuất Go có điều kiện.

## 4. Bằng chứng

- `src/lab13.py` (chạy `cd src && python lab13.py`), các file trong `report/team/`.
- Commit trên nhánh `theduythg/run` của repo `theduythg/K5-L3B-DAY13-RICONs-LaunchEconomics`.

## 5. Công cụ AI đã dùng

- **Claude Code (Anthropic):** đọc đề và tài liệu trong repo, viết `src/lab13.py`, soạn bản nháp các file hồ sơ từ output của code, gắn bộ nhãn 2 cho nhiệm vụ C (có ghi lý do từng ca).
- **Cách tự kiểm tra:** chạy lại `python lab13.py` và đối chiếu từng số với số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 2%); tính tay lại một số (chi phí mỗi việc thành công = 4.373.585 ÷ 978 = 4.472 đ; câu D1e: 2,82m ≥ 841,82 → m ≥ 299); chạy `yaml.safe_load` cho `pilot_plan.yaml`, kiểm tra không còn dấu `?` và không có từ cấm; đọc lại toàn bộ hồ sơ trước khi nộp.
- Không dùng AI để tạo số không có trong output của code, và không dùng AI để gắn bộ nhãn 1 hay chấm điểm duyệt chéo.

## 6. Tự đánh giá

- Hiểu và giải thích được: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công; vì sao số cụm quyết định cỡ mẫu hiệu dụng (luôn < c ÷ ICC); vì sao đề xuất là Go có điều kiện chứ không phải Go.
- Hạn chế: nhóm 1 người nên bộ nhãn 2 của nhiệm vụ C do AI gắn; các số chi phí phụ thuộc vào phút simulated, cần thay bằng phút đo thật khi pilot chạy.
