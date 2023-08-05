# -*- coding: utf-8 -*-
# Copyright 2022 Cohesity Inc.

import cohesity_management_sdk.models.source_throttling_configuration

class PhysicalParams(object):

    """Implementation of the 'PhysicalParams' model.

    Specifies the parameters required to register Application Servers
    running in a Protection Source specific to a physical adapter.

    Attributes:
        applications (ApplicationsEnum): Specifies the types of applications
            such as 'kSQL', 'kExchange', 'kAD' running on the Protection
            Source.
            overrideDescription: true
            Supported environment types such as 'kView', 'kSQL', 'kVMware', etc.
            NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.
            'kVMware' indicates the VMware Protection Source environment.
            'kHyperV' indicates the HyperV Protection Source environment.
            'kSQL' indicates the SQL Protection Source environment.
            'kView' indicates the View Protection Source environment.
            'kPuppeteer' indicates the Cohesity's Remote Adapter.
            'kPhysical' indicates the physical Protection Source environment.
            'kPure' indicates the Pure Storage Protection Source environment.
            'Nimble' indicates the Nimble Storage Protection Source environment.
            'kAzure' indicates the Microsoft's Azure Protection Source environment.
            'kNetapp' indicates the Netapp Protection Source environment.
            'kAgent' indicates the Agent Protection Source environment.
            'kGenericNas' indicates the Generic Network Attached Storage Protection
            Source environment.
            'kAcropolis' indicates the Acropolis Protection Source environment.
            'kPhsicalFiles' indicates the Physical Files Protection Source environment.
            'kIsilon' indicates the Dell EMC's Isilon Protection Source environment.
            'kGPFS' indicates IBM's GPFS Protection Source environment.
            'kKVM' indicates the KVM Protection Source environment.
            'kAWS' indicates the AWS Protection Source environment.
            'kExchange' indicates the Exchange Protection Source environment.
            'kHyperVVSS' indicates the HyperV VSS Protection Source
            environment.
            'kOracle' indicates the Oracle Protection Source environment.
            'kGCP' indicates the Google Cloud Platform Protection Source environment.
            'kFlashBlade' indicates the Flash Blade Protection Source environment.
            'kAWSNative' indicates the AWS Native Protection Source environment.
            'kO365' indicates the Office 365 Protection Source environment.
            'kO365Outlook' indicates Office 365 outlook Protection Source environment.
            'kHyperFlex' indicates the Hyper Flex Protection Source environment.
            'kGCPNative' indicates the GCP Native Protection Source environment.
            'kAzureNative' indicates the Azure Native Protection Source environment.
            'kKubernetes' indicates a Kubernetes Protection Source environment.
            'kElastifile' indicates Elastifile Protection Source environment.
            'kAD' indicates Active Directory Protection Source environment.
            'kRDSSnapshotManager' indicates AWS RDS Protection Source environment.
            'kCassandra' indicates Cassandra Protection Source environment.
            'kMongoDB' indicates MongoDB Protection Source environment.
            'kCouchbase' indicates Couchbase Protection Source environment.
            'kHdfs' indicates Hdfs Protection Source environment.
            'kHive' indicates Hive Protection Source environment.
            'kHBase' indicates HBase Protection Source environment.
          'kUDA' indicates Universal Data Adapter Protection Source environment.
        password (string): Specifies password of the username to access the
            target source.
        throttling_config (SourceThrottlingConfiguration): The configuration
            for throttling on registered source.
        username (string): Specifies username to access the target source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "applications":'applications',
        "password":'password',
        "throttling_config":'throttlingConfig',
        "username":'username'
    }

    def __init__(self,
                 applications=None,
                 password=None,
                 throttling_config=None,
                 username=None):
        """Constructor for the PhysicalParams class"""

        # Initialize members of the class
        self.applications = applications
        self.password = password
        self.throttling_config = throttling_config
        self.username = username


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
        applications = dictionary.get('applications')
        password = dictionary.get('password')
        throttling_config = cohesity_management_sdk.models.source_throttling_configuration.SourceThrottlingConfiguration.from_dictionary(dictionary.get('throttlingConfig')) if dictionary.get('throttlingConfig') else None
        username = dictionary.get('username')

        # Return an object of this model
        return cls(applications,
                   password,
                   throttling_config,
                   username)


