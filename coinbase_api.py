import requests
import apikey
import time
import pandas as pd
import datetime



url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'3',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': apikey.key,
}



def api_pull_coinbase():

  
    json = requests.get(url, params= parameters, headers = headers).json()


    coins = json['data']
    for x in coins:
        if x['symbol'] == 'ETH' or x['symbol'] == 'BTC':
          symbol_coin =[]
          price_usd = []
          percent_change_24h = []
          percent_change_7d = []

          symbol_coin.append(x['symbol']) 
          price_usd.append(x['quote']['USD']['price'])
          percent_change_24h.append(x['quote']['USD']['percent_change_24h'])
          percent_change_7d.append(x['quote']['USD']['percent_change_7d'])

          dict = {'coin': symbol_coin, 'price': price_usd , 'percent change 24h': percent_change_24h, 'percent change 7d': percent_change_7d} 
          df = pd.DataFrame(dict)   
          df['date_time'] = pd.to_datetime('now').strftime("%Y-%m-%d %H:%M")
          print(df)

          
          df.to_csv("s3://apache-airflow-s3-razvan/file_name.csv", mode='w', index=False, header=False)    
          
       



api_pull_coinbase()

