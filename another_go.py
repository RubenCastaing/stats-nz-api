import urllib.request, json
import stats_odata as odata

service = "https://api.stats.govt.nz/odata/v1"
endpoint = "EmploymentIndicators"
entity = "Observations" 
query_option = "$select=ResourceID,Period,Duration,Label1,Label2,Value,Unit,Measure,Multiplier&$top=10"
api_key = "dde082d59e0a4c49bf83f67ff6b9b032"
proxies = {}

#Observations = odata.get_odata(service, endpoint, entity, query_option, api_key, proxies)
#print(Observations)

