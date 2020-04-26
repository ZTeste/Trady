import pickle
import fxcmpy
from features.indicators import trend, momentum

CURRENCY = 'EUR/USD'
MODEL_FILENAME = '../models/model.sav'
TOKEN = "Your fxcm token"
SHIFT = -4

con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='warn', server='demo')

# Downloading last market data
data = con.get_candles(CURRENCY, period='H1', number=50)

print("Generating features with last data")

data['rsi'] = momentum.rsi(data['bidclose'])
data['macd'] = trend.macd(data['bidclose'])
data = data.drop(columns=['bidopen', 'bidclose', 'bidhigh', 'bidlow', 'askopen', 'askclose', 'askhigh', 'asklow', 'tickqty'])

print("Loading model")

model = pickle.load(open(MODEL_FILENAME, 'rb'))

# Making prediction with the last dataframe row
prediction = model.predict(data.tail(1))

direction = ("Bearish", "Bullish")[prediction[0] == 1]

print(CURRENCY + " should be " + direction + " for the next " + str(-SHIFT) + " hours")
print("end")