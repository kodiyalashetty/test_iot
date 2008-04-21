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
 * This test verifies failure of oh_el_append when event == None
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
         
        el = oh_el()
        retc = None

        # test oh_el_append with event==None
        el = oh_el_create(20)
        retc = oh_el_append(el, None, None, None)
        if (retc == SA_OK):
            print "ERROR: oh_el_append failed."
            return 1
        
        #  close el 
        retc = oh_el_close(el)
        if (retc != SA_OK):
            print "ERROR: oh_el_close on el failed."
            return 1
        return 0

if __name__=='__main__':
        unittest.main()  
