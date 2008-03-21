#!/usr/bin/env python

"""
 (C) Copyright IBM Corp. 2008
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 file and program are licensed under a BSD style license.  See
 the Copying file included with the OpenHPI distribution for
 full licensing terms.
 
 Authors:
    Suntrupth S Yadav <suntrupth@in.ibm.com>
 """

import unittest
from openhpi import *

"""
 runTest : Announcement test
 
 This test tests the creation of an announcement list.
 
 Return value: 0 on success, 1 on failure
"""

def runTest(self):
    ann = oh_announcement()
    ann = oh_announcement_create()

    if(ann == None): 
        print "ERROR: ann pointer == None."
        return 1
        
    if(ann.nextId != SAHPI_OLDEST_ENTRY + 1): 
        print "ERROR: ann.nextId invalid."
        return 1
        
    if(ann.annentries != None):
        print "ERROR: ann.annentries invalid."
        return 1
        
if __name__=='__main__':
    unittest.main()
