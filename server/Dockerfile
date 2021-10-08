# Образ который будет использоваться
# FROM python:3.8
FROM alpine:latest
# Преднастройка
RUN apk add git vim python3 py3-pip linux-headers libc-dev python3-dev musl-dev gcc g++
RUN git clone https://github.com/rombintu/flask-monitor.git
WORKDIR /flask-monitor
RUN cp .env.bak .env
RUN python3 -m pip install -r requirements.txt
RUN python3 -c 'from server import db, create_app; db.create_all(app=create_app())'
CMD ["python3", "-m", "flask", "run"]
