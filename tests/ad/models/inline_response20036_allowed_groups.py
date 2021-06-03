# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad

    OpenAPI spec version: production
    

"""

import pprint
import re   

import six

class InlineResponse20036AllowedGroups(object):
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
        'default_profile_id': 'int',
        'default_role_ids': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'default_profile_id': 'defaultProfileId',
        'default_role_ids': 'defaultRoleIds'
    }

    def __init__(self, name=None, default_profile_id=None, default_role_ids=None):
        """InlineResponse20036AllowedGroups - a model defined in Swagger"""
        self._name = None
        self._default_profile_id = None
        self._default_role_ids = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if default_profile_id is not None:
            self.default_profile_id = default_profile_id
        if default_role_ids is not None:
            self.default_role_ids = default_role_ids

    @property
    def name(self):
        """Gets the name of this InlineResponse20036AllowedGroups.


        :return: The name of this InlineResponse20036AllowedGroups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20036AllowedGroups.


        :param name: The name of this InlineResponse20036AllowedGroups.
        :type: str
        """

        self._name = name

    @property
    def default_profile_id(self):
        """Gets the default_profile_id of this InlineResponse20036AllowedGroups.


        :return: The default_profile_id of this InlineResponse20036AllowedGroups.
        :rtype: int
        """
        return self._default_profile_id

    @default_profile_id.setter
    def default_profile_id(self, default_profile_id):
        """Sets the default_profile_id of this InlineResponse20036AllowedGroups.


        :param default_profile_id: The default_profile_id of this InlineResponse20036AllowedGroups.
        :type: int
        """

        self._default_profile_id = default_profile_id

    @property
    def default_role_ids(self):
        """Gets the default_role_ids of this InlineResponse20036AllowedGroups.


        :return: The default_role_ids of this InlineResponse20036AllowedGroups.
        :rtype: list[int]
        """
        return self._default_role_ids

    @default_role_ids.setter
    def default_role_ids(self, default_role_ids):
        """Sets the default_role_ids of this InlineResponse20036AllowedGroups.


        :param default_role_ids: The default_role_ids of this InlineResponse20036AllowedGroups.
        :type: list[int]
        """

        self._default_role_ids = default_role_ids

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
        if issubclass(InlineResponse20036AllowedGroups, dict):
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
        if not isinstance(other, InlineResponse20036AllowedGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
