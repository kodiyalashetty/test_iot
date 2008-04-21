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
from openhpi import *

class TestSequence(unittest.TestCase):
       
    """
    runTest : EL test
    This test tests creates an EL and adds one event.
    It then verifies there is one event and compares the
    one event in the EL with the original event.
    Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):

        

if __name__=='__main__':
        unittest.main() 
