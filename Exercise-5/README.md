# 📄 Báo cáo Bài tập Data Engineering – Exercise 5

## 1. Thông tin nhóm
- Họ tên: Hoàng Trọng Nghĩa, Nguyễn Bá Đức
- MSSV: 23630761, 23732881
- Lớp: DHKHDL19A
- **Bài:** Exercise 5 – Mô hình dữ liệu với PostgreSQL + Python

---

## 2. Mục tiêu bài tập
- Phân tích các file CSV có sẵn và xây dựng lược đồ cơ sở dữ liệu phù hợp (schema.sql).
- Thiết lập kết nối PostgreSQL bằng Python (`psycopg2`) và thực thi các câu lệnh SQL.
- Tải dữ liệu từ các file CSV (`accounts.csv`, `products.csv`, `transactions.csv`) vào bảng tương ứng.

---

## 3. Nội dung thực hiện

- 📂 **Phân tích dữ liệu:**
  - Tạo file `schema.sql` với các lệnh `CREATE TABLE`, sử dụng kiểu dữ liệu thích hợp.
  - Thiết lập khoá chính (PRIMARY KEY) và khoá ngoại (FOREIGN KEY), thêm chỉ mục (INDEX) nếu cần.

- 🐍 **Viết script Python:**
  - Dùng `psycopg2` để kết nối đến PostgreSQL.
  - Chạy `schema.sql` để tạo bảng.
  - Xoá dữ liệu cũ trong bảng (nếu có).
  - Nạp dữ liệu từ CSV vào bảng bằng `copy_from`.

- 🐳 **Docker Compose:**
  - Chạy dịch vụ `postgres` và script Python đồng thời.
  - Đảm bảo `depends_on` với `condition: service_healthy` để chờ PostgreSQL sẵn sàng.

---

## 4. Kết quả đạt được

- ✅ Đã tạo thành công các bảng `accounts`, `products`, `transactions` trong PostgreSQL.
- ✅ Đã nạp dữ liệu thành công từ các file CSV vào bảng tương ứng.
- ✅ Không có lỗi xảy ra trong quá trình thực thi, mã thoát container là `0`.

---

## 5. Nhận xét & Hướng mở rộng

- Code Python sử dụng `copy_from` nên rất nhanh và hiệu quả với dữ liệu lớn.
- Có thể mở rộng:
  - Kiểm tra dữ liệu đầu vào (validation).
  - Ghi log chi tiết cho từng bước.
  - Tự động phát hiện schema từ dữ liệu (schema inference).

---

📅 **Ngày hoàn thành:** {date}
