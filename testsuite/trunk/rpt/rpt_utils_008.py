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
 * a random resource on going on to the next, compares
 * resource ids against the originals. A failed comparison
 * means the test failed, otherwise the test passed.`
        
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):

        rptable = RPTable()
        oh_init_rpt(rptable);
        tmpentry =  SaHpiRptEntryT()
        i = k = 0
        
        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rpte, None, 0), 0)

        k = randrange(0, len(rptentries), 1)
        
        tmpentry = oh_get_resource_by_id(rptable, rptentries[k].ResourceId)
        while  tmpentry:     
            self.assertEqual(rptentries[k].ResourceId==tmpentry.ResourceId, True)
            tmpentry = oh_get_resource_next(rptable, tmpentry.ResourceId)
            i=i+1

if __name__=='__main__':
        unittest.main()    
