FROM python:3.11

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django-extensions

COPY . /code/

RUN openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:secp384r1 -days 3650 \
    -nodes -keyout /code/unasus.com.key -out /code/unasus.com.crt -subj "/CN=unasus.com" \
    -addext "subjectAltName=DNS:unasus.com,DNS:*.unasus.com,IP:15.228.45.143" && \
    ls -l /code  # Verifique se os arquivos estão sendo criados corretamente

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py create_users_groups && python manage.py runserver_plus --cert-file=/code/unasus.com.crt --key-file=/code/unasus.com.key 0.0.0.0:8000"]
