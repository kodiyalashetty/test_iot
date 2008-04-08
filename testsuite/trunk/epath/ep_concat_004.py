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

# oh_concat_ep: concatenate 2 two element entity path 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        ep1 = SaHpiEntityPathT()
        ep1.Entry[0].EntityType = SAHPI_ENT_UNKNOWN
        ep1.Entry[0].EntityLocation = 11
        ep1.Entry[1].EntityType = SAHPI_ENT_OTHER
        ep1.Entry[1].EntityLocation = 22
        ep1.Entry[2].EntityType = SAHPI_ENT_ROOT
        ep1.Entry[2].EntityLocation = 0
        
        ep2 = SaHpiEntityPathT()
        ep2.Entry[0].EntityType = SAHPI_ENT_PROCESSOR
        ep2.Entry[0].EntityLocation = 39
        ep2.Entry[1].EntityType = SAHPI_ENT_DISK_BAY
        ep2.Entry[1].EntityLocation = 44
        ep2.Entry[2].EntityType = SAHPI_ENT_ROOT
        ep2.Entry[2].EntityLocation = 0
        
        ep3 = SaHpiEntityPathT()
        ep3.Entry[0].EntityType = SAHPI_ENT_UNKNOWN
        ep3.Entry[0].EntityLocation = 11
        ep3.Entry[1].EntityType = SAHPI_ENT_OTHER
        ep3.Entry[1].EntityLocation = 22
        ep3.Entry[2].EntityType = SAHPI_ENT_PROCESSOR
        ep3.Entry[2].EntityLocation = 39
        ep3.Entry[3].EntityType = SAHPI_ENT_DISK_BAY
        ep3.Entry[3].EntityLocation = 44
        ep3.Entry[4].EntityType = SAHPI_ENT_ROOT
        ep3.Entry[4].EntityLocation = 0
        
        err = oh_concat_ep(ep1, ep2)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (not oh_cmp_ep(ep1, ep3),False)
        
if __name__=='__main__':
    unittest.main()
