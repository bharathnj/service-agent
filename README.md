# Service Agent
The Service Agent streamlines case management and FAQ handling for enterprises, eliminating manual intervention and improving operational efficiency. Leveraging technologies below. 
* Vertex AI Agent Builder
* BigQuery
* Cloud run Functions (Python)
* Google Cloud Storage
* Web App (Flask)


## Make sure BigQuery tables created before you begin with this step.

We have created 2 CSV files for data.

Schema and Data Ingestion for **Sales_case**:
SaleID	Date	CustomerName	Product	Quantity	UnitPrice	TotalAmount	Salesperson	Region

Schema and Data Ingestion for **Support_sase**:
Case ID	Customer Name	Issue Summary	Priority	Status	Created Date	Resolved Date	Assigned To 

Now that the schema is defined, let’s go ahead and ingest data into the table.

## Python Cloud Run Functions

1. Go to Cloud Run Functions in Google Cloud Console to CREATE a new Cloud Run Function or use the link: https://console.cloud.google.com/functions/add. 

2. Provide Function Name “get_tables”, "list_table", "sql_query" and choose Region as “us-central1”. Set Authentication to “Allow unauthenticated invocations” and click NEXT. Choose Python latest version as runtime and Inline Editor for the source code.

3. Copy the contents of the Python file (main.py and requiremnts.txt) from this project and replace the ones in your new Google Cloud Python Cloud Run Function.

4. Remember to change the <<PROJECT_ID>> placeholder where its applicable.

5. Deploy the Cloud Function and test it from the TESTING tab of your newly deployed Cloud Functions (If there are deployment errors you can see them in the LOGS tab).


## How Does it work?

<img width="1111" alt="Screenshot 2024-11-26 at 1 10 11 PM" src="https://github.com/user-attachments/assets/b72e08cc-c610-45a7-8f51-b476ee95603e">


## Integrate the Service Agent into the website
<img width="885" alt="Screenshot 2024-11-26 at 1 12 43 PM" src="https://github.com/user-attachments/assets/f4215723-7221-4e98-9f1e-f41491374aa5">

