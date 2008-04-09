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

""" oh_set_ep_location: Entity path has 4 elements, victim element
    in middle. Only victim element's instance number changed """
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        ep = SaHpiEntityPathT()
        ep.Entry[0].EntityType = SAHPI_ENT_INTERCONNECT
        ep.Entry[0].EntityLocation = 1515
        ep.Entry[0].EntityType = SAHPI_ENT_PHYSICAL_SLOT
        ep.Entry[0].EntityLocation = 2525
        ep.Entry[0].EntityType = SAHPI_ENT_SUBRACK
        ep.Entry[0].EntityLocation = 3535
        ep.Entry[0].EntityType = SAHPI_ENT_IO_SUBBOARD
        ep.Entry[0].EntityLocation = 4545
        ep.Entry[0].EntityType = 0
    
        #SaHpiEntityLocationT
        x = 98765  
        
        err = oh_set_ep_location(ep, SAHPI_ENT_PHYSICAL_SLOT, x)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (ep.Entry[1].EntityLocation != x,True)
        
        self.assertEqual (ep.Entry[1].EntityType != SAHPI_ENT_PHYSICAL_SLOT,True)
        
        self.assertEqual (ep.Entry[0].EntityLocation != 1515,True)
        
        self.assertEqual (ep.Entry[0].EntityType != SAHPI_ENT_INTERCONNECT,True)
        
        self.assertEqual (ep.Entry[2].EntityLocation != 3535,True)
        
        self.assertEqual (ep.Entry[2].EntityType != SAHPI_ENT_SUBRACK,True)
        
        self.assertEqual (ep.Entry[3].EntityLocation != 4545,True)
        
        self.assertEqual (ep.Entry[3].EntityType != SAHPI_ENT_IO_SUBBOARD,True)
        
if __name__=='__main__':
    unittest.main()
