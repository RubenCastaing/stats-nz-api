# Stats NZ API Integration
This prroject to collects data from different goverment sources and make it easy to access from a single source. This repo reads employment indicators from Stats NZ. It cleans it, and put it into an SQLite database. This can then be queried via an API. This is hosted on a EC2 instance on AWS. It gets new data from Stats NZ at the start of each month. This is for a class project.

## Accessing the API
Call http://54.253.55.30:8080/employment_indicators

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

   That should look like the following if working
   [2024-05-30 01:16:06 +0000] [2625] [INFO] Starting gunicorn 22.0.0
   [2024-05-30 01:16:06 +0000] [2625] [INFO] Listening at: http://0.0.0.0:8080 (2625)
   [2024-05-30 01:16:06 +0000] [2625] [INFO] Using worker: sync
   [2024-05-30 01:16:06 +0000] [2626] [INFO] Booting worker with pid: 2626

7. **Run a cron job to call main.py each month**:


## API Usage

1. **Fetch data and insert into the database**:
    ```bash
    python main.py
    ```

2. **Access the SQLite database**:
    The database file `stats_nz_data.db` will be created/updated in the project directory. You can use any SQLite client to query the data.

## Features

- Fetches data from multiple endpoints of the Stats NZ API.
- Renames columns for better readability.
- Stores data in an SQLite database.
- Scheduled to run in AWS.

## Contact
Ruben Castaing castaingruben@gmail.com

