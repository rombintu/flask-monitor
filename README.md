# FLASK MONITORING
### powered by baso-03-17

## RUN
```
git clone https://github.com/rombintu/flask-auth.git
cd flask-auth
python3 -m venv venv
pip install -r requirements.txt
python
>>> from server import db, create_app
>>> db.create_all(app=create_app())
>>> exit
cp .env.bak .env
python3 -m flask run
```

## RUN ON HTTPS
```
sudo apt-get install openssl
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
python3 -m flask run --cert=cert.pem --key=key.pem 
```