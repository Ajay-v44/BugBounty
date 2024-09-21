FROM python:3.9-slim

# Install system dependencies required for SSL and Python build tools
RUN apt-get update && apt-get install -y \
    libssl-dev \
    libffi-dev \
    python3-dev \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
