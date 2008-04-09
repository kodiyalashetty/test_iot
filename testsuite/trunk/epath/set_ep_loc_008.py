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

""" oh_set_ep_location: 4 element entity path, victim element at head.
    Only head element's instance number changed. """
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        ep = SaHpiEntityPathT()
        ep.Entry[0].EntityType = SAHPI_ENT_ADD_IN_CARD
        ep.Entry[0].EntityLocation = 101
        ep.Entry[0].EntityType = SAHPI_ENT_POWER_MODULE
        ep.Entry[0].EntityLocation = 2020
        ep.Entry[0].EntityType = SAHPI_ENT_POWER_MGMNT
        ep.Entry[0].EntityLocation = 30303
        ep.Entry[0].EntityType = SAHPI_ENT_SUB_CHASSIS
        ep.Entry[0].EntityLocation = 404040
        ep.Entry[0].EntityType = 0
        
        #SaHpiEntityLocationT
        x = 555555
    
        err = oh_set_ep_location(ep, SAHPI_ENT_ADD_IN_CARD, x)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (ep.Entry[0].EntityLocation != x,True)
        
        self.assertEqual (ep.Entry[0].EntityType != SAHPI_ENT_ADD_IN_CARD,True)
        
        self.assertEqual (ep.Entry[1].EntityLocation != 2020,True)
        
        self.assertEqual (ep.Entry[1].EntityType != SAHPI_ENT_POWER_MODULE,True)
        
        self.assertEqual (ep.Entry[2].EntityLocation != 30303,True)
        
        self.assertEqual (ep.Entry[2].EntityType != SAHPI_ENT_POWER_MGMNT,True)
        
        self.assertEqual (ep.Entry[3].EntityLocation != 404040,True)
        
        self.assertEqual (ep.Entry[3].EntityType != SAHPI_ENT_SUB_CHASSIS,True)
        
if __name__=='__main__':
    unittest.main()
