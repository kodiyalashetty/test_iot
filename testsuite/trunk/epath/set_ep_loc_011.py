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

#include <string.h>
#include <stdio.h>

#include <SaHpi.h>
#include <oh_utils.h>

"""oh_set_ep_location: Full entity path, victim element at end.
    Only end element's instance number changed """
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        y = 77
        z = 29
        i = 0
        
        ep =SaHpiEntityPathT()
        #SaHpiEntityTypeT
        w = SAHPI_ENT_POWER_DISTRIBUTION_UNIT
        #SaHpiEntityLocationT
        x = 87654
        
        for i in range ( 0, SAHPI_MAX_ENTITY_PATH):
            ep.Entry[i].EntityType = w
            ep.Entry[i].EntityLocation = y
            i=i+1    
        ep.Entry[SAHPI_MAX_ENTITY_PATH-1].EntityType = SAHPI_ENT_REMOTE
        ep.Entry[SAHPI_MAX_ENTITY_PATH-1].EntityLocation = z
    
        err = oh_set_ep_location(ep, SAHPI_ENT_REMOTE, x)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual  (ep.Entry[SAHPI_MAX_ENTITY_PATH-1].EntityLocation != x,False)
        
        self.assertEqual (ep.Entry[SAHPI_MAX_ENTITY_PATH-1].EntityType != SAHPI_ENT_REMOTE,False)
        
        for i in range (0, SAHPI_MAX_ENTITY_PATH-1):
            self.assertEqual ((ep.Entry[i].EntityType != w) or
            (ep.Entry[i].EntityLocation != y),False) 
            
if __name__=='__main__':
    unittest.main()
