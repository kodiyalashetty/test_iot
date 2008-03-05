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
from rpt_resources import *
from random import *

class TestSequence(unittest.TestCase):
       
    """
    runTest : Starts with an RPTable of 10 resources, adds 5 rdr
 * to first resource. Fetches sensors ++in sequence by record id and compares
 * with original. A failed comparison means the test failed,
 * otherwise the test passed.
        
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):

        rptable = RPTable()
        oh_init_rpt(rptable)
        tmprdr = None
        i = 0
        
        for i in range (num_resources) :
            self.assertEqual(oh_add_resource(rptable, rptentries[i], None, 0), 0)
        
        for i in range (num_sensors):
            self.assertEqual(oh_add_rdr(rptable, SAHPI_FIRST_ENTRY, sensors[i], None,0), 0)
        
        tmprdr = oh_get_rdr_by_id(rptable, SAHPI_FIRST_ENTRY, SAHPI_FIRST_ENTRY)
        i=0
        while tmprdr :
            self.assertEqual((memcmp(sensors[i], tmprdr, sizeof_SaHpiRdrT)), 0)
            tmprdr = oh_get_rdr_next(rptable, SAHPI_FIRST_ENTRY,tmprdr.RecordId)
            i=i+1
                
if __name__=='__main__':
        unittest.main()    
