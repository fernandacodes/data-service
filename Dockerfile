FROM python:3.11

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000


# python3 manage.py makemigrations unasus_registros
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py create_users_groups && python manage.py runserver 0.0.0.0:8000"]
