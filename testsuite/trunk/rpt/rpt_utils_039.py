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
    runTest : Adds 10 resources to an rpt table.
    Fetches the 1st resource through the get_next call
    using SAHPI_FIRST_ENTRY for the Resource Id. Makes sure that the resource
    returned is the 1st resource.
    Passes the test if the interface returns a valid entry, else it fails.
 
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        tmpentry = SaHpiRptEntryT()
        i = 0
        
        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rptentries[1], None, 1), 0)  
             
        tmpentry = oh_get_resource_next(rptable, SAHPI_FIRST_ENTRY)
        self.assertEqual(not (tmpentry), 0)
        self.assertEqual((tmpentry.ResourceId != rptentries[0].ResourceId), 1)
                              
if __name__=='__main__':
        unittest.main()    
