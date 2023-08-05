# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.nis_netgroup

class NisNetgroups(object):

    """Implementation of the 'NisNetgroups' model.

    Response of NIS Netgroups.

    Attributes:
        nis_netgroups (list of NisNetgroup): A list of NIS Netgroups.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "nis_netgroups":'nisNetgroups'
    }

    def __init__(self,
                 nis_netgroups=None):
        """Constructor for the NisNetgroups class"""

        # Initialize members of the class
        self.nis_netgroups = nis_netgroups


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
        nis_netgroups = None
        if dictionary.get('nisNetgroups') != None:
            nis_netgroups = list()
            for structure in dictionary.get('nisNetgroups'):
                nis_netgroups.append(cohesity_management_sdk.models_v2.nis_netgroup.NisNetgroup.from_dictionary(structure))

        # Return an object of this model
        return cls(nis_netgroups)


