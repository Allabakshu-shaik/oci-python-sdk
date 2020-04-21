# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WafMeterDatum(object):
    """
    WafMeterDatum model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WafMeterDatum object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_observed:
            The value to assign to the time_observed property of this WafMeterDatum.
        :type time_observed: datetime

        :param time_range_in_seconds:
            The value to assign to the time_range_in_seconds property of this WafMeterDatum.
        :type time_range_in_seconds: int

        :param tenancy_id:
            The value to assign to the tenancy_id property of this WafMeterDatum.
        :type tenancy_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WafMeterDatum.
        :type compartment_id: str

        :param waas_policy_id:
            The value to assign to the waas_policy_id property of this WafMeterDatum.
        :type waas_policy_id: str

        :param is_oci_origin:
            The value to assign to the is_oci_origin property of this WafMeterDatum.
        :type is_oci_origin: bool

        :param is_bot_enabled:
            The value to assign to the is_bot_enabled property of this WafMeterDatum.
        :type is_bot_enabled: bool

        :param request_count:
            The value to assign to the request_count property of this WafMeterDatum.
        :type request_count: int

        :param traffic_in_bytes:
            The value to assign to the traffic_in_bytes property of this WafMeterDatum.
        :type traffic_in_bytes: int

        :param tag_slug:
            The value to assign to the tag_slug property of this WafMeterDatum.
        :type tag_slug: str

        """
        self.swagger_types = {
            'time_observed': 'datetime',
            'time_range_in_seconds': 'int',
            'tenancy_id': 'str',
            'compartment_id': 'str',
            'waas_policy_id': 'str',
            'is_oci_origin': 'bool',
            'is_bot_enabled': 'bool',
            'request_count': 'int',
            'traffic_in_bytes': 'int',
            'tag_slug': 'str'
        }

        self.attribute_map = {
            'time_observed': 'timeObserved',
            'time_range_in_seconds': 'timeRangeInSeconds',
            'tenancy_id': 'tenancyId',
            'compartment_id': 'compartmentId',
            'waas_policy_id': 'waasPolicyId',
            'is_oci_origin': 'isOciOrigin',
            'is_bot_enabled': 'isBotEnabled',
            'request_count': 'requestCount',
            'traffic_in_bytes': 'trafficInBytes',
            'tag_slug': 'tagSlug'
        }

        self._time_observed = None
        self._time_range_in_seconds = None
        self._tenancy_id = None
        self._compartment_id = None
        self._waas_policy_id = None
        self._is_oci_origin = None
        self._is_bot_enabled = None
        self._request_count = None
        self._traffic_in_bytes = None
        self._tag_slug = None

    @property
    def time_observed(self):
        """
        Gets the time_observed of this WafMeterDatum.
        The date and time the traffic was observed, rounded down to the start of a range, and expressed in RFC 3339 timestamp format.


        :return: The time_observed of this WafMeterDatum.
        :rtype: datetime
        """
        return self._time_observed

    @time_observed.setter
    def time_observed(self, time_observed):
        """
        Sets the time_observed of this WafMeterDatum.
        The date and time the traffic was observed, rounded down to the start of a range, and expressed in RFC 3339 timestamp format.


        :param time_observed: The time_observed of this WafMeterDatum.
        :type: datetime
        """
        self._time_observed = time_observed

    @property
    def time_range_in_seconds(self):
        """
        Gets the time_range_in_seconds of this WafMeterDatum.
        The number of seconds this data covers.


        :return: The time_range_in_seconds of this WafMeterDatum.
        :rtype: int
        """
        return self._time_range_in_seconds

    @time_range_in_seconds.setter
    def time_range_in_seconds(self, time_range_in_seconds):
        """
        Sets the time_range_in_seconds of this WafMeterDatum.
        The number of seconds this data covers.


        :param time_range_in_seconds: The time_range_in_seconds of this WafMeterDatum.
        :type: int
        """
        self._time_range_in_seconds = time_range_in_seconds

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this WafMeterDatum.
        The tenancy OCID of the data.


        :return: The tenancy_id of this WafMeterDatum.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this WafMeterDatum.
        The tenancy OCID of the data.


        :param tenancy_id: The tenancy_id of this WafMeterDatum.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this WafMeterDatum.
        The compartment OCID of the data.


        :return: The compartment_id of this WafMeterDatum.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WafMeterDatum.
        The compartment OCID of the data.


        :param compartment_id: The compartment_id of this WafMeterDatum.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def waas_policy_id(self):
        """
        Gets the waas_policy_id of this WafMeterDatum.
        The policy OCID of the data.


        :return: The waas_policy_id of this WafMeterDatum.
        :rtype: str
        """
        return self._waas_policy_id

    @waas_policy_id.setter
    def waas_policy_id(self, waas_policy_id):
        """
        Sets the waas_policy_id of this WafMeterDatum.
        The policy OCID of the data.


        :param waas_policy_id: The waas_policy_id of this WafMeterDatum.
        :type: str
        """
        self._waas_policy_id = waas_policy_id

    @property
    def is_oci_origin(self):
        """
        Gets the is_oci_origin of this WafMeterDatum.
        True if origin (endpoint) is an OCI resource. False if external.


        :return: The is_oci_origin of this WafMeterDatum.
        :rtype: bool
        """
        return self._is_oci_origin

    @is_oci_origin.setter
    def is_oci_origin(self, is_oci_origin):
        """
        Sets the is_oci_origin of this WafMeterDatum.
        True if origin (endpoint) is an OCI resource. False if external.


        :param is_oci_origin: The is_oci_origin of this WafMeterDatum.
        :type: bool
        """
        self._is_oci_origin = is_oci_origin

    @property
    def is_bot_enabled(self):
        """
        Gets the is_bot_enabled of this WafMeterDatum.
        True if bot manager is enabled.


        :return: The is_bot_enabled of this WafMeterDatum.
        :rtype: bool
        """
        return self._is_bot_enabled

    @is_bot_enabled.setter
    def is_bot_enabled(self, is_bot_enabled):
        """
        Sets the is_bot_enabled of this WafMeterDatum.
        True if bot manager is enabled.


        :param is_bot_enabled: The is_bot_enabled of this WafMeterDatum.
        :type: bool
        """
        self._is_bot_enabled = is_bot_enabled

    @property
    def request_count(self):
        """
        Gets the request_count of this WafMeterDatum.
        The number of incoming requests.


        :return: The request_count of this WafMeterDatum.
        :rtype: int
        """
        return self._request_count

    @request_count.setter
    def request_count(self, request_count):
        """
        Sets the request_count of this WafMeterDatum.
        The number of incoming requests.


        :param request_count: The request_count of this WafMeterDatum.
        :type: int
        """
        self._request_count = request_count

    @property
    def traffic_in_bytes(self):
        """
        Gets the traffic_in_bytes of this WafMeterDatum.
        Traffic in bytes.


        :return: The traffic_in_bytes of this WafMeterDatum.
        :rtype: int
        """
        return self._traffic_in_bytes

    @traffic_in_bytes.setter
    def traffic_in_bytes(self, traffic_in_bytes):
        """
        Sets the traffic_in_bytes of this WafMeterDatum.
        Traffic in bytes.


        :param traffic_in_bytes: The traffic_in_bytes of this WafMeterDatum.
        :type: int
        """
        self._traffic_in_bytes = traffic_in_bytes

    @property
    def tag_slug(self):
        """
        Gets the tag_slug of this WafMeterDatum.
        The tag slug for the specified `waasPolicyId`.


        :return: The tag_slug of this WafMeterDatum.
        :rtype: str
        """
        return self._tag_slug

    @tag_slug.setter
    def tag_slug(self, tag_slug):
        """
        Sets the tag_slug of this WafMeterDatum.
        The tag slug for the specified `waasPolicyId`.


        :param tag_slug: The tag_slug of this WafMeterDatum.
        :type: str
        """
        self._tag_slug = tag_slug

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
