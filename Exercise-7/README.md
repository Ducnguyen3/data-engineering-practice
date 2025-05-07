
## 1. Thông tin nhóm

- Họ tên: Hoàng Trọng Nghĩa, Nguyễn Bá Đức  
- MSSV: 23630761, 23732881  
- Lớp: DHKHDL19A  
- Bài: Exercise 7 – Phân tích lỗi ổ cứng với PySpark

---

## 2. Mục tiêu bài tập

- Sử dụng PySpark để xử lý dữ liệu ổ cứng từ Backblaze dạng `.csv.zip`.
- Không sử dụng UDF hoặc hàm Python thuần – chỉ dùng `pyspark.sql.functions`.
- Sinh ra các cột đặc trưng:
  - `source_file` – tên file nguồn
  - `file_date` – ngày được trích từ tên file, kiểu `date`
  - `brand` – thương hiệu được tách từ `model`
  - `storage_ranking` – xếp hạng theo dung lượng `capacity_bytes`
  - `primary_key` – băm từ `serial_number`, `date`, `model`

---

## 3. Nội dung thực hiện

- 📥 **Chuẩn bị dữ liệu:**
  - Giải nén `hard-drive-2022-01-01-failures.csv.zip` vào thư mục `data/`
  - Đọc file `.csv` bằng `spark.read.csv(...)` với `header=True, inferSchema=True`

- 🧠 **Xử lý với PySpark:**
  - `source_file`: dùng `input_file_name()`
  - `file_date`: dùng `regexp_extract()` + `to_date()`
  - `brand`: `split(model, " ")` nếu có khoảng trắng, ngược lại gán `"unknown"`
  - `storage_ranking`: dùng `dense_rank()` trên `capacity_bytes` giảm dần
  - `primary_key`: dùng `hash(serial_number, date, model)`

- 🐳 **Triển khai với Docker:**
  - Tạo `Dockerfile` cài Spark 3.0.1 + Python 3.8 + Java 11
  - Sử dụng `docker-compose` để build và chạy pipeline
  - Mount thư mục `data/` và `reports/` ra ngoài để kiểm tra đầu ra

---

## 4. Kết quả đạt được

- ✅ Đọc dữ liệu thành công từ file `.csv`
- ✅ Sinh đầy đủ các cột theo yêu cầu đề bài
- ✅ Toàn bộ xử lý thực hiện bằng hàm trong `pyspark.sql.functions`
- ✅ Chạy thành công trên môi trường Docker với `docker-compose`
- ✅ Có thể xuất kết quả ra file CSV nếu cần (`.write.csv(...)`)

---

## 5. Nhận xét & Hướng mở rộng

- Việc sử dụng các hàm gốc của PySpark cho phép xử lý dữ liệu rất nhanh và dễ kiểm soát.
- Docker giúp tái hiện môi trường ổn định, không cần cài Spark thủ công.
- **Hướng mở rộng:**
  - Tự động giải nén `.zip` trong pipeline
  - Kết hợp thêm phân tích lỗi (`failure == 1`) để dự đoán hỏng ổ đĩa
  - Lưu dữ liệu thành file Parquet hoặc ghi ra PostgreSQL để trực quan hóa

---

📅 **Ngày hoàn thành:** *05/06/2025*  

