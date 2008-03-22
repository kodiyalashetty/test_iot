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

from types import *
import unittest
import rpt_resources
from openhpi import *
from random import *
from rpt_resources import *

class TestSequence(unittest.TestCase):
       
    """
    runTest : Starts with an empty RPTable. Invokes oh_flush on it.
    Should return without crashing.
 
 Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        oh_flush_rpt(None)
            
if __name__=='__main__':
        unittest.main()    
