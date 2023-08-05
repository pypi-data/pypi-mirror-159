# -*- coding: utf-8 -*-

import cohesity_management_sdk.models_v2.agent_based_aws_protection_group_request_params
import cohesity_management_sdk.models_v2.aws_native_protection_group_request_params
import cohesity_management_sdk.models_v2.create_aws_snapshot_manager_protection_group_request_body
import cohesity_management_sdk.models_v2.awsrds_snapshot_manager_protection_group_request_params

class AWSProtectionGroupRequestParams(object):

    """Implementation of the 'AWS Protection Group Request Params.' model.

    Specifies the parameters which are specific to AWS related Protection
    Groups.

    Attributes:
        protection_type (ProtectionTypeEnum): Specifies the AWS Protection
            Group type.
        agent_protection_type_params
            (AgentBasedAWSProtectionGroupRequestParams): Specifies the
            parameters which are specific to AWS related Protection Groups
            using cohesity protection-service installed on EC2 instance.
        native_protection_type_params (AWSNativeProtectionGroupRequestParams):
            Specifies the parameters which are specific to AWS related
            Protection Groups using AWS native snapshot APIs. Atlease one of
            tags or objects must be specified.
        snapshot_manager_protection_type_params
            (CreateAWSSnapshotManagerProtectionGroupRequestBody): Specifies
            the parameters which are specific to AWS related Protection Groups
            using AWS native snapshot orchestration with snapshot manager.
            Atlease one of tags or objects must be specified.
        rds_protection_type_params
            (AWSRDSSnapshotManagerProtectionGroupRequestParams): Specifies the
            parameters which are specific to AWS RDS related Protection
            Groups.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protection_type":'protectionType',
        "agent_protection_type_params":'agentProtectionTypeParams',
        "native_protection_type_params":'nativeProtectionTypeParams',
        "snapshot_manager_protection_type_params":'snapshotManagerProtectionTypeParams',
        "rds_protection_type_params":'rdsProtectionTypeParams'
    }

    def __init__(self,
                 protection_type=None,
                 agent_protection_type_params=None,
                 native_protection_type_params=None,
                 snapshot_manager_protection_type_params=None,
                 rds_protection_type_params=None):
        """Constructor for the AWSProtectionGroupRequestParams class"""

        # Initialize members of the class
        self.protection_type = protection_type
        self.agent_protection_type_params = agent_protection_type_params
        self.native_protection_type_params = native_protection_type_params
        self.snapshot_manager_protection_type_params = snapshot_manager_protection_type_params
        self.rds_protection_type_params = rds_protection_type_params


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
        protection_type = dictionary.get('protectionType')
        agent_protection_type_params = cohesity_management_sdk.models_v2.agent_based_aws_protection_group_request_params.AgentBasedAWSProtectionGroupRequestParams.from_dictionary(dictionary.get('agentProtectionTypeParams')) if dictionary.get('agentProtectionTypeParams') else None
        native_protection_type_params = cohesity_management_sdk.models_v2.aws_native_protection_group_request_params.AWSNativeProtectionGroupRequestParams.from_dictionary(dictionary.get('nativeProtectionTypeParams')) if dictionary.get('nativeProtectionTypeParams') else None
        snapshot_manager_protection_type_params = cohesity_management_sdk.models_v2.create_aws_snapshot_manager_protection_group_request_body.CreateAWSSnapshotManagerProtectionGroupRequestBody.from_dictionary(dictionary.get('snapshotManagerProtectionTypeParams')) if dictionary.get('snapshotManagerProtectionTypeParams') else None
        rds_protection_type_params = cohesity_management_sdk.models_v2.awsrds_snapshot_manager_protection_group_request_params.AWSRDSSnapshotManagerProtectionGroupRequestParams.from_dictionary(dictionary.get('rdsProtectionTypeParams')) if dictionary.get('rdsProtectionTypeParams') else None

        # Return an object of this model
        return cls(protection_type,
                   agent_protection_type_params,
                   native_protection_type_params,
                   snapshot_manager_protection_type_params,
                   rds_protection_type_params)


