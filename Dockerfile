# Usa a imagem base oficial do Python 3.12 slim para manter o tamanho mínimo
FROM python:3.12-slim


COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]