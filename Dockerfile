FROM python:3.11

# Define o diretório de trabalho
WORKDIR /code

# Copia e instala as dependências
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Instala o gunicorn
RUN pip install gunicorn

# Copia o código da aplicação
COPY . /code/

# Copia os certificados SSL para dentro do container
COPY ssl /code/ssl/

# Expõe a porta 8000 (para HTTPS)
EXPOSE 8000

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Comando para rodar a aplicação com gunicorn utilizando HTTPS
CMD ["sh", "-c", "python manage.py makemigrations && \
                   python manage.py migrate && \
                   python manage.py create_users_groups && \
                   gunicorn project.wsgi:application \
                   --bind 0.0.0.0:8000 \
                   --workers 3 \
                   --certfile=/code/ssl/fullchain.crt \
                   --keyfile=/code/ssl/privkey.key"]
