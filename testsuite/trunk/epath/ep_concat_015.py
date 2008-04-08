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

""" oh_concat_ep: concatenate a 5 element entity path that has garbage 
   beyond end element with a 5 element. Garbage should be gone
   at end result. """
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
        ep1.Entry[5].EntityType = SAHPI_ENT_ROOT
        ep1.Entry[5].EntityLocation = 0
        ep1.Entry[6].EntityType = SAHPI_ENT_FAN
        ep1.Entry[6].EntityLocation = 11
        ep1.Entry[7].EntityType = SAHPI_ENT_RACK
        ep1.Entry[7].EntityLocation = 12 
        
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
        ep2.Entry[5].EntityType = SAHPI_ENT_ROOT
        ep2.Entry[5].EntityLocation = 0
        
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
        ep3.Entry[5].EntityType = SAHPI_ENT_GROUP
        ep3.Entry[5].EntityLocation = 101
        ep3.Entry[6].EntityType = SAHPI_ENT_REMOTE
        ep3.Entry[6].EntityLocation = 102
        ep3.Entry[7].EntityType = SAHPI_ENT_EXTERNAL_ENVIRONMENT
        ep3.Entry[7].EntityLocation = 103
        ep3.Entry[8].EntityType = SAHPI_ENT_BATTERY
        ep3.Entry[8].EntityLocation = 104
        ep3.Entry[9].EntityType = SAHPI_ENT_CHASSIS_SPECIFIC
        ep3.Entry[9].EntityLocation = 105
        ep3.Entry[10].EntityType = SAHPI_ENT_ROOT
        ep3.Entry[10].EntityLocation = 0
        
        err = oh_concat_ep(ep1, ep2)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (not oh_cmp_ep(ep1, ep3),False)
        
if __name__=='__main__':
    unittest.main()
