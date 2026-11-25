# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: RICONs
- Lớp: L3B
- Thành viên: xem `TEAM.md` (nhóm 1 thành viên, đảm nhận cả bốn vai)

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a duyệt kế hoạch pilot, trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào. Mọi con số do `src/lab13.py` tính từ hai file CSV; số đi từ cột `_simulated` ghi nhãn `simulated`. Nhiệm vụ sau dùng lại số của nhiệm vụ trước (A3 → phạm vi pilot, B → luật dừng và rủi ro, D3 → ngưỡng an toàn).

## 3. Giải pháp

- **A · Chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): ba hàm A1 theo công thức hình học; `mo_hinh` cộng token + tool của mọi 1.624 lần chạy (kể cả lỗi) và phút xem lại, làm lại, chia cho số việc `thanh_cong`; gọi lại theo `loai` (A3) và cộng chi phí cố định cho phạm vi (A4).
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): 9 kịch bản một yếu tố, 1 kịch bản một cặp, giới hạn 1–3 lần chạy với chi phí cả hệ thống, xem lại 100% cho noi_dia + hang_nang.
- **C · Lỗi** ([bang_loi.md](bang_loi.md)): gắn 20 ca theo 5 loại PAIR theo nguyên nhân gốc; bảng khắc phục 5 ca có event, ngưỡng, vai trò.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính 5 câu D1 trước, rồi chọn chia theo nhân viên 20 + 20 với mde 6 điểm; đặt ngưỡng an toàn sau khi tính tỉ lệ mở lại hiện tại.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): 3 chỉ số tính thử + 2 chỉ số tự đề xuất, 10 event có `trace_id`, 4 dòng rủi ro kinh tế, hồ sơ 7 mục.

## 4. Kết quả

- Ba phép thử A1: ĐẠT (1,20 · 1,25 · 1,25).
- Chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5% [simulated].
- Theo loại: noi_dia 0,22×, hang_nang 0,69×, quoc_te 1,88×, doi_tac 0,85× của 12.000 đ [simulated]; quoc_te chạy lại không giúp (lần 2 đúng 11,4%, lần 3 đúng 2,2%).
- Yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương (+23,1%) [simulated]. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ) [simulated].
- Xem lại 100%: 11.743 đ = 0,98× (hoặc 1,03× với phút làm lại thật) [simulated].
- D1: 1.251 · 3.103 (42 người/nhóm, không đủ) · tối đa 1.000 · tối đa 300 · m ≥ 299. Power 0,64 nếu tác động thật 5 điểm.
- Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 4,25%.
- **Đề xuất: Go có điều kiện** cho pilot noi_dia + hang_nang (điều kiện, người phụ trách, ngày kiểm tra trong `ho_so_launch_v0.md`).
- Kết quả duyệt chéo nhóm nhận được: ⟨ghi sau buổi duyệt chéo⟩.

## 5. Khó khăn và cách xử lý

- **Nhóm chỉ có 1 thành viên** trong khi lab thiết kế cho 4 vai. Một người đảm nhận cả bốn vai; dùng Claude Code làm trợ lý viết code và kiểm số (ghi rõ trong báo cáo cá nhân).
- **Nhiệm vụ C cần hai người gắn nhãn độc lập:** bộ nhãn 2 do Claude Code gắn theo định nghĩa PAIR, có lý do từng ca; bộ nhãn 1 do thành viên tự gắn mà không xem bộ nhãn 2, rồi mới so. Ghi rõ trong `bang_loi.md`.
- **Duyệt chéo:** phiếu chấm điền tại buổi dựa trên hồ sơ nhóm khác; không điền trước.
- **Môi trường Windows:** tạo venv bằng `python -m venv .venv` trong `src/`; thêm `sys.stdout.reconfigure(encoding='utf-8')` để in được tiếng Việt khi chuyển hướng output.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Chi phí xem lại, làm lại là phút **simulated**; phải thay bằng phút đo thật từ event `staff_review_decision`, `staff_rework_completed` sau tuần đầu pilot.
- Baseline 0,70 và ICC 0,02 là số đề cho; nên ước lượng lại ICC từ tỉ lệ thành công theo staff_id khi có dữ liệu pilot.
- Pilot chỉ đủ power cho mức chênh 6 điểm; muốn thấy 5 điểm cần thêm nhân viên hoặc kéo dài thời gian (số cụm quyết định, không phải tổng số yêu cầu).
- Chi phí cố định chiếm phần lớn khi khối lượng nhỏ (hoà vốn ≥ 4.659 việc thành công/tháng [simulated]); bước rollout 10% sẽ lỗ nếu tính đủ 40 triệu đ.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu statsmodels, lớp `NormalIndPower`.
- Tài liệu lab trong `docs/` (đề bài, hướng dẫn chi tiết, dữ liệu và công thức).
