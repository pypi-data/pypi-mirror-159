# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.filename_pattern_to_directory
import cohesity_management_sdk.models_v2.multi_stage_restore_options

class OriginalSourceConfig1(object):

    """Implementation of the 'OriginalSourceConfig1' model.

    Specifies the Source configuration if databases are being recovered to
    Original Source. If not specified, all the configuration parameters will
    be retained.

    Attributes:
        data_file_directory_location (string): Specifies the directory where
            to put the database data files. Missing directory will be
            automatically created. If you are overwriting the existing
            database then this field will be ignored.
        log_file_directory_location (string): Specifies the directory where to
            put the database log files. Missing directory will be
            automatically created. If you are overwriting the existing
            database then this field will be ignored.
        capture_tail_logs (bool): Set this to true if tail logs are to be
            captured before the recovery operation. This is only applicable if
            database is not being renamed.
        new_database_name (string): Specifies a new name for the restored
            database. If this field is not specified, then the original
            database will be overwritten after recovery.
        restore_time_usecs (long|int): Specifies the time in the past to which
            the Sql database needs to be restored. This allows for granular
            recovery of Sql databases. If this is not set, the Sql database
            will be restored from the full/incremental snapshot.
        secondary_data_files_dir_list (list of FilenamePatternToDirectory):
            Specifies the secondary data filename pattern and corresponding
            direcories of the DB. Secondary data files are optional and are
            user defined. The recommended file extention for secondary files
            is ".ndf". If this option is specified and the destination folders
            do not exist they will be automatically created.
        with_no_recovery (bool): Specifies the flag to bring DBs online or not
            after successful recovery. If this is passed as true, then it
            means DBs won't be brought online.
        keep_cdc (bool): Specifies whether to keep CDC (Change Data Capture)
            on recovered databases or not. If not passed, this is assumed to
            be true. If withNoRecovery is passed as true, then this field must
            not be set to true. Passing this field as true in this scenario
            will be a invalid request.
        overwriting_policy (OverwritingPolicyEnum): Specifies a policy to be
            used while recovering existing databases.
        multi_stage_restore_options (MultiStageRestoreOptions): Specifies the
            parameters related to multi stage Sql restore.
        native_recovery_with_clause (string): 'with_clause' contains 'with
            clause' to be used in native sql restore command. This is only
            applicable for database restore of native sql backup. Here user
            can specify multiple restore options. Example: 'WITH BUFFERCOUNT =
            575, MAXTRANSFERSIZE = 2097152'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_file_directory_location":'dataFileDirectoryLocation',
        "log_file_directory_location":'logFileDirectoryLocation',
        "capture_tail_logs":'captureTailLogs',
        "new_database_name":'newDatabaseName',
        "restore_time_usecs":'restoreTimeUsecs',
        "secondary_data_files_dir_list":'secondaryDataFilesDirList',
        "with_no_recovery":'withNoRecovery',
        "keep_cdc":'keepCdc',
        "overwriting_policy":'overwritingPolicy',
        "multi_stage_restore_options":'multiStageRestoreOptions',
        "native_recovery_with_clause":'nativeRecoveryWithClause'
    }

    def __init__(self,
                 data_file_directory_location=None,
                 log_file_directory_location=None,
                 capture_tail_logs=None,
                 new_database_name=None,
                 restore_time_usecs=None,
                 secondary_data_files_dir_list=None,
                 with_no_recovery=None,
                 keep_cdc=None,
                 overwriting_policy=None,
                 multi_stage_restore_options=None,
                 native_recovery_with_clause=None):
        """Constructor for the OriginalSourceConfig1 class"""

        # Initialize members of the class
        self.data_file_directory_location = data_file_directory_location
        self.log_file_directory_location = log_file_directory_location
        self.capture_tail_logs = capture_tail_logs
        self.new_database_name = new_database_name
        self.restore_time_usecs = restore_time_usecs
        self.secondary_data_files_dir_list = secondary_data_files_dir_list
        self.with_no_recovery = with_no_recovery
        self.keep_cdc = keep_cdc
        self.overwriting_policy = overwriting_policy
        self.multi_stage_restore_options = multi_stage_restore_options
        self.native_recovery_with_clause = native_recovery_with_clause


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
        data_file_directory_location = dictionary.get('dataFileDirectoryLocation')
        log_file_directory_location = dictionary.get('logFileDirectoryLocation')
        capture_tail_logs = dictionary.get('captureTailLogs')
        new_database_name = dictionary.get('newDatabaseName')
        restore_time_usecs = dictionary.get('restoreTimeUsecs')
        secondary_data_files_dir_list = None
        if dictionary.get('secondaryDataFilesDirList') != None:
            secondary_data_files_dir_list = list()
            for structure in dictionary.get('secondaryDataFilesDirList'):
                secondary_data_files_dir_list.append(cohesity_management_sdk.models_v2.filename_pattern_to_directory.FilenamePatternToDirectory.from_dictionary(structure))
        with_no_recovery = dictionary.get('withNoRecovery')
        keep_cdc = dictionary.get('keepCdc')
        overwriting_policy = dictionary.get('overwritingPolicy')
        multi_stage_restore_options = cohesity_management_sdk.models_v2.multi_stage_restore_options.MultiStageRestoreOptions.from_dictionary(dictionary.get('multiStageRestoreOptions')) if dictionary.get('multiStageRestoreOptions') else None
        native_recovery_with_clause = dictionary.get('nativeRecoveryWithClause')

        # Return an object of this model
        return cls(data_file_directory_location,
                   log_file_directory_location,
                   capture_tail_logs,
                   new_database_name,
                   restore_time_usecs,
                   secondary_data_files_dir_list,
                   with_no_recovery,
                   keep_cdc,
                   overwriting_policy,
                   multi_stage_restore_options,
                   native_recovery_with_clause)


