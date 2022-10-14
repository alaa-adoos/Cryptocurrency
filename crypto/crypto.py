
import requests # python3 -m pip install requests
from dotenv import load_dotenv
import os
load_dotenv()

class Crypto:
   '''
   Crypto Class :
   - contain function that return some information about the crypto coin that the user passed .
   - Coin Market Cap API was used in this app .
   - The top 100 crypto currencies were selected to search through.
   - dotenv used to secure API key 
   - KEY=c186227b-fc24-4722-8bfd-f08ecd6d1341
   ''' 

   def __init__(self):
      self.symbol=None
      self.r=None
      self.coin=None
      self.m=None
      self.api_key = os.getenv("KEY")
   def set_symbol(self,symbol):
      # set_symbol is a function that set what user symbol pass.
      self.symbol=symbol
   def get_data(self):
      # get_data is a function that get data from API as a JSON file
      self.url =f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&convert=USD&CMC_PRO_API_KEY={self.api_key}'
      self.r=requests.get(self.url).json()
   def get_coin(self):
      # get_coin is a function that get data for the selected coin by searching for its symbol
      i=0
      while i<100:
            if self.r["data"][i]["symbol"]==self.symbol:
               self.coin=self.r["data"][i]
               break
            i+=1
      return self.coin
   def get_name(self):
      return self.coin["name"]
   def get_price(self):
      return self.coin["quote"]["USD"]["price"]
   def get_max_supply(self):
      return self.coin["max_supply"]
   def get_categories(self):
      categori=self.coin["tags"][:3]
      return " - ".join(categori)
   def get_rank(self):
      return self.coin["cmc_rank"]
crypto=Crypto()
