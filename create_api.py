from flask import Flask, jsonify, request
import sqlite3
import logging
import json
import os

# Configure logging
logging.basicConfig(
    filename='/home/ubuntu/api_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

# Log details of incoming requests
@app.before_request
def log_request_info():
    app.logger.info('Received request: %s %s %s', request.remote_addr, request.method, request.url)

# Log details of outgoing responses
@app.after_request
def log_response_info(response):
    app.logger.info('Response status: %s', response.status)
    return response

def validate_input(input_value):
    # Add your validation logic here
    if not input_value.isalnum():
        raise ValueError("Invalid input")
    return input_value

def query_employment_data(label1=None, geo=None):
    conn = sqlite3.connect('stats_nz_data.db')
    cur = conn.cursor()
    query = "SELECT * FROM EmploymentData WHERE 1=1"
    params = []
    
    if label1:
        query += " AND Label1 = ?"
        params.append(label1)
    
    if geo:
        query += " AND Geo = ?"
        params.append(geo)
    
    cur.execute(query, params)
    rows = cur.fetchall()
    columns = [column[0] for column in cur.description]
    results = [dict(zip(columns, row)) for row in rows]
    conn.close()
    return results

def load_metadata():
    metadata_path = os.path.join(os.path.dirname(__file__), 'API_requests', 'metadata.json')
    app.logger.info('Attempting to load metadata from %s', metadata_path)
    try:
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
        app.logger.info('Metadata loaded successfully')
        return metadata
    except FileNotFoundError:
        app.logger.error('Metadata file not found at %s', metadata_path)
        return {"error": "Metadata file not found"}
    except json.JSONDecodeError:
        app.logger.error('Error decoding JSON from metadata file at %s', metadata_path)
        return {"error": "Error decoding JSON from metadata file"}

@app.route('/employment_indicators', methods=['GET'])
def get_employment_indicators():
    label1 = request.args.get('label1')
    geo = request.args.get('geo')

    if label1:
        label1 = validate_input(label1)
    if geo:
        geo = validate_input(geo)

    results = query_employment_data(label1, geo)
    metadata = load_metadata()

    response = {
        "metadata": metadata,
        "data": results
    }

    if results:
        app.logger.info('Data retrieved successfully for label1=%s, geo=%s', label1, geo)
        return jsonify(response)
    else:
        app.logger.warning('No data found for label1=%s, geo=%s', label1, geo)
        return jsonify({"error": "No data found", "metadata": metadata}), 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
