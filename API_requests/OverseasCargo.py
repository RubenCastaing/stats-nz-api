import urllib.request, json
import stats_odata as odata
import pandas as pd
from datetime import datetime, timedelta
pd.set_option('display.max_rows', 100)

def GetOverseasCargo():
    # Calculate the date for two months before today
    two_months_ago = (datetime.now() - timedelta(days=60)).strftime('%Y-%m-%d')

    endpoint = 'OverseasCargo'
    service = "https://api.stats.govt.nz/odata/v1"
    entity = "Observations" 
    query_option = "$top=10"
    api_key = "dde082d59e0a4c49bf83f67ff6b9b032"
    proxies = {}

    #Sending an API request
    Observations = odata.get_odata(service, endpoint, entity, query_option, api_key, proxies)
    print(Observations)
    
    #Cleaning the data
    columns_to_drop = ['ResourceID', 'Status', 'Label3', 'Label4', 'Label5', 'Label6']
    Observations.drop(columns_to_drop, axis=1, inplace=True)

    return(Observations)

print(GetOverseasCargo())