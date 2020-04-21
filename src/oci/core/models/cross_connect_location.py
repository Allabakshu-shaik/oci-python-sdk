# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CrossConnectLocation(object):
    """
    An individual FastConnect location.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CrossConnectLocation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CrossConnectLocation.
        :type description: str

        :param name:
            The value to assign to the name property of this CrossConnectLocation.
        :type name: str

        """
        self.swagger_types = {
            'description': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'name': 'name'
        }

        self._description = None
        self._name = None

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CrossConnectLocation.
        A description of the location.


        :return: The description of this CrossConnectLocation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CrossConnectLocation.
        A description of the location.


        :param description: The description of this CrossConnectLocation.
        :type: str
        """
        self._description = description

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CrossConnectLocation.
        The name of the location.

        Example: `CyrusOne, Chandler, AZ`


        :return: The name of this CrossConnectLocation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CrossConnectLocation.
        The name of the location.

        Example: `CyrusOne, Chandler, AZ`


        :param name: The name of this CrossConnectLocation.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
