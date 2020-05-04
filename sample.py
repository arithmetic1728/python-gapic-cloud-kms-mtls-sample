import google.api_core.client_options as ClientOptions
import google.api_core.path_template
from google.auth.transport import mtls
from google.cloud.kms import KeyManagementServiceClient
from google.cloud.kms import ListKeyRingsRequest
import google.oauth2.credentials


# Fill in your project_id.
project_id = "your_project_id"


def list_key_rings():
    # Get the user access token.
    cred = google.oauth2.credentials.UserAccessTokenCredentials()

    # If device client certificate exists, it will be used to establish mutual TLS connection,
    # and the pubsub client will automatically switch to pubsub mtls endpoint.
    # If device client certificate doesn't exists, mutual TLS connection will not be established,
    # and the default mtls endpoint will be used.
    # The existence of device client certificate can be checked via
    # 'mtls.has_default_client_cert_source()'. You can call 'mtls.default_client_cert_source()'
    # to get a callback, which produces the client certificate on execution.
    if mtls.has_default_client_cert_source():
        print(
            "Default client cert source is found. It will be used to create mutual TLS channel"
        )
        callback = mtls.default_client_cert_source()
    else:
        print(
            "Default client cert source is not found. Mutual TLS channel will not be created"
        )
        callback = None

    # Pass the callback to ClientOptions, and pass the ClientOptions to KeyManagementServiceClient.
    client_options = ClientOptions.ClientOptions(client_cert_source=callback)
    client = KeyManagementServiceClient(credentials=cred, client_options=client_options)

    # Lists keys in the "global" location.
    parent = "projects/{project}/locations/global".format(project)

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
