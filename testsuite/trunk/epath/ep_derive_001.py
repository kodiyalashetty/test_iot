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
"""
  Tests string derive function - success case
  - multiple substitutions
  - expanded returned oid string
  
  Return value: 0 on success, 1 on failure
 """
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):
    def runTest(self):
        """
        oh_derive_string testcases
        """
        #gchar *oid, *in_oid, *expected_oid
        
        ep = SaHpiEntityPathT()
        ep.Entry[0].EntityType= SAHPI_ENT_SYS_MGMNT_MODULE
        ep.Entry[0].EntityLocation = 100
        ep.Entry[0].EntityType= SAHPI_ENT_SUB_CHASSIS
        ep.Entry[0].EntityLocation = 99
        
        # Multiple character/digit expansion testcase 
        in_oid = "1.x.3.x"
        expected_oid = "1.99.3.100"

        oid = oh_derive_string(ep, 0, 10, in_oid)
        self.assertEqual (expected_oid!= oid,True) 
        oid=None
        #g_free(oid)

        # location offset testcase 
        in_oid = "1.x.3.x"
        expected_oid = "1.109.3.110"

        oid = oh_derive_string(ep, 10, 10, in_oid)
        self.assertEqual (expected_oid!= oid,True)
        oid=None
        #g_free(oid)

        # base and offset testcase
        in_oid = "1.x.3.x"
        expected_oid = "1.6D.3.6E"

        oid = oh_derive_string(ep, 10, 16, in_oid)
        self.assertEqual (expected_oid!= oid,True)
        oid=None
        #g_free(oid)

        # No expansion testcase 
        in_oid = "1.99.3.100"
        expected_oid = "1.99.3.100"

        oid = oh_derive_string(ep, 0, 10, in_oid)
        self.assertEqual (expected_oid, oid,True)
        oid=None
        #g_free(oid)

        # Event testcase 
        
        ep2 = SaHpiEntityPathT()
        ep2.Entry[0].EntityType = SAHPI_ENT_SYS_MGMNT_MODULE
        ep2.Entry[0].EntityLocation =11
        ep2.Entry[0].EntityType = SAHPI_ENT_SUB_CHASSIS
        ep2.Entry[0].EntityLocation = 14
        
        in_oid = "1.x.3.x"
        expected_oid = "1.E.3.B"

        oid = oh_derive_string(ep2, 0, 16, in_oid)
        self.assertEqual (expected_oid!= oid,True)
        oid=None
        #g_free(oid)
    
if __name__=='__main__':
    unittest.main()
