## 📘 BÀI 1: Pipeline Cào Dữ Liệu và Trực Quan Hóa

### 🎯 Mục tiêu
- Cào dữ liệu tỷ giá từ website: [x-rates.com](https://www.x-rates.com/table/?from=USD&amount=1)
- Lưu dữ liệu tỷ giá vào file `.csv`
- Vẽ biểu đồ trực quan tỷ giá của 10 đơn vị tiền tệ phổ biến
- Tự động hóa bằng script Python (và Docker)

### 🧪 Các bước thực hiện
1. Sử dụng `requests` và `BeautifulSoup` để lấy dữ liệu HTML.
2. Dùng `pandas.read_html()` để trích xuất bảng tỷ giá.
3. Lưu dữ liệu ra `data/rates.csv`
4. Dùng `matplotlib` để vẽ biểu đồ thanh (bar chart) tỷ giá so với USD.

### 📊 Kết quả
- File dữ liệu: `data/rates.csv`
- Biểu đồ: `plots/rates_<ngày>.png`

---
