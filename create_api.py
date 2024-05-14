from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def query_database(label1):
    conn = sqlite3.connect('stats_nz_data.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM EmploymentData WHERE Label1 = ?", (label1,))
    rows = cur.fetchall()
    columns = [column[0] for column in cur.description]
    results = [dict(zip(columns, row)) for row in rows]
    conn.close()
    return results

@app.route('/get_industries', methods=['GET'])
def get_industries():
    label1 = request.args.get('label1', 'All industries')  # Default to 'All industries' if no label provided
    results = query_database(label1)
    if results:
        return jsonify(results)
    else:
        return jsonify({"error": "No data found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
