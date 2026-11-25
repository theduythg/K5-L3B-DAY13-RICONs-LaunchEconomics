# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

`python lab13.py` in: `Ba phép thử đáp án biết trước: ĐẠT`.

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (= 1/p, vì (1 − (1 − p)^k) triệt tiêu) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` (mọi 1.624 lần chạy, kể cả lần lỗi) | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi × 15 đ) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút × 2.000 đ) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút × 2.000 đ) | simulated |
| Tổng chi phí | 4.373.585 | | simulated (có phần simulated) |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,3 lần** (4.472 ÷ 274,7) [simulated]: tử số cộng mọi lần chạy kể cả lỗi và giờ nhân viên, mẫu số chỉ 978 việc thành công.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại 51,8%** [simulated], rồi xem lại 40,7% [simulated]; giờ nhân viên cộng lại 92,5% [simulated], token chỉ 5,6%, tool 1,9%.
- Lưu ý khi so với 12.000 đ: 4.472 đ chưa tính 222 yêu cầu không thành công nhân viên phải làm thay; chi phí cả hệ thống = (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** [simulated].

## A3 · Tách theo loại yêu cầu

Chi phí mỗi việc thành công và cột "So với 12.000 đ" là số **simulated** (có tiền xem lại, làm lại).

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× [simulated] |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× [simulated] |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× [simulated] |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× [simulated] |

Tỉ lệ lần chạy `ok` theo lần thử (đo từ trace):

| Loại | Lần 1 | Lần 2 | Lần 3 |
| --- | ---: | ---: | ---: |
| noi_dia | 91,0% | 75,7% | 38,9% |
| hang_nang | 70,9% | 39,1% | 17,9% |
| quoc_te | 30,0% | 11,4% | 2,2% |
| doi_tac | 51,5% | 18,2% | 14,8% |

- Loại nào không đáng để trợ lý xử lý? **quoc_te**: thành công 27,3%, 2,32 lần chạy/yêu cầu, 22.515 đ = 1,88× nhân viên tự làm [simulated]. Chạy lại tới 3 lần **không giúp**: lần 2 chỉ đúng 11,4%, lần 3 còn 2,2%, lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ tốn thêm tiền.
- **doi_tac** sát ngưỡng (0,85× [simulated], thành công 54,4%) và có điều khoản riêng, nên cũng để ngoài phạm vi pilot. Phạm vi pilot: **noi_dia + hang_nang**.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi trong mẫu: 982 yêu cầu, 900 việc thành công, tổng 3.072.513 đ → 3.414 đ/việc [simulated]. Việc thành công mỗi tháng = 45.000 × 900 ÷ 1.200.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× [simulated] |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× [simulated] |

- Chi phí cố định có đổi kết luận không? **Không** ở quy mô đầy đủ (0,38×) hay một nửa (0,48×) [simulated]; nhưng nó tăng mạnh khi khối lượng nhỏ: hoà vốn với 12.000 đ chỉ khi có ≥ 4.659 việc thành công/tháng (≈ 14% khối lượng đầy đủ) [simulated], nên giai đoạn pilot 10% rollout sẽ lỗ nếu tính đủ 40 triệu đ.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated]. Mọi dòng dưới đây là số **simulated**.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" giảm đúng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated] = 5,6% + 40,7%, đúng bằng tổng hai tác động riêng vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại** (+51,8%) · 2. **Tỉ lệ xem lại** (+40,7%) · 3. **Lương nhân viên** (+23,1%) [simulated]. Giá token chỉ +5,6%: pilot phải theo dõi tỉ lệ làm lại và xem lại, không phải giá token.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay). Mọi số tiền là **simulated**.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- **Giới hạn 2 lần rẻ nhất cho công ty** (6.901.220 đ, rẻ hơn 3 lần 136.365 đ) [simulated]. **Không trùng** với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ): tối ưu riêng chỉ số đó đẩy thêm 85 việc sang nhân viên (319 so với 234).

## B4 · Nếu phải xem lại tất cả

Phạm vi noi_dia + hang_nang: 982 yêu cầu; 948 yêu cầu có ≥ 1 lần chạy ok × 5 phút = 9.480.000 đ; 48 ca lam_lai × 9 phút = 864.000 đ; token + tool 224.513 đ; tổng 10.568.513 đ ÷ 900 việc thành công.

- Chi phí mỗi việc thành công khi xem lại 100%: **11.743 đ = 0,98× của 12.000 đ** [simulated]. Nếu dùng phút làm lại thật của dữ liệu (TB 15,3 phút/ca, trung vị 14,5) thì **12.415 đ = 1,03×** [simulated], tức đắt hơn nhân viên tự làm.
- Pilot phải học được tỉ lệ xem lại giảm an toàn tới đâu và mỗi lần xem lại có dưới **5,1 phút** (làm lại 9 phút) hay **4,8 phút** (làm lại 15,3 phút) không, vì tiền xem lại chiếm 89,7% tổng [simulated]; xem lại 100% thì trợ lý gần như không tiết kiệm gì.
