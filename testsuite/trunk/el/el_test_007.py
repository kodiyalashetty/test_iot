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
        self.assertEqual (retc != SA_OK,False)
        
        retc = oh_el_append(el, event, None, None)
        self.assertEqual (retc != SA_OK,False)
        
        # get el info 
        retc = oh_el_info(el, info)
        self.assertEqual (retc != SA_OK,False)
        
        # Verifies timestamp basetime worked 
        self.assertEqual (info.UpdateTimestamp < timestamp,False)
        
        # close el without saving to file
        retc = oh_el_close(el)
        self.assertEqual (retc != SA_OK,False)
        
if __name__=='__main__':
        unittest.main()  
