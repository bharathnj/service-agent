# Service Agent
The Service Agent streamlines case management and FAQ handling for enterprises, eliminating manual intervention and improving operational efficiency. Leveraging cutting-edge technologies like BigQuery, Google Cloud Storage, and Vertex AI, the Service Agent ensures seamless performance, scalability, and real-time query handling.

## Make sure the Sales and Support cases are created before you begin with this step.

We have created 2 CSV files for data.

Schema and Data Ingestion for Sales_case:
SaleID	Date	CustomerName	Product	Quantity	UnitPrice	TotalAmount	Salesperson	Region

Schema and Data Ingestion for Support_sase:
Case ID	Customer Name	Issue Summary	Priority	Status	Created Date	Resolved Date	Assigned To 

Now that the schema is defined, let’s go ahead and ingest data into the table.

## Python Cloud Run Functions

1. Go to Cloud Functions in Google Cloud Console to CREATE a new Cloud Function or use the link: https://console.cloud.google.com/functions/add. 

2. Provide Function Name “get_tables”, "list_table", "sql_query" and choose Region as “us-central1”. Set Authentication to “Allow unauthenticated invocations” and click NEXT. Choose Python latest version as runtime and Inline Editor for the source code.

3. Copy the contents of the Python file (main.py and requiremnts.py) from this project and replace the ones in your new Google Cloud Java Cloud Function.

4. Remember to change the <<PROJECT_ID>> placeholder where its applicable.

5. Deploy the Cloud Function and test it from the TESTING tab of your newly deployed Cloud Functions (If there are deployment errors you can see them in the LOGS tab).

