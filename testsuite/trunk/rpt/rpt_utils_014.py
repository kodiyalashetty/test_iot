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
from rpt_resources import *
from random import *

class TestSequence(unittest.TestCase):
       
    """
    runTest : Starts with an RPTable of 10 resources, multiple rdrs
    on some resources. Remove resource. Check if resource was removed
    searching for it by id. If not fail, else passed test.
            
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):

        rptable = RPTable()
        oh_init_rpt(rptable)

        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rpte, None, 0), 0)

        for i in range (0,5):
            self.assertEqual(oh_add_rdr(rptable, SAHPI_FIRST_ENTRY,sensors[i], None,0), 0)
        
        for i in range (5,7):  
            self.assertEqual(oh_add_rdr(rptable, rptentries[9].ResourceId, sensors[i], None,0), 0)
            
        oh_remove_resource(rptable, rptentries[0].ResourceId)
        tmpentry = oh_get_resource_by_id(rptable, rptentries[0].ResourceId)
        self.assertEqual(tmpentry, None)
                      
if __name__=='__main__':
        unittest.main()    
