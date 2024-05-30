import urllib.request, json
import stats_odata as odata
import pandas as pd
from datetime import datetime, timedelta

def get_employment_indicators():
    # Calculate the date for two months before today
    two_months_ago = (datetime.now() - timedelta(days=60)).strftime('%Y-%m-%d')

    endpoint = 'EmploymentIndicators'
    service = "https://api.stats.govt.nz/odata/v1"
    entity = "Observations" 
    query_option = f"$filter=Period ge {two_months_ago}"
    api_key = "dde082d59e0a4c49bf83f67ff6b9b032" #The API_key is public. No need to keep it secure.
    proxies = {}

    #Sending an API request
    Observations = odata.get_odata(service, endpoint, entity, query_option, api_key, proxies)

    #Cleaning the data
    columns_to_drop = ['ResourceID', 'Status', 'Label3', 'Label4', 'Label5', 'Label6']
    #all_data_from_month.drop(columns_to_drop, axis=1, inplace=True)
    Observations.drop(columns_to_drop, axis=1, inplace=True)
    
    #Code to save an example CSV
    #Observations.to_csv('employment_indicators', index=False)

    return(Observations)
