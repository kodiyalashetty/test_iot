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
 * This test modifies the timestamp basetime. 
 * It then adds a new entry and examines the 
 * timestamp to verify accuracy.
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
 
        el = oh_el()
        retc = None
        info = SaHpiEventLogInfoT()
        event = SaHpiEventT()
        timestamp = 1000000000L
        data = []
        data.append("Test data")

        # create a new EL of size 20
        el = oh_el_create(20)

        # add an event to el 
        event.Source = 1;
        event.EventType = SAHPI_ET_USER
        event.Timestamp = SAHPI_TIME_UNSPECIFIED
        event.Severity = SAHPI_DEBUG
        event.EventDataUnion.UserEvent.UserEventData.Data = data[0]

        # modifies the timestamp basetime 
        retc = oh_el_timeset(el, timestamp)
        if (retc != SA_OK):
            print "ERROR: timeset failed"
            return 1
        
        retc = oh_el_append(el, event, None, None)
        if (retc != SA_OK):
            print "ERROR: oh_el_append failed."
            return 1
               
        # get el info 
        retc = oh_el_info(el, info)
        if (retc != SA_OK):
            print "ERROR: oh_el_info failed."
            return 1
        
        # Verifies timestamp basetime worked 
        if (info.UpdateTimestamp < timestamp):
            print "ERROR: Timestamp basetime failed"
            return 1

        # close el without saving to file
        retc = oh_el_close(el)
        if (retc != SA_OK):
            print "ERROR: oh_el_close on el failed."
            return 1
        return 0

if __name__=='__main__':
        unittest.main()  
