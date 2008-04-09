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

""" oh_set_ep_location: Entity type not in entity path.
     OK but nothing changed. """
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        y = 45321
        i = 0
        
        ep=SaHpiEntityPathT()
        #SaHpiEntityTypeT
        w = SAHPI_ENT_IO_BLADE
        #SaHpiEntityLocationT
        x = 56873

        for i in range(0 ,SAHPI_MAX_ENTITY_PATH):
            ep.Entry[i].EntityType = w
            ep.Entry[i].EntityLocation = y+i
            i=i+1

        err = oh_set_ep_location(ep, SAHPI_ENT_IO_SUBBOARD, x)
        self.assertEqual  (err!=None,True)
        
        for i in range(0,SAHPI_MAX_ENTITY_PATH):
            self.assertEqual ((ep.Entry[i].EntityType != w) or
            (ep.Entry[i].EntityLocation != y+i),False) 
            
if __name__=='__main__':
    unittest.main()
