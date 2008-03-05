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
    runTest : Starts with an RPTable of 10 resources, adds 1 rdr
 * to first resource. Fetches rdr by record id and compares
 * with original. A failed comparison means the test failed,
 * otherwise the test passed. 
        
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):

        rptable = RPTable()
        oh_init_rpt(rptable)
        record_id = None
        tmprdr = SaHpiRdrT()
        i = 0
        
        for i in range(num_resources):
            self.assertEqual(oh_add_resource(rptable, rptentries[i], None, 0), 0)
        
        self.assertEqual(oh_add_rdr(rptable, SAHPI_FIRST_ENTRY, sensors[0], None,0), 0)
        record_id = get_rdr_uid(sensors[0].RdrType, sensors[0].RdrTypeUnion.SensorRec.Num)
        sensors[0].RecordId = record_id
     
        tmprdr = oh_get_rdr_by_id(rptable, SAHPI_FIRST_ENTRY, record_id)
        self.assertEqual(not (tmprdr), False)
        self.assertEqual(memcmp(sensors[0], tmprdr, sizeof_SaHpiRdrT), 0)
                
if __name__=='__main__':
        unittest.main()    
