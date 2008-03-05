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
    runTest : Starts with an RPTable of 10 resources (one with data), adds 5 rdr
 * to first resource and 2 to the last one.
 * Invokes oh_flush on the table.
 * Should return without crashing and there should be no resources left
 * in the table.
 
 Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        i = 0
        data = "My data."
        
        self.assertEqual(oh_add_resource(rptable, rptentries[0], rptentries[0], 1), 0)  
        
        i = 1
        for i in range (num_resources):
            self.assertEqual(oh_add_resource(rptable, rptentries[i], None, 0),0)
                   
        for i in range(num_sensors):
            self.assertEqual(oh_add_rdr(rptable, SAHPI_FIRST_ENTRY, sensors[i], None, 0), 0)  
                   
        for i in range(5,7):
            self.assertEqual(oh_add_rdr(rptable, rptentries[9].ResourceId, sensors[i], None, 0), 0)
                        
        oh_flush_rpt(rptable)
        self.assertEqual(oh_get_resource_by_id(rptable, SAHPI_FIRST_ENTRY)==None, True)
            
if __name__=='__main__':
        unittest.main()    
