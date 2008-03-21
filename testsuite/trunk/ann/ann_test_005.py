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
    Suntrupth S Yadav <suntrupth@in.ibm.com>
"""

import unittest
from openhpi import *


"""
  main: Announcement test
 
  This test adds one announcement to the list
 
  Return value: 0 on success, 1 on failure
"""

def runTest(self):
        ann=oh_announcement()
        announ=SaHpiAnnouncementT()
        rc=SaErrorT()

        announ.EntryId = 0         # modified by oh_announcement_append
        announ.Timestamp = 0       # modified by oh_announcement_append
        announ.AddedByUser = False      # modified by oh_announcement_append
        announ.Severity = SAHPI_CRITICAL
        announ.Acknowledged = False
        announ.StatusCond.Type= SAHPI_STATUS_COND_TYPE_SENSOR
        announ.StatusCond.Entity.Entry[0].EntityType = SAHPI_ENT_SYSTEM_BOARD
        announ.StatusCond.Entity.Entry[0].EntityLocation = 1
        announ.StatusCond.Entity.Entry[1].EntityType = SAHPI_ENT_ROOT
        announ.StatusCond.Entity.Entry[1].EntityLocation = 0
        announ.StatusCond.DomainId = 1
        announ.StatusCond.ResourceId = 1
        announ.StatusCond.SensorNum = 1
        announ.StatusCond.EventState = SAHPI_ES_UNSPECIFIED
        announ.StatusCond.Name.Length = 5
        memcpy(announ.StatusCond.Name.Value,"announ", 5)
        announ.StatusCond.Mid = 123
        # we will not worry about the Data field for this test 

        ann = oh_announcement_create()

        rc = oh_announcement_append(ann, announ)
        if (rc != SA_OK):
            print "ERROR: 1 oh_announcement_append failed."
            return 1

        announ.Severity = SAHPI_MAJOR
        rc = oh_announcement_append(ann, announ)
        if (rc != SA_OK): 
            print "ERROR: 2 oh_announcement_append failed."
            return 1
        
        announ.Severity = SAHPI_MINOR
        rc = oh_announcement_append(ann, announ)
        if (rc != SA_OK):
            print "ERROR: 3 oh_announcement_append failed."
            return 1
        
        announ.Severity = SAHPI_CRITICAL
        rc = oh_announcement_append(ann, announ)
        if (rc != SA_OK):
            print "ERROR: 4 oh_announcement_append failed."
            return 1
        
        announ.EntryId = SAHPI_FIRST_ENTRY
        announ.Timestamp = 0
        rc = oh_announcement_get_next(ann, SAHPI_ALL_SEVERITIES, FALSE, announ)
        if(rc != SA_OK):
            print "ERROR: on_announcement_get_next returned " + rc
            return 1
            print "EntryId" + announ.EntryId + "returned with Severity" + announ.Severity

        rc = oh_announcement_get_next(ann, SAHPI_ALL_SEVERITIES, FALSE, announ)
        if(rc != SA_OK) :
            print "ERROR: on_announcement_get_next returned ", rc
            return 1
            print "EntryId " + announ.EntryId +  "returned with Severity" + announ.Severity

        rc = oh_announcement_get(ann, 1, announ)
        if (rc != SA_OK):
            print "ERROR: oh_announcement_get did not find anything."
            return 1
        
        rc = oh_announcement_get_next(ann, SAHPI_CRITICAL, FALSE, announ)
        if(rc != SA_OK or announ.Severity != SAHPI_CRITICAL):
            print " ERROR: on_announcement_get_next returned :" + rc + "Severity returned is :" + announ.Severity + "EntryId :" +announ.EntryId
            return 1
        print "EntryId" + announ.EntryId + "returned." 

if __name__=='__main__':
    unittest.main()

