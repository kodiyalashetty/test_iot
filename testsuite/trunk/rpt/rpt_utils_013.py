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

class TestSequence(unittest.TestCase):
    """
    runTest : Starts with an RPTable of 10 resources, adds 5 rdr
    to first resource. Fetches sensors in sequence by record id and compares
    with original. A failed comparison means the test failed,
    otherwise the test passed.
        
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):

        rptable = RPTable()
        oh_init_rpt(rptable)
        tmprdr = None
        
        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rpte, None, 0), 0)
        
        for sensor in sensors[:5]:
            self.assertEqual(oh_add_rdr(rptable, SAHPI_FIRST_ENTRY, sensor, None,0), 0)
        
        tmprdr = oh_get_rdr_by_id(rptable, SAHPI_FIRST_ENTRY, SAHPI_FIRST_ENTRY)
        while tmprdr:
            self.assertEqual((memcmp(sensors[tmprdr.RdrTypeUnion.SensorRec.Num-1], tmprdr, sizeof_SaHpiRdrT)), 0)
            tmprdr = oh_get_rdr_next(rptable, SAHPI_FIRST_ENTRY,tmprdr.RecordId)

if __name__=='__main__':
        unittest.main()    
