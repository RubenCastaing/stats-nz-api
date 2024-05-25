from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

#This file creates the api.
#It only needs to be run once to set up the API.
#You may need to change the ports to run it locally or host it online 

def query_employment_data(label1=None, geo=None):
    conn = sqlite3.connect('stats_nz_data.db')
    cur = conn.cursor()
    #These allow for basic queries to the API.
    #They are mainly for testing as the central collection team doesn't need to query certain sections.
    #However, having this set up makes including new changes easier.
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

@app.route('/employment_indicators', methods=['GET'])
def get_employment_indicators():
    label1 = request.args.get('label1')
    geo = request.args.get('geo')
    results = query_employment_data(label1, geo)
    
    if results:
        return jsonify(results)
    else:
        return jsonify({"error": "No data found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) #These are the ports
