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

import unittest
import rpt_resources
from openhpi import *
from rpt_resources import rptentries, sensors

class TestSequence(unittest.TestCase):
    """
    runTest : Starting with an empty RPTable, adds 1 resource to it.
    Checks rpt info to see if update count was updated, but it passes
    NULL for a table.
    If oh_get_rpt_info returns error, the test passes, otherwise it failed.
 
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
         
        error, update_count, update_timestamp = oh_get_rpt_info(rptable)
        self.assertEqual(error, SA_OK)
        
        self.assertEqual(oh_add_resource(rptable, rptentries[0], None, 0), 0)
        
        error, update_count, update_timestamp = oh_get_rpt_info(None)
        self.assertEqual(error != SA_OK, True)
        
                    
if __name__=='__main__':
        unittest.main()    
