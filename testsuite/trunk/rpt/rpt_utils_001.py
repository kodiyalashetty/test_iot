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
from rpt_resources import rptentries, objcmp

class TestSequence(unittest.TestCase):
       
    """
    runTest :Starting with an empty RPTable, adds 1 resource to it
    and tries to fetch it by the entity path and compare it against
    the original resource. A failed comparison means the test
    failed, otherwise the test passed.
 *
     
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):

        rptable = RPTable()
        
        oh_init_rpt(rptable)
        
        self.assertEqual(oh_add_resource(rptable, rptentries[0], None, 0), 0)
        
        tmpentry = oh_get_resource_by_ep(rptable, (rptentries[0].ResourceEntity))
        
        self.assertEqual(tmpentry != None, True)

        self.assertEqual(objcmp(rptentries[0], tmpentry), True)
        
if __name__=='__main__':
        unittest.main()        
        
        
