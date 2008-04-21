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
 * This test tests creates an EL and adds five events.
 * It then verifies there are five events in the EL and 
 * that they are the same as the original events.
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
 
        el = oh_el()
        retc = None
        event = SaHpiEventT()
        curr = SAHPI_FIRST_ENTRY
        prev = next = 0
        entry = oh_el_entry()
        data = []
        data.append("Test data one")
        data.append("Test data two")
        data.append("Test data three")
        data.append("Test data four")
        data.append("Test data five")
        
        # create the EL 
        el = oh_el_create(30)

        # add 5 events to el 
        for x in range (0,5):
            event.Source = 1
            event.EventType = SAHPI_ET_USER
            event.Timestamp = SAHPI_TIME_UNSPECIFIED
            event.Severity = SAHPI_DEBUG
            event.EventDataUnion.UserEvent.UserEventData.Data = data[x]
            retc = oh_el_append(el, event, None, None)
            self.assertEqual(retc != SA_OK, False)
            x = x+1
            
            #self.assertEqual(len(el.list) != 5, False)
                  
        x =0 
        while curr != SAHPI_NO_MORE_ENTRIES:
            retc, prev, next , entry = oh_el_get(el, curr);
            self.assertEqual(retc != SA_OK, False)
            self.assertEqual(entry.event.Event.EventDataUnion.UserEvent.UserEventData.Data == data[x], False)
            curr = next
            x = x + 1

# close the el 
        retc = oh_el_close(el)
        self.assertEqual(retc != SA_OK, False)
        return 0
        
if __name__=='__main__':
        unittest.main()  
