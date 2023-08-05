# -*- coding: utf-8 -*-


class NodeSpecificParams(object):

    """Implementation of the 'Node Specific Params.' model.

    Node params required for cluster creation

    Attributes:
        node_id (long|int): Specifies the node id of the node.
        node_ip (string): Specifies the node ip address which is either in
            ipv4/ipv6 format.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "node_id":'nodeId',
        "node_ip":'nodeIp'
    }

    def __init__(self,
                 node_id=None,
                 node_ip=None):
        """Constructor for the NodeSpecificParams class"""

        # Initialize members of the class
        self.node_id = node_id
        self.node_ip = node_ip


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
        node_id = dictionary.get('nodeId')
        node_ip = dictionary.get('nodeIp')

        # Return an object of this model
        return cls(node_id,
                   node_ip)


