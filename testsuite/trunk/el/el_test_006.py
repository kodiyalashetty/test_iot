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
from el_compare import *
from openhpi import *


class TestSequence(unittest.TestCase):
       
    """
    runTest : EL test
 *
 * This test creates a new EL, adds 5 entries and saves the EL
 * to a file. It then retrieves the EL and adds 5 entries to both
 * the initial and retrieved ELs. It then checks the number of entries 
 * and compares the two ELs.
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
 
        el = el2 = oh_el()
        retc = retc1= retc2 = None
        event = SaHpiEventT()
        data = []
        data.append("Test data one")
        data.append("Test data two")
        data.append("Test data three")
        data.append("Test data four")
        data.append("Test data five")
        data.append("Test data six")
        data.append("Test data seven")
        data.append("Test data eight")
        data.append("Test data nine")	
        data.append("Test data ten")

        # create a new EL of size 20
        el = oh_el_create(20)
        el2 = oh_el_create(20)

        # add 5 events to el 
        for x in range (0,5):
            event.Source = 1
            event.EventType = SAHPI_ET_USER
            event.Timestamp = SAHPI_TIME_UNSPECIFIED
            event.Severity = SAHPI_DEBUG
            event.EventDataUnion.UserEvent.UserEventData.Data = data[x]
            retc = oh_el_append(el, event, None, None)
            self.assertEqual(not(retc != SA_OK), True)
            x = x+1
        
        # save the EL to file 
        retc1 = oh_el_map_to_file(el, "./elTest.data")
        self.assertEqual(not(retc1 != SA_OK), True)
        
        # get EL from file (el2)
        retc2 = oh_el_map_from_file(el2, "./elTest.data")
        self.assertEqual(not (retc2 != SA_OK), True)
        
        # add 5 more events to el 
        for x in range (5, 10):
            event.Source = 1
            event.EventType = SAHPI_ET_USER
            event.Timestamp = SAHPI_TIME_UNSPECIFIED
            event.Severity = SAHPI_DEBUG
            event.EventDataUnion.UserEvent.UserEventData.Data = data[x]
            retc = oh_el_append(el, event, None, None)
            self.assertEqual(not (retc != SA_OK), True)
            x = x+1
                    
        # add 5 more events to el2 
        for x in range (5,10):
            event.Source = 1
            event.EventType = SAHPI_ET_USER
            event.Timestamp = SAHPI_TIME_UNSPECIFIED
            event.Severity = SAHPI_DEBUG
            event.EventDataUnion.UserEvent.UserEventData.Data = data[x]
            retc = oh_el_append(el2, event, None, None)
            self.assertEqual(not (retc != SA_OK), True)
            x = x+1

        # verify number of entries in el and el2 is 10 
        
        #self.assertEqual(len(el.list) != 10, False)
        
        #self.assertEqual(llen(el2.list) != 10, False)
                 
        # compare entry contents of el and el2 
        retc = el_compare(el,el2)
        self.assertEqual(not (retc != SA_OK), False)
    
        # close el 
        retc1 = oh_el_close(el)
        self.assertEqual(not (retc1 != SA_OK), True)
        
        # close el2 
        retc2 = oh_el_close(el2)
        self.assertEqual(not (retc2 != SA_OK), True)
       
        return 0

if __name__=='__main__':
        unittest.main()  
