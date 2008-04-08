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

# oh_concat_ep: concatenate two 3 element entity path 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        ep1 = SaHpiEntityPathT()
        ep1.Entry[0].EntityType = SAHPI_ENT_PERIPHERAL_BAY
        ep1.Entry[0].EntityLocation = 55
        ep1.Entry[1].EntityType = SAHPI_ENT_SYS_MGMNT_MODULE
        ep1.Entry[1].EntityLocation = 66
        ep1.Entry[2].EntityType = SAHPI_ENT_SYSTEM_BOARD
        ep1.Entry[2].EntityLocation = 77
        ep1.Entry[3].EntityType = SAHPI_ENT_ROOT
        ep1.Entry[3].EntityLocation = 0
        
        ep2 = SaHpiEntityPathT()
        ep2.Entry[0].EntityType = SAHPI_ENT_MEMORY_MODULE
        ep2.Entry[0].EntityLocation = 88
        ep2.Entry[1].EntityType = SAHPI_ENT_PROCESSOR_MODULE
        ep2.Entry[1].EntityLocation = 99
        ep2.Entry[2].EntityType = SAHPI_ENT_POWER_SUPPLY
        ep2.Entry[2].EntityLocation = 101
        ep2.Entry[3].EntityType = SAHPI_ENT_ROOT
        ep2.Entry[3].EntityLocation = 0
        
        ep3 = SaHpiEntityPathT()
        ep3.Entry[0].EntityType = SAHPI_ENT_PERIPHERAL_BAY
        ep3.Entry[0].EntityLocation = 55
        ep3.Entry[1].EntityType = SAHPI_ENT_SYS_MGMNT_MODULE
        ep3.Entry[1].EntityLocation = 66
        ep3.Entry[2].EntityType = SAHPI_ENT_SYSTEM_BOARD
        ep3.Entry[2].EntityLocation = 77
        ep3.Entry[3].EntityType = SAHPI_ENT_MEMORY_MODULE
        ep3.Entry[3].EntityLocation = 88
        ep3.Entry[4].EntityType = SAHPI_ENT_PROCESSOR_MODULE
        ep3.Entry[4].EntityLocation = 99
        ep3.Entry[5].EntityType = SAHPI_ENT_POWER_SUPPLY
        ep3.Entry[5].EntityLocation = 101
        ep3.Entry[6].EntityType = SAHPI_ENT_ROOT
        ep3.Entry[6].EntityLocation = 0
        
        err = oh_concat_ep(ep1, ep2)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (not oh_cmp_ep(ep1, ep3),False)
        
if __name__=='__main__':
    unittest.main()
