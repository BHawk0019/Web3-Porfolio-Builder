#rebuild arrays and math

from builder import token_names, prices
import configparser, csv

config = configparser.ConfigParser(inline_comment_prefixes=(';', '#'))
config.read("config.ini")

file_path = config["general"]["path"] 

def writeFile(n,p, path):
    '''Rewrite file with new data'''

    with open(path,"w",encoding="utf-8") as f:
        writer = csv.writer(path)
        data = list(writer)

        print(data)


        
            
    
    return True