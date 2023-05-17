FROM python:latest

WORKDIR /app

COPY src /app

RUN pip install pygame

CMD ["python", "main.py"]