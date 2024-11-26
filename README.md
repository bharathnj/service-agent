# Service Agent
The Service Agent streamlines case management and FAQ handling for enterprises, eliminating manual intervention and improving operational efficiency. Leveraging cutting-edge technologies like BigQuery, Google Cloud Storage, and Vertex AI, the Service Agent ensures seamless performance, scalability, and real-time query handling.


## Python Cloud Run Functions

1. Go to Cloud Functions in Google Cloud Console to CREATE a new Cloud Function or use the link: https://console.cloud.google.com/functions/add. 

2. Provide Function Name “service-agent” and choose Region as “us-central1”. Set Authentication to “Allow unauthenticated invocations” and click NEXT. Choose Java 11 as runtime and Inline Editor for the source code.

3. Copy the contents of the Python file (main.py and requiremnts.py) from this project and replace the ones in your new Google Cloud Java Cloud Function.

4. Remember to change the <<PROJECT_ID>> placeholder and the AlloyDB connection credentials in the Java class with your values.

5. Deploy the Cloud Function and test it from the TESTING tab of your newly deployed Cloud Functions (If there are deployment errors you can see them in the LOGS tab).


