# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.helios_frequency_schedule
import cohesity_management_sdk.models_v2.week_schedule_1
import cohesity_management_sdk.models_v2.month_schedule_1

class FullSchedule1(object):

    """Implementation of the 'Full Schedule1' model.

    Specifies settings that defines how frequent full backup will be performed
    for a Protection Group.

    Attributes:
        unit (Unit13Enum): Specifies how often to start new runs of a
            Protection Group. <br>'Days' specifies that Protection Group run
            starts periodically on every day. For full backup schedule,
            currently we only support frequecny of 1 which indicates that full
            backup will be performed daily. <br>'Weeks' specifies that new
            Protection Group runs start weekly on certain days specified using
            'dayOfWeek' field. <br>'Months' specifies that new Protection
            Group runs start monthly on certain day of specific week. This
            schedule needs 'weekOfMonth' and 'dayOfWeek' fields to be set.
            <br> Example: To run the Protection Group on Second Sunday of
            Every Month, following schedule need to be set: <br> unit: 'Month'
            <br> dayOfWeek: 'Sunday' <br> weekOfMonth: 'Second'
        day_schedule (HeliosFrequencySchedule): Specifies settings that define
            a schedule for a Protection Group runs to start after certain
            number of days.
        week_schedule (WeekSchedule1): Specifies settings that define a
            schedule for a Protection Group runs to start on certain days of
            week.
        month_schedule (MonthSchedule1): Specifies settings that define a
            schedule for a Protection Group runs to on specific week and
            specific days of that week.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "unit":'unit',
        "day_schedule":'daySchedule',
        "week_schedule":'weekSchedule',
        "month_schedule":'monthSchedule'
    }

    def __init__(self,
                 unit=None,
                 day_schedule=None,
                 week_schedule=None,
                 month_schedule=None):
        """Constructor for the FullSchedule1 class"""

        # Initialize members of the class
        self.unit = unit
        self.day_schedule = day_schedule
        self.week_schedule = week_schedule
        self.month_schedule = month_schedule


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
        unit = dictionary.get('unit')
        day_schedule = cohesity_management_sdk.models_v2.helios_frequency_schedule.HeliosFrequencySchedule.from_dictionary(dictionary.get('daySchedule')) if dictionary.get('daySchedule') else None
        week_schedule = cohesity_management_sdk.models_v2.week_schedule_1.WeekSchedule1.from_dictionary(dictionary.get('weekSchedule')) if dictionary.get('weekSchedule') else None
        month_schedule = cohesity_management_sdk.models_v2.month_schedule_1.MonthSchedule1.from_dictionary(dictionary.get('monthSchedule')) if dictionary.get('monthSchedule') else None

        # Return an object of this model
        return cls(unit,
                   day_schedule,
                   week_schedule,
                   month_schedule)


