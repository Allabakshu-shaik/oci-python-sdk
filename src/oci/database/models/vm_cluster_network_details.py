# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmClusterNetworkDetails(object):
    """
    Details for a VM cluster network.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VmClusterNetworkDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this VmClusterNetworkDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this VmClusterNetworkDetails.
        :type display_name: str

        :param scans:
            The value to assign to the scans property of this VmClusterNetworkDetails.
        :type scans: list[ScanDetails]

        :param dns:
            The value to assign to the dns property of this VmClusterNetworkDetails.
        :type dns: list[str]

        :param ntp:
            The value to assign to the ntp property of this VmClusterNetworkDetails.
        :type ntp: list[str]

        :param vm_networks:
            The value to assign to the vm_networks property of this VmClusterNetworkDetails.
        :type vm_networks: list[VmNetworkDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VmClusterNetworkDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this VmClusterNetworkDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'scans': 'list[ScanDetails]',
            'dns': 'list[str]',
            'ntp': 'list[str]',
            'vm_networks': 'list[VmNetworkDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'scans': 'scans',
            'dns': 'dns',
            'ntp': 'ntp',
            'vm_networks': 'vmNetworks',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._scans = None
        self._dns = None
        self._ntp = None
        self._vm_networks = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this VmClusterNetworkDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this VmClusterNetworkDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VmClusterNetworkDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this VmClusterNetworkDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this VmClusterNetworkDetails.
        The user-friendly name for the VM cluster network. The name does not need to be unique.


        :return: The display_name of this VmClusterNetworkDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VmClusterNetworkDetails.
        The user-friendly name for the VM cluster network. The name does not need to be unique.


        :param display_name: The display_name of this VmClusterNetworkDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def scans(self):
        """
        **[Required]** Gets the scans of this VmClusterNetworkDetails.
        The SCAN details.


        :return: The scans of this VmClusterNetworkDetails.
        :rtype: list[ScanDetails]
        """
        return self._scans

    @scans.setter
    def scans(self, scans):
        """
        Sets the scans of this VmClusterNetworkDetails.
        The SCAN details.


        :param scans: The scans of this VmClusterNetworkDetails.
        :type: list[ScanDetails]
        """
        self._scans = scans

    @property
    def dns(self):
        """
        Gets the dns of this VmClusterNetworkDetails.
        The list of DNS server IP addresses. Maximum of 3 allowed.


        :return: The dns of this VmClusterNetworkDetails.
        :rtype: list[str]
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """
        Sets the dns of this VmClusterNetworkDetails.
        The list of DNS server IP addresses. Maximum of 3 allowed.


        :param dns: The dns of this VmClusterNetworkDetails.
        :type: list[str]
        """
        self._dns = dns

    @property
    def ntp(self):
        """
        Gets the ntp of this VmClusterNetworkDetails.
        The list of NTP server IP addresses. Maximum of 3 allowed.


        :return: The ntp of this VmClusterNetworkDetails.
        :rtype: list[str]
        """
        return self._ntp

    @ntp.setter
    def ntp(self, ntp):
        """
        Sets the ntp of this VmClusterNetworkDetails.
        The list of NTP server IP addresses. Maximum of 3 allowed.


        :param ntp: The ntp of this VmClusterNetworkDetails.
        :type: list[str]
        """
        self._ntp = ntp

    @property
    def vm_networks(self):
        """
        **[Required]** Gets the vm_networks of this VmClusterNetworkDetails.
        Details of the client and backup networks.


        :return: The vm_networks of this VmClusterNetworkDetails.
        :rtype: list[VmNetworkDetails]
        """
        return self._vm_networks

    @vm_networks.setter
    def vm_networks(self, vm_networks):
        """
        Sets the vm_networks of this VmClusterNetworkDetails.
        Details of the client and backup networks.


        :param vm_networks: The vm_networks of this VmClusterNetworkDetails.
        :type: list[VmNetworkDetails]
        """
        self._vm_networks = vm_networks

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this VmClusterNetworkDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this VmClusterNetworkDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this VmClusterNetworkDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this VmClusterNetworkDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this VmClusterNetworkDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this VmClusterNetworkDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this VmClusterNetworkDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this VmClusterNetworkDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other