# Smarttbot - API Crypto
API source code - Get data from Poloniex API and build a candlestick graph webserver. 

The application developed in [Flask](https://flask.palletsprojects.com/en/1.1.x/), [Python](https://docs.python.org/3/) and [MySQL](https://www.mysql.com/) with [Adminer](https://www.adminer.org/)

## Requirements

Only Docker to Build image and run application:

- [Docker](https://docs.docker.com/docker-for-windows/install/)


## Getting started

To run the application, in the directory where the docker-compose.yml file is located, open the terminal and type the commands:

```
docker-compose up --build
```


After the RUN command, the server will be running on the local machine on port 5000 and MySQL Adminer on port 8080.



## Testing the application
Open your browser and access the address:

- Home: http://localhost:5000/
- Adminer: http://localhost:8080/
    - Server: db
    - Username: root
    - Password: root
    - Database: smarttbot_crypto

To access graph you need to access the cryptoname in top menu


![Home](linkfoto)


After select crypto, you can choose the time frames.

![Graph](linkfoto)
