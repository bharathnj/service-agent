from flask import Flask, request, make_response, jsonify
import json
from google.cloud import bigquery

app = Flask(__name__)

@app.route('/list_tables', methods=['GET'])
def list_tables(request):
    # Retrieve the 'dataset_id' parameter from the query string
    dataset_id = request.args.get('dataset_id')
    
    # Validate that 'dataset_id' is provided
    if not dataset_id:
        return make_response(json.dumps({"error": "Missing dataset_id parameter"}), 400)
    
    # Initialize the BigQuery client
    client = bigquery.Client()
    
    # Reference the dataset using the provided dataset ID
    dataset_ref = client.dataset(dataset_id)
    
    # Retrieve the list of tables within the specified dataset
    api_response = client.list_tables(dataset_ref)
    
    # Extract table IDs from the response and format them into a list
    table_ids = str([table.table_id for table in api_response])
    
    # Prepare the output with the table IDs
    output = {
        "tables": table_ids
    }
    
    # Return the output as a JSON response
    return jsonify(output)
