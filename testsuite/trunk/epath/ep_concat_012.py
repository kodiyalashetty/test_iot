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

# oh_concat_ep: concatenate a 15 element and a zero element entity path 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        
        ep1 = SaHpiEntityPathT()
        ep1.Entry[0].EntityType = SAHPI_ENT_GROUP
        ep1.Entry[0].EntityLocation = 1
        ep1.Entry[1].EntityType = SAHPI_ENT_REMOTE
        ep1.Entry[1].EntityLocation = 2
        ep1.Entry[2].EntityType = SAHPI_ENT_EXTERNAL_ENVIRONMENT
        ep1.Entry[2].EntityLocation = 3
        ep1.Entry[3].EntityType = SAHPI_ENT_BATTERY
        ep1.Entry[3].EntityLocation = 4
        ep1.Entry[4].EntityType = SAHPI_ENT_CHASSIS_SPECIFIC
        ep1.Entry[4].EntityLocation = 5
        ep1.Entry[5].EntityType = SAHPI_ENT_BOARD_SET_SPECIFIC
        ep1.Entry[5].EntityLocation = 6
        ep1.Entry[6].EntityType = SAHPI_ENT_OEM_SYSINT_SPECIFIC
        ep1.Entry[6].EntityLocation = 7
        ep1.Entry[7].EntityType = SAHPI_ENT_FAN
        ep1.Entry[7].EntityLocation = 8
        ep1.Entry[8].EntityType = SAHPI_ENT_RACK
        ep1.Entry[8].EntityLocation = 9
        ep1.Entry[9].EntityType = SAHPI_ENT_SUBRACK
        ep1.Entry[9].EntityLocation = 10
        ep1.Entry[10].EntityType = SAHPI_ENT_COMPACTPCI_CHASSIS
        ep1.Entry[10].EntityLocation = 11
        ep1.Entry[11].EntityType = SAHPI_ENT_ADVANCEDTCA_CHASSIS
        ep1.Entry[11].EntityLocation = 12
        ep1.Entry[12].EntityType = SAHPI_ENT_PHYSICAL_SLOT
        ep1.Entry[12].EntityLocation = 13
        ep1.Entry[13].EntityType = SAHPI_ENT_SBC_BLADE
        ep1.Entry[13].EntityLocation = 14
        ep1.Entry[14].EntityType = SAHPI_ENT_IO_BLADE
        ep1.Entry[14].EntityLocation = 15
        ep1.Entry[15].EntityType = SAHPI_ENT_ROOT
        ep1.Entry[15].EntityLocation = 0
        
        ep2 = SaHpiEntityPathT()
        ep2.Entry[0].EntityType = SAHPI_ENT_ROOT
        ep2.Entry[0].EntityLocation = 0
        
        ep3 = SaHpiEntityPathT()
        ep3.Entry[0].EntityType = SAHPI_ENT_GROUP
        ep3.Entry[0].EntityLocation = 1
        ep3.Entry[1].EntityType = SAHPI_ENT_REMOTE
        ep3.Entry[1].EntityLocation = 2
        ep3.Entry[2].EntityType = SAHPI_ENT_EXTERNAL_ENVIRONMENT
        ep3.Entry[2].EntityLocation = 3
        ep3.Entry[3].EntityType = SAHPI_ENT_BATTERY
        ep3.Entry[3].EntityLocation = 4
        ep3.Entry[4].EntityType = SAHPI_ENT_CHASSIS_SPECIFIC
        ep3.Entry[4].EntityLocation = 5
        ep3.Entry[5].EntityType = SAHPI_ENT_BOARD_SET_SPECIFIC
        ep3.Entry[5].EntityLocation = 6
        ep3.Entry[6].EntityType = SAHPI_ENT_OEM_SYSINT_SPECIFIC
        ep3.Entry[6].EntityLocation = 7
        ep3.Entry[7].EntityType = SAHPI_ENT_FAN
        ep3.Entry[7].EntityLocation = 8
        ep3.Entry[8].EntityType = SAHPI_ENT_RACK
        ep3.Entry[8].EntityLocation = 9
        ep3.Entry[9].EntityType = SAHPI_ENT_SUBRACK
        ep3.Entry[9].EntityLocation = 10
        ep3.Entry[10].EntityType = SAHPI_ENT_COMPACTPCI_CHASSIS
        ep3.Entry[10].EntityLocation = 11
        ep3.Entry[11].EntityType = SAHPI_ENT_ADVANCEDTCA_CHASSIS
        ep3.Entry[11].EntityLocation = 12
        ep3.Entry[12].EntityType = SAHPI_ENT_PHYSICAL_SLOT
        ep3.Entry[12].EntityLocation = 13
        ep3.Entry[13].EntityType = SAHPI_ENT_SBC_BLADE
        ep3.Entry[13].EntityLocation = 14
        ep3.Entry[14].EntityType = SAHPI_ENT_IO_BLADE
        ep3.Entry[14].EntityLocation = 15
        ep3.Entry[15].EntityType = SAHPI_ENT_ROOT
        ep3.Entry[15].EntityLocation = 0
        
        err = oh_concat_ep(ep1, ep2)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (not oh_cmp_ep(ep1, ep3),False) 
        
if __name__=='__main__':
    unittest.main()
