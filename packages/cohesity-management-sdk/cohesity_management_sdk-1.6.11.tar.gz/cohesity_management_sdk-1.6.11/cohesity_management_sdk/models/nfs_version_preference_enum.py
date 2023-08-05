# -*- coding: utf-8 -*-
# Copyright 2022 Cohesity Inc.

class NasProtocolEnum(object):

    """Implementation of the 'NasProtocol' enum.

    Specifies the preferred NFS protocol to use for the backup when multiple
    NFS protocols are present on a single volume.
    Specifies the protocol used by a NAS server.
    'kNfs3' indicates NFS v3 protocol.
    'kCifs1' indicates CIFS v1.0 protocol.

    Attributes:
        KNFS3: TODO: type description here.
        KCIFS1: TODO: type description here.

    """

    KNFS3 = 'kNfs3'

    KCIFS1 = 'kCifs1'

