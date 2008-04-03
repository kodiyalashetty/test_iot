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

    """
     main: 
     epathstr -> epath test
     
     Test if an entity path string is converted properly into an entity path.
    """
    def runTest(self): 
        test_string = ("{SUB_CHASSIS,26}{SYS_MGMNT_MODULE,76}")
        bigbuf =oh_big_textbuffer()
        ep =SaHpiEntityPathT()        
        err = oh_encode_entitypath(test_string, ep)
        
        self.assertEqual (err!=None,True)
        
        self.assertEqual (ep.Entry[0].EntityType != SAHPI_ENT_SYS_MGMNT_MODULE,False) 
        
        self.assertEqual (ep.Entry[0].EntityLocation != 76,False) 
        
        self.assertEqual (ep.Entry[1].EntityType != SAHPI_ENT_SUB_CHASSIS,False)
        
        self.assertEqual (ep.Entry[1].EntityLocation != 26,False) 
        
        oh_init_bigtext(bigbuf)
        err = oh_decode_entitypath(ep,bigbuf)
        
        self.assertEqual (err!=None,True)
        
        self.assertEqual (bigbuf.Data!= test_string,False) 
        
if __name__=='__main__':
    unittest.main()
