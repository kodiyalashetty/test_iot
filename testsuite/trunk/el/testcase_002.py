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
        data = ["Test data one"]
        
        # create the EL 
        el = oh_el_create(5)
        if(el == None):
            print "ERROR: el pointer == None."
        
        # add a single event
        event.Source = 1
        event.EventType = SAHPI_ET_USER
        event.Timestamp = SAHPI_TIME_UNSPECIFIED
        event.Severity = SAHPI_DEBUG
        event.EventDataUnion.UserEvent.UserEventData.Data = data[0]

        retc = oh_el_append(el, event, None, None)
        if (retc != SA_OK): 
            print "ERROR: oh_el_append failed."
                     
        #entry = (oh_el_entry *)(g_list_first(el->list)->data)
        entry = el.list[0]
        entry = (oh_el_entry())

        if(len(el.list) != 1):
            print "ERROR: g_list_length does not return the correct number of entries."

        # fetch the event for el
        retc = oh_el_get(el, entry.event.EntryId, prev, next, entry)
        if (retc != SA_OK):
            print "ERROR: oh_el_get failed."
                
        if (event.Event.EventDataUnion.UserEvent.UserEventData.Data == data[0]):
            print "ERROR: Data from el and what was entered into el do not match"
                       
        # close the EL 
        retc = oh_el_close(el)
        if (retc != SA_OK):
            print "ERROR: oh_el_close failed."
                            
if __name__=='__main__':
        unittest.main()  
