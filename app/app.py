from flask import Flask, render_template
import plotly.graph_objects as go
import plotly
import pandas as pd
import json
from init_db import mydb

app = Flask(__name__,template_folder='templates')

def get_data(name,period):

    sql = "SELECT * FROM crypto WHERE name = %s AND period = %s"
    adr = (name, period)

    mycursor = mydb.cursor()
    mycursor.execute(sql, adr)
    result = mycursor.fetchall()

    df = pd.DataFrame(result,columns=['name','period','date_time','open','low','high','close'])
    date_time = pd.to_datetime(df['date_time'])
    df['date_time'] = date_time

    fig = go.Figure(data=[go.Candlestick(x=df['date_time'],
                                         open=df['open'], high=df['high'],
                                         low=df['low'], close=df['close'])
                          ])

    fig.update_layout(xaxis_rangeslider_visible=False)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/<name>/<int:period>')
def post(name,period):
    graphJSON = get_data(name,period)
    return render_template('graph.html', plot=graphJSON, name=name, period=period)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

