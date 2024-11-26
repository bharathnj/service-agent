# 🚀 Service Agent  
The **Service Agent** streamlines case management and FAQ handling for enterprises, eliminating manual intervention and improving operational efficiency. It leverages the following technologies:  

- 🤖 **Vertex AI Agent Builder**  
- 🗃️ **BigQuery**  
- 🐍 **Cloud Run Functions (Python)**  
- ☁️ **Google Cloud Storage**  
- 🌐 **Web App (Flask)**  

---

## ⚙️ Prerequisites  

### 🗂️ BigQuery Tables  
Ensure the following BigQuery tables are created before proceeding:  

#### **Sales_case**  
Schema:  
`SaleID | Date | CustomerName | Product | Quantity | UnitPrice | TotalAmount | Salesperson | Region`  

#### **Support_case**  
Schema:  
`CaseID | CustomerName | IssueSummary | Priority | Status | CreatedDate | ResolvedDate | AssignedTo`  

Prepare your data using the provided CSV files and ingest it into the respective tables.  

---

## 🐍 Python Cloud Run Functions  

1. Navigate to **Cloud Run Functions** in the Google Cloud Console to create a new function:  
   [➕ Add Cloud Function](https://console.cloud.google.com/functions/add)  

2. Provide the function names:  
   - `get_tables`  
   - `list_table`  
   - `sql_query`  

   Choose the region as `us-central1`. Set authentication to **Allow unauthenticated invocations** and click **NEXT**.  

3. Select the latest Python runtime and use the **Inline Editor** for source code.  

4. Copy the contents of the `main.py` and `requirements.txt` files from this project into the respective fields in the editor.  

5. Replace all instances of `<<PROJECT_ID>>` with your project ID.  

6. Deploy the Cloud Function and test it using the **TESTING** tab. For deployment errors, check the **LOGS** tab.  

---

## 🔍 How Does It Work?  
<img width="800" alt="Screenshot 2024-11-26 at 2 23 44 PM" src="https://github.com/user-attachments/assets/ef63beb1-da16-4751-a808-e2405217dbb4">

---

## 🌐 Integrate the Service Agent into the Website  

1. Open **Agent Builder** and select your agent.  
2. Navigate to the **Main Menu** and click on **Integrations**.  
3. Under the **Text-Based** section, select **Conversational Messenger** and click **Connect**.  
4. Choose the desired UI and submit. A code snippet will be generated.  
5. Copy the generated code snippet and embed it into your website.  
   
<img width="551" alt="Screenshot 2024-11-26 at 2 30 50 PM" src="https://github.com/user-attachments/assets/286097ad-b75d-408a-b2e8-87cbcfd2cbec">



## 📖 Read More  

Check out the detailed blog post on Medium:  
[Service Agent Powered by Vertex AI](https://medium.com/@njbharathkumar/service-agent-powered-by-vertex-ai-a4e137ccdae6)  

