from flask import Flask, jsonify
import airtable_client

app = Flask(__name__)

@app.route('/get_data/<table_name>')
def get_data(table_name):
    records = airtable_client.get_records(table_name)
    return jsonify(records)

if __name__ == '__main__':
    app.run(debug=True)

#curl http://127.0.0.1:5000/get_data/tables
