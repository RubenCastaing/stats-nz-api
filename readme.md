# Stats NZ API Integration
This prroject to collects data from different goverment sources and makes it easy to access from a single source. This repo reads employment indicators from Stats NZ. It cleans it, and put it into an SQLite database. This can then be queried via an API. This is hosted on a EC2 instance on AWS. It gets new data from Stats NZ at the start of each month. This is for a class project. The data avaliable is from March 2024 onwards.

## Accessing the API
Call http://54.253.55.30:8080/employment_indicators
Note the metadata is also in the JSON, it is at the bottom.


## Features
- Fetches data from employment_indicators of the Stats NZ API each month.
- Renames columns for better readability.
- Stores data in an SQLite database.
- Contains logging to check who logged in.
- Restarts the API in case it goes down

## Installation on an AWS EC2 instance

1. **Clone the repository**:
    ```bash
    git clone https://github.com/RubenCastaing/stats-nz-api.git
    cd stats-nz-api
    ```

2. **Update Package List and Install python3-venv**:
    ```bash
    sudo apt update
    sudo apt install python3-venv
    ```

3. **Create a virtual environment**:
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
    ```

4. **Install dependencies**:
    ```bash
    pip install pandas requests flask gunicorn
    ```

5. **Set up the SQLite database and the API**:
    Run both the create_database and create_api files.
    ```bash
    python create_database.py
    python main.py
    gunicorn --bind 0.0.0.0:8080 create_api:app
    ```
    Gunicorn is safer for running a production enviroment. Simply run create_api.py if running locally.
    Note that ports may be an issue. This currently runs on port 8080. Make sure you don't run multiple processes on the same port

6. **Run a cron job**:
    This calls main.py each at the start of the month at 2:30am and checks the API keeps running every 10 min. It restarts if it goes down.
   ```bash
    crontab -e # then select nano
    30 2 1 * * /home/ubuntu/stats-nz-api/myenv/bin/python /home/ubuntu/stats-nz-api/main.py >> /home/ubuntu/stats-nz-api/cron_test.log 2>&1
   */10 * * * * /home/ubuntu/stats-nz-api/myenv/bin/python /home/ubuntu/stats-nz-api/health_check.py >> /home/ubuntu/stats-nz-api/health_c>
    ```
## Logging
This has logging for checking that cron is working and checking API requests.

    cat /home/ubuntu/api_logs.log #User logs
    cat /home/ubuntu/stats-nz-api/cron_test.log #Cron logs
    #Use tail -f to veiw the logs in real time
    
Logs look like this
2024-05-30 01:44:40,219 - create_api - INFO - Received request: 202.36.179.72 GET http://54.253.55.30:8080/employment_indicators
2024-05-30 01:44:40,223 - create_api - INFO - Data retrieved successfully for label1=None, geo=None
2024-05-30 01:44:40,226 - create_api - INFO - Response status: 200 OK

I tried setting up elastic search for visulising logs but this broke the project when it ran out of memory.

## Security

## Contact
Ruben Castaing castaingruben@gmail.com

