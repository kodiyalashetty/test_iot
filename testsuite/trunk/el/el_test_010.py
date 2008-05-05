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
 * This test verifies oh_el_prepend by reading an
 * existing EL from a file, then prepending 5 events to the EL.
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
 
        el = oh_el()
        retc = None
        event = SaHpiEventT()
        data = []
        data.append("Test data one")
        data.append("Test data two")
        data.append("Test data three")
        data.append("Test data four")
        data.append("Test data five")
    
        # test oh_el_prepend with existing EL
        el = oh_el_create(20)

        # get EL from file (el) 
        retc = oh_el_map_from_file(el, "./elTest.data")
        self.assertEqual (retc != SA_OK,False)
        
        # add 5 more events to el 
        for x in range (0,5):
            event.Source = 1
            event.EventType = SAHPI_ET_USER
            event.Timestamp = SAHPI_TIME_UNSPECIFIED
            event.Severity = SAHPI_DEBUG
            event.EventDataUnion.UserEvent.UserEventData.Data = data[x]
            retc = oh_el_prepend(el, event, None, None)
            self.assertEqual (retc != SA_OK,False)
            
            x = x+1        

        # close el 
        retc = oh_el_close(el)
        self.assertEqual (retc != SA_OK,False)
        
if __name__=='__main__':
        unittest.main()  
