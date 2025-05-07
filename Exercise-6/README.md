# BÁO CÁO BÀI TẬP DATA ENGINEERING - EXERCISE 6

## 1. Thông tin nhóm
- Họ tên: Hoàng Trọng Nghĩa, Nguyễn Bá Đức
- MSSV: 23630761, 23732881
- Lớp: DHKHDL19A  
- Bài tập: Exercise 6 – Ingestion and Aggregation with PySpark

## 2. Mục tiêu bài tập
Thực hành xử lý dữ liệu lớn với PySpark:  
đọc file `.zip` chứa dữ liệu `.csv`, thực hiện truy vấn phân tích và xuất báo cáo dưới dạng `.csv`.

## 3. Nội dung thực hiện
- Dữ liệu gốc là các file `.zip` chưa giải nén chứa thông tin chuyến đi của người dùng xe đạp.
- Dùng thư viện `zipfile` và `pyspark.sql` để:
  - Giải nén tạm thời các file zip ra thư mục `unzipped_data`.
  - Đọc tất cả các file `.csv` và ép kiểu cho cột `tripduration`.
- Xử lý dữ liệu để trả lời các câu hỏi:
  1. Thời gian chuyến đi trung bình theo ngày.
  2. Số lượng chuyến đi mỗi ngày.
  3. Trạm xuất phát phổ biến nhất mỗi tháng.
  4. Top 3 trạm phổ biến mỗi ngày trong 2 tuần cuối cùng.
  5. Giới tính nào có thời gian đi trung bình cao hơn.
  6. Top 10 độ tuổi có thời gian đi dài nhất và ngắn nhất.

## 4. Kết quả
- Các báo cáo được xuất ra thư mục `reports/` dưới dạng `.csv`:
  - `average_trip_duration_per_day.csv`
  - `trips_count_per_day.csv`
  - `most_popular_start_station_per_month.csv`
  - `top_3_stations_last_2_weeks.csv`
  - `average_duration_by_gender.csv`
  - `top_10_ages_longest_shortest.csv`
- Dữ liệu được xử lý hoàn toàn bằng PySpark, thực hiện chính xác theo yêu cầu đề bài.

## 5. Nhận xét và hướng mở rộng
- Nên áp dụng cấu trúc pipeline rõ ràng hơn cho PySpark để dễ bảo trì.
- Có thể tối ưu hiệu suất bằng cách dùng cache hoặc persist nếu dữ liệu lớn.
- Có thể bổ sung unit test cho từng hàm xử lý dữ liệu.
- Có thể sử dụng Airflow để lên lịch xử lý định kỳ.

## Ngày hoàn thành
- 06/05/2025
