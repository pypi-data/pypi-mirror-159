# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
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


class FrameworkOutputRepository(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, version=None ,runtime= None, runtimes = None, libraries = None):
        """
        FrameworkOutputRepository - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'version': 'str',
            'runtime' : 'FrameworkOutputRepositoryRuntimes',
            'runtimes': 'list[FrameworkOutputRepositoryRuntimes]',
            'libraries': 'list[FrameworkOutputRepositoryLibraries]'
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'runtime' : 'runtime',
            'runtimes': 'runtimes',
            'libraries': 'libraries'
        }

        self._name = name
        self._version = version
        self._runtime = runtime
        self._runtimes = runtimes
        self._libraries = libraries

    @property
    def name(self):
        """
        Gets the name of this FrameworkOutputRepository.


        :return: The name of this FrameworkOutputRepository.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FrameworkOutputRepository.


        :param name: The name of this FrameworkOutputRepository.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """
        Gets the version of this FrameworkOutputRepository.


        :return: The version of this FrameworkOutputRepository.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this FrameworkOutputRepository.


        :param version: The version of this FrameworkOutputRepository.
        :type: str
        """
        self._version = version

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


    @property
    def runtimes(self):
        """
        Gets the runtimes of this FrameworkOutputRepository.


        :return: The runtimes of this FrameworkOutputRepository.
        :rtype: list[FrameworkOutputRepositoryRuntimes]
        """
        return self._runtimes

    @runtimes.setter
    def runtimes(self, runtimes):
        """
        Sets the runtimes of this FrameworkOutputRepository.


        :param runtimes: The runtimes of this FrameworkOutputRepository.
        :type: list[FrameworkOutputRepositoryRuntimes]
        """
        self._runtimes = runtimes

    @property
    def libraries(self):
        """
        Gets the libraries of this FrameworkOutputRepository.


        :return: The libraries of this FrameworkOutputRepository.
        :rtype: list[FrameworkOutputRepositoryLibraries]
        """

        return self._libraries

    @libraries.setter
    def libraries(self, libraries):
        """
        Sets the libraries of this FrameworkOutputRepository.

        :param runtimes: The runtimes of this FrameworkOutputRepository.
        :type: list[FrameworkOutputRepositoryLibraries]
        """
        self._libraries = libraries


    @property
    def runtime(self):
        """
        Gets the runtime of this FrameworkOutputRepository.


        :return: The runtimes of this FrameworkOutputRepository.
        :rtype: list[FrameworkOutputRepositoryRuntimes]
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """
        Sets the runtimes of this FrameworkOutputRepository.


        :param runtimes: The runtimes of this FrameworkOutputRepository.
        :type: list[FrameworkOutputRepositoryRuntimes]
        """
        self._runtimes = runtime

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

