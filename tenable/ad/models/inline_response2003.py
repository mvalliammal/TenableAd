# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

import pprint
import re   

import six

class InlineResponse2003(object):
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
        'attribute_name': 'str',
        'value_type': 'str',
        'values': 'ApiinfrastructuresinfrastructureIddirectoriesdirectoryIdeventseventIdadobjectsidchangesValues'
    }

    attribute_map = {
        'attribute_name': 'attributeName',
        'value_type': 'valueType',
        'values': 'values'
    }

    def __init__(self, attribute_name=None, value_type=None, values=None):   
        """InlineResponse2003 - a model defined in Swagger"""   
        self._attribute_name = None
        self._value_type = None
        self._values = None
        self.discriminator = None
        self.attribute_name = attribute_name
        if value_type is not None:
            self.value_type = value_type
        self.values = values

    @property
    def attribute_name(self):
        """Gets the attribute_name of this InlineResponse2003.   


        :return: The attribute_name of this InlineResponse2003.   
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """Sets the attribute_name of this InlineResponse2003.


        :param attribute_name: The attribute_name of this InlineResponse2003.   
        :type: str
        """
        if attribute_name is None:
            raise ValueError("Invalid value for `attribute_name`, must not be `None`")   

        self._attribute_name = attribute_name

    @property
    def value_type(self):
        """Gets the value_type of this InlineResponse2003.   


        :return: The value_type of this InlineResponse2003.   
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this InlineResponse2003.


        :param value_type: The value_type of this InlineResponse2003.   
        :type: str
        """
        allowed_values = ["boolean", "string", "integer", "date", "object", "array/boolean", "array/string", "array/integer", "array/date", "array/object"]   
        if value_type not in allowed_values:
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"   
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    @property
    def values(self):
        """Gets the values of this InlineResponse2003.   


        :return: The values of this InlineResponse2003.   
        :rtype: ApiinfrastructuresinfrastructureIddirectoriesdirectoryIdeventseventIdadobjectsidchangesValues
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this InlineResponse2003.


        :param values: The values of this InlineResponse2003.   
        :type: ApiinfrastructuresinfrastructureIddirectoriesdirectoryIdeventseventIdadobjectsidchangesValues
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")   

        self._values = values

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
        if issubclass(InlineResponse2003, dict):
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
        if not isinstance(other, InlineResponse2003):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
