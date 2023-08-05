# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.network_port_group

class NewNetworkConfig(object):

    """Implementation of the 'NewNetworkConfig' model.

    Specifies a new network configuration for the VM recovery.

    Attributes:
        network_port_group (NetworkPortGroup): Specifies the network port
            group (i.e, either a standard switch port group or a distributed
            port group) that will attached to the recovered Object. This
            parameter is mandatory if detach network is specified as false.
        disable_network (bool): Specifies whether the attached network should
            be left in disabled state. Default is false
        preserve_mac_address (bool): If this is true and we are attaching to a
            new network entity, then the VM's MAC address will be preserved on
            the new network. Default value is false.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "network_port_group":'networkPortGroup',
        "disable_network":'disableNetwork',
        "preserve_mac_address":'preserveMacAddress'
    }

    def __init__(self,
                 network_port_group=None,
                 disable_network=None,
                 preserve_mac_address=None):
        """Constructor for the NewNetworkConfig class"""

        # Initialize members of the class
        self.network_port_group = network_port_group
        self.disable_network = disable_network
        self.preserve_mac_address = preserve_mac_address


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        network_port_group = cohesity_management_sdk.models_v2.network_port_group.NetworkPortGroup.from_dictionary(dictionary.get('networkPortGroup')) if dictionary.get('networkPortGroup') else None
        disable_network = dictionary.get('disableNetwork')
        preserve_mac_address = dictionary.get('preserveMacAddress')

        # Return an object of this model
        return cls(network_port_group,
                   disable_network,
                   preserve_mac_address)


