from flask import Flask, jsonify, request
import config
import modules.databases.airtable_client.airtable_client as airtable_client
from modules.chat_gpt.chat_gpt import ChatGPT
from test_discovery import find_untested_modules, get_module_info
import os
from dotenv import load_dotenv

api_key = config.AIRTABLE_PERSONAL_ACCESS_TOKEN

load_dotenv()
python_path = os.environ.get("PYTHONPATH")

app = Flask(__name__)
app.config['ENV'] = 'development'
app.env = 'development'
app.debug = True
modules_dir = './modules'
tests_dir = './tests'

@app.route('/get_data/<table_name>')
def get_data(table_name):
    # Create an instance of AirtableClient
    print("getting")
    airtable_instance = airtable_client.AirtableClient(api_key)
    print("instanced", airtable_instance)
    # Create an instance of the Read inner class
    read_instance = airtable_instance.Read(airtable_instance)
    print("read instanced", read_instance)
    records = read_instance.get_records(table_name)
    return jsonify(records)

@app.route('/config')
def show_config():
    return jsonify(
        environment=app.env,
        debug=app.debug,
    )
@app.route('/generate_tests')
def generate_tests():
    try:
        untested_modules = find_untested_modules(modules_dir, tests_dir)
        chat_gpt = ChatGPT()
        tests_data = {}  # Dictionary to hold generated tests for each module
        for untested_module in untested_modules:
            module_info = get_module_info(untested_module)
            generated_test = chat_gpt.generate_test(module_info)
            tests_data[untested_module] = generated_test  # Store generated tests in the dictionary
        return jsonify({"status": "success", "tests": tests_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


#curl http://127.0.0.1:5000/get_data/tables
