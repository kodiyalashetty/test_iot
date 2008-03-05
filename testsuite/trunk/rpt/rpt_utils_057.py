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
from rpt_resources import *

class TestSequence(unittest.TestCase):
       
    """
    runTest : Starts with an RPTable of 1 resource, adds 5 sensors ++to first resource.
 * Fetches an rdr using get_next with a Resource Id not present in the table.
 * Success if the interface returns an error, otherwise there was a failure.
 
 Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        i = 0
        
        self.assertEqual(oh_add_resource(rptable, rptentries[0], None, 1), 0)  
          
        for i in range(0,5):
            self.assertEqual(oh_add_rdr(rptable, rptentries[0].ResourceId, sensors[i], None, 1), 0)  
        self.assertEqual(oh_get_rdr_next(rptable, rptentries[1].ResourceId, sensors[0].RecordId)==None, True) 
            
if __name__=='__main__':
        unittest.main()    
