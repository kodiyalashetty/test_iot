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

"""oh_set_ep_location: Dull entity path and victim element in the middle.
    Only victim element's instance number changed. """
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        y = 77002
        z = 3;
        i = 0;
        
        ep=SaHpiEntityPathT()
        #SaHpiEntityTypeT
        w = SAHPI_ENT_SBC_BLADE
        #SaHpiEntityLocationT
        x = 56873
        
        for i in range(0,z):
            ep.Entry[i].EntityType = w
            ep.Entry[i].EntityLocation = y
            i=i+1
        ep.Entry[z].EntityType = SAHPI_ENT_FAN
        ep.Entry[z].EntityLocation = z
        for i in range(z+1, SAHPI_MAX_ENTITY_PATH):
            ep.Entry[i].EntityType = w
            ep.Entry[i].EntityLocation = y
            i=i+1

        err = oh_set_ep_location(ep, SAHPI_ENT_FAN, x)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (ep.Entry[z].EntityLocation != x,False)
        
        self.assertEqual (ep.Entry[z].EntityType != SAHPI_ENT_FAN,False)
        
        for i in range ( 0,z ):
            self.assertEqual ((ep.Entry[i].EntityType != w) or
            (ep.Entry[i].EntityLocation != y),False) 
            i=i+1
            
        for i in range ( z+1, SAHPI_MAX_ENTITY_PATH):
            self.assertEqual  ((ep.Entry[i].EntityType != w) or
            (ep.Entry[i].EntityLocation != y),False)
            
if __name__=='__main__':
    unittest.main()
