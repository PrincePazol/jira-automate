from fastapi import FastAPI
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os


# Initialize application
app = FastAPI()

# Load .env variable
load_dotenv()
jira_url = os.getenv("JIRA_URL")
jira_email = os.getenv("JIRA_EMAIL")
jira_token = os.getenv("JIRA_TOKEN")

# Authentication with Jira API
auth = HTTPBasicAuth(jira_email, jira_token)

@app.post("/createJira")
def createJira():
    """Create jira tickets with when administrator 
        comments a GitHub issue with /jira."""
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "Jira ticket created with API",
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
        "id": "10006"
        },
        "project": {
        "key": "PP"
        },
        "summary": "Main order flow broken",
    "update": {}
    } )

    # Make a POST request to Jira
    response = requests.post(url=jira_url,
                             data=payload,
                             headers=headers,
                             auth=auth)

    # Return a response to the user
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
