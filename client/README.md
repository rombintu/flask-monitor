# FLASK MONITORING (AGENT)
### powered by baso-03-17

## Pre-RUN
```
sudo apt-get install nginx
sudo systemctl enable ngnix
sudo systemctl start ngnix
```

## RUN
```
git clone https://github.com/rombintu/flask-monitor.git
cd flask-monitor/client
pip3 install psutil
python3 main.py
sudo ln info.json /usr/share/nginx/html/
настройте cron для автоматического обновления файла
```
