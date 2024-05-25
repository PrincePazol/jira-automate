# Import the necessary packages
import requests
from requests.auth import HTTPBasicAuth
import os
import json
from dotenv import load_dotenv


# Load env files
load_dotenv()

# Extract the user credentials
jira_url = os.getenv("JIRA_URL")
jira_token = os.getenv("JIRA_TOKEN")
jira_email = os.getenv("JIRA_EMAIL")

auth = HTTPBasicAuth(jira_email, jira_token)
headers = {
    "Accept": "application/json"
}

# Make a GET request
response = requests.get(url=f"{jira_url}/rest/api/3/project", 
                        auth=auth, 
                        headers=headers)
print(response.json())
print(jira_email)
