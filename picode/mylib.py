import datetime
import json
import requests

from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from binance.client import Client

client = Client("MKABjbT8JekGSo4SW2EwI4QzNKPVleYl3Z9CLKWqY22Ymuhqz8iilDEyrELdUm4C", 'I1mUUvHiJhloTPpLhQnIhRLmyx8NoLFx4HUQDGlRo1nwCljKEz3yG3YnjEIx90MU')

# Get rates and return data as dictionary
def get_rates():
    now=str(datetime.datetime.now().timestamp()).split('.')[0]
    open_url='https://openexchangerates.org/api/latest.json?app_id="ce68f2e290594ccca768cf41e821dba3"&base=USD'
    data = requests.get(open_url)
    prices=client.get_all_tickers()
    open_data_dict=data.json()
    btc_value=[d['price']  for d in prices if d['symbol']=='BTCUSDT']
    btc_usd=btc_value[0].split('.')[0]
    eth_value=[d['price']  for d in prices if d['symbol']=='ETHUSDT']
    eth_usd=eth_value[0].split('.')[0]
    hot_value=[d['price']  for d in prices if d['symbol']=='HOTUSDT']
    hot_usd=hot_value[0]
    rate_dict={'TimeStamp':now,
            'USDTRY':open_data_dict['rates']['TRY'],
            'BTCUSD':btc_usd,
            'ETHUSD':eth_usd,
            'HOTUSD':hot_usd,
            'GOLDTRY':get_gold_rate()
    }
    return rate_dict

# Get gold rates from sozcu.com
def get_gold_rate():
    try:
        gold_url = 'https://www.sozcu.com.tr/doviz-hesapla/altin/'
        gold = requests.get(gold_url)
    except ConnectionError:
        print('Cant access sozcu, maybe you are offline!')
    else:
        golddata = gold.text
        goldsoup = BeautifulSoup(golddata,"html.parser")
        gold_tl = goldsoup.find_all('strong')[4].contents[0][:6]
    return gold_tl

def save_rate_to_file():
    rate_dict=get_rates()
    try:
        with open("rates_log.json",'a') as f:
            rate_json=json.dumps(rate_dict)
            f.writelines(rate_json+"\n")
    except FileNotFoundError:
        print('no file like that, maybe you are not in picode folder')
    else:
        print('Success')

# Returns an array of rate_dict dictinaries
def see_rates():
    try:
        rates=[]
        with open("rates_log.json",'r') as fh:
            for line in fh.readlines():
                rate_dict=json.loads(line)
                # transforms unix time to datetime
                #rate_dict['Date']=datetime.datetime.fromtimestamp(rate_dict['Date'])
                # Append rate_dict dict to rates list
                rates.append(rate_dict)
    except FileNotFoundError:
        print('no file like that, maybe you are not in picode folder')
    else:
        #df=pd.DataFrame(rates)
        return rates

def display_file1():
    """Read a text file and display to stdout."""
    filename=input("enter filename pls:")
    try:
        with open(filename) as fh:
            # Read the whole file in memory'
            contents=fh.read()
    except FileNotFoundError:
        msg="Sorry, the file "+ filename + " does not exist."
        print('machine-> '+msg)
    else:
        print(contents)
        
def display_file2():
    """Read a text file and display to stdout."""
    filename=input("enter filename pls:")
    try:
        with open(filename) as fh:
            # Reading the file line by line
            lines=fh.readlines()
    except FileNotFoundError:
        msg="Sorry, the file "+ filename + " does not exist."
        print('machine-> '+msg)
    else:
        for line in lines:
            print(f"{line.rstrip()}")
           
# Creating the Day class
class ToDay():
    """Represent today from the first conscious breath to sleep"""
    def __init__(self):
        """Initialize day object."""
        # self.this_moment=datetime.datetime.now()
        self.user=input('Your name: ')
    """Gives info about the day"""
    def greetings(self):
        print(f"Hello {self.user} \n\nToday is: ")
        # print(self.this_moment.strftime('%A, %d %B\nTime: %H:%M'))

def w2programming():
    text=input('Enter some text : ')
    # Write to a file
    filename='programming.txt'
    with open(filename,'a') as f:
        f.write(text+'\n')

class User:
    """A simple attempt to represent a user."""
    def __init__(self,username, first_name, last_name):
        """Initialize attributes to describe a user."""
        self.username=username
        self.first_name=first_name
        self.last_name=last_name
    def get_full_name(self):
        print(f"{self.first_name.title()} {self.last_name.title()}")
