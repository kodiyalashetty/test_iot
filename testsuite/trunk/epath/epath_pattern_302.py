#!/usr/bin/env python
""" (C) Copyright IBM Corp. 2008
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 file and program are licensed under a BSD style license.  See
 the Copying file included with the OpenHPI distribution for
 full licensing terms.
 
 Authors:
    Suntrupth S Yadav <suntrupth@in.ibm.com>
"""
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):
        
    def runTest(self):
        ep_str = "{PHYSICAL_SLOT,4}{SBC_BLADE,3}{ADD_IN_CARD,8}"
        epp_str = "{SYSTEM_CHASSIS,1}{SBC_BLADE,.}*"
        epp=oh_entitypath_pattern()
        ep=SaHpiEntityPathT()
        error = SA_OK
        #SaHpiBoolT
        match = "0"

        error = oh_encode_entitypath(ep_str, ep)
        self.assertEqual  (error == SA_OK,True) 
        
        error = oh_compile_entitypath_pattern(epp_str, epp)
        self.assertEqual  (error == SA_OK,True) 
        
        self.assertEqual (oh_match_entitypath_pattern(epp, ep) != match,True)
        
        
        
if __name__=='__main__':
    unittest.main()
        
