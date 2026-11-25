# Team

## Thông tin nhóm

- Tên nhóm: RICONs
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-RICONs-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/theduythg/K5-L3B-DAY13-RICONs-LaunchEconomics · nhánh `theduythg/run` (merge vào `main` khi nộp) · ⟨commit hash sau khi push⟩

## Thành viên

Nhóm chỉ có **1 thành viên**, đảm nhận cả bốn vai.

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Hoàng Thế Duyệt | 2A202603980 | ⟨Email⟩ | theduythg | Người viết code · Người kiểm số · Người gắn nhãn 1 · Người gắn nhãn 2 kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Vì nhóm có 1 người: bộ nhãn 2 của nhiệm vụ C do trợ lý AI Claude Code gắn (ghi rõ trong `report/team/bang_loi.md`), thành viên gắn bộ nhãn 1 độc lập rồi mới so.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

## HoangTheDuyet-2A202603980

Báo cáo cá nhân: [report/team/2A202603980_HoangTheDuyet.md](report/team/2A202603980_HoangTheDuyet.md)

### Phần việc phụ trách

- Cả bốn vai: viết code, kiểm số, gắn nhãn, giữ hồ sơ; làm hội đồng chấm nhóm n + 1.

### Đóng góp cụ thể

- `src/lab13.py`: ba hàm A1, `mo_hinh`, A3, A4, B1–B4, D1, D3, E1; chạy hết, ba phép thử ĐẠT.
- `report/team/bang_chi_phi.md`: bảng A1–A4, B1–B4.
- `report/team/bang_loi.md`: bộ nhãn 1, so nhãn, quy tắc phân biệt, bảng khắc phục 5 ca.
- `report/team/pilot_plan.yaml`: D1, D2, ngưỡng an toàn, 4 luật dừng.
- `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`: chỉ số, 10 event, 4 rủi ro, hồ sơ 7 mục, đề xuất Go có điều kiện.
- `report/team/phieu_cham.md`: chấm nhóm n + 1 tại buổi duyệt chéo.

### Bằng chứng

- Output `cd src && python lab13.py` (ba phép thử ĐẠT; chi phí mỗi việc thành công 4.472 đ [simulated]).
- `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` chạy không lỗi.
- Commit trên nhánh `theduythg/run` của repo nhóm.
