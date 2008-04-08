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

# oh_concat_ep: concatenate two 4 element entity path 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        ep1 = SaHpiEntityPathT()
        ep1.Entry[0].EntityType = SAHPI_ENT_ADD_IN_CARD
        ep1.Entry[0].EntityLocation = 111
        ep1.Entry[1].EntityType = SAHPI_ENT_FRONT_PANEL_BOARD
        ep1.Entry[1].EntityLocation = 122
        ep1.Entry[2].EntityType = SAHPI_ENT_BACK_PANEL_BOARD
        ep1.Entry[2].EntityLocation = 133
        ep1.Entry[3].EntityType = SAHPI_ENT_POWER_SYSTEM_BOARD
        ep1.Entry[3].EntityLocation = 144
        ep1.Entry[4].EntityType = SAHPI_ENT_ROOT
        ep1.Entry[4].EntityLocation = 0
        
        ep2 = SaHpiEntityPathT()
        ep2.Entry[0].EntityType = SAHPI_ENT_DRIVE_BACKPLANE
        ep2.Entry[0].EntityLocation = 155
        ep2.Entry[1].EntityType = SAHPI_ENT_SYS_EXPANSION_BOARD
        ep2.Entry[1].EntityLocation = 166
        ep2.Entry[2].EntityType = SAHPI_ENT_OTHER_SYSTEM_BOARD
        ep2.Entry[2].EntityLocation = 177
        ep2.Entry[3].EntityType = SAHPI_ENT_PROCESSOR_BOARD
        ep2.Entry[3].EntityLocation = 188
        ep2.Entry[4].EntityType = SAHPI_ENT_ROOT
        ep2.Entry[4].EntityLocation = 0
        
        ep3 = SaHpiEntityPathT()
        ep3.Entry[0].EntityType = SAHPI_ENT_ADD_IN_CARD
        ep3.Entry[0].EntityLocation = 111
        ep3.Entry[1].EntityType = SAHPI_ENT_FRONT_PANEL_BOARD
        ep3.Entry[1].EntityLocation = 122
        ep3.Entry[2].EntityType = SAHPI_ENT_BACK_PANEL_BOARD
        ep3.Entry[2].EntityLocation = 133
        ep3.Entry[3].EntityType = SAHPI_ENT_POWER_SYSTEM_BOARD
        ep3.Entry[3].EntityLocation = 144
        ep3.Entry[4].EntityType = SAHPI_ENT_DRIVE_BACKPLANE
        ep3.Entry[4].EntityLocation = 155
        ep3.Entry[5].EntityType = SAHPI_ENT_SYS_EXPANSION_BOARD
        ep3.Entry[5].EntityLocation = 166
        ep3.Entry[6].EntityType = SAHPI_ENT_OTHER_SYSTEM_BOARD
        ep3.Entry[6].EntityLocation = 177
        ep3.Entry[7].EntityType = SAHPI_ENT_PROCESSOR_BOARD
        ep3.Entry[7].EntityLocation = 188
        ep3.Entry[8].EntityType = SAHPI_ENT_ROOT
        ep3.Entry[8].EntityLocation = 0

        err = oh_concat_ep(ep1, ep2)
        self.assertEqual  (err!=None,True)
		
        self.assertEqual (not oh_cmp_ep(ep1, ep3),False)
		
if __name__=='__main__':
    unittest.main()
