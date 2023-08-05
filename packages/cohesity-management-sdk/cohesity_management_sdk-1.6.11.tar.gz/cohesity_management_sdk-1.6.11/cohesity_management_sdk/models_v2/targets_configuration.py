# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.replication_target_configuration_1
import cohesity_management_sdk.models_v2.archival_target_configuration
import cohesity_management_sdk.models_v2.cloud_spin_target_configuration

class TargetsConfiguration(object):

    """Implementation of the 'TargetsConfiguration' model.

    Specifies the replication, archival and cloud spin targets of Protection
    Policy.

    Attributes:
        replication_targets (list of ReplicationTargetConfiguration1): TODO:
            type description here.
        archival_targets (list of ArchivalTargetConfiguration): TODO: type
            description here.
        cloud_spin_targets (list of CloudSpinTargetConfiguration): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "replication_targets":'replicationTargets',
        "archival_targets":'archivalTargets',
        "cloud_spin_targets":'cloudSpinTargets'
    }

    def __init__(self,
                 replication_targets=None,
                 archival_targets=None,
                 cloud_spin_targets=None):
        """Constructor for the TargetsConfiguration class"""

        # Initialize members of the class
        self.replication_targets = replication_targets
        self.archival_targets = archival_targets
        self.cloud_spin_targets = cloud_spin_targets


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
        replication_targets = None
        if dictionary.get('replicationTargets') != None:
            replication_targets = list()
            for structure in dictionary.get('replicationTargets'):
                replication_targets.append(cohesity_management_sdk.models_v2.replication_target_configuration_1.ReplicationTargetConfiguration1.from_dictionary(structure))
        archival_targets = None
        if dictionary.get('archivalTargets') != None:
            archival_targets = list()
            for structure in dictionary.get('archivalTargets'):
                archival_targets.append(cohesity_management_sdk.models_v2.archival_target_configuration.ArchivalTargetConfiguration.from_dictionary(structure))
        cloud_spin_targets = None
        if dictionary.get('cloudSpinTargets') != None:
            cloud_spin_targets = list()
            for structure in dictionary.get('cloudSpinTargets'):
                cloud_spin_targets.append(cohesity_management_sdk.models_v2.cloud_spin_target_configuration.CloudSpinTargetConfiguration.from_dictionary(structure))

        # Return an object of this model
        return cls(replication_targets,
                   archival_targets,
                   cloud_spin_targets)


