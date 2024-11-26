from flask import Flask, request, make_response, jsonify
import json
from google.cloud import bigquery

app = Flask(__name__)

def schemafield_to_dict(schema):
    """Converts a list of SchemaField objects into a list of dictionaries"""
    return [
        {
            'name': field.name,
            'field_type': field.field_type,
            'mode': field.mode,
            'description': field.description,
            'fields': schemafield_to_dict(field.fields) if field.fields else []
        }
        for field in schema
    ]

@app.route('/get_table', methods=['GET'])
def get_table(request):
    # Extract table_id from query parameters
    print(f'Request: {request}')
    try:
        table_id = request.args.get('table_id')
    except Exception as e:
        print(f'Error {e}')
        return make_response(jsonify({"error": "Invalid JSON payload"}), 400)

    # Ensure table_id parameter is provided
    if not table_id:
        return make_response(jsonify({"error": "Missing table_id parameter"}), 400)
    
    print(f'Table id: {table_id}')
    
    # Initialize BigQuery client
    client = bigquery.Client()

    #  Attempt to fetch the table details from BigQuery
    try:
        table_ref = client.get_table(table_id)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 404)

    api_response = {
        "description": table_ref.description,
        "schema": schemafield_to_dict(table_ref.schema),
        "num_rows": table_ref.num_rows,
    }
    
    return jsonify(api_response)
