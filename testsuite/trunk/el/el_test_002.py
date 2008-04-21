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
    This test tests creates an EL and adds one event.
    It then verifies there is one event and compares the
    one event in the EL with the original event.
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        el = oh_el()
        retc = None
        event = SaHpiEventT()
        entry = oh_el_entry()
        prev = next = None
        data = []
        data.append("Test data one")

        # create the EL 
        el = oh_el_create(5)
        self.assertEqual(el == None, False)
        
        # add a single event 
        event.Source = 1
        event.EventType = SAHPI_ET_USER
        event.Timestamp = SAHPI_TIME_UNSPECIFIED
        event.Severity = SAHPI_DEBUG
        event.EventDataUnion.UserEvent.UserEventData.Data = data[0]

        retc = oh_el_append(el, event, None, None)
        self.assertEqual(retc != SA_OK, False)
                
        # fetch the event for el
        #retc, prev, next, entry = oh_el_get(el, entry.event.EntryId)
        self.assertEqual(retc != SA_OK, False)
          
        if (entry.event.Event.EventDataUnion.UserEvent.UserEventData.Data == data[0]):
            print "ERROR: Data from el and what was entered into el do not match"
                 
        # close the EL 
        retc = oh_el_close(el)
        self.assertEqual(retc != SA_OK, False)
        return 0
                                        
if __name__=='__main__':
        unittest.main()  
