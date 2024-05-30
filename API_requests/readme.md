# API_requests
Each file in API request sends an API request to Stats NZ. These all get pulled together in main.py. I've set up EmploymentIndicators to be scraped automaticly on AWS. Other endpoints are similar but require slightly difffernt wrangling. Having them all in the same folder makes scaling up eaiser.

Each request returns a cleaned dataframe containing the relevant data.

## Possible endpoints
#There are 9 endpoints as of 14/05/2024. These are:
#EmploymentIndicators
#OverseasCargo
#Covid-19Indicators
#InternationalMigration
#HouseholdLabourForceSurvey
#2018Census-PopulationDwellings
#OverseasMerchandiseTrade
#InternationalTravel
#NationalAccounts

When starting the project, the endpoints were not easy to access by Stats NZ. I sent them working code which they have included into their Github documentation. 

https://github.com/StatisticsNZ/open-data-api/blob/main/Python/get-odata-catalogue.py