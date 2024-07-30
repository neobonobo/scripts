import requests,json
from bs4 import BeautifulSoup
from time import localtime, strftime

url='www.sozcu.com.tr/doviz-hesapla/dolar/'
r  = requests.get("https://" +url)
data = r.text
soup = BeautifulSoup(data,"html.parser")

a=soup.find_all('strong')[3].contents[0][:6]
b=soup.find_all('strong')[4].contents[0][:6]
t=strftime("%Y-%m-%d %H:%M", localtime())

with open("rates_log",'a') as f:
    f.write(f"{t} {a} {b}\n")
f.close()
