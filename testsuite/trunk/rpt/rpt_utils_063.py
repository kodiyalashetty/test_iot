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
    runTest : Starting with an empty RPTable, adds 1 resource to it
 * and then adds 1 rdr to it. Removes rdr using a special value like
 * SAHPI_FIRST_ENTRY.
 * Passes the test if the interface returns ok, else it fails.
 
 Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        i = 0
        
        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rptentries[i], None, 0),0)
                   
        self.assertEqual(oh_add_rdr(rptable, rptentries[0].ResourceId, sensors[0], None, 1), 0)  
        self.assertEqual(oh_remove_rdr(rptable, rptentries[0].ResourceId, SAHPI_FIRST_ENTRY), 0)
                    
if __name__=='__main__':
        unittest.main()    
