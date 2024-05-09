import urllib.request, json
import pandas as pd

api_key = "dde082d59e0a4c49bf83f67ff6b9b032"

try:
    url = "https://api.stats.govt.nz/opendata/v1/data.json"
    
    hdr = {
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': api_key, 
        'user-agent': ''
    }

    req = urllib.request.Request(url, headers=hdr)
    req.get_method = lambda: 'GET'
    with urllib.request.urlopen(req) as response:
        # Read the response and decode it
        response_data = response.read().decode('utf-8')

        # Load the JSON into a Python dictionary
        data = json.loads(response_data)

        # Use json_normalize to convert the nested JSON to a flat table
        df = pd.json_normalize(data, record_path=['dataset'])

        # Display the DataFrame
        pd.set_option('display.max_rows', 100)
        print(df)
        df.to_csv('stats_nz_data.csv', index=False)


except Exception as e:
    print(e)
