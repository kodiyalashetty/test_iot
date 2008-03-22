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
from rpt_resources import rptentries
from rpt_resources import sensors


class TestSequence(unittest.TestCase):
       
    """
    runTest : Invoke oh_init_rpt with a NULL param.
    If it returns error, the test passes, otherwise it failed.
 
 Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        self.assertEqual(not (oh_init_rpt(None)), 0)
        
                    
if __name__=='__main__':
        unittest.main()    
