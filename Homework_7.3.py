
import json

from urllib.request import urlopen

api_key = "ITZE47G6KTD0XUPY"

response = urlopen("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=ITZE47G6KTD0XUPY").read()
data = json.loads(response)

print(data)

print(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

print(exchange_rate)

print("One BTC is worth " + exchange_rate + " USD.")