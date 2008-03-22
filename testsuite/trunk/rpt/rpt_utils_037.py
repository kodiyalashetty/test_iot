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
    runTest : Adds 2 resources to an rpt table.
    Fetches the 2nd resource through the get_next call
    using a NULL table.
    Passes the test if the interface returns NULL, else it fails. 
 
 Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        self.assertEqual(oh_add_resource(rptable, rptentries[0], None, 1), 0)
        self.assertEqual(oh_add_resource(rptable, rptentries[1], None, 1), 0)   
        self.assertEqual(oh_get_resource_next(None, rptentries[0].ResourceId)==None, True)
                            
if __name__=='__main__':
        unittest.main()    
