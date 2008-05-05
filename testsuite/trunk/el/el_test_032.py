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
    Jayashree Padmanabhan <jayshree@in.ibm.com>
"""

import unittest
from openhpi import *


class TestSequence(unittest.TestCase):
       
    """
    runTest : EL test
 *
 * This test creates an EL and resets info.OverflowFlag (oh_el_overflowreset)
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
        
        el = oh_el()
        retc = None
    
        # map el from file
        el = oh_el_create(20)
        retc = oh_el_map_from_file(el, "./elTest.data")
        self.assertEqual (retc != SA_OK,False)
            
        retc = oh_el_overflowreset(el)
        self.assertEqual (retc != SA_OK,False)
            
if __name__=='__main__':
    unittest.main()  
