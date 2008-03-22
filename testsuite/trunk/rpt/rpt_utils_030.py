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
    Jayashree Padmanabhan <jayshree@in.ibm.com>
"""

from types import *
import unittest
from openhpi import *
from random import *
from rpt_resources import *

class TestSequence(unittest.TestCase):
       
    """
    runTest : Starting with an empty RPTable, adds one resource to it with NULL data
    and another with data.
    Fetches the resource's NULL data back.
    Passes the test if the interface returns the NULL data, else it fails.
 *
 Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        data = "My data "
        
        self.assertEqual(oh_add_resource(rptable, rptentries[0], rptentries[0], 1), 0)
        self.assertEqual(oh_add_resource(rptable, rptentries[1], None, 1), 0)
        self.assertEqual(oh_get_resource_data(rptable, rptentries[1].ResourceId)==None, True)
                       
if __name__=='__main__':
        unittest.main()    
