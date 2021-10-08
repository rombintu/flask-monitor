# Образ который будет использоваться
# FROM python:3.8
FROM alpine:latest
# Преднастройка
RUN apk add git python3 vim nginx py3-psutil
RUN git clone https://github.com/rombintu/flask-monitor.git
WORKDIR /flask-monitor/client
RUN rm /etc/nginx/http.d/*
COPY nginx.conf /etc/nginx/
RUN python3 main.py
RUN cp info.json /usr/share/nginx/
CMD ["nginx", "-g", "daemon off;"]
