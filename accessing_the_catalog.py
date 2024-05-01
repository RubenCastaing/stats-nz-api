import urllib.request, json
import stats_odata as odata

try:
    url = "https://api.stats.govt.nz/opendata/v1/data.json"
    
    Observations = odata.get_odata(url, proxies)
    print(Observations)
    
    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    print(response.getcode())
    print(response.read())
except Exception as e:
    print(e)