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
    runTest : Starting with an empty RPTable, adds 10 resources to it
    and removes one by specifying SAHPI_FIRST_ENTRY as the Resource Id.
    Removes again to make sure it is not there anymore.
    Passes the test if the interface returns 0 (success), else it fails.

    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        i = 0
        
        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rptentries[i], None,0), 0)
                
        self.assertEqual(oh_remove_resource(rptable, SAHPI_FIRST_ENTRY),0)
        self.assertEqual(not (oh_remove_resource(rptable, rptentries[0].ResourceId)), 0)
        
if __name__=='__main__':
        unittest.main()    
