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
    runTest : Calls oh_entity_path_lookup using a NULL id and entity path.
    Passes if it returns -1,
    otherwise fails.

    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        ep = SaHpiEntityPathT()
               
        oh_init_ep(ep)
        
        self.assertEqual(oh_uid_initialize(),0)
        
        self.iid = oh_uid_from_entity_path(ep)
        
        self.assertEqual(not (self.iid), False)
         
        self.assertEqual(not (oh_entity_path_lookup(0, None)), False)
              
if __name__=='__main__':
    unittest.main()  
