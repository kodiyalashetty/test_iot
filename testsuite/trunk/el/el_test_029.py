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
 * This test verifies failure of oh_el_get when entryid < myentry->event.EntryId
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
        
        el = oh_el()
        retc = None

        # set entryid < myentry->event.EntryId 
        el = oh_el_create(20)
        retc = oh_el_map_from_file(el, "./elTest.data")
        if (retc != SA_OK):
            print "ERROR: oh_el_map_from_file failed."
            return 1
        
        retc, prev, next, entry = oh_el_get(el, SAHPI_FIRST_ENTRY)
        myentry = entry.event.EntryId
	entry.event.EntryId -= 1
    
        retc, prev, next, entry = oh_el_get(el, myentry)
        if (retc == SA_OK):
            print "ERROR: oh_el_get failed."
            return 1
        
        # close el 
        retc = oh_el_close(el)
        if (retc != SA_OK):
            print "ERROR: oh_el_close on el failed."
            return 1
        return 0

if __name__=='__main__':
    unittest.main()  
