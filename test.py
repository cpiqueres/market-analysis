import requests
import json
import pandas as pd
from matplotlib import pyplot as plt

# read the api-key
f = open('api-key.txt','r')
key = f.readline().rstrip('\n')

print("key:", key)
params = {'access_key':key}

# call the ccy end-point
#print(params)
#url= "http://api.marketstack.com/v1/currencies"
#r = requests.get("http://api.marketstack.com/v1/currencies?access_key=xxxxxx")
#r = requests.get(url,params)

# call the ccy for tickers
############
def tickers():
    paramsTicker = {'search':'PHM.BMEX', 'exchange':'BMEX'}
    # add the key
    paramsTicker['access_key'] = key
    urlTicker = 'http://api.marketstack.com/v1/tickers'
    r = requests.get(urlTicker,paramsTicker)
    print(r.text)

def eod(symbol):
    params = {
                'symbols':symbol, 
                'exchange':'BMEX',
                'date_from':'2021-01-01',
                'date_to':'2021-01-31'}
    # add the key
    params['access_key'] = key
    url = 'http://api.marketstack.com/v1/eod'
    r = requests.get(url,params)
    data = json.loads(r.text)
    df = pd.DataFrame(data['data'])
    print(df)

if __name__ == "__main__":
       #tickers()
       eod('PHM.BMEX')
    
    
    
    
