
# BÁO CÁO BÀI TẬP DATA ENGINEERING - EXERCISE 2

## 1. Thông tin nhóm
- Họ tên: Hoàng Trọng Nghĩa, Nguyễn Bá Đức
- MSSV: 23630761, 23732881
- Lớp: DHKHDL19A
- Bài tập: Exercise 2 – Phân tích dữ liệu thời tiết  

## 2. Mục tiêu bài tập
Thực hành sử dụng Python để tải một tệp dữ liệu thời tiết từ URL, phân tích dữ liệu để tìm ra nhiệt độ cao nhất theo giờ, sau đó trích xuất các dòng dữ liệu tương ứng.

## 3. Nội dung thực hiện
- Dùng thư viện `requests` để tải file `.csv` thời tiết từ URL.  
- Đọc file bằng `pandas`, xử lý cột nhiệt độ `HourlyDryBulbTemperature`.  
- Tìm giá trị lớn nhất và các dòng tương ứng với giá trị này.  
- In kết quả ra màn hình (stdout) khi chạy bằng Docker container.  
- Viết mã xử lý trong `main.py`, thực thi bằng Docker Compose.

## 4. Kết quả
- File `01023199999.csv` đã được tải thành công.  
- **Nhiệt độ cao nhất**: `54.0°F`  
- Bản ghi tương ứng đã được trích xuất và hiển thị với đầy đủ thông tin về độ ẩm, tốc độ gió và lượng mưa.

## 5. Nhận xét và hướng mở rộng
- Có thể mở rộng để phân tích nhiều file cùng lúc.  
- Có thể tính thêm các thống kê trung bình, tối thiểu hoặc trực quan hóa dữ liệu bằng biểu đồ.  
- Có thể xử lý các giá trị thiếu (NaN) tốt hơn và ghi kết quả ra file hoặc database.

## Ngày hoàn thành
- 06/05/2025
