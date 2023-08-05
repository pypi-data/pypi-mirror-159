# -*- coding: utf-8 -*-

import sys
import logging

from cohesity_management_sdk.api_helper import APIHelper

logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)


class ConfigurationV2(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "csv"

    # True if the client should skip verification of SSL certificates
    skip_ssl_verification = True

    # An enum for SDK environments
    class Environment(object):
        PRODUCTION = 0

    # An enum for API servers
    class Server(object):
        DEFAULT = 0

    # The environment in which the SDK is running
    environment = Environment.PRODUCTION

    # TODO: Set an appropriate value
    default_host = 'www.example.com'

    # TODO: Set an appropriate value
    api_key = None

    auth_token = None

    # TODO: Set an appropriate value
    cluster_vip = 'prod-cluster.eng.cohesity.com'
 
    # Specifies the login name of the Cohesity user.
    # TODO: Set an appropriate value
    username = None
 
    # Specifies the password of the Cohesity user account.
    # TODO: Set an appropriate value
    password = None
 
    # Specifies the domain the user is logging in to. For a Local user model,
    # the domain is always LOCAL. For LDAP / AD user models, the domain will
    # map to an LDAP connection string. A user is uniquely identified by a
    # combination of username and domain. If this is not set, LOCAL is
    # assumed.
    # TODO: Set an appropriate value
    domain = None


    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.DEFAULT: 'https://{defaultHost}/v2',
        },
    }

    def get_base_uri(self, server=Server.DEFAULT):
        """Generates the appropriate base URI for the environment and the server.

        Args:
            server (Configuration.Server): The server enum for which the base URI is required.

        Returns:
            String: The base URI.

        """
        parameters = {
            "defaultHost": self.cluster_vip,
        }
        return APIHelper.append_url_with_template_parameters(
            self.environments[self.environment][server], parameters, False)

    def disable_logging(cls):
        """Disable all logging in the SDK
        """
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    def enable_logging(cls, filename=None, filemode='a',
                       stream=sys.stdout, level=logging.INFO):
        """Enable logging in the SDK

        Args:
            filename: Specifies that a FileHandler be created, using the specified
                filename, rather than a StreamHandler.
            filemode: If filename is specified, open the file in this mode.
                Defaults to 'a'.
            stream: Use the specified stream to initialize the StreamHandler.
            level: Set the root logger level to the specified level.
        """

        cls.disable_logging()   # clear previously set logging info

        if filename is None:
            logging.basicConfig(stream=stream, level=level)
        else:
            logging.basicConfig(filename=filename, filemode=filemode,
                                level=level)
