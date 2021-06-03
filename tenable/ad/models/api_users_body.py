# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

import pprint
import re

import six

class ApiUsersBody(object):
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
        'surname': 'str',
        'name': 'str',
        'email': 'str',
        'password': 'str',
        'department': 'str',
        'biography': 'str',
        'active': 'bool',
        'picture': 'list[float]'
    }

    attribute_map = {
        'surname': 'surname',
        'name': 'name',
        'email': 'email',
        'password': 'password',
        'department': 'department',
        'biography': 'biography',
        'active': 'active',
        'picture': 'picture'
    }

    def __init__(self, surname=None, name=None, email=None, password=None, department=None, biography=None, active=False, picture=None):   
        """ApiUsersBody - a model defined in Swagger"""   
        self._surname = None
        self._name = None
        self._email = None
        self._password = None
        self._department = None
        self._biography = None
        self._active = None
        self._picture = None
        self.discriminator = None
        if surname is not None:
            self.surname = surname
        self.name = name
        self.email = email
        self.password = password
        if department is not None:
            self.department = department
        if biography is not None:
            self.biography = biography
        if active is not None:
            self.active = active
        if picture is not None:
            self.picture = picture

    @property
    def surname(self):
        """Gets the surname of this ApiUsersBody.   


        :return: The surname of this ApiUsersBody.   
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this ApiUsersBody.


        :param surname: The surname of this ApiUsersBody.   
        :type: str
        """

        self._surname = surname

    @property
    def name(self):
        """Gets the name of this ApiUsersBody.   


        :return: The name of this ApiUsersBody.   
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiUsersBody.


        :param name: The name of this ApiUsersBody.   
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")   

        self._name = name

    @property
    def email(self):
        """Gets the email of this ApiUsersBody.   


        :return: The email of this ApiUsersBody.   
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ApiUsersBody.


        :param email: The email of this ApiUsersBody.   
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")   

        self._email = email

    @property
    def password(self):
        """Gets the password of this ApiUsersBody.   


        :return: The password of this ApiUsersBody.   
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ApiUsersBody.


        :param password: The password of this ApiUsersBody.   
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")   

        self._password = password

    @property
    def department(self):
        """Gets the department of this ApiUsersBody.   


        :return: The department of this ApiUsersBody.   
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this ApiUsersBody.


        :param department: The department of this ApiUsersBody.   
        :type: str
        """

        self._department = department

    @property
    def biography(self):
        """Gets the biography of this ApiUsersBody.   


        :return: The biography of this ApiUsersBody.   
        :rtype: str
        """
        return self._biography

    @biography.setter
    def biography(self, biography):
        """Sets the biography of this ApiUsersBody.


        :param biography: The biography of this ApiUsersBody.   
        :type: str
        """

        self._biography = biography

    @property
    def active(self):
        """Gets the active of this ApiUsersBody.   


        :return: The active of this ApiUsersBody.   
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ApiUsersBody.


        :param active: The active of this ApiUsersBody.   
        :type: bool
        """

        self._active = active

    @property
    def picture(self):
        """Gets the picture of this ApiUsersBody.   


        :return: The picture of this ApiUsersBody.   
        :rtype: list[float]
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this ApiUsersBody.


        :param picture: The picture of this ApiUsersBody.   
        :type: list[float]
        """

        self._picture = picture

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
        if issubclass(ApiUsersBody, dict):
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
        if not isinstance(other, ApiUsersBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
