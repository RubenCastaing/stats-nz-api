# Stats NZ API Integration


This project is a small part of Data engineering class project to collect data from many
different goverment sources and make it easy to access from a single source. This repo reads employment indicators from Stats Nz. It cleans it, and put it into an SQLite database. This can then be queried via an API. This is hosted on a EC2 instance on AWS. It gets new data from stats_nz at the start of each month. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contact](#contact)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/RubenCastaing/stats-nz-api.git
    cd stats-nz-api
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the SQLite database and API**:
    ```bash
    python create_database.py
    python create_api.py
    ```

5. **Run a cron job to call main.py each month**:
    ```bash
    #This loads the data from Stats NZ
    python create_database.py
    python create_api.py
    ```

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

