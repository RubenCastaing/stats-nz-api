# -*- coding: utf-8 -*-
import pandas as pd
import requests

# Function to call Stats NZ open data api.
# This was written by Stats NZ
# Consider it a import that doesn't need to be marked

def get_odata(service = '', endpoint= '', entity = '', query_option = '', api_key = "dde082d59e0a4c49bf83f67ff6b9b032", proxies = {}):
    
# setup variables    
    headers = {'Ocp-Apim-Subscription-Key': api_key, 'user-agent':''}
    proxies = proxies
    url = service + '/' + endpoint + '/' + entity + '?' + query_option
    top_query = "$top" in query_option
    results = pd.DataFrame()

    # continue getting results while there are more pages 
    while url:
    
        try:
            r = requests.get(url,headers=headers,proxies=proxies)
            r.raise_for_status()
    
        # raise request errors        
        except requests.HTTPError as exception:
            print(exception)
            print(r.text)
            break
            
        df = pd.json_normalize(r.json()['value'])
        results = pd.concat([results,df])
        
        # get the next page url
        try:
            url = r.json()['@odata.nextLink'] 
            # return just the first page if $top was used
            if top_query:
                url = None
        except KeyError:
            url = None
        # show progress    
        print('.', end = ' ', flush = True)
 
    print(len(results.index),'Obs retrieved')

    return results

