# coding: utf-8

"""
    IBM Watson Machine Learning REST API

    ## Authorization  ### IBM Watson Machine Learning Credentials  To start working with API one needs to generate an `access token` using the `username` and `password` available on the Service Credentials tab of the IBM Watson Machine Learning service instance or also available in the VCAP environment variable.  Example of the Service Credentials:  ```json {     \"url\": \"https://ibm-watson-ml.mybluemix.net\",     \"access_key\": \"ERY9vcBfE4sE+F4g8hcotF9L+j81WXWeZv\",     \"username\": \"c1ef4b80-2ee2-458e-ab92-e9ca97ec657d\",     \"password\": \"030528d4-5a3e-4d4c-9258-5d553513be6f\" } ```  Example of obtaining `access token` from Token Endpoint using HTTP Basic Auth (for details please refer to Token section below):  ` curl --basic --user username:password https://ibm-watson-ml.mybluemix.net/v2/identity/token `   ### Apache Spark Service Credentials  The IBM Watson Machine Learning co-operates with the Apache Spark as a Service to deploy pipeline models. For API methods requiring Apache Spark Service instance a custom header: `X-Spark-Service-Instance` with Service Credentials must be specified. The header value is a **base64 encoded** string with the Service Credentials JSON data.  [Example of API method requiring Apache Spark Service](https://console.ng.bluemix.net/docs/services/PredictiveModeling/index-gentopic1.html#pm_service_api_spark_batch)

    OpenAPI spec version: 2.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

#  (C) Copyright IBM Corp. 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from pprint import pformat
from six import iteritems
import re


class ModelContentLocation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, type=None, connection=None, location=None, schema=None):
        """
        ModelContentLocation - location of model content defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'connection': 'dict(str, str)',
            'location': 'dict(str, str)',
            'schema': 'dict(str,str)'
        }

        self.attribute_map = {
            'name' : 'name',
            'type': 'type',
            'connection': 'connection',
            'location': 'location',
            'schema':'schema'
        }

        self._name = name
        self._type = type
        self._connection = connection
        self._location = location
        self._schema = schema

    @property
    def name(self):
        """
        Gets the temp cos url of this ModelContentLocation.

        :return: The url of this ModelContentLocation.
        :rtype: dict(str, str)
        """
        return self._name

    @type.setter
    def type(self, type):
        """
        Sets the url of temp cos of this ModelContentLocation.

        :param connection: The connection of this ModelContentLocation.
        :type: dict(str, str)
        """

        self._type = type

    @property
    def connection(self):
        """
        Gets the connection of this ModelContentLocation.

        :return: The connection of this ModelContentLocation.
        :rtype: dict(str, str)
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this ModelContentLocation.

        :param connection: The connection of this ModelContentLocation.
        :type: dict(str, str)
        """

        self._connection = connection

    @property
    def location(self):
        """
        Gets the source of this ModelContentLocation.
        Details of the resource in the content source

        :return: The source of this ModelContentLocation.
        :rtype: dict(str, str)
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the source of this ModelContentLocation.
        Details of the resource in the content data source

        :param source: The source of this ModelContentLocation.
        :type: dict(str, str)
        """

        self._location = location

    @property
    def schema(self):
        """
        Gets the source of this ModelContentLocation.
        Details of the resource in the content source

        :return: The source of this ModelContentLocation.
        :rtype: dict(str, str)
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the source of this ModelContentLocation.
        Details of the resource in the content data source

        :param source: The source of this ModelContentLocation.
        :type: dict(str, str)
        """

        self._schema = schema

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
