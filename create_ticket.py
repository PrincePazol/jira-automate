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

payload = json.dumps({
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10009"
    },
    "project": {
      "key": "QQ"
    },
    "summary": "Second JIRA Ticket"
  }
})

response = requests.post(
   jira_url,
   data=payload,
   headers=headers,
   auth=auth
)


print(response.json())