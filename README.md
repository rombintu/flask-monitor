# MONITORING
### BASO-03-17

## RUN
```
git clone https://github.com/rombintu/flask-flask-monitor.git
cd flask-monitor
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python
>>> from server import db, create_app
>>> db.create_all(app=create_app())
>>> exit
cp .env.bak .env
cd server/
python3 -m flask run
```


## RUN ON HTTPS
```
sudo apt-get install openssl
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
python3 -m flask run --cert=cert.pem --key=key.pem 
```

# DOCKER RUN

```
git clone https://github.com/rombintu/flask-monitor.git
cd flask-monitor
docker build -t server-mon server/ 
docker build -t client-mon client/ 
docker run -d -p 5000:3000 server-mon
docker run -d -p 80:80 client-mon

docker exec <server-id-container> ip a 

Go to http://<server-ip>:5000
```