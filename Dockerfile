FROM python:3.11

# Define o diretório de trabalho no contêiner
WORKDIR /code

# Copia o arquivo requirements.txt para dentro do contêiner
COPY requirements.txt /code/
# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instala o gunicorn, um servidor WSGI usado para produção
RUN pip install gunicorn

# Copia o código da aplicação Django para dentro do contêiner
COPY . /code/

# Copia os certificados SSL para dentro do contêiner (necessário para HTTPS)
COPY ssl /code/ssl/

# Expõe a porta 8000 (o Django vai rodar nessa porta)
EXPOSE 8000

# Define variáveis de ambiente para evitar escrever arquivos .pyc e para facilitar o debug
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Comando que será executado quando o contêiner for iniciado
# Usamos "sh -c" para rodar múltiplos comandos

# Condição para verificar se estamos no ambiente de produção ou de desenvolvimento.
# Para desenvolvimento, não executa o Gunicorn, apenas os comandos de migração e criação de usuários/grupos.
CMD ["sh", "-c", "if [ \"$ENVIRONMENT\" = \"PRODUION\" ]; then \
                   python manage.py makemigrations && \
                   python manage.py migrate && \
                   python manage.py create_users_groups && \
                   gunicorn project.wsgi:application \
                   --bind 0.0.0.0:8000 \
                   --workers 3 \
                   --certfile=/code/ssl/fullchain.crt \
                   --keyfile=/code/ssl/privkey.key; \
                 else \
                   python manage.py makemigrations && \
                   python manage.py migrate && \
                   python manage.py create_users_groups && \
                   python manage.py runserver 0.0.0.0:8000; \
                 fi"]
