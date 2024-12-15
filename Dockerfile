FROM python:3.11

# Define o diretório de trabalho
WORKDIR /code

# Copia e instala as dependências
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django-extensions

# Copia o código da aplicação
COPY . /code/

# Expõe a porta 8000
EXPOSE 8000

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Comando para rodar a aplicação
CMD ["sh", "-c", "python manage.py makemigrations && \
                   python manage.py migrate && \
                   python manage.py create_users_groups && \
                   python manage.py runserver_plus --cert-file=/code/ssl/fullchain.crt --key-file=/code/ssl/privkey.key 0.0.0.0:8000"]
