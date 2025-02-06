# import requests
# from requests.auth import HTTPBasicAuth

# class CloudantClient:
#     def __init__(self, account_name: str, api_key: str):
#         self.base_url = f"https://293e9a3b-b044-4b74-a92a-3b331de2350a-bluemix.cloudantnosqldb.appdomain.cloud"
#         self.auth = HTTPBasicAuth("apikey", api_key)

#     def create_database(self, db_name: str) -> dict:
#         url = f"{self.base_url}/{db_name}"
#         response = requests.put(url, auth=self.auth)
#         return response.json()

#     def add_document(self, db_name: str, document: dict) -> dict:
#         url = f"{self.base_url}/{db_name}"
#         response = requests.post(url, json=document, auth=self.auth)
#         return response.json()

#     def get_document(self, db_name: str, doc_id: str) -> dict:
#         url = f"{self.base_url}/{db_name}/{doc_id}"
#         response = requests.get(url, auth=self.auth)
#         return response.json()

#     def delete_document(self, db_name: str, doc_id: str, rev: str) -> dict:
#         url = f"{self.base_url}/{db_name}/{doc_id}?rev={rev}"
#         response = requests.delete(url, auth=self.auth)
#         return response.json()

# if __name__ == "__main__":
#     # Replace with your IBM Cloudant account information
#     ACCOUNT_NAME = "293e9a3b-b044-4b74-a92a-3b331de2350a-bluemix"
#     API_KEY = "0Peu2FUOWZpa1C-oR7sKO-F4wvBaU7jcI6n7KJL1vHiS"

#     cloudant_client = CloudantClient(ACCOUNT_NAME, API_KEY)

#     # Example usage
#     database_name = "testusercloudant_db"
#     document = {"name": "John Doe", "age": 30, "city": "New York"}

#     # Create database
#     print("Creating database...")
#     create_db_response = cloudant_client.create_database(database_name)
#     print(create_db_response)

#     # Add a document
#     print("Adding document...")
#     add_doc_response = cloudant_client.add_document(database_name, document)
#     print(add_doc_response)

#     # Get the document
#     doc_id = add_doc_response.get("id")
#     print("Fetching document...")
#     get_doc_response = cloudant_client.get_document(database_name, doc_id)
#     print(get_doc_response)

#     # Delete the document
#     # rev_id = add_doc_response.get("rev")
#     # print("Deleting document...")
#     # delete_doc_response = cloudant_client.delete_document(database_name, doc_id, rev_id)
#     # print(delete_doc_response)

#     print("Done.")

# # curl -X GET "https://293e9a3b-b044-4b74-a92a-3b331de2350a-bluemix.cloudantnosqldb.appdomain.cloud/_all_dbs" -u "apikey:0Peu2FUOWZpa1C-oR7sKO-F4wvBaU7jcI6n7KJL1vHiS"





# from cloudant.client import Cloudant
# from cloudant.error import CloudantException
# from cloudant.result import Result, ResultByKey

# # Cloudant credentials
# username = "293e9a3b-b044-4b74-a92a-3b331de2350a-bluemix"
# api_key = "0Peu2FUOWZpa1C-oR7sKO-F4wvBaU7jcI6n7KJL1vHiS"
# url = "https://293e9a3b-b044-4b74-a92a-3b331de2350a-bluemix.cloudantnosqldb.appdomain.cloud"

# # Connect to Cloudant
# client = Cloudant(username, api_key, url=url)
# client.connect()

# # Create or connect to a database
# database_name = "testclientcloudant_db"
# if database_name not in client.all_dbs():
#     db = client.create_database(database_name)
# else:
#     db = client[database_name]

# # Create a document
# document = {
#     "name": "John Doe",
#     "age": 30,
#     "email": "john.doe@example.com"
# }

# # Save the document to the database
# new_document = db.create_document(document)
# if new_document.exists():
#     print(f"Document created with ID: {new_document['_id']}")

# # Retrieve all documents
# result_collection = Result(db.all_docs, include_docs=True)
# print("All documents in the database:")
# for doc in result_collection:
#     print(doc)

# # Query a specific document by ID
# doc_id = new_document['_id']
# specific_doc = db[doc_id]
# print(f"Retrieved document: {specific_doc}")

# # Disconnect from Cloudant
# client.disconnect()







import requests

class CloudantClient:
    def __init__(self, base_url: str, iam_token: str):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {iam_token}",
            "Content-Type": "application/json"
        }

    def create_database(self, db_name: str) -> dict:
        url = f"{self.base_url}/{db_name}"
        response = requests.put(url, headers=self.headers)
        return response.json()

    def add_document(self, db_name: str, document: dict) -> dict:
        url = f"{self.base_url}/{db_name}"
        response = requests.post(url, json=document, headers=self.headers)
        return response.json()

    def get_document(self, db_name: str, doc_id: str) -> dict:
        url = f"{self.base_url}/{db_name}/{doc_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def delete_document(self, db_name: str, doc_id: str, rev: str) -> dict:
        url = f"{self.base_url}/{db_name}/{doc_id}?rev={rev}"
        response = requests.delete(url, headers=self.headers)
        return response.json()


def get_iam_token(api_key: str) -> str:
    url = "https://iam.cloud.ibm.com/identity/token"
    data = {
        "apikey": api_key,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json().get("access_token")


if __name__ == "__main__":
    ACCOUNT_NAME = "293e9a3b-b044-4b74-a92a-3b331de2350a-bluemix.cloudantnosqldb.appdomain.cloud"
    API_KEY = "0Peu2FUOWZpa1C-oR7sKO-F4wvBaU7jcI6n7KJL1vHiS"
    BASE_URL = f"https://293e9a3b-b044-4b74-a92a-3b331de2350a-bluemix.cloudantnosqldb.appdomain.cloud"

    print("Fetching IAM token...")
    iam_token = get_iam_token(API_KEY)

    cloudant_client = CloudantClient(BASE_URL, iam_token)

    # Example usage
    database_name = "test_db"
    document = {"name": "John Doe", "age": 30, "city": "New York"}

    print("Creating database...")
    print(cloudant_client.create_database(database_name))

    print("Adding document...")
    print(cloudant_client.add_document(database_name, document))
    
    print("Done")
