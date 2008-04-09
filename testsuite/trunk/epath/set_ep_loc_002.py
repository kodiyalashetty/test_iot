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

# oh_set_ep_location: Entity path that has 1 element testcase. 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        ep = SaHpiEntityPathT()
        ep.Entry[0].EntityType = SAHPI_ENT_OTHER
        ep.Entry[0].EntityLocation = 1
        ep.Entry[0].EntityType = 0
        
        #SaHpiEntityPathT ep = {{{SAHPI_ENT_OTHER, 1},{0}}};
        #SaHpiEntityLocationT
        x = 5
        
        err = oh_set_ep_location(ep, SAHPI_ENT_OTHER, x)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (ep.Entry[0].EntityLocation != x,True)
        
        self.assertEqual  (ep.Entry[0].EntityType != SAHPI_ENT_OTHER,True)

if __name__=='__main__':
    unittest.main()
