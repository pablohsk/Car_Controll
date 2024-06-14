FROM python:3.9-slim

RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /app

COPY requirements.yml requirements.yml

RUN pip install --no-cache-dir -r requirements.yml

RUN pip install pytest pytest-cov

COPY . .

COPY wait-for-it.sh /wait-for-it.sh

RUN chmod +x /wait-for-it.sh

CMD ["sh", "/wait-for-it.sh", "db", "5432", "flask run --host=0.0.0.0"]
