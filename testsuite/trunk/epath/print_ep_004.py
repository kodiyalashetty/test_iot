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

# oh_print_ep: Multi-element numeric entity path testcase. 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):
    def runTest(self):
        offsets = 1
        ep = SaHpiEntityPathT()
        ep.Entry[0].EntityType = 210
        ep.Entry[0].EntityLocation = 8
        ep.Entry[0].EntityType = 211
        ep.Entry[0].EntityLocation = 7
        ep.Entry[0].EntityType = 212
        ep.Entry[0].EntityLocation = 6
        ep.Entry[0].EntityType = 213
        ep.Entry[0].EntityLocation = 5
        ep.Entry[0].EntityType = 214
        ep.Entry[0].EntityLocation = 4
        ep.Entry[0].EntityType = 215
        ep.Entry[0].EntityLocation = 3
        ep.Entry[0].EntityType = 216
        ep.Entry[0].EntityLocation = 2
        ep.Entry[0].EntityType = 255
        ep.Entry[0].EntityLocation = 1
        ep.Entry[0].EntityType = SAHPI_ENT_ROOT
        ep.Entry[0].EntityLocation = 1
        ep.Entry[0].EntityType = 0
        
        err = oh_print_ep(ep, offsets)
        self.assertEqual (err!=None,True)
        
if __name__=='__main__':
    unittest.main()
