# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.data_usage_stats

class Stats(object):

    """Implementation of the 'Stats' model.

    Specifies statistics about the View.

    Attributes:
        id (long|int): Specifies the id of the View.
        data_usage_stats (DataUsageStats): Specifies the data usage metric of
            the data stored in this View.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "data_usage_stats":'dataUsageStats'
    }

    def __init__(self,
                 id=None,
                 data_usage_stats=None):
        """Constructor for the Stats class"""

        # Initialize members of the class
        self.id = id
        self.data_usage_stats = data_usage_stats


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
        id = dictionary.get('id')
        data_usage_stats = cohesity_management_sdk.models_v2.data_usage_stats.DataUsageStats.from_dictionary(dictionary.get('dataUsageStats')) if dictionary.get('dataUsageStats') else None

        # Return an object of this model
        return cls(id,
                   data_usage_stats)


