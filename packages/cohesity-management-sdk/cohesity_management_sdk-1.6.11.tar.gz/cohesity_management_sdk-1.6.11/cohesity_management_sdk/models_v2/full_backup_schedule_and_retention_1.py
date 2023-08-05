# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.full_schedule_1

class FullBackupScheduleAndRetention1(object):

    """Implementation of the 'Full Backup Schedule and Retention.1' model.

    Specifies full backup settings for a Protection Group.

    Attributes:
        schedule (FullSchedule1): Specifies settings that defines how frequent
            full backup will be performed for a Protection Group.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "schedule":'schedule'
    }

    def __init__(self,
                 schedule=None):
        """Constructor for the FullBackupScheduleAndRetention1 class"""

        # Initialize members of the class
        self.schedule = schedule


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
        schedule = cohesity_management_sdk.models_v2.full_schedule_1.FullSchedule1.from_dictionary(dictionary.get('schedule')) if dictionary.get('schedule') else None

        # Return an object of this model
        return cls(schedule)


