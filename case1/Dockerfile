FROM python:3.10-slim

WORKDIR /app

# Copy code
COPY . .

# Cài thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Tạo thư mục nếu cần (hoặc script sẽ tự tạo)
RUN mkdir -p data plots

# Chạy script chính
CMD ["python", "main.py"]
    