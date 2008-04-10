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

"""oh_set_ep_location: Entity type not in multi-element entity path.
    OK but nothing changed """
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        ep = SaHpiEntityPathT()
        ep.Entry[0].EntityType = SAHPI_ENT_GROUP
        ep.Entry[0].EntityLocation = 100
        ep.Entry[1].EntityType = SAHPI_ENT_REMOTE
        ep.Entry[1].EntityLocation = 200
        ep.Entry[2].EntityType = SAHPI_ENT_EXTERNAL_ENVIRONMENT
        ep.Entry[2].EntityLocation = 300
        ep.Entry[3].EntityType = SAHPI_ENT_BATTERY
        ep.Entry[3].EntityLocation = 400
        ep.Entry[4].EntityType = SAHPI_ENT_CHASSIS_SPECIFIC
        ep.Entry[4].EntityLocation = 500
        ep.Entry[5].EntityType = SAHPI_ENT_BOARD_SET_SPECIFIC
        ep.Entry[5].EntityLocation = 600
        ep.Entry[6].EntityType = SAHPI_ENT_OEM_SYSINT_SPECIFIC
        ep.Entry[6].EntityLocation = 700
        ep.Entry[7].EntityType = SAHPI_ENT_ROOT
        ep.Entry[7].EntityLocation = 800
        ep.Entry[8].EntityType = SAHPI_ENT_RACK
        ep.Entry[8].EntityLocation = 900
        ep.Entry[9].EntityType = SAHPI_ENT_SUBRACK
        ep.Entry[9].EntityLocation = 1000
        
        #SaHpiEntityLocationT
        x = 11000

        err = oh_set_ep_location(ep, SAHPI_ENT_FAN, x)
        #self.assertEqual  (err!=None,True)
        self.assertEqual  (err == SA_OK,True) 
        
        self.assertEqual ((ep.Entry[0].EntityLocation != 100) or
           (ep.Entry[0].EntityType != SAHPI_ENT_GROUP) or
           (ep.Entry[1].EntityLocation != 200) or
           (ep.Entry[1].EntityType != SAHPI_ENT_REMOTE) or
           (ep.Entry[2].EntityLocation != 300) or
           (ep.Entry[2].EntityType != SAHPI_ENT_EXTERNAL_ENVIRONMENT) or
           (ep.Entry[3].EntityLocation != 400) or
           (ep.Entry[3].EntityType != SAHPI_ENT_BATTERY) or
           (ep.Entry[4].EntityLocation != 500) or
           (ep.Entry[4].EntityType != SAHPI_ENT_CHASSIS_SPECIFIC) or
           (ep.Entry[5].EntityLocation != 600) or
           (ep.Entry[5].EntityType != SAHPI_ENT_BOARD_SET_SPECIFIC) or
           (ep.Entry[6].EntityLocation != 700) or
           (ep.Entry[6].EntityType != SAHPI_ENT_OEM_SYSINT_SPECIFIC) or
           (ep.Entry[7].EntityLocation != 800) or
           (ep.Entry[7].EntityType != SAHPI_ENT_ROOT) or
           (ep.Entry[8].EntityLocation != 900) or
           (ep.Entry[8].EntityType != SAHPI_ENT_RACK) or
           (ep.Entry[9].EntityLocation != 1000) or
           (ep.Entry[9].EntityType != SAHPI_ENT_SUBRACK),False) 
            
if __name__=='__main__':
    unittest.main()
