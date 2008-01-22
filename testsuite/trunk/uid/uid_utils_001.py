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
    runTest : Get a new unique id. Get another one with the same entity path.
    Passes if returned id is equal to previous one,
    otherwise fails.

    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        ep = SaHpiEntityPathT()
        
        
        self.assertEqual(oh_uid_initialize(),0)
        
        oh_init_ep(ep)
        id = oh_uid_from_entity_path(ep)
        rid = oh_uid_from_entity_path(ep)
        
        self.assertEqual((id != rid), 0)
        
        
if __name__=='__main__':
        unittest.main()        
        
