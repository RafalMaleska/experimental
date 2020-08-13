# Copyright 2020 The Tekton Authors
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

# coding: utf-8

"""
    Tekton

    Tekton Pipeline  # noqa: E501

    The version of the OpenAPI document: v0.17.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tekton.configuration import Configuration


class V1beta1PipelineRunSpecServiceAccountName(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'service_account_name': 'str',
        'task_name': 'str'
    }

    attribute_map = {
        'service_account_name': 'serviceAccountName',
        'task_name': 'taskName'
    }

    def __init__(self, service_account_name=None, task_name=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1PipelineRunSpecServiceAccountName - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._service_account_name = None
        self._task_name = None
        self.discriminator = None

        if service_account_name is not None:
            self.service_account_name = service_account_name
        if task_name is not None:
            self.task_name = task_name

    @property
    def service_account_name(self):
        """Gets the service_account_name of this V1beta1PipelineRunSpecServiceAccountName.  # noqa: E501


        :return: The service_account_name of this V1beta1PipelineRunSpecServiceAccountName.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this V1beta1PipelineRunSpecServiceAccountName.


        :param service_account_name: The service_account_name of this V1beta1PipelineRunSpecServiceAccountName.  # noqa: E501
        :type: str
        """

        self._service_account_name = service_account_name

    @property
    def task_name(self):
        """Gets the task_name of this V1beta1PipelineRunSpecServiceAccountName.  # noqa: E501


        :return: The task_name of this V1beta1PipelineRunSpecServiceAccountName.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this V1beta1PipelineRunSpecServiceAccountName.


        :param task_name: The task_name of this V1beta1PipelineRunSpecServiceAccountName.  # noqa: E501
        :type: str
        """

        self._task_name = task_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1PipelineRunSpecServiceAccountName):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1PipelineRunSpecServiceAccountName):
            return True

        return self.to_dict() != other.to_dict()
