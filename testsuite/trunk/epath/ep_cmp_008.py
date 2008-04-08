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
# oh_cmp_ep: compare zero to multi-element entity path testcase. 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        ep1 = SaHpiEntityPathT()
        ep1.Entry[0].EntityType = SAHPI_ENT_ROOT
        ep1.Entry[0].EntityLocation = 0
        
        ep2 = SaHpiEntityPathT()
        ep2.Entry[0].EntityType = SAHPI_ENT_FAN
        ep2.Entry[0].EntityLocation = 4
        ep2.Entry[1].EntityType = SAHPI_ENT_SBC_BLADE
        ep2.Entry[1].EntityLocation = 3
        ep2.Entry[2].EntityType = SAHPI_ENT_RACK
        ep2.Entry[2].EntityLocation = 2
        ep2.Entry[3].EntityType = SAHPI_ENT_ROOT
        ep2.Entry[3].EntityLocation = 1
        ep2.Entry[4].EntityType = SAHPI_ENT_ROOT
        ep2.Entry[4].EntityLocation = 0
        
        self.assertEqual (oh_cmp_ep(ep1, ep2),False)
        
if __name__=='__main__':
    unittest.main()
