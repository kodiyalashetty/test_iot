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
import rpt_resources
from openhpi import *
from random import *
from rpt_resources import rptentries
from rpt_resources import sensors


class TestSequence(unittest.TestCase):
       
    """
    runTest : Invokes rpt_diff with new table param as NULL.
 * If it returns error, the test passes, otherwise it failed.
 
 Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        curr_table = RPTable()
        new_table = RPTable()
        new_res, new_rdr, gone_res, gone_rdr = []
        
        oh_init_rpt(curr_table)
        oh_init_rpt(new_table)
        
        self.assertEqual(oh_add_resource(curr_table, rptentries, None, 0), 0) 
        
        self.assertEqual(oh_add_resource(new_table, rptentries[1], None, 0), 0)
        
        rpt_diff(curr_table, None, new_res, new_rdr, gone_res, gone_rdr)
        
                    
if __name__=='__main__':
        unittest.main()    
