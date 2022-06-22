import requests
import time

def home():

    web = ""    
    date = requests.get(web)
    date.json()
    
    time.sleep(3)
    for r in date:
        print(r)
        
home()
    
