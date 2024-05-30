import logging
from flask import Flask, jsonify, request
import sqlite3

# Configure logging
logging.basicConfig(
    filename='/var/log/api_logs.log',  # Path to your log file
    level=logging.INFO,                # Log level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Log format
)

app = Flask(__name__)

# Database query function
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

# API route
@app.route('/employment_indicators', methods=['GET'])
def get_employment_indicators():
    label1 = request.args.get('label1')
    geo = request.args.get('geo')
    results = query_employment_data(label1, geo)
    
    if results:
        app.logger.info('Data retrieved successfully for label1=%s, geo=%s', label1, geo)
        return jsonify(results)
    else:
        app.logger.warning('No data found for label1=%s, geo=%s', label1, geo)
        return jsonify({"error": "No data found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
