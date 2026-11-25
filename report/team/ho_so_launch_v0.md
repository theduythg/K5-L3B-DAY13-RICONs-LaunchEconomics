# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: RICONs · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ toàn mẫu [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); trong phạm vi noi_dia + hang_nang 3.414 đ, cộng cố định 40 triệu đ/tháng thành 4.599 đ ở 45.000 yêu cầu/tháng [simulated]. Làm lại chiếm 51,8%, xem lại 40,7% tổng chi phí [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại ×2: +51,8% · 2. Tỉ lệ xem lại ×2: +40,7% · 3. Lương +25%: +23,1% [simulated]; giá token ×2 chỉ +5,6%. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ cho 1.200 yêu cầu) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Theo loại: noi_dia 0,22×, hang_nang 0,69×, quoc_te 1,88×, doi_tac 0,85× của 12.000 đ [simulated] → phạm vi pilot chỉ noi_dia + hang_nang (0,38× khi cộng cố định). Bất lợi: xem lại 100% thì 11.743 đ = 0,98×, hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử (không đối chứng): chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200); trong phạm vi 92,26% · 21,09% · 3,97%. 10 event có trace_id, mọi chỉ số tính được từ event | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | 20 ca gắn 5 loại (người 2: người dùng 4, hệ thống 5, ngữ cảnh 4, giới hạn 4, ngầm 3); 5 dòng khắc phục có event, ngưỡng, vai trò. Nghiêm trọng nhất: ca 7 (báo "đã hoàn" khi sổ cái lỗi 503) và ca 20 (hoàn trùng, ngưỡng 0 ca). Đồng thuận hai bộ nhãn: chờ bộ nhãn người 1 | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot; mde 6 điểm, 859 mỗi nhóm, DE 6,96, ≥ 299 yêu cầu/nhân viên. Bất lợi: không cách chia nào đủ mẫu cho 5 điểm (tối đa 1.000 < 1.251), power chỉ 0,64 nếu tác động thật là 5 điểm. 4 luật dừng; trần mở lại 6% hoặc +2 điểm so với đối chứng (hiện 3,97%); quyết định 2027-01-11 | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2 → 6.787 đ (+51,8%); xem lại 100% kéo dài → 0,98–1,03×; khối lượng còn một nửa → +2.370 đ/việc, hoà vốn ≥ 4.659 việc thành công/tháng [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chỉ noi_dia + hang_nang, 40 nhân viên, chia 20 + 20 (không phải mọi yêu cầu: quoc_te 1,88× và doi_tac 0,85× [simulated] để ngoài).

- Sửa khoá chống trùng và đối soát sổ cái mỗi giờ (ca 7, 20), kiểm thử lại đạt 0 ca trùng · Kỹ sư trưởng agent · kiểm tra 2026-12-04.
- Ký chấp nhận mức chênh 6 điểm, biết power chỉ 0,64 nếu tác động thật là 5 điểm · Giám đốc vận hành LogiX-VN · kiểm tra 2026-12-04.
- Bật đủ 10 event có trace_id; thay phút xem lại, làm lại simulated bằng phút đo thật sau tuần đầu và tính lại mục 1–3 · PM trợ lý hoàn phí · kiểm tra 2026-12-14.
- Kế hoạch giảm xem lại theo bậc (100% → 50% → 20% khi sua + bo < 15%), vì xem lại 100% thì 0,98–1,03× không tiết kiệm; phút xem lại trung bình phải ≤ 5 phút · Trưởng nhóm CSKH · kiểm tra 2026-12-21 (trước bước 0.50).
- Hoàn tất so hai bộ nhãn độc lập của nhiệm vụ C, đồng thuận ≥ 16/20 · Người gắn nhãn 1 · kiểm tra trước khi nộp hồ sơ.
