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

# oh_print_ep: Full entity path testcase. 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):
    def runTest(self):
        offsets = 1
        ep=SaHpiEntityPathT()

        for i in range (0, SAHPI_MAX_ENTITY_PATH): 
            ep.Entry[i].EntityType = SAHPI_ENT_SBC_BLADE
            ep.Entry[i].EntityLocation = i+10
            i=i+1

        err = oh_print_ep(ep, offsets)
        self.assertEqual (err!=None,True)
        
if __name__=='__main__':
    unittest.main()
