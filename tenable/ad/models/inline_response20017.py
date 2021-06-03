# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

import pprint
import re

import six

class InlineResponse20017(object):
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
        'codename': 'str',
        'profile_id': 'float',
        'checker_id': 'float',
        'directory_id': 'float',
        'value': 'str',
        'value_type': 'str',
        'name': 'str',
        'description': 'str',
        'translations': 'list[str]',
        'staged': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'codename': 'codename',
        'profile_id': 'profileId',
        'checker_id': 'checkerId',
        'directory_id': 'directoryId',
        'value': 'value',
        'value_type': 'valueType',
        'name': 'name',
        'description': 'description',
        'translations': 'translations',
        'staged': 'staged'
    }

    def __init__(self, id=None, codename=None, profile_id=None, checker_id=None, directory_id=None, value=None, value_type=None, name=None, description=None, translations=None, staged=None):   
        """InlineResponse20017 - a model defined in Swagger"""   
        self._id = None
        self._codename = None
        self._profile_id = None
        self._checker_id = None
        self._directory_id = None
        self._value = None
        self._value_type = None
        self._name = None
        self._description = None
        self._translations = None
        self._staged = None
        self.discriminator = None
        self.id = id
        self.codename = codename
        self.profile_id = profile_id
        self.checker_id = checker_id
        self.directory_id = directory_id
        self.value = value
        self.value_type = value_type
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if translations is not None:
            self.translations = translations
        self.staged = staged

    @property
    def id(self):
        """Gets the id of this InlineResponse20017.   


        :return: The id of this InlineResponse20017.   
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20017.


        :param id: The id of this InlineResponse20017.   
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")   

        self._id = id

    @property
    def codename(self):
        """Gets the codename of this InlineResponse20017.   


        :return: The codename of this InlineResponse20017.   
        :rtype: str
        """
        return self._codename

    @codename.setter
    def codename(self, codename):
        """Sets the codename of this InlineResponse20017.


        :param codename: The codename of this InlineResponse20017.   
        :type: str
        """
        if codename is None:
            raise ValueError("Invalid value for `codename`, must not be `None`")   

        self._codename = codename

    @property
    def profile_id(self):
        """Gets the profile_id of this InlineResponse20017.   


        :return: The profile_id of this InlineResponse20017.   
        :rtype: float
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this InlineResponse20017.


        :param profile_id: The profile_id of this InlineResponse20017.   
        :type: float
        """
        if profile_id is None:
            raise ValueError("Invalid value for `profile_id`, must not be `None`")   

        self._profile_id = profile_id

    @property
    def checker_id(self):
        """Gets the checker_id of this InlineResponse20017.   


        :return: The checker_id of this InlineResponse20017.   
        :rtype: float
        """
        return self._checker_id

    @checker_id.setter
    def checker_id(self, checker_id):
        """Sets the checker_id of this InlineResponse20017.


        :param checker_id: The checker_id of this InlineResponse20017.   
        :type: float
        """
        if checker_id is None:
            raise ValueError("Invalid value for `checker_id`, must not be `None`")   

        self._checker_id = checker_id

    @property
    def directory_id(self):
        """Gets the directory_id of this InlineResponse20017.   


        :return: The directory_id of this InlineResponse20017.   
        :rtype: float
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this InlineResponse20017.


        :param directory_id: The directory_id of this InlineResponse20017.   
        :type: float
        """
        if directory_id is None:
            raise ValueError("Invalid value for `directory_id`, must not be `None`")   

        self._directory_id = directory_id

    @property
    def value(self):
        """Gets the value of this InlineResponse20017.   


        :return: The value of this InlineResponse20017.   
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InlineResponse20017.


        :param value: The value of this InlineResponse20017.   
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")   

        self._value = value

    @property
    def value_type(self):
        """Gets the value_type of this InlineResponse20017.   


        :return: The value_type of this InlineResponse20017.   
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this InlineResponse20017.


        :param value_type: The value_type of this InlineResponse20017.   
        :type: str
        """
        if value_type is None:
            raise ValueError("Invalid value for `value_type`, must not be `None`")   
        allowed_values = ["string", "regex", "float", "integer", "boolean", "date", "object", "array/string", "array/regex", "array/integer", "array/boolean", "array/select", "array/object"]   
        if value_type not in allowed_values:
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"   
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    @property
    def name(self):
        """Gets the name of this InlineResponse20017.   


        :return: The name of this InlineResponse20017.   
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20017.


        :param name: The name of this InlineResponse20017.   
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this InlineResponse20017.   


        :return: The description of this InlineResponse20017.   
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse20017.


        :param description: The description of this InlineResponse20017.   
        :type: str
        """

        self._description = description

    @property
    def translations(self):
        """Gets the translations of this InlineResponse20017.   


        :return: The translations of this InlineResponse20017.   
        :rtype: list[str]
        """
        return self._translations

    @translations.setter
    def translations(self, translations):
        """Sets the translations of this InlineResponse20017.


        :param translations: The translations of this InlineResponse20017.   
        :type: list[str]
        """

        self._translations = translations

    @property
    def staged(self):
        """Gets the staged of this InlineResponse20017.   


        :return: The staged of this InlineResponse20017.   
        :rtype: bool
        """
        return self._staged

    @staged.setter
    def staged(self, staged):
        """Sets the staged of this InlineResponse20017.


        :param staged: The staged of this InlineResponse20017.   
        :type: bool
        """
        if staged is None:
            raise ValueError("Invalid value for `staged`, must not be `None`")   

        self._staged = staged

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
        if issubclass(InlineResponse20017, dict):
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
        if not isinstance(other, InlineResponse20017):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
