import const
from requests.exceptions import HTTPError
import requests
import json
import logging

##api
def api_get(path:str):
    url=const.API_URL()+"/"+path
    try:
        resp=requests.get(url)
        #If the response was successful, no Exception will be raised
        resp.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
        
    parsed_content = resp.json()[0]
    
    return {"content":parsed_content,"path":path,"response":resp}

