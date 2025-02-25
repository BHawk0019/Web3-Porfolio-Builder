# main program file
import configparser
from pathlib import Path
import os
import csv, time, json
import builder

#create create time object

time = int(time.time())


#create config object
config = configparser.ConfigParser(inline_comment_prefixes=(';', '#'))
config.read("config.ini")


#check for csv file - create file if one does not exist
file_path = config["general"]["path"] 
currency_path = config['general']['currencypath']


#Global Variables
name = config['csvformat']["tokenname_column"]
ticker =config['csvformat']["ticker_column"]
tokensheld = config['csvformat']["tokensheld_column"]
currentprice = config['csvformat']["currentprice"]
currency_name = config['csvformat']["currencycolumn"]
CURRENCY = config['general']['defaultcurrency']

ticker_DATA = []
num_TOKEN_DATA = []


def checkFile():
    """Checks to see if file exists in specified path."""

    if not os.path.exists(file_path):
        create_FILE_DATA = [[f"{name}",f"{ticker}",f"{tokensheld}",f"{currentprice}",f"{currency_name}"]]

        with open(file_path,"w",newline="",encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(create_FILE_DATA)

        print("File has written successfully.")

    else:
    
        print("File already exists.")

    return
    



def readFile():

    """Stores csv data into memory via DictReader."""

    with open(file_path,"r",newline="",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        ticker_column_data = [row[ticker] for row in reader if ticker in row]
        tokensheld_column_data = [row[tokensheld] for row in reader if tokensheld in row]

        for element in ticker_column_data:
            ticker_DATA.append(element)
        
        for element in tokensheld_column_data:
            num_TOKEN_DATA.append(element)


    return

def assignCurrency(c):
    #read json library - check for term in if-any statement

    with open(c,"r",newline='', encoding='utf-8') as f:
        reader = json.load(f)

        for currency in range(len(reader)):
            if reader[currency]['currency_code'] == CURRENCY:
                coinmarketcap_id = reader[currency]['currency_code']
                continue

    return coinmarketcap_id


def main():
    checkFile()
    readFile()
    builder
    
   
    #store variables into memory
    #rewrite files with data




    return





#program start
currencyID = assignCurrency(currency_path) #Coin Market Cap ID of FIAT currency used for conversion calculations
main()

