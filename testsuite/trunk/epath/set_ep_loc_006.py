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

""" oh_set_ep_location: Entity path has 4 elements, victim element 
   in the middle. Only victim element's instance number changed """
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        
        ep = SaHpiEntityPathT()
        ep.Entry[0].EntityType = SAHPI_ENT_FAN
        ep.Entry[0].EntityLocation = 11099
        ep.Entry[1].EntityType = SAHPI_ENT_BATTERY
        ep.Entry[1].EntityLocation = 2002
        ep.Entry[2].EntityType = SAHPI_ENT_RACK
        ep.Entry[2].EntityLocation = 37373
        ep.Entry[3].EntityType = SAHPI_ENT_DISK_BAY
        ep.Entry[3].EntityLocation = 440044
        
        #SaHpiEntityLocationT 
        x = 123456

        err = oh_set_ep_location( ep, SAHPI_ENT_RACK, x)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (ep.Entry[2].EntityLocation != x,False)
        
        self.assertEqual (ep.Entry[2].EntityType != SAHPI_ENT_RACK,False)
        
        self.assertEqual (ep.Entry[0].EntityLocation != 11099,False)
        
        self.assertEqual (ep.Entry[0].EntityType != SAHPI_ENT_FAN,False)
        
        self.assertEqual (ep.Entry[1].EntityLocation != 2002,False)
        
        self.assertEqual (ep.Entry[1].EntityType != SAHPI_ENT_BATTERY,False)
        
        self.assertEqual (ep.Entry[3].EntityLocation != 440044,False)
        
        self.assertEqual (ep.Entry[3].EntityType != SAHPI_ENT_DISK_BAY,False)
        
if __name__=='__main__':
    unittest.main()
