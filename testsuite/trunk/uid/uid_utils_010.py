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

#!/usr/bin/env python

from openhpi import *
import unittest

class TestSequence(unittest.TestCase):
    """
    runTest : Calls oh_uid_lookup using a NULL entity path.
    Passes if it returns 0,
    otherwise fails.

    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        ep = SaHpiEntityPathT()
        
        oh_init_ep(ep)
        
        self.assertEqual(oh_uid_initialize(),0)
        
        self.assertEqual(not (oh_uid_from_entity_path(ep)), False)
         
        self.assertEqual(oh_uid_lookup(None),0)
              
if __name__=='__main__':
    unittest.main()  
