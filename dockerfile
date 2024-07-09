FROM python:3.9-slim

WORKDIR /app

COPY payment_service.py .

RUN pip install flask

EXPOSE 5001

CMD ["python", "payment_service.py"]
