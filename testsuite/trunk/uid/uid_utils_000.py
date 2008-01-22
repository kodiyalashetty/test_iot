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
    runTest : Get a new unique id. Use id to lookup original entity path.
    Passes if returned entity path is equal to original entity path,
    otherwise fails.
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        ep = SaHpiEntityPathT()
        rep = SaHpiEntityPathT()
        
        self.assertEqual(oh_uid_initialize(),0)
        
        oh_init_ep(ep)
        id = oh_uid_from_entity_path(ep)
        
        self.assertEqual(oh_entity_path_lookup(id, rep), 0)
        self.assertEqual(oh_cmp_ep(ep, rep), 1)
        
if __name__=='__main__':
        unittest.main()        
        
        
