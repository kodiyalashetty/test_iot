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
from rpt_resources import sensors, rptentries

class TestSequence(unittest.TestCase):
    """
    runTest : Invokes rpt_diff with gone_res param as NULL.
    If it returns error, the test passes, otherwise it failed.
 
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        curr_table = RPTable()
        new_table = RPTable()
        new_res = []; new_rdr = []; gone_res = []; gone_rdr = []
        
        oh_init_rpt(curr_table)
        oh_init_rpt(new_table)
        
        self.assertEqual(oh_add_resource(curr_table, rptentries[0], None, 0), 0)        
        self.assertEqual(oh_add_resource(new_table, rptentries[1], None, 0), 0)
        
        error = rpt_diff(curr_table, new_table, new_res, new_rdr, None, gone_rdr)
        self.assertEqual(error != SA_OK, True)        

if __name__=='__main__':
    unittest.main()    
