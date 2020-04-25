from pandas import read_csv
import numpy as np
from pandas import datetime
from features.indicators import trend, momentum

FILE = "../data/EURUSD_H1.csv"
RES_FILE = "../data/results.csv"
SHIFT = -4

def parser_fxcm(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

data = read_csv(FILE, header=0, parse_dates=[0], index_col=0,
                  usecols=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow'], squeeze=True, date_parser=parser_fxcm)

print("Generating features")

data['rsi'] = momentum.rsi(data['bidclose'])
data['macd'] = trend.macd(data['bidclose'])

data['direction'] = np.where(data['bidclose'].shift(SHIFT) > data['bidclose'], 1, -1)

data = data.dropna()

print("Saving...")

data.to_csv(RES_FILE)

print("end")