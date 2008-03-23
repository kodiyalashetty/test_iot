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
from openhpi import *
from rpt_resources import *
from random import *
#import pdb

class TestSequence(unittest.TestCase):
    """
    runTest : Starts with an RPTable of 10 resources, adds 5 rdr
    to first resource. Fetches sensors randomly by record id and compares
    with original. A failed comparison means the test failed,
    otherwise the test passed.
                
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        #pdb.set_trace()
        rptable = RPTable()
        oh_init_rpt(rptable)
        records = []
        
        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rpte, None, 0), 0)
                
        for sensor in sensors[:5]:
            self.assertEqual(oh_add_rdr(rptable, SAHPI_FIRST_ENTRY, sensor, None,0), 0)
            records.append(sensor)
        
        while len(records) > 0:
            k = randrange(0,len(records),1)
            
            randrdr = records[k]
            randrdr.RecordId = oh_get_rdr_uid(randrdr.RdrType,randrdr.RdrTypeUnion.SensorRec.Num)
            tmprdr = oh_get_rdr_by_id(rptable, SAHPI_FIRST_ENTRY,randrdr.RecordId)
    
            self.assertEqual(tmprdr != None, True)
            self.assertEqual(memcmp(randrdr, tmprdr, sizeof_SaHpiRdrT), 0)
            records.pop(k)

if __name__=='__main__':
        unittest.main()    
