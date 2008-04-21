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
 * This test verifies failure of oh_el_append when el == None
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
         
        el = oh_el()
        retc = None
        event = SaHpiEventT()
        data = []
        data.append("Test data one")


        # test oh_el_append with el==None
        el = None
        event.Source = 1
        event.EventType = SAHPI_ET_USER
        event.Timestamp = SAHPI_TIME_UNSPECIFIED
        event.Severity = SAHPI_DEBUG
        event.EventDataUnion.UserEvent.UserEventData.Data = data[0]
        retc = oh_el_append(el, event, None, None)
        if (retc == SA_OK):
            print "ERROR: oh_el_append failed."
            return 1
        return 0

if __name__=='__main__':
        unittest.main()  
