import json
import requests
import mysql.connector
import datetime
from init_db import mydb

url_api = "https://poloniex.com/public?command=returnTicker"
crypto_name = 'USDC_BTC'
print(mydb)

data = {
    1: {},
    5: {},
    15: {}
}


def check_high_low(last):
    if last > data[1]['high']:
        data[1]['high'] = last
    if last < data[1]['low']:
        data[1]['low'] = last


def compare(low_period, high_period):
    if data[low_period]['high'] > data[high_period]['high']:
        data[high_period]['high'] = data[low_period]['high']
    if data[low_period]['low'] < data[high_period]['low']:
        data[high_period]['low'] = data[low_period]['low']


def post_period(period, last, now, crypto_name):
    sql = "INSERT INTO crypto(name, period, date_time, open, low, high, close) VALUES (%s, %s, %s, %s, " \
          "%s, %s, %s)"
    val = (crypto_name, period, now.strftime('%Y-%m-%d %H:%M'), data[period]['open'], data[period]['low'],
           data[period]['high'], last)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()


def clear(period, last):
    data[period]['high'] = 0
    data[period]['low'] = 2**31
    data[period]['open'] = last


def get_last(crypto_name):
    response = requests.get(url_api)
    data_crypto = json.loads(response.content)
    return float(data_crypto[crypto_name]['last'])


if __name__ == '__main__':

    last = get_last(crypto_name)
    clear(1, last)
    clear(5, last)
    clear(15, last)
    before = datetime.datetime.now()

    while True:

        last = get_last(crypto_name)
        check_high_low(last)

        now = datetime.datetime.now()

        if before.minute != now.minute:
            compare(1, 5)
            post_period(1, last, before, crypto_name)
            clear(1, last)
            if not before.minute % 5:
                compare(5, 15)
                post_period(5, last, before, crypto_name)
                clear(5, last)
            if not before.minute % 15:
                post_period(15, last, before, crypto_name)
                clear(15, last)
            before = now
