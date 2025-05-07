## 🤖 BÀI 2: Pipeline Huấn Luyện Mô Hình Dự Đoán Tỷ Giá

### 🎯 Mục tiêu
- Từ dữ liệu tỷ giá đã cào, huấn luyện mô hình phân loại (tăng/giảm)
- Mô hình: `RandomForestClassifier`
- Gán nhãn:
  - `1` nếu tỷ giá > 1 (tăng)
  - `0` nếu tỷ giá ≤ 1 (giảm)
- Đánh giá độ chính xác và lưu mô hình

### 🧪 Các bước thực hiện
1. Cào dữ liệu từ [x-rates.com](https://www.x-rates.com) tương tự Bài 1
2. Tiền xử lý:
   - Chuyển `Rate` sang float
   - Gán nhãn `Label`
3. Huấn luyện:
   - Train/Test split
   - Train RandomForest
   - Đánh giá `accuracy`
4. Lưu mô hình thành `model/model.pkl` bằng `joblib`
## Ngày hoàn thành
- 06/05/2025
