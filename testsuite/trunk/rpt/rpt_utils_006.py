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
    runTest : Starts with an RPTable of 10 resources, starting at
 * the beginning on going on to the next, compares
 * resource ids against the originals. A failed comparison
 * means the test failed, otherwise the test passed.
        
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):

        print "start"
    
        rptable = RPTable()
        oh_init_rpt(rptable);
        tmpentry = SaHpiRptEntryT()
      
        for i in range (num_resources):
                self.assertEqual(oh_add_resource(rptable, rptentries[i], None, 0), 0)
        
        tmpentry = oh_get_resource_by_id(rptable, SAHPI_FIRST_ENTRY)
	i=0
        while tmpentry :
            self.assertEqual(not(rptentries[i].ResourceId, tmpentry.ResourceId),False)
            tmpentry = oh_get_resource_next(rptable, tmpentry.ResourceId)
            i = i+1
            
if __name__=='__main__':
        unittest.main()    
