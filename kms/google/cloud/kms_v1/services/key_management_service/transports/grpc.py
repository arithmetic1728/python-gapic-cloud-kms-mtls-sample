# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Callable, Dict, Tuple

from google.api_core import grpc_helpers   # type: ignore
from google import auth                    # type: ignore
from google.auth import credentials        # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore


import grpc  # type: ignore

from google.cloud.kms_v1.types import resources
from google.cloud.kms_v1.types import service

from .base import KeyManagementServiceTransport


class KeyManagementServiceGrpcTransport(KeyManagementServiceTransport):
    """gRPC backend transport for KeyManagementService.

    Google Cloud Key Management Service

    Manages cryptographic keys and operations using those keys.
    Implements a REST model with the following objects:

    -  [KeyRing][google.cloud.kms.v1.KeyRing]
    -  [CryptoKey][google.cloud.kms.v1.CryptoKey]
    -  [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
    -  [ImportJob][google.cloud.kms.v1.ImportJob]

    If you are using manual gRPC libraries, see `Using gRPC with Cloud
    KMS <https://cloud.google.com/kms/docs/grpc>`__.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    def __init__(self, *,
            host: str = 'cloudkms.googleapis.com',
            credentials: credentials.Credentials = None,
            channel: grpc.Channel = None,
            api_mtls_endpoint: str = None,
            client_cert_source: Callable[[], Tuple[bytes, bytes]] = None) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): The mutual TLS endpoint. If
                provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]): A
                callback to provide client SSL certificate bytes and private key
                bytes, both in PEM format. It is ignored if ``api_mtls_endpoint``
                is None.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
        """
        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
        elif api_mtls_endpoint:
            host = api_mtls_endpoint if ":" in api_mtls_endpoint else api_mtls_endpoint + ":443"

            if credentials is None:
                credentials, _ = auth.default(scopes=self.AUTH_SCOPES)

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = grpc_helpers.create_channel(
                host,
                credentials=credentials,
                ssl_credentials=ssl_credentials,
                scopes=self.AUTH_SCOPES,
            )

        # Run the base constructor.
        super().__init__(host=host, credentials=credentials)
        self._stubs = {}  # type: Dict[str, Callable]

    @classmethod
    def create_channel(cls,
                       host: str = 'cloudkms.googleapis.com',
                       credentials: credentials.Credentials = None,
                       **kwargs) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            address (Optionsl[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            scopes=cls.AUTH_SCOPES,
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Sanity check: Only create a new channel if we do not already
        # have one.
        if not hasattr(self, '_grpc_channel'):
            self._grpc_channel = self.create_channel(
                self._host,
                credentials=self._credentials,
            )

        # Return the channel from cache.
        return self._grpc_channel

    @property
    def list_key_rings(self) -> Callable[
            [service.ListKeyRingsRequest],
            service.ListKeyRingsResponse]:
        r"""Return a callable for the list key rings method over gRPC.

        Lists [KeyRings][google.cloud.kms.v1.KeyRing].

        Returns:
            Callable[[~.ListKeyRingsRequest],
                    ~.ListKeyRingsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_key_rings' not in self._stubs:
            self._stubs['list_key_rings'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/ListKeyRings',
                request_serializer=service.ListKeyRingsRequest.serialize,
                response_deserializer=service.ListKeyRingsResponse.deserialize,
            )
        return self._stubs['list_key_rings']

    @property
    def list_crypto_keys(self) -> Callable[
            [service.ListCryptoKeysRequest],
            service.ListCryptoKeysResponse]:
        r"""Return a callable for the list crypto keys method over gRPC.

        Lists [CryptoKeys][google.cloud.kms.v1.CryptoKey].

        Returns:
            Callable[[~.ListCryptoKeysRequest],
                    ~.ListCryptoKeysResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_crypto_keys' not in self._stubs:
            self._stubs['list_crypto_keys'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/ListCryptoKeys',
                request_serializer=service.ListCryptoKeysRequest.serialize,
                response_deserializer=service.ListCryptoKeysResponse.deserialize,
            )
        return self._stubs['list_crypto_keys']

    @property
    def list_crypto_key_versions(self) -> Callable[
            [service.ListCryptoKeyVersionsRequest],
            service.ListCryptoKeyVersionsResponse]:
        r"""Return a callable for the list crypto key versions method over gRPC.

        Lists [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion].

        Returns:
            Callable[[~.ListCryptoKeyVersionsRequest],
                    ~.ListCryptoKeyVersionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_crypto_key_versions' not in self._stubs:
            self._stubs['list_crypto_key_versions'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/ListCryptoKeyVersions',
                request_serializer=service.ListCryptoKeyVersionsRequest.serialize,
                response_deserializer=service.ListCryptoKeyVersionsResponse.deserialize,
            )
        return self._stubs['list_crypto_key_versions']

    @property
    def list_import_jobs(self) -> Callable[
            [service.ListImportJobsRequest],
            service.ListImportJobsResponse]:
        r"""Return a callable for the list import jobs method over gRPC.

        Lists [ImportJobs][google.cloud.kms.v1.ImportJob].

        Returns:
            Callable[[~.ListImportJobsRequest],
                    ~.ListImportJobsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_import_jobs' not in self._stubs:
            self._stubs['list_import_jobs'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/ListImportJobs',
                request_serializer=service.ListImportJobsRequest.serialize,
                response_deserializer=service.ListImportJobsResponse.deserialize,
            )
        return self._stubs['list_import_jobs']

    @property
    def get_key_ring(self) -> Callable[
            [service.GetKeyRingRequest],
            resources.KeyRing]:
        r"""Return a callable for the get key ring method over gRPC.

        Returns metadata for a given
        [KeyRing][google.cloud.kms.v1.KeyRing].

        Returns:
            Callable[[~.GetKeyRingRequest],
                    ~.KeyRing]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_key_ring' not in self._stubs:
            self._stubs['get_key_ring'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/GetKeyRing',
                request_serializer=service.GetKeyRingRequest.serialize,
                response_deserializer=resources.KeyRing.deserialize,
            )
        return self._stubs['get_key_ring']

    @property
    def get_crypto_key(self) -> Callable[
            [service.GetCryptoKeyRequest],
            resources.CryptoKey]:
        r"""Return a callable for the get crypto key method over gRPC.

        Returns metadata for a given
        [CryptoKey][google.cloud.kms.v1.CryptoKey], as well as its
        [primary][google.cloud.kms.v1.CryptoKey.primary]
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].

        Returns:
            Callable[[~.GetCryptoKeyRequest],
                    ~.CryptoKey]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_crypto_key' not in self._stubs:
            self._stubs['get_crypto_key'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/GetCryptoKey',
                request_serializer=service.GetCryptoKeyRequest.serialize,
                response_deserializer=resources.CryptoKey.deserialize,
            )
        return self._stubs['get_crypto_key']

    @property
    def get_crypto_key_version(self) -> Callable[
            [service.GetCryptoKeyVersionRequest],
            resources.CryptoKeyVersion]:
        r"""Return a callable for the get crypto key version method over gRPC.

        Returns metadata for a given
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].

        Returns:
            Callable[[~.GetCryptoKeyVersionRequest],
                    ~.CryptoKeyVersion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_crypto_key_version' not in self._stubs:
            self._stubs['get_crypto_key_version'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/GetCryptoKeyVersion',
                request_serializer=service.GetCryptoKeyVersionRequest.serialize,
                response_deserializer=resources.CryptoKeyVersion.deserialize,
            )
        return self._stubs['get_crypto_key_version']

    @property
    def get_public_key(self) -> Callable[
            [service.GetPublicKeyRequest],
            resources.PublicKey]:
        r"""Return a callable for the get public key method over gRPC.

        Returns the public key for the given
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]. The
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] must
        be
        [ASYMMETRIC\_SIGN][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ASYMMETRIC\_SIGN]
        or
        [ASYMMETRIC\_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ASYMMETRIC\_DECRYPT].

        Returns:
            Callable[[~.GetPublicKeyRequest],
                    ~.PublicKey]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_public_key' not in self._stubs:
            self._stubs['get_public_key'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/GetPublicKey',
                request_serializer=service.GetPublicKeyRequest.serialize,
                response_deserializer=resources.PublicKey.deserialize,
            )
        return self._stubs['get_public_key']

    @property
    def get_import_job(self) -> Callable[
            [service.GetImportJobRequest],
            resources.ImportJob]:
        r"""Return a callable for the get import job method over gRPC.

        Returns metadata for a given
        [ImportJob][google.cloud.kms.v1.ImportJob].

        Returns:
            Callable[[~.GetImportJobRequest],
                    ~.ImportJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_import_job' not in self._stubs:
            self._stubs['get_import_job'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/GetImportJob',
                request_serializer=service.GetImportJobRequest.serialize,
                response_deserializer=resources.ImportJob.deserialize,
            )
        return self._stubs['get_import_job']

    @property
    def create_key_ring(self) -> Callable[
            [service.CreateKeyRingRequest],
            resources.KeyRing]:
        r"""Return a callable for the create key ring method over gRPC.

        Create a new [KeyRing][google.cloud.kms.v1.KeyRing] in a given
        Project and Location.

        Returns:
            Callable[[~.CreateKeyRingRequest],
                    ~.KeyRing]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_key_ring' not in self._stubs:
            self._stubs['create_key_ring'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/CreateKeyRing',
                request_serializer=service.CreateKeyRingRequest.serialize,
                response_deserializer=resources.KeyRing.deserialize,
            )
        return self._stubs['create_key_ring']

    @property
    def create_crypto_key(self) -> Callable[
            [service.CreateCryptoKeyRequest],
            resources.CryptoKey]:
        r"""Return a callable for the create crypto key method over gRPC.

        Create a new [CryptoKey][google.cloud.kms.v1.CryptoKey] within a
        [KeyRing][google.cloud.kms.v1.KeyRing].

        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] and
        [CryptoKey.version\_template.algorithm][google.cloud.kms.v1.CryptoKeyVersionTemplate.algorithm]
        are required.

        Returns:
            Callable[[~.CreateCryptoKeyRequest],
                    ~.CryptoKey]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_crypto_key' not in self._stubs:
            self._stubs['create_crypto_key'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/CreateCryptoKey',
                request_serializer=service.CreateCryptoKeyRequest.serialize,
                response_deserializer=resources.CryptoKey.deserialize,
            )
        return self._stubs['create_crypto_key']

    @property
    def create_crypto_key_version(self) -> Callable[
            [service.CreateCryptoKeyVersionRequest],
            resources.CryptoKeyVersion]:
        r"""Return a callable for the create crypto key version method over gRPC.

        Create a new
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] in a
        [CryptoKey][google.cloud.kms.v1.CryptoKey].

        The server will assign the next sequential id. If unset,
        [state][google.cloud.kms.v1.CryptoKeyVersion.state] will be set
        to
        [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED].

        Returns:
            Callable[[~.CreateCryptoKeyVersionRequest],
                    ~.CryptoKeyVersion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_crypto_key_version' not in self._stubs:
            self._stubs['create_crypto_key_version'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/CreateCryptoKeyVersion',
                request_serializer=service.CreateCryptoKeyVersionRequest.serialize,
                response_deserializer=resources.CryptoKeyVersion.deserialize,
            )
        return self._stubs['create_crypto_key_version']

    @property
    def import_crypto_key_version(self) -> Callable[
            [service.ImportCryptoKeyVersionRequest],
            resources.CryptoKeyVersion]:
        r"""Return a callable for the import crypto key version method over gRPC.

        Imports a new
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] into an
        existing [CryptoKey][google.cloud.kms.v1.CryptoKey] using the
        wrapped key material provided in the request.

        The version ID will be assigned the next sequential id within
        the [CryptoKey][google.cloud.kms.v1.CryptoKey].

        Returns:
            Callable[[~.ImportCryptoKeyVersionRequest],
                    ~.CryptoKeyVersion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'import_crypto_key_version' not in self._stubs:
            self._stubs['import_crypto_key_version'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/ImportCryptoKeyVersion',
                request_serializer=service.ImportCryptoKeyVersionRequest.serialize,
                response_deserializer=resources.CryptoKeyVersion.deserialize,
            )
        return self._stubs['import_crypto_key_version']

    @property
    def create_import_job(self) -> Callable[
            [service.CreateImportJobRequest],
            resources.ImportJob]:
        r"""Return a callable for the create import job method over gRPC.

        Create a new [ImportJob][google.cloud.kms.v1.ImportJob] within a
        [KeyRing][google.cloud.kms.v1.KeyRing].

        [ImportJob.import\_method][google.cloud.kms.v1.ImportJob.import\_method]
        is required.

        Returns:
            Callable[[~.CreateImportJobRequest],
                    ~.ImportJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_import_job' not in self._stubs:
            self._stubs['create_import_job'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/CreateImportJob',
                request_serializer=service.CreateImportJobRequest.serialize,
                response_deserializer=resources.ImportJob.deserialize,
            )
        return self._stubs['create_import_job']

    @property
    def update_crypto_key(self) -> Callable[
            [service.UpdateCryptoKeyRequest],
            resources.CryptoKey]:
        r"""Return a callable for the update crypto key method over gRPC.

        Update a [CryptoKey][google.cloud.kms.v1.CryptoKey].

        Returns:
            Callable[[~.UpdateCryptoKeyRequest],
                    ~.CryptoKey]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_crypto_key' not in self._stubs:
            self._stubs['update_crypto_key'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/UpdateCryptoKey',
                request_serializer=service.UpdateCryptoKeyRequest.serialize,
                response_deserializer=resources.CryptoKey.deserialize,
            )
        return self._stubs['update_crypto_key']

    @property
    def update_crypto_key_version(self) -> Callable[
            [service.UpdateCryptoKeyVersionRequest],
            resources.CryptoKeyVersion]:
        r"""Return a callable for the update crypto key version method over gRPC.

        Update a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]'s
        metadata.

        [state][google.cloud.kms.v1.CryptoKeyVersion.state] may be
        changed between
        [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
        and
        [DISABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DISABLED]
        using this method. See
        [DestroyCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DestroyCryptoKeyVersion]
        and
        [RestoreCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersion]
        to move between other states.

        Returns:
            Callable[[~.UpdateCryptoKeyVersionRequest],
                    ~.CryptoKeyVersion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_crypto_key_version' not in self._stubs:
            self._stubs['update_crypto_key_version'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/UpdateCryptoKeyVersion',
                request_serializer=service.UpdateCryptoKeyVersionRequest.serialize,
                response_deserializer=resources.CryptoKeyVersion.deserialize,
            )
        return self._stubs['update_crypto_key_version']

    @property
    def encrypt(self) -> Callable[
            [service.EncryptRequest],
            service.EncryptResponse]:
        r"""Return a callable for the encrypt method over gRPC.

        Encrypts data, so that it can only be recovered by a call to
        [Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt]. The
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] must
        be
        [ENCRYPT\_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT\_DECRYPT].

        Returns:
            Callable[[~.EncryptRequest],
                    ~.EncryptResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'encrypt' not in self._stubs:
            self._stubs['encrypt'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/Encrypt',
                request_serializer=service.EncryptRequest.serialize,
                response_deserializer=service.EncryptResponse.deserialize,
            )
        return self._stubs['encrypt']

    @property
    def decrypt(self) -> Callable[
            [service.DecryptRequest],
            service.DecryptResponse]:
        r"""Return a callable for the decrypt method over gRPC.

        Decrypts data that was protected by
        [Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt]. The
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] must
        be
        [ENCRYPT\_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT\_DECRYPT].

        Returns:
            Callable[[~.DecryptRequest],
                    ~.DecryptResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'decrypt' not in self._stubs:
            self._stubs['decrypt'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/Decrypt',
                request_serializer=service.DecryptRequest.serialize,
                response_deserializer=service.DecryptResponse.deserialize,
            )
        return self._stubs['decrypt']

    @property
    def asymmetric_sign(self) -> Callable[
            [service.AsymmetricSignRequest],
            service.AsymmetricSignResponse]:
        r"""Return a callable for the asymmetric sign method over gRPC.

        Signs data using a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] with
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose]
        ASYMMETRIC\_SIGN, producing a signature that can be verified
        with the public key retrieved from
        [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey].

        Returns:
            Callable[[~.AsymmetricSignRequest],
                    ~.AsymmetricSignResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'asymmetric_sign' not in self._stubs:
            self._stubs['asymmetric_sign'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/AsymmetricSign',
                request_serializer=service.AsymmetricSignRequest.serialize,
                response_deserializer=service.AsymmetricSignResponse.deserialize,
            )
        return self._stubs['asymmetric_sign']

    @property
    def asymmetric_decrypt(self) -> Callable[
            [service.AsymmetricDecryptRequest],
            service.AsymmetricDecryptResponse]:
        r"""Return a callable for the asymmetric decrypt method over gRPC.

        Decrypts data that was encrypted with a public key retrieved
        from
        [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey]
        corresponding to a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] with
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose]
        ASYMMETRIC\_DECRYPT.

        Returns:
            Callable[[~.AsymmetricDecryptRequest],
                    ~.AsymmetricDecryptResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'asymmetric_decrypt' not in self._stubs:
            self._stubs['asymmetric_decrypt'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/AsymmetricDecrypt',
                request_serializer=service.AsymmetricDecryptRequest.serialize,
                response_deserializer=service.AsymmetricDecryptResponse.deserialize,
            )
        return self._stubs['asymmetric_decrypt']

    @property
    def update_crypto_key_primary_version(self) -> Callable[
            [service.UpdateCryptoKeyPrimaryVersionRequest],
            resources.CryptoKey]:
        r"""Return a callable for the update crypto key primary
        version method over gRPC.

        Update the version of a
        [CryptoKey][google.cloud.kms.v1.CryptoKey] that will be used in
        [Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt].

        Returns an error if called on an asymmetric key.

        Returns:
            Callable[[~.UpdateCryptoKeyPrimaryVersionRequest],
                    ~.CryptoKey]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_crypto_key_primary_version' not in self._stubs:
            self._stubs['update_crypto_key_primary_version'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/UpdateCryptoKeyPrimaryVersion',
                request_serializer=service.UpdateCryptoKeyPrimaryVersionRequest.serialize,
                response_deserializer=resources.CryptoKey.deserialize,
            )
        return self._stubs['update_crypto_key_primary_version']

    @property
    def destroy_crypto_key_version(self) -> Callable[
            [service.DestroyCryptoKeyVersionRequest],
            resources.CryptoKeyVersion]:
        r"""Return a callable for the destroy crypto key version method over gRPC.

        Schedule a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] for
        destruction.

        Upon calling this method,
        [CryptoKeyVersion.state][google.cloud.kms.v1.CryptoKeyVersion.state]
        will be set to
        [DESTROY\_SCHEDULED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROY\_SCHEDULED]
        and
        [destroy\_time][google.cloud.kms.v1.CryptoKeyVersion.destroy\_time]
        will be set to a time 24 hours in the future, at which point the
        [state][google.cloud.kms.v1.CryptoKeyVersion.state] will be
        changed to
        [DESTROYED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROYED],
        and the key material will be irrevocably destroyed.

        Before the
        [destroy\_time][google.cloud.kms.v1.CryptoKeyVersion.destroy\_time]
        is reached,
        [RestoreCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersion]
        may be called to reverse the process.

        Returns:
            Callable[[~.DestroyCryptoKeyVersionRequest],
                    ~.CryptoKeyVersion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'destroy_crypto_key_version' not in self._stubs:
            self._stubs['destroy_crypto_key_version'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/DestroyCryptoKeyVersion',
                request_serializer=service.DestroyCryptoKeyVersionRequest.serialize,
                response_deserializer=resources.CryptoKeyVersion.deserialize,
            )
        return self._stubs['destroy_crypto_key_version']

    @property
    def restore_crypto_key_version(self) -> Callable[
            [service.RestoreCryptoKeyVersionRequest],
            resources.CryptoKeyVersion]:
        r"""Return a callable for the restore crypto key version method over gRPC.

        Restore a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] in the
        [DESTROY\_SCHEDULED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROY\_SCHEDULED]
        state.

        Upon restoration of the CryptoKeyVersion,
        [state][google.cloud.kms.v1.CryptoKeyVersion.state] will be set
        to
        [DISABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DISABLED],
        and
        [destroy\_time][google.cloud.kms.v1.CryptoKeyVersion.destroy\_time]
        will be cleared.

        Returns:
            Callable[[~.RestoreCryptoKeyVersionRequest],
                    ~.CryptoKeyVersion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'restore_crypto_key_version' not in self._stubs:
            self._stubs['restore_crypto_key_version'] = self.grpc_channel.unary_unary(
                '/google.cloud.kms.v1.KeyManagementService/RestoreCryptoKeyVersion',
                request_serializer=service.RestoreCryptoKeyVersionRequest.serialize,
                response_deserializer=resources.CryptoKeyVersion.deserialize,
            )
        return self._stubs['restore_crypto_key_version']


__all__ = (
    'KeyManagementServiceGrpcTransport',
)
