import google.api_core.client_options as ClientOptions
import google.api_core.path_template
from google.auth.transport import mtls
from google.cloud.kms import KeyManagementServiceClient
from google.cloud.kms import ListKeyRingsRequest
import google.oauth2.credentials


# Fill in your project_id.
project_id = "<FILL IN PROJECT ID>"


def list_key_rings():
    # Get the user access token.
    cred = google.oauth2.credentials.UserAccessTokenCredentials()

    client = KeyManagementServiceClient(credentials=cred)

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


if __name__ == "__main__":
    list_key_rings()
