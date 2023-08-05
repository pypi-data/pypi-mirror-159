# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.cdp_object_last_run_info

class VmwareCdpObject(object):

    """Implementation of the 'VmwareCdpObject' model.

    Specifies the VMware specific CDP object details.

    Attributes:
        cdp_enabled (bool): Specifies whether CDP is currently active or not.
            CDP might have been active on this object before, but it might not
            be anymore.
        last_run_info (CdpObjectLastRunInfo): Specifies the last backup
            information for a given CDP object.
        protection_group_id (string): Specifies the protection group id to
            which this CDP object belongs.
        io_filter_status (IoFilterStatusEnum): Specifies the state of CDP IO
            filter. CDP IO filter is an agent which will be installed on the
            object for performing continuous backup. <br> 1. 'kNotInstalled'
            specifies that CDP is enabled on this object but filter is not
            installed. <br> 2. 'kInstallFilterInProgress' specifies that IO
            filter installation is triggered and in progress. <br> 3.
            'kFilterInstalledIOInactive' specifies that IO filter is installed
            but IO streaming is disabled due to missing backup or explicitly
            disabled by the user. <br> 4. 'kIOActivationInProgress' specifies
            that IO filter is activated to start streaming. <br> 5.
            'kIOActive' specifies that filter is attached to the object and
            started streaming. <br> 6. 'kIODeactivationInProgress' specifies
            that deactivation has been initiated to stop the IO streaming.
            <br> 7. 'kUninstallFilterInProgress' specifies that uninstallation
            of IO filter is in progress.
        io_filter_error_message (string): Specifies the error message related
            to IO filter if there is any.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cdp_enabled":'cdpEnabled',
        "last_run_info":'lastRunInfo',
        "protection_group_id":'protectionGroupId',
        "io_filter_status":'ioFilterStatus',
        "io_filter_error_message":'ioFilterErrorMessage'
    }

    def __init__(self,
                 cdp_enabled=None,
                 last_run_info=None,
                 protection_group_id=None,
                 io_filter_status=None,
                 io_filter_error_message=None):
        """Constructor for the VmwareCdpObject class"""

        # Initialize members of the class
        self.cdp_enabled = cdp_enabled
        self.last_run_info = last_run_info
        self.protection_group_id = protection_group_id
        self.io_filter_status = io_filter_status
        self.io_filter_error_message = io_filter_error_message


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
        cdp_enabled = dictionary.get('cdpEnabled')
        last_run_info = cohesity_management_sdk.models_v2.cdp_object_last_run_info.CdpObjectLastRunInfo.from_dictionary(dictionary.get('lastRunInfo')) if dictionary.get('lastRunInfo') else None
        protection_group_id = dictionary.get('protectionGroupId')
        io_filter_status = dictionary.get('ioFilterStatus')
        io_filter_error_message = dictionary.get('ioFilterErrorMessage')

        # Return an object of this model
        return cls(cdp_enabled,
                   last_run_info,
                   protection_group_id,
                   io_filter_status,
                   io_filter_error_message)


