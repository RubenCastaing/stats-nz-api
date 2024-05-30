import requests
import subprocess

#This script checks if the API is running. If it is not, it will restart it.
#There is a Cron job that runs this file every 5 min.
#This is set up for Ubuntu, some changes may be needed for other operating systems

# URL to check
URL = "http://localhost:8080/employment_indicators"

try:
    # Send a GET request to the API
    response = requests.get(URL)
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        print("API is working fine.")
    else:
        print("API is not working. Status Code:", response.status_code)
        raise Exception("API returned a non-200 status code.")
except Exception as e:
    print("Error occurred:", e)
    
    # Restart the API using Gunicorn
    print("Restarting the API...")
    # Kill the existing Gunicorn process
    subprocess.run(["pkill", "-f", "gunicorn"])
    # Start a new Gunicorn process
    subprocess.Popen(["/home/ubuntu/stats-nz-api/myenv/bin/gunicorn", "--bind", "0.0.0.0:8080", "create_api:app"])
