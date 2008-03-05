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
    runTest : Starting with an empty RPTable, adds a resource to it
 * twice. Checks to see if the udpate count was updated the 
 * second time. If it was the test failed, otherwise the test passed. 
 Return value: 0 on success, 1 on failure
    """
   
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        update_count = SaHpiUint32T()
               
        self.assertEqual(oh_add_resource(rptable, rptentries, None, 0))
        
        update_count = rptable.update_count
        
        self.assertEqual(oh_add_resource(rptable, rptentries, None, 0))
        
        self.assertEqual((rptable.update_count,update_count),1)
        
                    
if __name__=='__main__':
        unittest.main()    
