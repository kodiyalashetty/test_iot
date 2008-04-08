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

# oh_concat_ep: NULL parameter testcase.
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):
    def runTest(self):
        test_string = ("{CHASSIS_SPECIFIC,89}{OPERATING_SYSTEM,46}")
        ep=SaHpiEntityPathT()
        err = oh_encode_entitypath(test_string, ep)
        
        self.assertEqual (err!=None,True)
        
        expected_err = SA_ERR_HPI_INVALID_PARAMS
        err = oh_concat_ep(None, ep)

        self.assertEqual (err != expected_err,False)

if __name__=='__main__':
    unittest.main()
