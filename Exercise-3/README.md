# 📘 Báo cáo Bài tập Data Engineering – Exercise 3

## 1. Thông tin nhóm
- Họ tên: Hoàng Trọng Nghĩa, Nguyễn Bá Đức
- MSSV: 23630761, 23732881
- Lớp: DHKHDL19A
- **Bài:** Exercise 3 – Tải dữ liệu từ CommonCrawl S3 (WET File)

---

## 2. Mục tiêu bài tập
- Làm quen với việc **làm việc với dữ liệu từ S3 bucket** (CommonCrawl).
- Viết script Python để:
  - Tải file `wet.paths.gz` từ CommonCrawl.
  - Đọc URI từ dòng đầu tiên.
  - Tải file `.wet.gz` tương ứng với URI.
  - In ra **10 dòng đầu tiên** từ file `.wet.gz`.

---

## 3. Công nghệ & thư viện sử dụng
- 🐍 Python 3
- 📦 Thư viện: `requests`, `gzip`, `io`  
- 🐳 Docker + docker-compose
- 📄 Yêu cầu trong `requirements.txt`:  
  ```txt
  boto3==1.26.137
  requests>=2.31.0
