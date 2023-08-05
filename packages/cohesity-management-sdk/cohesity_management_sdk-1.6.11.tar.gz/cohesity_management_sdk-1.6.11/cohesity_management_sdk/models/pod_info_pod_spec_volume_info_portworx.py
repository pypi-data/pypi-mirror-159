# -*- coding: utf-8 -*-
# Copyright 2022 Cohesity Inc.

class PodInfo_PodSpec_VolumeInfo_Portworx(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_Portworx' model.

    Attributes:
        fs_type (string):  TODO: Type description here.
        read_only (bool): TODO: Type description here.
        volume_id (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fs_type":'fsType',
        "read_only":'readOnly',
        "volume_id":'volumeId'
    }

    def __init__(self,
                 fs_type=None,
                 read_only=None,
                 volume_id=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_Portworx class"""

        # Initialize members of the class
        self.fs_type = fs_type
        self.read_only = read_only
        self.volume_id = volume_id


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
        fs_type = dictionary.get('fsType')
        read_only = dictionary.get('readOnly')
        volume_id = dictionary.get('volumeId')

        # Return an object of this model
        return cls(fs_type,
                   read_only,
                   volume_id)


