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
# oh_concat_ep: concatenate two full entity path
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        ep1 = SaHpiEntityPathT()
        ep2 = SaHpiEntityPathT()
        ep3 = SaHpiEntityPathT()

        for i in range (0, SAHPI_MAX_ENTITY_PATH): 
            ep1.Entry[i].EntityType = SAHPI_ENT_IO_BLADE
            ep1.Entry[i].EntityLocation = 896
            ep3.Entry[i].EntityType = SAHPI_ENT_IO_BLADE
            ep3.Entry[i].EntityLocation = 896
            ep2.Entry[i].EntityType = SAHPI_ENT_SBC_BLADE
            ep2.Entry[i].EntityLocation = 123
            i=i+1
        
        err = oh_concat_ep(ep1, ep2)
        
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (not oh_cmp_ep(ep1, ep3),False)
        
if __name__=='__main__':
    unittest.main()
