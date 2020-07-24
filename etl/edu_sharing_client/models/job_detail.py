# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class JobDetail(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'group': 'str',
        'description': 'str',
        'job_data_map': 'dict(str, object)',
        'key': 'Key',
        'volatile': 'bool',
        'full_name': 'str',
        'job_listener_names': 'list[str]',
        'stateful': 'bool',
        'durable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'group': 'group',
        'description': 'description',
        'job_data_map': 'jobDataMap',
        'key': 'key',
        'volatile': 'volatile',
        'full_name': 'fullName',
        'job_listener_names': 'jobListenerNames',
        'stateful': 'stateful',
        'durable': 'durable'
    }

    def __init__(self, name=None, group=None, description=None, job_data_map=None, key=None, volatile=False, full_name=None, job_listener_names=None, stateful=False, durable=False):  # noqa: E501
        """JobDetail - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._group = None
        self._description = None
        self._job_data_map = None
        self._key = None
        self._volatile = None
        self._full_name = None
        self._job_listener_names = None
        self._stateful = None
        self._durable = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if group is not None:
            self.group = group
        if description is not None:
            self.description = description
        if job_data_map is not None:
            self.job_data_map = job_data_map
        if key is not None:
            self.key = key
        if volatile is not None:
            self.volatile = volatile
        if full_name is not None:
            self.full_name = full_name
        if job_listener_names is not None:
            self.job_listener_names = job_listener_names
        if stateful is not None:
            self.stateful = stateful
        if durable is not None:
            self.durable = durable

    @property
    def name(self):
        """Gets the name of this JobDetail.  # noqa: E501


        :return: The name of this JobDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobDetail.


        :param name: The name of this JobDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def group(self):
        """Gets the group of this JobDetail.  # noqa: E501


        :return: The group of this JobDetail.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this JobDetail.


        :param group: The group of this JobDetail.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def description(self):
        """Gets the description of this JobDetail.  # noqa: E501


        :return: The description of this JobDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobDetail.


        :param description: The description of this JobDetail.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def job_data_map(self):
        """Gets the job_data_map of this JobDetail.  # noqa: E501


        :return: The job_data_map of this JobDetail.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._job_data_map

    @job_data_map.setter
    def job_data_map(self, job_data_map):
        """Sets the job_data_map of this JobDetail.


        :param job_data_map: The job_data_map of this JobDetail.  # noqa: E501
        :type: dict(str, object)
        """

        self._job_data_map = job_data_map

    @property
    def key(self):
        """Gets the key of this JobDetail.  # noqa: E501


        :return: The key of this JobDetail.  # noqa: E501
        :rtype: Key
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this JobDetail.


        :param key: The key of this JobDetail.  # noqa: E501
        :type: Key
        """

        self._key = key

    @property
    def volatile(self):
        """Gets the volatile of this JobDetail.  # noqa: E501


        :return: The volatile of this JobDetail.  # noqa: E501
        :rtype: bool
        """
        return self._volatile

    @volatile.setter
    def volatile(self, volatile):
        """Sets the volatile of this JobDetail.


        :param volatile: The volatile of this JobDetail.  # noqa: E501
        :type: bool
        """

        self._volatile = volatile

    @property
    def full_name(self):
        """Gets the full_name of this JobDetail.  # noqa: E501


        :return: The full_name of this JobDetail.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this JobDetail.


        :param full_name: The full_name of this JobDetail.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def job_listener_names(self):
        """Gets the job_listener_names of this JobDetail.  # noqa: E501


        :return: The job_listener_names of this JobDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._job_listener_names

    @job_listener_names.setter
    def job_listener_names(self, job_listener_names):
        """Sets the job_listener_names of this JobDetail.


        :param job_listener_names: The job_listener_names of this JobDetail.  # noqa: E501
        :type: list[str]
        """

        self._job_listener_names = job_listener_names

    @property
    def stateful(self):
        """Gets the stateful of this JobDetail.  # noqa: E501


        :return: The stateful of this JobDetail.  # noqa: E501
        :rtype: bool
        """
        return self._stateful

    @stateful.setter
    def stateful(self, stateful):
        """Sets the stateful of this JobDetail.


        :param stateful: The stateful of this JobDetail.  # noqa: E501
        :type: bool
        """

        self._stateful = stateful

    @property
    def durable(self):
        """Gets the durable of this JobDetail.  # noqa: E501


        :return: The durable of this JobDetail.  # noqa: E501
        :rtype: bool
        """
        return self._durable

    @durable.setter
    def durable(self, durable):
        """Sets the durable of this JobDetail.


        :param durable: The durable of this JobDetail.  # noqa: E501
        :type: bool
        """

        self._durable = durable

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(JobDetail, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
