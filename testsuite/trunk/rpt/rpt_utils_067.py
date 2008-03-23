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
    runTest : Starting with an empty RPTable, adds 10 resources to it
    and then adds 1 rdr to it with an out-of-range instrument id.
    Passes the test if the interface returns an error, else it fails.
 
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        
        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rpte, None, 0), 0)
                       
        saved_num = sensors[0].RdrTypeUnion.SensorRec.Num
        sensors[0].RdrTypeUnion.SensorRec.Num = SAHPI_STANDARD_SENSOR_MAX - 1
        self.assertEqual(not (oh_add_rdr(rptable, SAHPI_FIRST_ENTRY, sensors[0], None, 1)), 0)
        sensors[0].RdrTypeUnion.SensorRec.Num = saved_num
                   
if __name__=='__main__':
        unittest.main()    
