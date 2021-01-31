import requests

# read the api-key
f = open('api-key.txt','r')
key = f.readline().rstrip('\n')

print("key:", key)
params = {'access_key':key}

# call the ccy end-point
#print(params)
#url= "http://api.marketstack.com/v1/currencies"
#r = requests.get("http://api.marketstack.com/v1/currencies?access_key=43f4225b52ef3fad61c9154d43a07fdc")
#r = requests.get(url,params)

# call the ccy for tickers
############
paramsTicker = {'search':'PHM.BMEX', 'exchange':'BMEX'}
# add the key
paramsTicker['access_key'] = key

urlTicker = 'http://api.marketstack.com/v1/tickers'

r = requests.get(urlTicker,paramsTicker)

print(r.text)
