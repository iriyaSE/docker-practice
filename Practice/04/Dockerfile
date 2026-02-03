FROM python:3.9-slim AS builder
WORKDIR /build

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.9-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY app.py .

ENV PATH=/root/.local/bin:$PATH

EXPOSE 8080
CMD ["python", "app.py"]
