# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

import pprint
import re   

import six

class InlineResponse20020(object):
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
        'directory_id': 'float',
        'checker_id': 'float',
        'profile_id': 'float',
        'ad_object_id': 'float',
        'reason_id': 'float',
        'resolved_event_id': 'float',
        'resolved_at': 'datetime',
        'created_event_id': 'float',
        'event_date': 'datetime',
        'ignore_until': 'datetime',
        'created_event_provider_id': 'str',
        'resolved_event_provider_id': 'str',
        'deviance_provider_id': 'str',
        'attributes': 'list[ApiinfrastructuresinfrastructureIddirectoriesdirectoryIddeviancesAttributes]',
        'description': 'ApiinfrastructuresinfrastructureIddirectoriesdirectoryIddeviancesDescription'
    }

    attribute_map = {
        'id': 'id',
        'directory_id': 'directoryId',
        'checker_id': 'checkerId',
        'profile_id': 'profileId',
        'ad_object_id': 'adObjectId',
        'reason_id': 'reasonId',
        'resolved_event_id': 'resolvedEventId',
        'resolved_at': 'resolvedAt',
        'created_event_id': 'createdEventId',
        'event_date': 'eventDate',
        'ignore_until': 'ignoreUntil',
        'created_event_provider_id': 'createdEventProviderId',
        'resolved_event_provider_id': 'resolvedEventProviderId',
        'deviance_provider_id': 'devianceProviderId',
        'attributes': 'attributes',
        'description': 'description'
    }

    def __init__(self, id=None, directory_id=None, checker_id=None, profile_id=None, ad_object_id=None, reason_id=None, resolved_event_id=None, resolved_at=None, created_event_id=None, event_date=None, ignore_until=None, created_event_provider_id=None, resolved_event_provider_id=None, deviance_provider_id=None, attributes=None, description=None):   
        """InlineResponse20020 - a model defined in Swagger"""   
        self._id = None
        self._directory_id = None
        self._checker_id = None
        self._profile_id = None
        self._ad_object_id = None
        self._reason_id = None
        self._resolved_event_id = None
        self._resolved_at = None
        self._created_event_id = None
        self._event_date = None
        self._ignore_until = None
        self._created_event_provider_id = None
        self._resolved_event_provider_id = None
        self._deviance_provider_id = None
        self._attributes = None
        self._description = None
        self.discriminator = None
        self.id = id
        self.directory_id = directory_id
        self.checker_id = checker_id
        self.profile_id = profile_id
        self.ad_object_id = ad_object_id
        self.reason_id = reason_id
        self.resolved_event_id = resolved_event_id
        if resolved_at is not None:
            self.resolved_at = resolved_at
        self.created_event_id = created_event_id
        self.event_date = event_date
        if ignore_until is not None:
            self.ignore_until = ignore_until
        self.created_event_provider_id = created_event_provider_id
        self.resolved_event_provider_id = resolved_event_provider_id
        self.deviance_provider_id = deviance_provider_id
        self.attributes = attributes
        self.description = description

    @property
    def id(self):
        """Gets the id of this InlineResponse20020.   


        :return: The id of this InlineResponse20020.   
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20020.


        :param id: The id of this InlineResponse20020.   
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")   

        self._id = id

    @property
    def directory_id(self):
        """Gets the directory_id of this InlineResponse20020.   


        :return: The directory_id of this InlineResponse20020.   
        :rtype: float
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this InlineResponse20020.


        :param directory_id: The directory_id of this InlineResponse20020.   
        :type: float
        """
        if directory_id is None:
            raise ValueError("Invalid value for `directory_id`, must not be `None`")   

        self._directory_id = directory_id

    @property
    def checker_id(self):
        """Gets the checker_id of this InlineResponse20020.   


        :return: The checker_id of this InlineResponse20020.   
        :rtype: float
        """
        return self._checker_id

    @checker_id.setter
    def checker_id(self, checker_id):
        """Sets the checker_id of this InlineResponse20020.


        :param checker_id: The checker_id of this InlineResponse20020.   
        :type: float
        """
        if checker_id is None:
            raise ValueError("Invalid value for `checker_id`, must not be `None`")   

        self._checker_id = checker_id

    @property
    def profile_id(self):
        """Gets the profile_id of this InlineResponse20020.   


        :return: The profile_id of this InlineResponse20020.   
        :rtype: float
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this InlineResponse20020.


        :param profile_id: The profile_id of this InlineResponse20020.   
        :type: float
        """
        if profile_id is None:
            raise ValueError("Invalid value for `profile_id`, must not be `None`")   

        self._profile_id = profile_id

    @property
    def ad_object_id(self):
        """Gets the ad_object_id of this InlineResponse20020.   


        :return: The ad_object_id of this InlineResponse20020.   
        :rtype: float
        """
        return self._ad_object_id

    @ad_object_id.setter
    def ad_object_id(self, ad_object_id):
        """Sets the ad_object_id of this InlineResponse20020.


        :param ad_object_id: The ad_object_id of this InlineResponse20020.   
        :type: float
        """
        if ad_object_id is None:
            raise ValueError("Invalid value for `ad_object_id`, must not be `None`")   

        self._ad_object_id = ad_object_id

    @property
    def reason_id(self):
        """Gets the reason_id of this InlineResponse20020.   


        :return: The reason_id of this InlineResponse20020.   
        :rtype: float
        """
        return self._reason_id

    @reason_id.setter
    def reason_id(self, reason_id):
        """Sets the reason_id of this InlineResponse20020.


        :param reason_id: The reason_id of this InlineResponse20020.   
        :type: float
        """
        if reason_id is None:
            raise ValueError("Invalid value for `reason_id`, must not be `None`")   

        self._reason_id = reason_id

    @property
    def resolved_event_id(self):
        """Gets the resolved_event_id of this InlineResponse20020.   


        :return: The resolved_event_id of this InlineResponse20020.   
        :rtype: float
        """
        return self._resolved_event_id

    @resolved_event_id.setter
    def resolved_event_id(self, resolved_event_id):
        """Sets the resolved_event_id of this InlineResponse20020.


        :param resolved_event_id: The resolved_event_id of this InlineResponse20020.   
        :type: float
        """
        if resolved_event_id is None:
            raise ValueError("Invalid value for `resolved_event_id`, must not be `None`")   

        self._resolved_event_id = resolved_event_id

    @property
    def resolved_at(self):
        """Gets the resolved_at of this InlineResponse20020.   


        :return: The resolved_at of this InlineResponse20020.   
        :rtype: datetime
        """
        return self._resolved_at

    @resolved_at.setter
    def resolved_at(self, resolved_at):
        """Sets the resolved_at of this InlineResponse20020.


        :param resolved_at: The resolved_at of this InlineResponse20020.   
        :type: datetime
        """

        self._resolved_at = resolved_at

    @property
    def created_event_id(self):
        """Gets the created_event_id of this InlineResponse20020.   


        :return: The created_event_id of this InlineResponse20020.   
        :rtype: float
        """
        return self._created_event_id

    @created_event_id.setter
    def created_event_id(self, created_event_id):
        """Sets the created_event_id of this InlineResponse20020.


        :param created_event_id: The created_event_id of this InlineResponse20020.   
        :type: float
        """
        if created_event_id is None:
            raise ValueError("Invalid value for `created_event_id`, must not be `None`")   

        self._created_event_id = created_event_id

    @property
    def event_date(self):
        """Gets the event_date of this InlineResponse20020.   


        :return: The event_date of this InlineResponse20020.   
        :rtype: datetime
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this InlineResponse20020.


        :param event_date: The event_date of this InlineResponse20020.   
        :type: datetime
        """
        if event_date is None:
            raise ValueError("Invalid value for `event_date`, must not be `None`")   

        self._event_date = event_date

    @property
    def ignore_until(self):
        """Gets the ignore_until of this InlineResponse20020.   


        :return: The ignore_until of this InlineResponse20020.   
        :rtype: datetime
        """
        return self._ignore_until

    @ignore_until.setter
    def ignore_until(self, ignore_until):
        """Sets the ignore_until of this InlineResponse20020.


        :param ignore_until: The ignore_until of this InlineResponse20020.   
        :type: datetime
        """

        self._ignore_until = ignore_until

    @property
    def created_event_provider_id(self):
        """Gets the created_event_provider_id of this InlineResponse20020.   


        :return: The created_event_provider_id of this InlineResponse20020.   
        :rtype: str
        """
        return self._created_event_provider_id

    @created_event_provider_id.setter
    def created_event_provider_id(self, created_event_provider_id):
        """Sets the created_event_provider_id of this InlineResponse20020.


        :param created_event_provider_id: The created_event_provider_id of this InlineResponse20020.   
        :type: str
        """
        if created_event_provider_id is None:
            raise ValueError("Invalid value for `created_event_provider_id`, must not be `None`")   

        self._created_event_provider_id = created_event_provider_id

    @property
    def resolved_event_provider_id(self):
        """Gets the resolved_event_provider_id of this InlineResponse20020.   


        :return: The resolved_event_provider_id of this InlineResponse20020.   
        :rtype: str
        """
        return self._resolved_event_provider_id

    @resolved_event_provider_id.setter
    def resolved_event_provider_id(self, resolved_event_provider_id):
        """Sets the resolved_event_provider_id of this InlineResponse20020.


        :param resolved_event_provider_id: The resolved_event_provider_id of this InlineResponse20020.   
        :type: str
        """
        if resolved_event_provider_id is None:
            raise ValueError("Invalid value for `resolved_event_provider_id`, must not be `None`")   

        self._resolved_event_provider_id = resolved_event_provider_id

    @property
    def deviance_provider_id(self):
        """Gets the deviance_provider_id of this InlineResponse20020.   


        :return: The deviance_provider_id of this InlineResponse20020.   
        :rtype: str
        """
        return self._deviance_provider_id

    @deviance_provider_id.setter
    def deviance_provider_id(self, deviance_provider_id):
        """Sets the deviance_provider_id of this InlineResponse20020.


        :param deviance_provider_id: The deviance_provider_id of this InlineResponse20020.   
        :type: str
        """
        if deviance_provider_id is None:
            raise ValueError("Invalid value for `deviance_provider_id`, must not be `None`")   

        self._deviance_provider_id = deviance_provider_id

    @property
    def attributes(self):
        """Gets the attributes of this InlineResponse20020.   


        :return: The attributes of this InlineResponse20020.   
        :rtype: list[ApiinfrastructuresinfrastructureIddirectoriesdirectoryIddeviancesAttributes]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this InlineResponse20020.


        :param attributes: The attributes of this InlineResponse20020.   
        :type: list[ApiinfrastructuresinfrastructureIddirectoriesdirectoryIddeviancesAttributes]
        """
        if attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")   

        self._attributes = attributes

    @property
    def description(self):
        """Gets the description of this InlineResponse20020.   


        :return: The description of this InlineResponse20020.   
        :rtype: ApiinfrastructuresinfrastructureIddirectoriesdirectoryIddeviancesDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse20020.


        :param description: The description of this InlineResponse20020.   
        :type: ApiinfrastructuresinfrastructureIddirectoriesdirectoryIddeviancesDescription
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")   

        self._description = description

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
        if issubclass(InlineResponse20020, dict):
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
        if not isinstance(other, InlineResponse20020):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other