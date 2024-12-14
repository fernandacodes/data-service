FROM python:3.11

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django-extensions

COPY . /code/

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py create_users_groups && python manage.py runserver_plus --cert-file=/etc/letsencrypt/live/sistemaunasus.ufam.edu.br/fullchain.pem --key-file=/etc/letsencrypt/live/sistemaunasus.ufam.edu.br/privkey.pem 0.0.0.0:8000"]
