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


class PAComponent(object):
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
        'accounts': 'list[PAIdentifier]',
        'benchmarks': 'list[PAIdentifier]',
        'currencyisocode': 'str',
        'dates': 'PADateParameters',
        'snapshot': 'bool',
        'name': 'str',
        'category': 'str'
    }

    attribute_map = {
        'id': 'id',
        'accounts': 'accounts',
        'benchmarks': 'benchmarks',
        'currencyisocode': 'currencyisocode',
        'dates': 'dates',
        'snapshot': 'snapshot',
        'name': 'name',
        'category': 'category'
    }

    def __init__(self, id=None, accounts=None, benchmarks=None, currencyisocode=None, dates=None, snapshot=None, name=None, category=None, local_vars_configuration=None):  # noqa: E501
        """PAComponent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._accounts = None
        self._benchmarks = None
        self._currencyisocode = None
        self._dates = None
        self._snapshot = None
        self._name = None
        self._category = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if accounts is not None:
            self.accounts = accounts
        if benchmarks is not None:
            self.benchmarks = benchmarks
        if currencyisocode is not None:
            self.currencyisocode = currencyisocode
        if dates is not None:
            self.dates = dates
        if snapshot is not None:
            self.snapshot = snapshot
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category

    @property
    def id(self):
        """Gets the id of this PAComponent.  # noqa: E501

        Component identifier.  # noqa: E501

        :return: The id of this PAComponent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PAComponent.

        Component identifier.  # noqa: E501

        :param id: The id of this PAComponent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def accounts(self):
        """Gets the accounts of this PAComponent.  # noqa: E501

        List of accounts saved in the PA document.  # noqa: E501

        :return: The accounts of this PAComponent.  # noqa: E501
        :rtype: list[PAIdentifier]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this PAComponent.

        List of accounts saved in the PA document.  # noqa: E501

        :param accounts: The accounts of this PAComponent.  # noqa: E501
        :type: list[PAIdentifier]
        """

        self._accounts = accounts

    @property
    def benchmarks(self):
        """Gets the benchmarks of this PAComponent.  # noqa: E501

        List of benchmarks saved in the PA document.  # noqa: E501

        :return: The benchmarks of this PAComponent.  # noqa: E501
        :rtype: list[PAIdentifier]
        """
        return self._benchmarks

    @benchmarks.setter
    def benchmarks(self, benchmarks):
        """Sets the benchmarks of this PAComponent.

        List of benchmarks saved in the PA document.  # noqa: E501

        :param benchmarks: The benchmarks of this PAComponent.  # noqa: E501
        :type: list[PAIdentifier]
        """

        self._benchmarks = benchmarks

    @property
    def currencyisocode(self):
        """Gets the currencyisocode of this PAComponent.  # noqa: E501


        :return: The currencyisocode of this PAComponent.  # noqa: E501
        :rtype: str
        """
        return self._currencyisocode

    @currencyisocode.setter
    def currencyisocode(self, currencyisocode):
        """Sets the currencyisocode of this PAComponent.


        :param currencyisocode: The currencyisocode of this PAComponent.  # noqa: E501
        :type: str
        """

        self._currencyisocode = currencyisocode

    @property
    def dates(self):
        """Gets the dates of this PAComponent.  # noqa: E501


        :return: The dates of this PAComponent.  # noqa: E501
        :rtype: PADateParameters
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this PAComponent.


        :param dates: The dates of this PAComponent.  # noqa: E501
        :type: PADateParameters
        """

        self._dates = dates

    @property
    def snapshot(self):
        """Gets the snapshot of this PAComponent.  # noqa: E501

        Is the component type snapshot or subperiod.  # noqa: E501

        :return: The snapshot of this PAComponent.  # noqa: E501
        :rtype: bool
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this PAComponent.

        Is the component type snapshot or subperiod.  # noqa: E501

        :param snapshot: The snapshot of this PAComponent.  # noqa: E501
        :type: bool
        """

        self._snapshot = snapshot

    @property
    def name(self):
        """Gets the name of this PAComponent.  # noqa: E501

        Component name.  # noqa: E501

        :return: The name of this PAComponent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PAComponent.

        Component name.  # noqa: E501

        :param name: The name of this PAComponent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def category(self):
        """Gets the category of this PAComponent.  # noqa: E501

        Component category.  # noqa: E501

        :return: The category of this PAComponent.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this PAComponent.

        Component category.  # noqa: E501

        :param category: The category of this PAComponent.  # noqa: E501
        :type: str
        """

        self._category = category

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
        if not isinstance(other, PAComponent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PAComponent):
            return True

        return self.to_dict() != other.to_dict()
