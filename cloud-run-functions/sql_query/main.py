
from flask import Flask, request, make_response, jsonify
import json
from google.cloud import bigquery

app = Flask(__name__)

@app.route('/sql_query', methods=['GET', 'POST'])
def sql_query(request):
    # Parse JSON data from the request body
    data = request.get_json()
    print(data)
    
    # Validate the presence of the 'query' parameter in the request
    if not data or 'query' not in data:
        return jsonify({"error": "Missing 'query' parameter"}), 400
    
    query = data['query']

    # Initialize the BigQuery client
    client = bigquery.Client()
    
    # Configure query job to limit the maximum bytes billed
    job_config = bigquery.QueryJobConfig(
        maximum_bytes_billed=100000000  # Set a limit to avoid excessive costs
    )
    
    try:
        # Clean up the query string to ensure it executes properly
        cleaned_query = (
            query
            .replace("\\n", " ")  # Replace escaped newlines with a space
            .replace("\n", "")     # Remove actual newline characters
            .replace("\\", "")     # Remove backslashes
        )
        
        # Execute the query using the BigQuery client
        query_job = client.query(cleaned_query, job_config=job_config)
        
        # Retrieve and format the query results
        api_response = query_job.result()
        api_response = str([dict(row) for row in api_response])
        api_response = api_response.replace("\\", "").replace("\n", "")
        
        # Return the query results as a JSON response
        return jsonify(api_response)
    
    except Exception as e:
        # Handle and return any errors that occur during query execution
        return jsonify(str(e))
