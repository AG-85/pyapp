# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY src/pyapp/app.py .

CMD ["python3", "app.py"]
