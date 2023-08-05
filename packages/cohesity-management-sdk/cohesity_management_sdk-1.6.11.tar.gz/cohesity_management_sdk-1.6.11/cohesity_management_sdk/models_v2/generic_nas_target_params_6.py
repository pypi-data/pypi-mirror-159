# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.volume_1
import cohesity_management_sdk.models_v2.parent_source
import cohesity_management_sdk.models_v2.recovery_vlan_config

class GenericNasTargetParams6(object):

    """Implementation of the 'GenericNasTargetParams6' model.

    Specifies the params for a Generic NAS recovery target.

    Attributes:
        volume (Volume1): Specifies the id and name of the parent volume to
            recover to. This volume will be the target of the recovery.
        parent_source (ParentSource): Specifies the id of the parent source of
            the recovery target.
        overwrite_existing_file (bool): Specifies whether to overwrite
            existing file/folder during recovery.
        preserve_file_attributes (bool): Specifies whether to preserve
            file/folder attributes during recovery.
        continue_on_error (bool): Specifies whether to continue recovering
            other volumes if one of the volumes fails to recover. Default
            value is false.
        encryption_enabled (bool): Specifies whether encryption should be
            enabled during recovery.
        vlan_config (RecoveryVLANConfig): Specifies the VLAN configuration for
            Recovery.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "volume":'volume',
        "parent_source":'parentSource',
        "overwrite_existing_file":'overwriteExistingFile',
        "preserve_file_attributes":'preserveFileAttributes',
        "continue_on_error":'continueOnError',
        "encryption_enabled":'encryptionEnabled',
        "vlan_config":'vlanConfig'
    }

    def __init__(self,
                 volume=None,
                 parent_source=None,
                 overwrite_existing_file=None,
                 preserve_file_attributes=None,
                 continue_on_error=None,
                 encryption_enabled=None,
                 vlan_config=None):
        """Constructor for the GenericNasTargetParams6 class"""

        # Initialize members of the class
        self.volume = volume
        self.parent_source = parent_source
        self.overwrite_existing_file = overwrite_existing_file
        self.preserve_file_attributes = preserve_file_attributes
        self.continue_on_error = continue_on_error
        self.encryption_enabled = encryption_enabled
        self.vlan_config = vlan_config


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
        volume = cohesity_management_sdk.models_v2.volume_1.Volume1.from_dictionary(dictionary.get('volume')) if dictionary.get('volume') else None
        parent_source = cohesity_management_sdk.models_v2.parent_source.ParentSource.from_dictionary(dictionary.get('parentSource')) if dictionary.get('parentSource') else None
        overwrite_existing_file = dictionary.get('overwriteExistingFile')
        preserve_file_attributes = dictionary.get('preserveFileAttributes')
        continue_on_error = dictionary.get('continueOnError')
        encryption_enabled = dictionary.get('encryptionEnabled')
        vlan_config = cohesity_management_sdk.models_v2.recovery_vlan_config.RecoveryVLANConfig.from_dictionary(dictionary.get('vlanConfig')) if dictionary.get('vlanConfig') else None

        # Return an object of this model
        return cls(volume,
                   parent_source,
                   overwrite_existing_file,
                   preserve_file_attributes,
                   continue_on_error,
                   encryption_enabled,
                   vlan_config)


