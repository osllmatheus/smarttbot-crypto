FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY script_btc.py /app
COPY init_db.py /app
COPY init.sql /app
COPY ./app/app.py /app
COPY ./app/templates /app/templates

CMD python script_btc.py & python app.py
