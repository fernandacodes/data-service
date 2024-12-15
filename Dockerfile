FROM python:3.11

# Diretório de trabalho no container
WORKDIR /code

# Instalar dependências do projeto
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django-extensions

# Copiar código do projeto
COPY . /code/

# Copiar os certificados do Let's Encrypt
COPY /etc/letsencrypt/live/sistemaunasus.ufam.edu.br/fullchain.pem /code/unasus.com.crt
COPY /etc/letsencrypt/live/sistemaunasus.ufam.edu.br/privkey.pem /code/unasus.com.key

# Expor a porta 8000
EXPOSE 8000

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Comando para rodar o Django com suporte a HTTPS
CMD ["sh", "-c", "python manage.py makemigrations && \
                   python manage.py migrate && \
                   python manage.py create_users_groups && \
                   python manage.py runserver_plus --cert-file=/code/unasus.com.crt --key-file=/code/unasus.com.key 0.0.0.0:8000"]
