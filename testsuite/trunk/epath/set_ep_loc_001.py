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

""" oh_set_ep_location: Zero entry entity path testcase.
 * Call should be ok but not change anything. """
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):	
        ep = SaHpiEntityPathT()
        ep.Entry[0].EntityType = 0
        ep.Entry[0].EntityLocation = 0
        #SaHpiEntityPathT ep = {{{0,0}}}
        #SaHpiEntityLocationT 
        x = 3

        err = oh_set_ep_location(ep, SAHPI_ENT_BACK_PANEL_BOARD, x)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (ep.Entry[0].EntityLocation != 0,False)
        
        self.assertEqual (ep.Entry[0].EntityType != 0,False) 
        
if __name__=='__main__':
    unittest.main()
