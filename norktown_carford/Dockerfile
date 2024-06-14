FROM python:3.9-slim

# Instale netcat-openbsd
RUN apt-get update && apt-get install -y netcat-openbsd

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.yml requirements.yml

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.yml

RUN pip install pytest pytest-cov

# Copie o conteúdo da aplicação para o diretório de trabalho
COPY . .

# Copie o script wait-for-it.sh para o diretório de trabalho
COPY wait-for-it.sh /wait-for-it.sh

# Torne o script executável
RUN chmod +x /wait-for-it.sh

# Comando para rodar a aplicação
CMD ["sh", "/wait-for-it.sh", "db", "5432", "flask run --host=0.0.0.0"]
