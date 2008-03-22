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
       
        rptentries[0].ResourceCapabilities = rptentries[0].ResourceCapabilities and 0xFFFFDFFF
        
        i=0
        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rptentries[i], None, 0),0)
            
        sensors[0].RdrTypeUnion.SensorRec.Num = SAHPI_STANDARD_SENSOR_MIN    
        self.assertEqual(not (oh_add_rdr(rptable, SAHPI_FIRST_ENTRY, sensors[0], None, 1)), 0) 
        
if __name__=='__main__':
        unittest.main()    
