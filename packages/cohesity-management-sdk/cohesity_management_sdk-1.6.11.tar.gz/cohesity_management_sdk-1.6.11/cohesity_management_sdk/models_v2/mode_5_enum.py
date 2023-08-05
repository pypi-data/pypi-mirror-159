# -*- coding: utf-8 -*-

class Mode5Enum(object):

    """Implementation of the 'Mode5' enum.

    Specifies the mode of file level datalock.
    Enterprise mode can be upgraded to Compliance mode, but Compliance mode
    cannot be downgraded to Enterprise mode.
    Compliance: This mode would disallow all user to delete/modify file or
    view under any condition when it 's in locked status except for deleting
    view when the view is empty.
    Enterprise: This mode would follow the rules as compliance mode for
    normal users. But it would allow the storage admin
    (1) to delete view or file anytime no matter
    it is in locked status or expired.
    (2) to rename the view
    (3) to bring back the retention period when it's in locked mode
    A lock mode of a file in a view can be in one of the following:
    'Compliance': Default mode of datalock, in this mode, Data Security Admin
    cannot modify/delete this view when datalock is in effect. Data Security
    Admin can delete this view when datalock is expired.
    'kEnterprise' : In this mode, Data Security Admin can change view name or
    delete view when datalock is in effect. Datalock in this mode can be
    upgraded to 'Compliance' mode.

    Attributes:
        COMPLIANCE: TODO: type description here.
        ENTERPRISE: TODO: type description here.

    """

    COMPLIANCE = 'Compliance'

    ENTERPRISE = 'Enterprise'

