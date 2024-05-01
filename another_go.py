import urllib.request, json
import stats_odata as odata

try:
    url = "https://api.stats.govt.nz/opendata/v1/data.json"

    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': 'dde082d59e0a4c49bf83f67ff6b9b032',
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    print(response.getcode())
    print(response.read())
except Exception as e:
    print(e)

service = "https://api.stats.govt.nz/odata/v1"
endpoint = "EmploymentIndicators"
entity = "Observations" 
query_option = "$select=ResourceID,Period,Duration,Label1,Label2,Value,Unit,Measure,Multiplier&$top=10"
api_key = "dde082d59e0a4c49bf83f67ff6b9b032"
proxies = {}

Observations = odata.get_odata(service, endpoint, entity, query_option, api_key, proxies)
print(Observations)