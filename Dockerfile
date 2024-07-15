FROM python:3.9-slim

WORKDIR /app

COPY payment_service.py /app

RUN pip install Flask requests

CMD ["python", "payment_service.py"]
