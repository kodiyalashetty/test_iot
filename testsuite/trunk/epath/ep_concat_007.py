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

# oh_concat_ep: concatenate a 4 and a 12 element entity path 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        
        ep1 = SaHpiEntityPathT()
        ep1.Entry[0].EntityType = SAHPI_ENT_POWER_UNIT
        ep1.Entry[0].EntityLocation = 199
        ep1.Entry[1].EntityType = SAHPI_ENT_CHASSIS_BACK_PANEL_BOARD
        ep1.Entry[1].EntityLocation = 202
        ep1.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
        ep1.Entry[2].EntityLocation = 211
        ep1.Entry[3].EntityType = SAHPI_ENT_SUB_CHASSIS
        ep1.Entry[3].EntityLocation = 222
        ep1.Entry[4].EntityType = SAHPI_ENT_ROOT
        ep1.Entry[4].EntityLocation = 0
        
        ep2 = SaHpiEntityPathT()
        ep2.Entry[0].EntityType = SAHPI_ENT_OTHER_CHASSIS_BOARD
        ep2.Entry[0].EntityLocation = 233
        ep2.Entry[1].EntityType = SAHPI_ENT_DISK_DRIVE_BAY
        ep2.Entry[1].EntityLocation = 244
        ep2.Entry[2].EntityType = SAHPI_ENT_PERIPHERAL_BAY_2
        ep2.Entry[2].EntityLocation = 255
        ep2.Entry[3].EntityType = SAHPI_ENT_DEVICE_BAY
        ep2.Entry[3].EntityLocation = 255
        ep2.Entry[4].EntityType = SAHPI_ENT_COOLING_DEVICE
        ep2.Entry[4].EntityLocation = 277
        ep2.Entry[5].EntityType = SAHPI_ENT_COOLING_UNIT
        ep2.Entry[5].EntityLocation = 288
        ep2.Entry[6].EntityType = SAHPI_ENT_INTERCONNECT
        ep2.Entry[6].EntityLocation = 299
        ep2.Entry[7].EntityType = SAHPI_ENT_MEMORY_DEVICE
        ep2.Entry[7].EntityLocation = 303
        ep2.Entry[8].EntityType = SAHPI_ENT_SYS_MGMNT_SOFTWARE
        ep2.Entry[8].EntityLocation = 311
        ep2.Entry[9].EntityType = SAHPI_ENT_BIOS
        ep2.Entry[9].EntityLocation = 322
        ep2.Entry[10].EntityType = SAHPI_ENT_OPERATING_SYSTEM
        ep2.Entry[10].EntityLocation = 333
        ep2.Entry[11].EntityType = SAHPI_ENT_SYSTEM_BUS
        ep2.Entry[11].EntityLocation = 344
        ep2.Entry[12].EntityType = SAHPI_ENT_ROOT
        ep2.Entry[12].EntityLocation = 0
        
        ep3 = SaHpiEntityPathT()
        ep3.Entry[0].EntityType = SAHPI_ENT_POWER_UNIT
        ep3.Entry[0].EntityLocation = 199
        ep3.Entry[1].EntityType = SAHPI_ENT_CHASSIS_BACK_PANEL_BOARD
        ep3.Entry[1].EntityLocation = 202
        ep3.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
        ep3.Entry[2].EntityLocation = 211
        ep3.Entry[3].EntityType = SAHPI_ENT_SUB_CHASSIS
        ep3.Entry[3].EntityLocation = 222
        ep3.Entry[4].EntityType = SAHPI_ENT_OTHER_CHASSIS_BOARD
        ep3.Entry[4].EntityLocation = 233
        ep3.Entry[5].EntityType = SAHPI_ENT_DISK_DRIVE_BAY
        ep3.Entry[5].EntityLocation = 244
        ep3.Entry[6].EntityType = SAHPI_ENT_PERIPHERAL_BAY_2
        ep3.Entry[6].EntityLocation = 255
        ep3.Entry[7].EntityType = SAHPI_ENT_DEVICE_BAY
        ep3.Entry[7].EntityLocation = 255
        ep3.Entry[8].EntityType = SAHPI_ENT_COOLING_DEVICE
        ep3.Entry[8].EntityLocation = 277
        ep3.Entry[9].EntityType = SAHPI_ENT_COOLING_UNIT
        ep3.Entry[9].EntityLocation = 288
        ep3.Entry[10].EntityType = SAHPI_ENT_INTERCONNECT
        ep3.Entry[10].EntityLocation = 299
        ep3.Entry[11].EntityType = SAHPI_ENT_MEMORY_DEVICE
        ep3.Entry[11].EntityLocation = 303
        ep3.Entry[12].EntityType = SAHPI_ENT_SYS_MGMNT_SOFTWARE
        ep3.Entry[12].EntityLocation = 311
        ep3.Entry[13].EntityType = SAHPI_ENT_BIOS
        ep3.Entry[13].EntityLocation = 322
        ep3.Entry[14].EntityType = SAHPI_ENT_OPERATING_SYSTEM
        ep3.Entry[14].EntityLocation = 333
        ep3.Entry[15].EntityType = SAHPI_ENT_SYSTEM_BUS
        ep3.Entry[15].EntityLocation = 344

        err = oh_concat_ep(ep1, ep2)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (not oh_cmp_ep(ep1, ep3),False)
        
if __name__=='__main__':
    unittest.main()
