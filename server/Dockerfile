# Образ который будет использоваться
# FROM python:3.8
FROM alpine:latest
# Преднастройка
RUN apk add git vim python3 py3-pip linux-headers libc-dev python3-dev musl-dev gcc g++
# Клонируем проект
RUN git clone https://github.com/rombintu/flask-monitor.git
# Переходим в рабочую область
WORKDIR /flask-monitor
# Копируем конфигурационный файл
RUN cp .env.bak .env
# Скачиваем зависимости
RUN python3 -m pip install -r requirements.txt
# Создаем базу данных
RUN python3 -c 'from server import db, create_app; db.create_all(app=create_app())'
# Указываем что необходимо будет запускать
CMD ["python3", "-m", "flask", "run"]
