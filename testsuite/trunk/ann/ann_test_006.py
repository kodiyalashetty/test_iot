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
 * main: Announcement test
 *
 * This test adds one announcement to the list
 *
 * Return value: 0 on success, 1 on failure
"""

def runTest(self):
        ann=oh_announcement()
        announ=SaHpiAnnouncementT()
        rc=SaErrorT()

        announ.EntryId = 0         # modified by oh_announcement_append
        announ.Timestamp = 0       # modified by oh_announcement_append
        announ.AddedByUser = False   # modified by oh_announcement_append
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

        announ.Severity = SAHPI_MAJOR
        rc = oh_announcement_append(ann, announ)

        announ.Severity = SAHPI_MINOR
        rc = oh_announcement_append(ann, announ)

        rc = oh_announcement_ack(ann, 2, SAHPI_MAJOR)
        if(rc != SA_OK):
            print "ERROR: on_announcement_ack returned " +rc
            return 1
        
        rc = oh_announcement_get(ann, 2, announ)
        if(rc != SA_OK):
            print "ERROR: on_announcement_get returned " +rc
            return 1
        
        if(announ.Acknowledged != TRUE):
            print "ERROR: announ.Acknowledged invalid" +rc
            return 1
        
if __name__=='__main__':
    unittest.main()

