import stats_odata as odata

service = "https://api.stats.govt.nz/odata/v1"
endpoint = "EmploymentIndicators"
entity = "Observations" 
query_option = "$select=ResourceID,Period,Duration,Label1,Label2,Value,Unit,Measure,Multiplier&$top=10"
api_key = "xxxxxxxxxxxxxxxxxxxxx"
proxies = {}

Observations = odata.get_odata(service, endpoint, entity, query_option, api_key, proxies)
print(Observations)