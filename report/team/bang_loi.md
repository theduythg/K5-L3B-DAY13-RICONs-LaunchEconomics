# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Nhóm RICONs chỉ có 1 thành viên, nên hai bộ nhãn được làm như sau (ghi rõ để minh bạch theo `RULES.md`):

- **Người gắn nhãn 1:** thành viên của nhóm, tự gắn cả 20 ca trong 8 phút, **không xem** cột người 2 và không xem nhãn tham khảo trong `docs/`.
- **Người gắn nhãn 2:** Claude Code (trợ lý AI), gắn độc lập theo bảng định nghĩa PAIR của đề, có ghi lý do từng ca ở cột cuối.

Sau khi so, không sửa hai cột nhãn độc lập; chỉ điền cột "Nhãn thống nhất".

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất | Lý do của người 2 (nguyên nhân gốc) |
| --: | --- | --- | --- | --- | --- |
| 1 | ⟨chờ điền⟩ | Do người dùng | | | Khách nhập số tài khoản thiếu 2 chữ số |
| 2 | ⟨chờ điền⟩ | Hệ thống | | | Trợ lý gọi tool sai tham số (hàng thường thay hàng nặng), sai chính sách, khách đã thấy và mở lại |
| 3 | ⟨chờ điền⟩ | Ngữ cảnh | | | Hoàn về ví đúng thiết kế; giả định "khách dùng ví" không khớp kỳ vọng của khách |
| 4 | ⟨chờ điền⟩ | Giới hạn hệ thống | | | Không có dữ liệu chặng hãng nước ngoài, không thể trả lời dù cố gắng |
| 5 | ⟨chờ điền⟩ | Ngầm | | | Hoàn thừa 14 đơn, không khách nào báo, không cảnh báo nào; chỉ lộ qua kiểm tra mẫu |
| 6 | ⟨chờ điền⟩ | Do người dùng | | | Khách chọn sai mục "giao trễ" cho hàng vỡ; việc trợ lý không đối chiếu mô tả là chỗ cần sửa, không phải gốc |
| 7 | ⟨chờ điền⟩ | Hệ thống | | | Báo "đã hoàn" khi sổ cái trả 503, vi phạm thiết kế |
| 8 | ⟨chờ điền⟩ | Hệ thống | | | Trích điều 7.2 không tồn tại; sai nhìn thấy được trong câu trả lời nên không phải ngầm |
| 9 | ⟨chờ điền⟩ | Do người dùng | | | Khách nhập mã đơn sàn TMĐT thay vì mã vận đơn |
| 10 | ⟨chờ điền⟩ | Ngữ cảnh | | | Từ chối đúng chính sách bất khả kháng; khách thấy vô lý vì app hiện "cam kết 24 giờ" |
| 11 | ⟨chờ điền⟩ | Giới hạn hệ thống | | | Không xử lý được tin nhắn thoại (dạng đầu vào không hỗ trợ) |
| 12 | ⟨chờ điền⟩ | Ngầm | | | Kết quả đúng nhưng chi phí token D05 gấp 3 lần suốt 3 tuần, không ai thấy |
| 13 | ⟨chờ điền⟩ | Giới hạn hệ thống | | | Phí bảo hiểm của đối tác nằm ngoài phạm vi; xử lý giới hạn kém là chỗ cần sửa |
| 14 | ⟨chờ điền⟩ | Do người dùng | | | Khách bấm nhầm "Xác nhận đã nhận tiền" |
| 15 | ⟨chờ điền⟩ | Hệ thống | | | Tính 100% thay vì 50% theo chính sách; nhân viên bắt được nên không ngầm |
| 16 | ⟨chờ điền⟩ | Ngữ cảnh | | | Gửi lúc 2:14 sáng đúng thiết kế "gửi ngay", không khớp hoàn cảnh khách |
| 17 | ⟨chờ điền⟩ | Ngầm | | | Dùng bảng giá cũ trong bộ nhớ đệm, lệch 212 đơn trong 9 ngày, không ai mở lại |
| 18 | ⟨chờ điền⟩ | Ngữ cảnh | | | Số tiền đúng; giả định "khách hiểu cách tính" không khớp nên khách mở lại |
| 19 | ⟨chờ điền⟩ | Giới hạn hệ thống | | | Chỉ truy cập được 12 tháng dữ liệu, đơn 14 tháng trước |
| 20 | ⟨chờ điền⟩ | Hệ thống | | | Hoàn hai lần vì lệnh thứ hai thiếu khoá chống trùng, sai thiết kế |

