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

from openhpi import *

def el_compare(el1, el2):
       
      
        entry1 = entry2 = oh_el_entry()
        prev1= prev2 = next1 = next2 = cur1 = cur2 = None
        retc = None
 
        next1 = SAHPI_OLDEST_ENTRY
        next2 = SAHPI_OLDEST_ENTRY
        while next1 != SAHPI_NO_MORE_ENTRIES:
            cur1 = next1
            cur2 = next2
        
		# fetch the event for el1
            retc, prev1, next1, entry1 = oh_el_get(el1, cur1)
            if (retc != SA_OK):
                print "ERROR: oh_el_get failed."
                return 1
                            
     
        # fetch the event for el2
            retc, prev2, next2, entry2 = oh_el_get(el2, cur2)
            if (retc != SA_OK):
                print "ERROR: oh_el_get failed."
                return 1
            
            if (memcmp(entry1.event.Event, entry2.event.Event, sizeof_SaHpiEventT)):
                print "ERROR: Data from el1 and el2 do not match"
                return 1
                
                            
            # Compare resource from el1 and el2 
            if (memcmp(entry1.res, entry2.res, sizeof_SaHpiRptEntryT)):
                print "ERROR: Res from el1 and el2 do not match."
                return 1
                                     
     
            # Compare rdr from el1 and el2 
            if (memcmp(entry1.rdr, entry2.rdr, sizeof_SaHpiRdrT)):
                print "ERROR: Rdr from el1 and el2 do not match."
                return 1
 
