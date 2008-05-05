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
 * This test verifies failure of oh_el_append when el->info.Enabled == SAHPI_FALSE && event->EventType != SAHPI_ET_USER
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
        
        el = oh_el()
        retc = None
        event = SaHpiEventT()
        data = []
        data.append("Test data one")

        # test oh_el_append with el->info.Enabled == SAHPI_FALSE && event->EventType != SAHPI_ET_USER 

        el = oh_el_create(20)

        el.info.Enabled = False
        event.Source = 1
        event.EventType = SAHPI_ET_DOMAIN
        event.Timestamp = SAHPI_TIME_UNSPECIFIED
        event.Severity = SAHPI_DEBUG
        event.EventDataUnion.UserEvent.UserEventData.Data = data[0]
        retc = oh_el_append(el, event, None, None)
        self.assertEqual (retc == SA_OK,False)
            
    # close el 
        retc = oh_el_close(el)
        self.assertEqual (retc != SA_OK,False)
        
if __name__=='__main__':
        unittest.main()  