Bộ nhãn người 2 theo loại: Do người dùng 1, 6, 9, 14 (4) · Hệ thống 2, 7, 8, 15, 20 (5) · Ngữ cảnh 3, 10, 16, 18 (4) · Giới hạn hệ thống 4, 11, 13, 19 (4) · Ngầm 5, 12, 17 (3).

**Tỉ lệ đồng thuận:** ⟨số ca trùng⟩ / 20 = ⟨…⟩% (điền sau khi so; cần ≥ 16/20 = 80%)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu (điền sau khi so). Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ⟨điền sau khi so nhãn⟩

Quy tắc nhóm dùng cho các ca dễ lẫn (viết trước khi so, để thống nhất):

- **Người dùng hay hệ thống (ca 6, 9):** đầu vào của khách sai thì là do người dùng; việc trợ lý không gợi ý chỉ là chỗ cần cải thiện, ghi ở cột khắc phục.
- **Giới hạn (ca 13):** ngoài phạm vi thì là giới hạn hệ thống, kể cả khi trợ lý xử lý giới hạn đó kém.
- **Hệ thống hay ngầm (ca 8, 15):** sai đã lộ ra (khách hoặc nhân viên thấy) là hệ thống; ngầm chỉ khi không ai nhận ra cho tới lúc kiểm tra.
- **Ngữ cảnh (ca 18):** kết quả đúng chính sách, chỉ giả định về khách không khớp.
- **Ngầm về chi phí (ca 12):** "sai" có thể là sai chi phí, không chỉ sai câu trả lời.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội". Tên event khớp danh sách trong `chi_so.md`.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_ledger_write` có `ket_qua = bank_rejected_invalid_account` (kèm `trace_id`); đếm mỗi ngày, cảnh báo khi > 1% số lệnh hoàn trong ngày | Kiểm tra độ dài và tra tên chủ tài khoản trước khi tạo lệnh hoàn; hiện tên chủ tài khoản để khách xác nhận lại | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ: số `refund_ledger_write` có cùng `request_id` và mã đơn > 1; ngưỡng 0 ca, có 1 ca là báo động | Khoá chống trùng (idempotency key = mã đơn + loại hoàn) ở dịch vụ sổ cái; lệnh trùng trả lại kết quả lệnh đầu | Kỹ sư trưởng agent |
| 3 | Ngữ cảnh | Event `ticket_reopened` với `reason = chua_nhan_tien` trong khi sổ cái đã ghi `ok` vào ví; tính tỉ lệ theo tuần, cảnh báo khi > 0,5% số yêu cầu đã hoàn | Hỏi khách chọn nơi nhận (ví hoặc ngân hàng) trước khi hoàn; tin nhắn ghi rõ "đã hoàn về ví LogiX, xem tại…" | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = dau_vao_khong_ho_tro` (loại `audio`); đếm theo ngày, xem lại khi > 2% số yêu cầu | Nói rõ giới hạn và chuyển nhân viên kèm tóm tắt ngay, không bắt khách gõ lại; xét thêm chuyển giọng nói sang chữ ở bản sau | PM trợ lý hoàn phí |
| 12 | Ngầm | Từ `agent_run_completed`: chi phí token + tool mỗi việc thành công theo depot, tính hằng ngày; cảnh báo khi một depot > 1,5 lần trung vị các depot 2 ngày liên tiếp | Kiểm tra lược đồ kết quả tool, thiếu trường thì báo lỗi ngay thay vì gọi lại; sửa tool tra đơn D05 | Kỹ sư trưởng agent |
