 #This example uses Python 2.7 and the python-request library.

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import configparser
from main import ticker_DATA, currencyID

token_names = []
token_IDs = []
tokens_list = []
prices_data = []
prices = []
tickerLIST = ",".join(ticker_DATA)
SPAM_KEYWORDS = ["HarryPotter", "Trump", "PacMan", "Boost", "Sonic", "batcat", "Pumpomoto"]

#----------------Config Variables-------------------#

config = configparser.ConfigParser(inline_comment_prefixes=(';', '#'))
config.read("config.ini")
url = config['urls']['cmcurl']
idMAP = config['urls']['idMAP']
convert = config['urls']['convert']
api_key = config['general']['cmcapikey']



headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': f'{api_key}',
}


idMAPparameters = {
  'start':'1',
  'limit':'100',
  'symbol':f'{tickerLIST}'
}

convert_parameters = {
  'amount':'1',
  'id':'',
  'convert':f'{currencyID}' #!!! Needs Currency ID


}



#----------------Check Connection-------------------#
def pullData(s,api_SEARCH,api_PARAM):
    try:
        response = s.get(url + api_SEARCH, params=api_PARAM)
        APIdata = json.loads(response.text)
        #print(APIdata)
        item = APIdata['data']
        
  

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    return item



#-----------------Filter Spam---------------------#
def filterSpam(tokens):
  
 for token in tokens:
  if token.get("is_active") == 0:  # Inactive tokens
    continue
  elif token.get("status") not in [1]:  # Status codes that indicate valid tokens
    continue
  elif token.get("rank") is None or token.get("rank") > 5000:  # Avoid low-ranked/spam tokens
    continue
  elif any(keyword.lower() in token["name"].lower() for keyword in SPAM_KEYWORDS):  # Spam keywords
    continue
  else:
    tokens_list.append(token)
    
  

 return tokens_list





#START

session = Session()
session.headers.update(headers)

#Build and Store general info of crypto names and IDs
cryptoID_data = pullData(session,idMAP,idMAPparameters)
cryptoJSONdata= filterSpam(cryptoID_data)
coin_DATA = [item for item in cryptoJSONdata if item.get("name")]
#print(json.dumps(coin_DATA, indent=2)) #indent formatting for easy json reading -- remove # for debugging

for index in range(len(coin_DATA)):
  token_names.append(coin_DATA[index]['name']) #store token names
  token_IDs.append(coin_DATA[index]['id']) #store token ids


#Call Current Price Data for currencies stored.

for token in token_IDs:
  convert_parameters["id"] = f"{token}"
  price_Data = pullData(session,convert,convert_parameters)
  prices_data.append(price_Data) 

#print(json.dumps(prices_data,indent=2))

for item in range(len(prices_data)):
  prices.append(prices_data[item]['quote'][f"{currencyID}"]['price']) #store currency price
  #print(prices)

