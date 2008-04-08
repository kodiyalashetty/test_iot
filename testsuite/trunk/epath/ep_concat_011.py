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

# oh_concat_ep: concatenate a zero element and a 9 element entity path 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        ep1 = SaHpiEntityPathT()
        ep1.Entry[0].EntityType = SAHPI_ENT_ROOT
        ep1.Entry[0].EntityLocation = 0
        
        ep2 = SaHpiEntityPathT()
        ep2.Entry[0].EntityType = SAHPI_ENT_GROUP
        ep2.Entry[0].EntityLocation = 101
        ep2.Entry[1].EntityType = SAHPI_ENT_REMOTE
        ep2.Entry[1].EntityLocation = 102
        ep2.Entry[2].EntityType = SAHPI_ENT_EXTERNAL_ENVIRONMENT
        ep2.Entry[2].EntityLocation = 103
        ep2.Entry[3].EntityType = SAHPI_ENT_BATTERY
        ep2.Entry[3].EntityLocation = 104
        ep2.Entry[4].EntityType = SAHPI_ENT_CHASSIS_SPECIFIC
        ep2.Entry[4].EntityLocation = 105
        ep2.Entry[5].EntityType = SAHPI_ENT_BOARD_SET_SPECIFIC
        ep2.Entry[5].EntityLocation = 106
        ep2.Entry[6].EntityType = SAHPI_ENT_OEM_SYSINT_SPECIFIC
        ep2.Entry[6].EntityLocation = 107
        ep2.Entry[7].EntityType = SAHPI_ENT_FAN
        ep2.Entry[7].EntityLocation = 108
        ep2.Entry[8].EntityType = SAHPI_ENT_RACK
        ep2.Entry[8].EntityLocation = 109
        ep2.Entry[9].EntityType = SAHPI_ENT_ROOT
        ep2.Entry[9].EntityLocation = 0
        
        ep3 = SaHpiEntityPathT()
        ep3.Entry[0].EntityType = SAHPI_ENT_GROUP
        ep3.Entry[0].EntityLocation = 101
        ep3.Entry[1].EntityType = SAHPI_ENT_REMOTE
        ep3.Entry[1].EntityLocation = 102
        ep3.Entry[2].EntityType = SAHPI_ENT_EXTERNAL_ENVIRONMENT
        ep3.Entry[2].EntityLocation = 103
        ep3.Entry[3].EntityType = SAHPI_ENT_BATTERY
        ep3.Entry[3].EntityLocation = 104
        ep3.Entry[4].EntityType = SAHPI_ENT_CHASSIS_SPECIFIC
        ep3.Entry[4].EntityLocation = 105
        ep3.Entry[5].EntityType = SAHPI_ENT_BOARD_SET_SPECIFIC
        ep3.Entry[5].EntityLocation = 106
        ep3.Entry[6].EntityType = SAHPI_ENT_OEM_SYSINT_SPECIFIC
        ep3.Entry[6].EntityLocation = 107
        ep3.Entry[7].EntityType = SAHPI_ENT_FAN
        ep3.Entry[7].EntityLocation = 108
        ep3.Entry[8].EntityType = SAHPI_ENT_RACK
        ep3.Entry[8].EntityLocation = 109
        ep3.Entry[9].EntityType = SAHPI_ENT_ROOT
        ep3.Entry[9].EntityLocation = 0
        
        err = oh_concat_ep(ep1, ep2)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual  (not oh_cmp_ep(ep1, ep3),False)
        
if __name__=='__main__':
    unittest.main()
