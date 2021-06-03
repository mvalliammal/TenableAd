# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

import pprint
import re

import six

class InlineResponse20040Infrastructures(object):
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
        'uid': 'str',
        'name': 'str',
        'known': 'bool',
        'directories': 'list[InlineResponse20040Directories]'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'known': 'known',
        'directories': 'directories'
    }

    def __init__(self, uid=None, name=None, known=None, directories=None):   
        """InlineResponse20040Infrastructures - a model defined in Swagger"""   
        self._uid = None
        self._name = None
        self._known = None
        self._directories = None
        self.discriminator = None
        self.uid = uid
        self.name = name
        self.known = known
        self.directories = directories

    @property
    def uid(self):
        """Gets the uid of this InlineResponse20040Infrastructures.   


        :return: The uid of this InlineResponse20040Infrastructures.   
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this InlineResponse20040Infrastructures.


        :param uid: The uid of this InlineResponse20040Infrastructures.   
        :type: str
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")   

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this InlineResponse20040Infrastructures.   


        :return: The name of this InlineResponse20040Infrastructures.   
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20040Infrastructures.


        :param name: The name of this InlineResponse20040Infrastructures.   
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")   

        self._name = name

    @property
    def known(self):
        """Gets the known of this InlineResponse20040Infrastructures.   


        :return: The known of this InlineResponse20040Infrastructures.   
        :rtype: bool
        """
        return self._known

    @known.setter
    def known(self, known):
        """Sets the known of this InlineResponse20040Infrastructures.


        :param known: The known of this InlineResponse20040Infrastructures.   
        :type: bool
        """
        if known is None:
            raise ValueError("Invalid value for `known`, must not be `None`")   

        self._known = known

    @property
    def directories(self):
        """Gets the directories of this InlineResponse20040Infrastructures.   


        :return: The directories of this InlineResponse20040Infrastructures.   
        :rtype: list[InlineResponse20040Directories]
        """
        return self._directories

    @directories.setter
    def directories(self, directories):
        """Sets the directories of this InlineResponse20040Infrastructures.


        :param directories: The directories of this InlineResponse20040Infrastructures.   
        :type: list[InlineResponse20040Directories]
        """
        if directories is None:
            raise ValueError("Invalid value for `directories`, must not be `None`")   

        self._directories = directories

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
        if issubclass(InlineResponse20040Infrastructures, dict):
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
        if not isinstance(other, InlineResponse20040Infrastructures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
