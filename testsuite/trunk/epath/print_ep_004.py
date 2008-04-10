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
        ep.Entry[1].EntityType = 211
        ep.Entry[1].EntityLocation = 7
        ep.Entry[2].EntityType = 212
        ep.Entry[2].EntityLocation = 6
        ep.Entry[3].EntityType = 213
        ep.Entry[3].EntityLocation = 5
        ep.Entry[4].EntityType = 214
        ep.Entry[4].EntityLocation = 4
        ep.Entry[5].EntityType = 215
        ep.Entry[5].EntityLocation = 3
        ep.Entry[6].EntityType = 216
        ep.Entry[6].EntityLocation = 2
        ep.Entry[7].EntityType = 255
        ep.Entry[7].EntityLocation = 1
        ep.Entry[8].EntityType = SAHPI_ENT_ROOT
        ep.Entry[8].EntityLocation = 1
        
        err = oh_print_ep(ep, offsets)
        self.assertEqual (err!=None,True)
        
if __name__=='__main__':
    unittest.main()
