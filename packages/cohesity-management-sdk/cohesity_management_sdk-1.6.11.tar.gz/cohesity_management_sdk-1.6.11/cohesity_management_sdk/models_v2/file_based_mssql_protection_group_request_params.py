# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.mssql_file_protection_group_object_params
import cohesity_management_sdk.models_v2.mssql_file_protection_group_container_params
import cohesity_management_sdk.models_v2.pre_and_post_script_params
import cohesity_management_sdk.models_v2.filter

class FileBasedMSSQLProtectionGroupRequestParams(object):

    """Implementation of the 'File based MSSQL Protection Group Request Params.' model.

    Specifies the params to create a File based MSSQL Protection Group.

    Attributes:
        objects (list of MSSQLFileProtectionGroupObjectParams): Specifies the
            list of object params to be protected.
        perform_source_side_deduplication (bool): Specifies whether or not to
            perform source side deduplication on this Protection Group.
        additional_host_params (list of
            MSSQLFileProtectionGroupContainerParams): Specifies settings which
            are to be applied to specific host containers in this protection
            group.
        user_db_backup_preference_type (UserDbBackupPreferenceTypeEnum):
            Specifies the preference type for backing up user databases on the
            host.
        backup_system_dbs (bool): Specifies whether to backup system
            databases. If not specified then parameter is set to true.
        use_aag_preferences_from_server (bool): Specifies whether or not the
            AAG backup preferences specified on the SQL Server host should be
            used.
        aag_backup_preference_type (AagBackupPreferenceType1Enum): Specifies
            the preference type for backing up databases that are part of an
            AAG. If not specified, then default preferences of the AAG server
            are applied. This field wont be applicable if user DB preference
            is set to skip AAG databases.
        full_backups_copy_only (bool): Specifies whether full backups should
            be copy-only.
        pre_post_script (PreAndPostScriptParams): Specifies the params for pre
            and post scripts.
        exclude_filters (list of Filter): Specifies the list of exclusion
            filters applied during the group creation or edit. These exclusion
            filters can be wildcard supported strings or regular expressions.
            Objects satisfying the will filters will be excluded during backup
            and also auto protected objects will be ignored if filtered by any
            of the filters.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "objects":'objects',
        "perform_source_side_deduplication":'performSourceSideDeduplication',
        "additional_host_params":'additionalHostParams',
        "user_db_backup_preference_type":'userDbBackupPreferenceType',
        "backup_system_dbs":'backupSystemDbs',
        "use_aag_preferences_from_server":'useAagPreferencesFromServer',
        "aag_backup_preference_type":'aagBackupPreferenceType',
        "full_backups_copy_only":'fullBackupsCopyOnly',
        "pre_post_script":'prePostScript',
        "exclude_filters":'excludeFilters'
    }

    def __init__(self,
                 objects=None,
                 perform_source_side_deduplication=None,
                 additional_host_params=None,
                 user_db_backup_preference_type=None,
                 backup_system_dbs=None,
                 use_aag_preferences_from_server=None,
                 aag_backup_preference_type=None,
                 full_backups_copy_only=None,
                 pre_post_script=None,
                 exclude_filters=None):
        """Constructor for the FileBasedMSSQLProtectionGroupRequestParams class"""

        # Initialize members of the class
        self.objects = objects
        self.perform_source_side_deduplication = perform_source_side_deduplication
        self.additional_host_params = additional_host_params
        self.user_db_backup_preference_type = user_db_backup_preference_type
        self.backup_system_dbs = backup_system_dbs
        self.use_aag_preferences_from_server = use_aag_preferences_from_server
        self.aag_backup_preference_type = aag_backup_preference_type
        self.full_backups_copy_only = full_backups_copy_only
        self.pre_post_script = pre_post_script
        self.exclude_filters = exclude_filters


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
        objects = None
        if dictionary.get('objects') != None:
            objects = list()
            for structure in dictionary.get('objects'):
                objects.append(cohesity_management_sdk.models_v2.mssql_file_protection_group_object_params.MSSQLFileProtectionGroupObjectParams.from_dictionary(structure))
        perform_source_side_deduplication = dictionary.get('performSourceSideDeduplication')
        additional_host_params = None
        if dictionary.get('additionalHostParams') != None:
            additional_host_params = list()
            for structure in dictionary.get('additionalHostParams'):
                additional_host_params.append(cohesity_management_sdk.models_v2.mssql_file_protection_group_container_params.MSSQLFileProtectionGroupContainerParams.from_dictionary(structure))
        user_db_backup_preference_type = dictionary.get('userDbBackupPreferenceType')
        backup_system_dbs = dictionary.get('backupSystemDbs')
        use_aag_preferences_from_server = dictionary.get('useAagPreferencesFromServer')
        aag_backup_preference_type = dictionary.get('aagBackupPreferenceType')
        full_backups_copy_only = dictionary.get('fullBackupsCopyOnly')
        pre_post_script = cohesity_management_sdk.models_v2.pre_and_post_script_params.PreAndPostScriptParams.from_dictionary(dictionary.get('prePostScript')) if dictionary.get('prePostScript') else None
        exclude_filters = None
        if dictionary.get('excludeFilters') != None:
            exclude_filters = list()
            for structure in dictionary.get('excludeFilters'):
                exclude_filters.append(cohesity_management_sdk.models_v2.filter.Filter.from_dictionary(structure))

        # Return an object of this model
        return cls(objects,
                   perform_source_side_deduplication,
                   additional_host_params,
                   user_db_backup_preference_type,
                   backup_system_dbs,
                   use_aag_preferences_from_server,
                   aag_backup_preference_type,
                   full_backups_copy_only,
                   pre_post_script,
                   exclude_filters)


