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
from rpt_resources import *

class TestSequence(unittest.TestCase):
    """
    runTest : Starting with an empty RPTable, adds a resource to it
    twice. Checks to see if the udpate count was updated the 
    second time. If it was the test failed, otherwise the test passed. 
    Return value: 0 on success, 1 on failure
    """
   
    def runTest(self):

        rptable = RPTable()
        oh_init_rpt(rptable)

        error, update_count, update_timestamp = oh_get_rpt_info(rptable)
        self.assertEqual(error, SA_OK)

        self.assertEqual(oh_add_resource(rptable, rptentries[0], None, 0), 0)
        self.assertEqual(oh_add_resource(rptable, rptentries[1], None, 0), 0)
        
        error, update_count_new, update_timestamp = oh_get_rpt_info(rptable)
        self.assertEqual(error, SA_OK)

        self.assertEqual((update_count+2) == update_count_new, True)

if __name__=='__main__':
        unittest.main()    
