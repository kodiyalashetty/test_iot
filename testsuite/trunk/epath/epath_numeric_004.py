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

import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        bigbuf=oh_big_textbuffer()
        ep=SaHpiEntityPathT()

        # check if we can convert the last entry of the list 
        test_string = "{PHYSICAL_SLOT,12}"

        err = oh_encode_entitypath(test_string, ep)
        self.assertEqual (err!=None,True)
        
        oh_init_bigtext(bigbuf)
        err = oh_decode_entitypath(ep, bigbuf)
        
        self.assertEqual (err!=None,True)
        
        self.assertEqual  (bigbuf.Data!= test_string,False)
    
if __name__=='__main__':
    unittest.main()
