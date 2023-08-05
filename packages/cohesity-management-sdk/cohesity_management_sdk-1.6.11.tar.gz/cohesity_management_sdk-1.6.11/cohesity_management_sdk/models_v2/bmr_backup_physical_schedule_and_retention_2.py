# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.bmr_schedule_1
import cohesity_management_sdk.models_v2.helios_retention

class BMRBackupPhysicalScheduleAndRetention2(object):

    """Implementation of the 'BMR Backup (Physical) Schedule and Retention.2' model.

    Specifies the BMR schedule in case of physical source protection.

    Attributes:
        schedule (BmrSchedule1): Specifies settings that defines how frequent
            bmr backup will be performed for a Protection Group.
        retention (HeliosRetention): Specifies the retention of a backup.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "schedule":'schedule',
        "retention":'retention'
    }

    def __init__(self,
                 schedule=None,
                 retention=None):
        """Constructor for the BMRBackupPhysicalScheduleAndRetention2 class"""

        # Initialize members of the class
        self.schedule = schedule
        self.retention = retention


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
        schedule = cohesity_management_sdk.models_v2.bmr_schedule_1.BmrSchedule1.from_dictionary(dictionary.get('schedule')) if dictionary.get('schedule') else None
        retention = cohesity_management_sdk.models_v2.helios_retention.HeliosRetention.from_dictionary(dictionary.get('retention')) if dictionary.get('retention') else None

        # Return an object of this model
        return cls(schedule,
                   retention)


