# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad

    OpenAPI spec version: production
    

"""

import pprint
import re

import six

class InlineResponse20042(object):
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
        'id': 'float',
        'name': 'str',
        'email': 'str',
        'provider': 'str',
        'department': 'str',
        'roles': 'list[InlineResponse20033]',
        'eula_version': 'float',
        'internal': 'bool',
        'active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'email': 'email',
        'provider': 'provider',
        'department': 'department',
        'roles': 'roles',
        'eula_version': 'eulaVersion',
        'internal': 'internal',
        'active': 'active'
    }

    def __init__(self, id=None, name=None, email=None, provider=None, department=None, roles=None, eula_version=None, internal=None, active=None):
        """InlineResponse20042 - a model defined in Swagger"""
        self._id = None
        self._name = None
        self._email = None
        self._provider = None
        self._department = None
        self._roles = None
        self._eula_version = None
        self._internal = None
        self._active = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.email = email
        self.provider = provider
        if department is not None:
            self.department = department
        self.roles = roles
        self.eula_version = eula_version
        self.internal = internal
        self.active = active

    @property
    def id(self):
        """Gets the id of this InlineResponse20042.


        :return: The id of this InlineResponse20042.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20042.


        :param id: The id of this InlineResponse20042.
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20042.


        :return: The name of this InlineResponse20042.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20042.


        :param name: The name of this InlineResponse20042.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def email(self):
        """Gets the email of this InlineResponse20042.


        :return: The email of this InlineResponse20042.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse20042.


        :param email: The email of this InlineResponse20042.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def provider(self):
        """Gets the provider of this InlineResponse20042.


        :return: The provider of this InlineResponse20042.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this InlineResponse20042.


        :param provider: The provider of this InlineResponse20042.
        :type: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")

        self._provider = provider

    @property
    def department(self):
        """Gets the department of this InlineResponse20042.


        :return: The department of this InlineResponse20042.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this InlineResponse20042.


        :param department: The department of this InlineResponse20042.
        :type: str
        """

        self._department = department

    @property
    def roles(self):
        """Gets the roles of this InlineResponse20042.


        :return: The roles of this InlineResponse20042.
        :rtype: list[InlineResponse20033]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this InlineResponse20042.


        :param roles: The roles of this InlineResponse20042.
        :type: list[InlineResponse20033]
        """
        if roles is None:
            raise ValueError("Invalid value for `roles`, must not be `None`")

        self._roles = roles

    @property
    def eula_version(self):
        """Gets the eula_version of this InlineResponse20042.


        :return: The eula_version of this InlineResponse20042.
        :rtype: float
        """
        return self._eula_version

    @eula_version.setter
    def eula_version(self, eula_version):
        """Sets the eula_version of this InlineResponse20042.


        :param eula_version: The eula_version of this InlineResponse20042.
        :type: float
        """
        if eula_version is None:
            raise ValueError("Invalid value for `eula_version`, must not be `None`")

        self._eula_version = eula_version

    @property
    def internal(self):
        """Gets the internal of this InlineResponse20042.


        :return: The internal of this InlineResponse20042.
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this InlineResponse20042.


        :param internal: The internal of this InlineResponse20042.
        :type: bool
        """
        if internal is None:
            raise ValueError("Invalid value for `internal`, must not be `None`")

        self._internal = internal

    @property
    def active(self):
        """Gets the active of this InlineResponse20042.


        :return: The active of this InlineResponse20042.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this InlineResponse20042.


        :param active: The active of this InlineResponse20042.
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")

        self._active = active

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
        if issubclass(InlineResponse20042, dict):
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
        if not isinstance(other, InlineResponse20042):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other