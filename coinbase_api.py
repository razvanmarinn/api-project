
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

    #File = open("title.txt", "a+" , encoding='utf8')
    #csv_writer = csv.writer(File)
    json = requests.get(url, params= parameters, headers = headers).json()


    coins = json['data']
    for x in coins:
        # if x['symbol'] == 'BTC' or x['symbol'] == 'ETH':
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
        df['date_time'] = pd.to_datetime('now').strftime("%Y-%m-%d %H:%M:%S")
        print(df)
        #csv_writer.writerow([symbol_coin, price_usd, percent_change_24h, percent_change_7d])
      
        df.to_csv('file_name.csv', mode='a+', index=False, header=False)    
       
      

    
def auto_repeat():
    while 0 < 1:
        api_pull_coinbase()
        print("Api Pull done")
        time.sleep(10)

auto_repeat()


