# coding: utf-8

"""
    Engines API

    Allow clients to fetch Engines Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: 2
    Contact: analytics.api.support@factset.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fds.analyticsapi.engines.configuration import Configuration


class ComponentBenchmark(object):
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
        'id': 'str',
        'name': 'str',
        'holdingsmode': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'holdingsmode': 'holdingsmode'
    }

    def __init__(self, id=None, name=None, holdingsmode=None, local_vars_configuration=None):  # noqa: E501
        """ComponentBenchmark - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._holdingsmode = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if holdingsmode is not None:
            self.holdingsmode = holdingsmode

    @property
    def id(self):
        """Gets the id of this ComponentBenchmark.  # noqa: E501

        User's FactSet account path OR a benchmark id to compare against.  # noqa: E501

        :return: The id of this ComponentBenchmark.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentBenchmark.

        User's FactSet account path OR a benchmark id to compare against.  # noqa: E501

        :param id: The id of this ComponentBenchmark.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ComponentBenchmark.  # noqa: E501

        User's FactSet account path OR a benchmark name to compare against.  # noqa: E501

        :return: The name of this ComponentBenchmark.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentBenchmark.

        User's FactSet account path OR a benchmark name to compare against.  # noqa: E501

        :param name: The name of this ComponentBenchmark.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def holdingsmode(self):
        """Gets the holdingsmode of this ComponentBenchmark.  # noqa: E501

        Holdings Mode.  # noqa: E501

        :return: The holdingsmode of this ComponentBenchmark.  # noqa: E501
        :rtype: str
        """
        return self._holdingsmode

    @holdingsmode.setter
    def holdingsmode(self, holdingsmode):
        """Sets the holdingsmode of this ComponentBenchmark.

        Holdings Mode.  # noqa: E501

        :param holdingsmode: The holdingsmode of this ComponentBenchmark.  # noqa: E501
        :type: str
        """

        self._holdingsmode = holdingsmode

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
        if not isinstance(other, ComponentBenchmark):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComponentBenchmark):
            return True

        return self.to_dict() != other.to_dict()
