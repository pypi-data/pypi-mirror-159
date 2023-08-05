# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.vmware_object_protection_request_params
import cohesity_management_sdk.models_v2.generic_nas_object_protection_request_params
import cohesity_management_sdk.models_v2.gpfs_object_protection_request_params
import cohesity_management_sdk.models_v2.elastifile_object_protection_request_params
import cohesity_management_sdk.models_v2.netapp_object_protection_request_params
import cohesity_management_sdk.models_v2.isilon_object_protection_request_params
import cohesity_management_sdk.models_v2.flashblade_object_protection_request_params
import cohesity_management_sdk.models_v2.mssql_object_protection_params
import cohesity_management_sdk.models_v2.office_365_object_protection_common_params

class EnvSpecificObjectProtectionRequestParams(object):

    """Implementation of the 'EnvSpecificObjectProtectionRequestParams' model.

    Specifies the parameters which are specific to adapter identified by
    enviournment.

    Attributes:
        environment (Environment15Enum): Specifies the environment for current
            object.
        vmware_params (VmwareObjectProtectionRequestParams): Specifies the
            parameters which are specific to VMware object protection.
        generic_nas_params (GenericNasObjectProtectionRequestParams):
            Specifies the parameters which are specific to Generic NAS object
            protection.
        gpfs_params (GpfsObjectProtectionRequestParams): Specifies the
            parameters which are specific to Gpfs object protection.
        elastifile_params (ElastifileObjectProtectionRequestParams): Specifies
            the parameters which are specific to Elastifile object
            protection.
        netapp_params (NetappObjectProtectionRequestParams): Specifies the
            parameters which are specific to Netapp object protection.
        isilon_params (IsilonObjectProtectionRequestParams): Specifies the
            parameters which are specific to Isilon object protection.
        flashblade_params (FlashbladeObjectProtectionRequestParams): Specifies
            the parameters which are specific to Flashblade object
            protection.
        mssql_params (MssqlObjectProtectionParams): Specifies the request
            parameters specific to MSSQL object protection.
        office_365_user_mailbox_params
            (Office365ObjectProtectionCommonParams): Specifies the request
            parameters specific to Microsoft 365 User Mailbox object
            protection.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "environment":'environment',
        "vmware_params":'vmwareParams',
        "generic_nas_params":'genericNasParams',
        "gpfs_params":'gpfsParams',
        "elastifile_params":'elastifileParams',
        "netapp_params":'netappParams',
        "isilon_params":'isilonParams',
        "flashblade_params":'flashbladeParams',
        "mssql_params":'mssqlParams',
        "office_365_user_mailbox_params":'office365UserMailboxParams'
    }

    def __init__(self,
                 environment=None,
                 vmware_params=None,
                 generic_nas_params=None,
                 gpfs_params=None,
                 elastifile_params=None,
                 netapp_params=None,
                 isilon_params=None,
                 flashblade_params=None,
                 mssql_params=None,
                 office_365_user_mailbox_params=None):
        """Constructor for the EnvSpecificObjectProtectionRequestParams class"""

        # Initialize members of the class
        self.environment = environment
        self.vmware_params = vmware_params
        self.generic_nas_params = generic_nas_params
        self.gpfs_params = gpfs_params
        self.elastifile_params = elastifile_params
        self.netapp_params = netapp_params
        self.isilon_params = isilon_params
        self.flashblade_params = flashblade_params
        self.mssql_params = mssql_params
        self.office_365_user_mailbox_params = office_365_user_mailbox_params


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
        environment = dictionary.get('environment')
        vmware_params = cohesity_management_sdk.models_v2.vmware_object_protection_request_params.VmwareObjectProtectionRequestParams.from_dictionary(dictionary.get('vmwareParams')) if dictionary.get('vmwareParams') else None
        generic_nas_params = cohesity_management_sdk.models_v2.generic_nas_object_protection_request_params.GenericNasObjectProtectionRequestParams.from_dictionary(dictionary.get('genericNasParams')) if dictionary.get('genericNasParams') else None
        gpfs_params = cohesity_management_sdk.models_v2.gpfs_object_protection_request_params.GpfsObjectProtectionRequestParams.from_dictionary(dictionary.get('gpfsParams')) if dictionary.get('gpfsParams') else None
        elastifile_params = cohesity_management_sdk.models_v2.elastifile_object_protection_request_params.ElastifileObjectProtectionRequestParams.from_dictionary(dictionary.get('elastifileParams')) if dictionary.get('elastifileParams') else None
        netapp_params = cohesity_management_sdk.models_v2.netapp_object_protection_request_params.NetappObjectProtectionRequestParams.from_dictionary(dictionary.get('netappParams')) if dictionary.get('netappParams') else None
        isilon_params = cohesity_management_sdk.models_v2.isilon_object_protection_request_params.IsilonObjectProtectionRequestParams.from_dictionary(dictionary.get('isilonParams')) if dictionary.get('isilonParams') else None
        flashblade_params = cohesity_management_sdk.models_v2.flashblade_object_protection_request_params.FlashbladeObjectProtectionRequestParams.from_dictionary(dictionary.get('flashbladeParams')) if dictionary.get('flashbladeParams') else None
        mssql_params = cohesity_management_sdk.models_v2.mssql_object_protection_params.MssqlObjectProtectionParams.from_dictionary(dictionary.get('mssqlParams')) if dictionary.get('mssqlParams') else None
        office_365_user_mailbox_params = cohesity_management_sdk.models_v2.office_365_object_protection_common_params.Office365ObjectProtectionCommonParams.from_dictionary(dictionary.get('office365UserMailboxParams')) if dictionary.get('office365UserMailboxParams') else None

        # Return an object of this model
        return cls(environment,
                   vmware_params,
                   generic_nas_params,
                   gpfs_params,
                   elastifile_params,
                   netapp_params,
                   isilon_params,
                   flashblade_params,
                   mssql_params,
                   office_365_user_mailbox_params)


