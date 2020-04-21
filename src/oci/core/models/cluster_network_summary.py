# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterNetworkSummary(object):
    """
    Summary information for a cluster network.
    """

    #: A constant which can be used with the lifecycle_state property of a ClusterNetworkSummary.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetworkSummary.
    #: This constant has a value of "SCALING"
    LIFECYCLE_STATE_SCALING = "SCALING"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetworkSummary.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetworkSummary.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetworkSummary.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetworkSummary.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetworkSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a ClusterNetworkSummary.
    #: This constant has a value of "RUNNING"
    LIFECYCLE_STATE_RUNNING = "RUNNING"

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterNetworkSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ClusterNetworkSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ClusterNetworkSummary.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this ClusterNetworkSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this ClusterNetworkSummary.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ClusterNetworkSummary.
        :type freeform_tags: dict(str, str)

        :param instance_pools:
            The value to assign to the instance_pools property of this ClusterNetworkSummary.
        :type instance_pools: list[InstancePoolSummary]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ClusterNetworkSummary.
            Allowed values for this property are: "PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ClusterNetworkSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ClusterNetworkSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'instance_pools': 'list[InstancePoolSummary]',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'instance_pools': 'instancePools',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._instance_pools = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ClusterNetworkSummary.
        The `OCID`__ of the cluster network.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ClusterNetworkSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ClusterNetworkSummary.
        The `OCID`__ of the cluster network.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ClusterNetworkSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ClusterNetworkSummary.
        The `OCID`__ of the compartment containing the
        cluster netowrk.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ClusterNetworkSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ClusterNetworkSummary.
        The `OCID`__ of the compartment containing the
        cluster netowrk.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ClusterNetworkSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ClusterNetworkSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ClusterNetworkSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ClusterNetworkSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ClusterNetworkSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this ClusterNetworkSummary.
        A user-friendly name for the cluster network. Does not have to be unique, and it's changeable.


        :return: The display_name of this ClusterNetworkSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ClusterNetworkSummary.
        A user-friendly name for the cluster network. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this ClusterNetworkSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ClusterNetworkSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ClusterNetworkSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ClusterNetworkSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ClusterNetworkSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def instance_pools(self):
        """
        Gets the instance_pools of this ClusterNetworkSummary.
        The instance pools in the cluster network.


        :return: The instance_pools of this ClusterNetworkSummary.
        :rtype: list[InstancePoolSummary]
        """
        return self._instance_pools

    @instance_pools.setter
    def instance_pools(self, instance_pools):
        """
        Sets the instance_pools of this ClusterNetworkSummary.
        The instance pools in the cluster network.


        :param instance_pools: The instance_pools of this ClusterNetworkSummary.
        :type: list[InstancePoolSummary]
        """
        self._instance_pools = instance_pools

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ClusterNetworkSummary.
        The current state of the cluster network.

        Allowed values for this property are: "PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ClusterNetworkSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ClusterNetworkSummary.
        The current state of the cluster network.


        :param lifecycle_state: The lifecycle_state of this ClusterNetworkSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ClusterNetworkSummary.
        The date and time the resource was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this ClusterNetworkSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ClusterNetworkSummary.
        The date and time the resource was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this ClusterNetworkSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ClusterNetworkSummary.
        The date and time the resource was updated, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_updated of this ClusterNetworkSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ClusterNetworkSummary.
        The date and time the resource was updated, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_updated: The time_updated of this ClusterNetworkSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
