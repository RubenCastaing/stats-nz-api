import urllib.request, json
import stats_odata as odata

List_of_endpoints = ['EmploymentIndicators', 'OverseasCargo', 'Covid-19Indicators', 'InternationalMigration', 'HouseholdLabourForceSurvey', '2018Census-PopulationDwellings', 'OverseasMerchandiseTrade', 'InternationalTravel', 'NationalAccounts']
Dictionary_of_columns = {Employment_Indicators: }

service = "https://api.stats.govt.nz/odata/v1"
entity = "Observations" 
query_option = "$top=10"
api_key = "dde082d59e0a4c49bf83f67ff6b9b032"
proxies = {}

for endpoint in List_of_endpoints:
    Observations = odata.get_odata(service, endpoint, entity, query_option, api_key, proxies
    print(Observations)
    output_string = endpoint + '.csv'
    Observations.to_csv(output_string, index=False)
