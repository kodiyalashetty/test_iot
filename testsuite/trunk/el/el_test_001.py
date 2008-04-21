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
 * This test tests the creation of an EL.
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
    
        el = oh_el()

        el = oh_el_create(5)

        self.assertEqual(el == None, False)
                   
        self.assertEqual(el.info.Enabled != True, False)
                   
        self.assertEqual(el.info.OverflowFlag != False, False)
                           
        self.assertEqual(el.info.UpdateTimestamp != SAHPI_TIME_UNSPECIFIED, False)
                   
        self.assertEqual(el.basetime != 0,False)
        
        self.assertEqual(el.nextid != SAHPI_OLDEST_ENTRY + 1, False)
                
        self.assertEqual(el.info.Size != 5, False)
            
        self.assertEqual(el.list != None, False)
            
if __name__=='__main__':
        unittest.main()  
