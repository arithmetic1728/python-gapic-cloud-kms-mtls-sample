from google.cloud.kms import KeyManagementServiceClient
from google.cloud.kms import ListKeyRingsRequest
import google.oauth2.credentials
import google.auth.transport.requests


# Fill in your project_id.
project_id = "dcatest-281318"

# Fill in the 3LO client ID json file.
json_file_path = "/usr/local/google/home/sijunliu/wks/creds/client_secret_web.json"

from flask import Flask, redirect, request

app = Flask(__name__)

from google_auth_oauthlib.flow import Flow

flow = Flow.from_client_secrets_file(
    json_file_path,
    scopes=[
        'openid', 
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/cloud-platform',
        'https://www.googleapis.com/auth/appengine.admin',
        'https://www.googleapis.com/auth/compute', 
        'https://www.googleapis.com/auth/accounts.reauth'
    ],
    redirect_uri='http://localhost:3000/auth')
creds = None

@app.route("/")
def login():
    # Tell the user to go to the authorization URL.
    auth_url, _ = flow.authorization_url(prompt='consent')
    return redirect(auth_url)

@app.route("/auth")
def get_code():
    code = request.args.get('code')
    flow.fetch_token(code=code)
    creds = flow.credentials
    print(creds.token)
    client = KeyManagementServiceClient(credentials=creds)
    

    # Lists keys in the "global" location.
    parent = "projects/{project}/locations/{location}".format(
        project=project_id, location="global"
    )

    # Lists key rings
    response = client.list_key_rings(parent=parent)
    response_list = list(response)

    if len(response_list) > 0:
        print("Key rings:")
        for key_ring in response_list:
            print(key_ring.name)
    else:
        print("No key rings found.")
