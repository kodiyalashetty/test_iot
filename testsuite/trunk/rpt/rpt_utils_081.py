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
from random import *
from rpt_resources import *

class TestSequence(unittest.TestCase):
    """
    runTest : resource must NOT have SAHPI_CAPABILITY_AGGREGATE_STATUS capability,
    sensor num should be between SAHPI_STANDARD_SENSOR_MIN and
    SAHPI_STANDARD_SENSOR_MAX and less than SENSOR_AGGREGATE_MAX.
    With these conditions, oh_add_rdr is expected to return an error.
    This is because for a sensor to have a num in the reserved range,
    the resource must have SAHPI_CAPABILITY_AGGREGATE_STATUS capability
    set.
    If so, the test passes, otherwise it failed.
 
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        records = []
        
        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rpte, None, 0),0)
        
        for watchdog in watchdogs:
            self.assertEqual(oh_add_rdr(rptable, SAHPI_FIRST_ENTRY, watchdog, None, 0), 0)
            records.append(watchdog)
            
        while len(records) > 0:
            k = randrange(0,len(records),1)
            
            randrdr = records[k]
            randrdr.RecordId = oh_get_rdr_uid(randrdr.RdrType,randrdr.RdrTypeUnion.WatchdogRec.WatchdogNum)
            tmprdr = oh_get_rdr_by_id(rptable, SAHPI_FIRST_ENTRY,randrdr.RecordId)
    
            self.assertEqual(tmprdr != None, True)
            self.assertEqual(memcmp(randrdr, tmprdr, sizeof_SaHpiRdrT),0)
            records.pop(k)
        
if __name__=='__main__':
        unittest.main()    
