# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.xms_client_request_id_operations import XMsClientRequestIdOperations
from .operations.subscription_in_credentials_operations import SubscriptionInCredentialsOperations
from .operations.subscription_in_method_operations import SubscriptionInMethodOperations
from .operations.api_version_default_operations import ApiVersionDefaultOperations
from .operations.api_version_local_operations import ApiVersionLocalOperations
from .operations.skip_url_encoding_operations import SkipUrlEncodingOperations
from .operations.odata_operations import OdataOperations
from .operations.header_operations import HeaderOperations
from . import models


class AutoRestAzureSpecialParametersTestClientConfiguration(AzureConfiguration):
    """Configuration for AutoRestAzureSpecialParametersTestClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription id, which appears in the path,
     always modeled in credentials. The value is always '1234-5678-9012-3456'
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestAzureSpecialParametersTestClientConfiguration, self).__init__(base_url)

        self.add_user_agent('autorestazurespecialparameterstestclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class AutoRestAzureSpecialParametersTestClient(SDKClient):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestAzureSpecialParametersTestClientConfiguration

    :ivar xms_client_request_id: XMsClientRequestId operations
    :vartype xms_client_request_id: azurespecialproperties.operations.XMsClientRequestIdOperations
    :ivar subscription_in_credentials: SubscriptionInCredentials operations
    :vartype subscription_in_credentials: azurespecialproperties.operations.SubscriptionInCredentialsOperations
    :ivar subscription_in_method: SubscriptionInMethod operations
    :vartype subscription_in_method: azurespecialproperties.operations.SubscriptionInMethodOperations
    :ivar api_version_default: ApiVersionDefault operations
    :vartype api_version_default: azurespecialproperties.operations.ApiVersionDefaultOperations
    :ivar api_version_local: ApiVersionLocal operations
    :vartype api_version_local: azurespecialproperties.operations.ApiVersionLocalOperations
    :ivar skip_url_encoding: SkipUrlEncoding operations
    :vartype skip_url_encoding: azurespecialproperties.operations.SkipUrlEncodingOperations
    :ivar odata: Odata operations
    :vartype odata: azurespecialproperties.operations.OdataOperations
    :ivar header: Header operations
    :vartype header: azurespecialproperties.operations.HeaderOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription id, which appears in the path,
     always modeled in credentials. The value is always '1234-5678-9012-3456'
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = AutoRestAzureSpecialParametersTestClientConfiguration(credentials, subscription_id, base_url)
        super(AutoRestAzureSpecialParametersTestClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2015-07-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.xms_client_request_id = XMsClientRequestIdOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.subscription_in_credentials = SubscriptionInCredentialsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.subscription_in_method = SubscriptionInMethodOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.api_version_default = ApiVersionDefaultOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.api_version_local = ApiVersionLocalOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.skip_url_encoding = SkipUrlEncodingOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.odata = OdataOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.header = HeaderOperations(
            self._client, self.config, self._serialize, self._deserialize)
