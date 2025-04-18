FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/src

COPY backend/src/test_service .

RUN pip install poetry && poetry install
