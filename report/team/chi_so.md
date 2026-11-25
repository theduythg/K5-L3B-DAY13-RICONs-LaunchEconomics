# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py` (mục E1, D3). Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200); trong phạm vi noi_dia + hang_nang 92,26% (906/982) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177); trong phạm vi 21,09% (27/128) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); trong phạm vi 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: **tỉ lệ yêu cầu của nhóm trợ lý được mở bằng trợ lý** | Số `refund_request_created` của nhân viên nhóm trợ lý có ít nhất một `agent_suggestion_shown` cùng `trace_id`, chia tổng số yêu cầu của nhóm trợ lý; tính theo tuần, theo staff_id | Không cần tính |
| An toàn | Nhóm tự đề xuất: **tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu** (bắt lỗi ngầm như ca 5, 17) | Số đơn trong mẫu 100 đơn/tuần có `so_tien_da_hoan` khác `so_tien_dung` (event `audit_sample_checked`), chia 100 | Không cần tính |

Đây là **chỉ số trong đợt chạy thử là 82,83%**, không phải tác động của trợ lý: đợt chạy thử không có nhóm đối chứng, nên chưa thể so với baseline 0,70. Pilot mới trả lời câu đó.

## Danh sách event

Mười event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, staff_id, arm (tro_ly / doi_chung), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status (ok / loi), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu / sua / bo), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua (ok / loi / bank_rejected_invalid_account), trace_id | Khi ghi lệnh hoàn |
| `handoff_to_staff` | Agent | reason (thieu_du_lieu / ngoai_pham_vi / dau_vao_khong_ho_tro / het_lan_chay), tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, created_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính:** `ticket_closed` (closed_at − created_at ≤ 24 giờ) và không có `ticket_reopened` trong 7 ngày, chia số `refund_request_created`, tách theo `arm`. Đo được.
- **Dùng (bỏ qua gợi ý):** `staff_review_decision` có quyet_dinh là sua hoặc bo, chia tổng số `staff_review_decision`. Đo được.
- **An toàn (mở lại):** số `ticket_reopened` trong 7 ngày sau `ticket_closed`, chia số `refund_request_created`. Đo được.
- **Dùng (tự đề xuất):** `agent_suggestion_shown` nối `refund_request_created` qua `trace_id`, lọc arm = tro_ly. Đo được.
- **An toàn (tự đề xuất):** `audit_sample_checked`. Đo được.
- **Chi phí mỗi việc thành công (luật dừng chi phí):** `agent_run_completed` (token, tool, mọi lần chạy) + `staff_review_decision.phut_xem_lai` + `staff_rework_completed.phut_lam_lai`, chia số việc thành công. Đo được; thay số phút simulated bằng phút đo thật từ tuần 1.
- **Hoàn trùng (luật dừng an toàn):** đếm `refund_ledger_write` ok theo idempotency_key / mã đơn. Đo được.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy (`bang_chi_phi.md`). Mọi tác động là số **simulated**.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công từ 4.472 đ lên 6.787 đ [simulated] (yếu tố nhạy nhất) | Tỉ lệ `staff_rework_completed` trên số yêu cầu theo tuần > 7% (đợt chạy thử 4,9% trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất trong 2 ngày | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× với làm lại 9 phút; 12.415 đ = 1,03× với làm lại 15,3 phút như dữ liệu [simulated]; xem lại gấp đôi đã +40,7% | % yêu cầu được xem lại còn > 50% cuối bước 0.25, hoặc phút xem lại trung bình > 5 phút (hoà vốn 5,1 / 4,8 phút) | Giảm xem lại theo bậc (100% → 50% → 20%) khi tỉ lệ sua + bo < 15% trong 1 tuần | Trưởng nhóm CSKH |
| Lương nhân viên tăng 25% | +23,1%, lên 5.506 đ [simulated] | Đơn giá phút nhân viên trong kỳ điều chỉnh lương | Tính lại mô hình, ưu tiên giảm phút xem lại hơn giảm token | PM trợ lý hoàn phí |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng (4.599 đ = 0,38×), +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×); hoà vốn khi ≥ 4.659 việc thành công/tháng [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | Giám đốc vận hành LogiX-VN |
