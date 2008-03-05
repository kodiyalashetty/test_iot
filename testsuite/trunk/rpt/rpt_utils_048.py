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
    runTest : Starts with an RPTable of 1 resource, adds 1 rdr with data
 * to first resource. Fetches data using a NULL table.
 * Success if the interface returns an error, otherwise there was a failure.
 
 Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        data = "My data"
        
        self.assertEqual(oh_add_resource(rptable, rptentries[0], None, 1), 0)  
        self.assertEqual(oh_add_rdr(rptable, rptentries[0].ResourceId, sensors[0], sensors[0], 1), 0)     
        self.assertEqual(oh_get_rdr_data(None, rptentries[0].ResourceId, sensors[0].RecordId)==None, True)
                                       
if __name__=='__main__':
        unittest.main()    
