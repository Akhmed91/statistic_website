FROM python:3.9.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip3 install -r /app/requirements.txt --no-cache-dir


# CMD ["python3", "manage.py", "runserver", "0:8000"]
# EXPOSE 8000


# Запуск контейнера
# docker build . -t name_image
# docker build -t statistic .
# docker run -d -p 8000:8000 statistic
# docker run --name name_container -it -p 8000:8000 name_image

# Выполнить запуск сервера разработки при старте контейнера.
CMD ["gunicorn", "statistic_site.wsgi:application", "--bind", "0:8000" ]