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
from .operations.head_exception_operations import HeadExceptionOperations


class AutoRestHeadExceptionTestServiceConfiguration(AzureConfiguration):
    """Configuration for AutoRestHeadExceptionTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestHeadExceptionTestServiceConfiguration, self).__init__(base_url)

        self.add_user_agent('autorestheadexceptiontestservice/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class AutoRestHeadExceptionTestService(SDKClient):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestHeadExceptionTestServiceConfiguration

    :ivar head_exception: HeadException operations
    :vartype head_exception: headexceptions.operations.HeadExceptionOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = AutoRestHeadExceptionTestServiceConfiguration(credentials, base_url)
        super(AutoRestHeadExceptionTestService, self).__init__(self.config.credentials, self.config)

        client_models = {}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.head_exception = HeadExceptionOperations(
            self._client, self.config, self._serialize, self._deserialize)
