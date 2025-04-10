# Base image
FROM python:3.14

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# 환경 변수 로드 설정
ENV PYTHONUNBUFFERED=1

# Expose FastAPI port
EXPOSE 8000


