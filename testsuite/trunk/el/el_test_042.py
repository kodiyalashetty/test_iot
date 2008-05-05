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
 * This test creates an EL and verifies correctness of oh_el_timeset
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
        
        el = oh_el()
        timestamp = 0
        retc = None

        # tests oh_el_timeset when el != None

        el = oh_el_create(20)

        retc = oh_el_timeset(el, timestamp + 20)
        self.assertEqual (retc != SA_OK,False)
            
        # close el without saving to file
        retc = oh_el_close(el)
        self.assertEqual (retc != SA_OK,False)
            
if __name__=='__main__':
    unittest.main()  
