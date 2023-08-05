# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.vmware_target_params_3

class RecoverVmwareVAppParams(object):

    """Implementation of the 'Recover VMware vApp params.' model.

    Specifies the parameters to recover VMware vApp.

    Attributes:
        target_environment (string): Specifies the environment of the recovery
            target. The corresponding params below must be filled out.
        vmware_target_params (VmwareTargetParams3): Specifies the params for
            recovering to a VMware target.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "target_environment":'targetEnvironment',
        "vmware_target_params":'vmwareTargetParams'
    }

    def __init__(self,
                 target_environment='kVMware',
                 vmware_target_params=None):
        """Constructor for the RecoverVmwareVAppParams class"""

        # Initialize members of the class
        self.target_environment = target_environment
        self.vmware_target_params = vmware_target_params


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
        target_environment = dictionary.get("targetEnvironment") if dictionary.get("targetEnvironment") else 'kVMware'
        vmware_target_params = cohesity_management_sdk.models_v2.vmware_target_params_3.VmwareTargetParams3.from_dictionary(dictionary.get('vmwareTargetParams')) if dictionary.get('vmwareTargetParams') else None

        # Return an object of this model
        return cls(target_environment,
                   vmware_target_params)


