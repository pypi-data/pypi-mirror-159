# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.azure_tier

class AzureTiers(object):

    """Implementation of the 'AzureTiers' model.

    Specifies Azure tiers.

    Attributes:
        tiers (list of AzureTier): Specifies the tiers that are used to move
            the archived backup from current tier to next tier. The order of
            the tiers determines which tier will be used next for moving the
            archived backup. The first tier input should always be default
            tier where backup will be acrhived. Each tier specifies how much
            time after the backup will be moved to next tier from the current
            tier.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tiers":'tiers'
    }

    def __init__(self,
                 tiers=None):
        """Constructor for the AzureTiers class"""

        # Initialize members of the class
        self.tiers = tiers


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
        tiers = None
        if dictionary.get('tiers') != None:
            tiers = list()
            for structure in dictionary.get('tiers'):
                tiers.append(cohesity_management_sdk.models_v2.azure_tier.AzureTier.from_dictionary(structure))

        # Return an object of this model
        return cls(tiers)


