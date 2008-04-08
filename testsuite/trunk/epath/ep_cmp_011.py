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
# oh_cmp_ep: unidentical multi-element entity path testcase. 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        ep1 = SaHpiEntityPathT()
        ep1.Entry[0].EntityType = SAHPI_ENT_ADD_IN_CARD
        ep1.Entry[0].EntityLocation = 51
        ep1.Entry[1].EntityType = SAHPI_ENT_FRONT_PANEL_BOARD
        ep1.Entry[1].EntityLocation = 52
        ep1.Entry[2].EntityType = SAHPI_ENT_BACK_PANEL_BOARD
        ep1.Entry[2].EntityLocation = 53
        ep1.Entry[3].EntityType = SAHPI_ENT_POWER_SYSTEM_BOARD
        ep1.Entry[3].EntityLocation = 54
        ep1.Entry[4].EntityType = SAHPI_ENT_DRIVE_BACKPLANE
        ep1.Entry[4].EntityLocation = 55
        ep1.Entry[5].EntityType = SAHPI_ENT_SYS_EXPANSION_BOARD
        ep1.Entry[5].EntityLocation = 56
        ep1.Entry[6].EntityType = SAHPI_ENT_OTHER_SYSTEM_BOARD
        ep1.Entry[6].EntityLocation = 57
        ep1.Entry[7].EntityType = SAHPI_ENT_PROCESSOR_BOARD
        ep1.Entry[7].EntityLocation = 58
        ep1.Entry[8].EntityType = SAHPI_ENT_ROOT
        ep1.Entry[8].EntityLocation = 0
        
        ep2 = SaHpiEntityPathT()
        ep2.Entry[0].EntityType = SAHPI_ENT_ADD_IN_CARD
        ep2.Entry[0].EntityLocation = 51
        ep2.Entry[1].EntityType = SAHPI_ENT_FRONT_PANEL_BOARD
        ep2.Entry[1].EntityLocation = 52
        ep2.Entry[2].EntityType = SAHPI_ENT_BACK_PANEL_BOARD
        ep2.Entry[2].EntityLocation = 53
        ep2.Entry[3].EntityType = SAHPI_ENT_POWER_SYSTEM_BOARD
        ep2.Entry[3].EntityLocation = 54
        ep2.Entry[4].EntityType = SAHPI_ENT_DRIVE_BACKPLANE
        ep2.Entry[4].EntityLocation = 55
        ep2.Entry[5].EntityType = SAHPI_ENT_SYS_EXPANSION_BOARD
        ep2.Entry[5].EntityLocation = 56
        ep2.Entry[6].EntityType = SAHPI_ENT_POWER_MODULE
        ep2.Entry[6].EntityLocation = 57
        ep2.Entry[7].EntityType = SAHPI_ENT_PROCESSOR_BOARD
        ep2.Entry[7].EntityLocation = 58
        ep2.Entry[8].EntityType = SAHPI_ENT_ROOT
        ep2.Entry[8].EntityLocation = 0

        self.assertEqual (oh_cmp_ep(ep1, ep2),False) 
        
if __name__=='__main__':
    unittest.main()
