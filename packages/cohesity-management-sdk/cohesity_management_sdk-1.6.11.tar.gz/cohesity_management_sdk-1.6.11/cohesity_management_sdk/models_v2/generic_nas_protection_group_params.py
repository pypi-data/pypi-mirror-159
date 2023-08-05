# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.protection_object_input
import cohesity_management_sdk.models_v2.indexing_policy
import cohesity_management_sdk.models_v2.file_level_data_lock_configurations
import cohesity_management_sdk.models_v2.protection_group_file_filtering_policy
import cohesity_management_sdk.models_v2.host_based_backup_script_params

class GenericNasProtectionGroupParams(object):

    """Implementation of the 'GenericNasProtectionGroupParams' model.

    Specifies the parameters which are specific to NAS related Protection
    Groups.

    Attributes:
        objects (list of ProtectionObjectInput): Specifies the objects to be
            included in the Protection Group.
        direct_cloud_archive (bool): Specifies whether or not to store the
            snapshots in this run directly in an Archive Target instead of on
            the Cluster. If this is set to true, the associated policy must
            have exactly one Archive Target associated with it and the policy
            must be set up to archive after every run. Also, a Storage Domain
            cannot be specified. Default behavior is 'false'.
        native_format (bool): Specifies whether or not to enable native format
            for direct archive job. This field is set to true if native format
            should be used for archiving.
        indexing_policy (IndexingPolicy): Specifies settings for indexing
            files found in an Object (such as a VM) so these files can be
            searched and recovered. This also specifies inclusion and
            exclusion rules that determine the directories to index.
        continue_on_error (bool): Specifies whether or not the Protection
            Group should continue regardless of whether or not an error was
            encountered.
        encryption_enabled (bool): Specifies whether the protection group
            should use encryption while backup or not.
        file_lock_config (FileLevelDataLockConfigurations): Specifies a config
            to lock files in a view - to protect from malicious or an
            accidental attempt to delete or modify the files in this view.
        file_filters (ProtectionGroupFileFilteringPolicy): Specifies a set of
            filters for a file based Protection Group. These values are
            strings which can represent a prefix or suffix. Example: '/tmp' or
            '*.mp4'. For file based Protection Groups, all files under
            prefixes specified by the 'includeFilters' list will be protected
            unless they are explicitly excluded by the 'excludeFilters' list.
        pre_post_script (HostBasedBackupScriptParams): Specifies params of a
            pre/post scripts to be executed before and after a backup run.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "objects":'objects',
        "direct_cloud_archive":'directCloudArchive',
        "native_format":'nativeFormat',
        "indexing_policy":'indexingPolicy',
        "continue_on_error":'continueOnError',
        "encryption_enabled":'encryptionEnabled',
        "file_lock_config":'fileLockConfig',
        "file_filters":'fileFilters',
        "pre_post_script":'prePostScript'
    }

    def __init__(self,
                 objects=None,
                 direct_cloud_archive=None,
                 native_format=None,
                 indexing_policy=None,
                 continue_on_error=None,
                 encryption_enabled=None,
                 file_lock_config=None,
                 file_filters=None,
                 pre_post_script=None):
        """Constructor for the GenericNasProtectionGroupParams class"""

        # Initialize members of the class
        self.objects = objects
        self.direct_cloud_archive = direct_cloud_archive
        self.native_format = native_format
        self.indexing_policy = indexing_policy
        self.continue_on_error = continue_on_error
        self.encryption_enabled = encryption_enabled
        self.file_lock_config = file_lock_config
        self.file_filters = file_filters
        self.pre_post_script = pre_post_script


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
                objects.append(cohesity_management_sdk.models_v2.protection_object_input.ProtectionObjectInput.from_dictionary(structure))
        direct_cloud_archive = dictionary.get('directCloudArchive')
        native_format = dictionary.get('nativeFormat')
        indexing_policy = cohesity_management_sdk.models_v2.indexing_policy.IndexingPolicy.from_dictionary(dictionary.get('indexingPolicy')) if dictionary.get('indexingPolicy') else None
        continue_on_error = dictionary.get('continueOnError')
        encryption_enabled = dictionary.get('encryptionEnabled')
        file_lock_config = cohesity_management_sdk.models_v2.file_level_data_lock_configurations.FileLevelDataLockConfigurations.from_dictionary(dictionary.get('fileLockConfig')) if dictionary.get('fileLockConfig') else None
        file_filters = cohesity_management_sdk.models_v2.protection_group_file_filtering_policy.ProtectionGroupFileFilteringPolicy.from_dictionary(dictionary.get('fileFilters')) if dictionary.get('fileFilters') else None
        pre_post_script = cohesity_management_sdk.models_v2.host_based_backup_script_params.HostBasedBackupScriptParams.from_dictionary(dictionary.get('prePostScript')) if dictionary.get('prePostScript') else None

        # Return an object of this model
        return cls(objects,
                   direct_cloud_archive,
                   native_format,
                   indexing_policy,
                   continue_on_error,
                   encryption_enabled,
                   file_lock_config,
                   file_filters,
                   pre_post_script)


