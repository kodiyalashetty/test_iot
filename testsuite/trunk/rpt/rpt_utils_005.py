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
from random import randrange
from openhpi import *
from rpt_resources import rptentries

class TestSequence(unittest.TestCase):
    """
    runTest : Starts with an RPTable of 10 resources with data and fetches
    them randomly by the Resource Id and compares the data against
    the original data. A failed comparison means the test failed,
    otherwise the test passed.
        
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):

        rptable = RPTable()
        oh_init_rpt(rptable)
        resources = []

        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rpte, rpte, 0), 0)
            resources.append(rpte)

        while len(resources) > 0:
            k = randrange(0, len(resources))
            tmpdata = oh_get_resource_data(rptable, resources[k].ResourceId)

            self.assertEqual(not tmpdata, 0)
            self.assertEqual(memcmp(tmpdata, resources[k], sizeof_SaHpiRptEntryT), 0)
            resources.pop(k)

if __name__=='__main__':
    unittest.main()

