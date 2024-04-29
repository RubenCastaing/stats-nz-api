import stats_odata as odata

api_key = 'dde082d59e0a4c49bf83f67ff6b9b032'
service = "https://api.stats.govt.nz/odata/v1"
endpoint = "EmploymentIndicators"
entity = ""
query_option = ""
proxies = {}

ServiceEntities = odata.get_odata(service, endpoint, entity, query_option, api_key, proxies)

print(ServiceEntities)

service = "https://api.stats.govt.nz/odata/v1"
endpoint = "EmploymentIndicators"
entity = "Observations" 
query_option = "$select=ResourceID,Period,Duration,Label1,Label2,Value,Unit,Measure,Multiplier&$top=10"
proxies = {}

Observations = odata.get_odata(service, endpoint, entity, query_option, api_key, proxies)
print(Observations)

service = "https://api.stats.govt.nz/odata/v1"
endpoint = "EmploymentIndicators"
entity = "Resources"
query_option = "$select=ResourceID,Title,Var1,Var2,Modified,Frequency&$top=10"
proxies = {}

Resources = odata.get_odata(service, endpoint, entity, query_option, api_key, proxies)

print(Resources)

service = "https://api.stats.govt.nz/odata/v1"
endpoint = "EmploymentIndicators"
entity = "Observations"
query_option = """$filter=(
                        ResourceID eq 'MEI1.1' and
                        Period ge 2020-08-31 and
                        Label2 eq 'Actual' and
                        Duration eq 'P1M'
                          )
                &$select=ResourceID,Period,Duration,Label1,Label2,Value,Unit,Measure,Multiplier
                &$top=10"""

Observations = odata.get_odata(service, endpoint, entity, query_option, api_key, proxies)

print(Observations)
