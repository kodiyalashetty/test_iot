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
    Suntrupth S Yadav <suntrupth@in.ibm.com>
"""

# oh_set_ep_location: Entity path that has 2 elements testcase. 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        
        ep = SaHpiEntityPathT()
        ep.Entry[0].EntityType = SAHPI_ENT_BIOS
        ep.Entry[0].EntityLocation = 1
        ep.Entry[1].EntityType = SAHPI_ENT_UNKNOWN
        ep.Entry[1].EntityLocation = 2
        
        #SaHpiEntityLocationT
        x = 777
        
        err = oh_set_ep_location(ep, SAHPI_ENT_UNKNOWN, x)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (ep.Entry[1].EntityLocation != x,False)
        
        self.assertEqual (ep.Entry[1].EntityType != SAHPI_ENT_UNKNOWN,False)
        
        self.assertEqual (ep.Entry[0].EntityLocation != 1,False)
        
        self.assertEqual (ep.Entry[0].EntityType != SAHPI_ENT_BIOS,False)
        
if __name__=='__main__':
    unittest.main()
