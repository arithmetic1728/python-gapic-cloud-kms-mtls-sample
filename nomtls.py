import os


def run_quickstart():
    # [START kms_quickstart]
    # Imports the Google APIs client library
    from google.cloud import kms_v1

    # Your Google Cloud Platform project ID
    project_id = "YOUR_PROJECT_ID"
    # [END kms_quickstart]
    project_id = os.environ["GCLOUD_PROJECT"]
    # [START kms_quickstart]

    # Lists keys in the "global" location.
    location = "global"

    # Creates an API client for the KMS API.
    client = kms_v1.KeyManagementServiceClient()

    # The resource name of the location associated with the key rings.
    parent = client.location_path(project_id, location)

    # Lists key rings
    response = client.list_key_rings(parent)
    response_list = list(response)

    if len(response_list) > 0:
        print("Key rings:")
        for key_ring in response_list:
            print(key_ring.name)
    else:
        print("No key rings found.")
    # [END kms_quickstart]


if __name__ == "__main__":
    run_quickstart()
