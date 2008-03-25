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

class TestSequence(unittest.TestCase):

    """
    runTest : Announcement test
 
    This test tests the creation of an announcement list.
 
    Return value: 0 on success, 1 on failure
    """

    def runTest(self):
        ann = oh_announcement()
        ann = oh_announcement_create()

        self.assertEqual(ann != None, True) 
        
        self.assertEqual(ann.nextId == SAHPI_OLDEST_ENTRY + 1,True)
       
        self.assertEqual(ann.annentries == None, True)

    if __name__=='__main__':
        unittest.main()
