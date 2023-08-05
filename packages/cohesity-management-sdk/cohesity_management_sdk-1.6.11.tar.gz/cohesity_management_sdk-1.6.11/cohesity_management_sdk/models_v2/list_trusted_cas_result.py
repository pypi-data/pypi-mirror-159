# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.trusted_ca

class ListTrustedCasResult(object):

    """Implementation of the 'ListTrustedCasResult' model.

    Specifies the basic info about CA Root Certificate.

    Attributes:
        certificates (list of TrustedCa): Array of trusted certificates.
            Specifies the list of certificates returned in this response. List
            is not sorted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "certificates":'certificates'
    }

    def __init__(self,
                 certificates=None):
        """Constructor for the ListTrustedCasResult class"""

        # Initialize members of the class
        self.certificates = certificates


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
        certificates = None
        if dictionary.get('certificates') != None:
            certificates = list()
            for structure in dictionary.get('certificates'):
                certificates.append(cohesity_management_sdk.models_v2.trusted_ca.TrustedCa.from_dictionary(structure))

        # Return an object of this model
        return cls(certificates)


