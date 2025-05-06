# 📄 Báo cáo Bài tập Data Engineering – Exercise 4

## 1. Thông tin nhóm
- Họ tên: Hoàng Trọng Nghĩa, Nguyễn Bá Đức
- MSSV: 23630761, 23732881
- Lớp: DHKHDL19A 
- **Bài:** Exercise 4 – Chuyển đổi dữ liệu JSON thành CSV trong thư mục lồng nhau

---

## 2. Mục tiêu bài tập
- Tìm và xử lý tất cả các file `.json` trong thư mục `data/` và các thư mục con.
- Làm phẳng cấu trúc dữ liệu JSON lồng nhau.
- Ghi lại kết quả dưới dạng `.csv` với cùng tên và vị trí như file gốc.

---

## 3. Công nghệ sử dụng
- 🐍 Python 3
- 📦 Thư viện: `json`, `csv`, `glob`, `os`
- 🐳 Docker, docker-compose

---

## 4. Nội dung thực hiện

- Sử dụng `glob.glob('data/**/*.json', recursive=True)` để tìm các file JSON.
- Đọc từng file JSON bằng `json.load()`.
- Làm phẳng cấu trúc lồng nhau bằng hàm `flatten_json()`.
- Ghi dữ liệu sang `.csv` tương ứng.
- File `.csv` được lưu cùng thư mục và tên gốc như `.json`.

---

## 5. Kết quả đạt được
- ✅ Đã xử lý thành công các file sau:
  - `data/file-1.json`
  - `data/enough_already/file-4.json`
  - `data/other_folder/file-3.json`
  - `data/some_folder/other_folder/file-2.json`
- ✅ Đã tạo đúng các file CSV tại vị trí tương ứng.
- ✅ Chạy không lỗi bằng Docker (`exit code 0`).

---

## 6. Nhận xét & Hướng mở rộng
- Script xử lý hiệu quả cả thư mục lồng nhau phức tạp.
- Có thể mở rộng:
  - Ghi log lỗi nếu file sai định dạng.
  - Lưu tất cả `.csv` ra thư mục `/output` để quản lý tập trung.
  - Dùng đa luồng để tăng hiệu suất nếu số lượng file lớn.

---

⏱ Ngày hoàn thành: 06/05/2025