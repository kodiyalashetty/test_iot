#!/usr/bin/env python
import sys

patterns = ['{SYSTEM_CHASSIS,1}{SBC_BLADE,3}',
	    '{SYSTEM_CHASSIS,1}{SBC_BLADE,.}',
	    '{SYSTEM_CHASSIS,1}{SBC_BLADE,.}*',
	    '{SYSTEM_CHASSIS,1}{.,.}',
	    '{SYSTEM_CHASSIS,1}{.,.}*',
	    '{SYSTEM_CHASSIS,1}*',
	    '{SYSTEM_CHASSIS,1}',
	    '{SBC_BLADE,3}',
	    '*{SBC_BLADE,3}',
	    '*{SBC_BLADE,.}',
	    '*{SBC_BLADE,.}*',
	    '*{SYSTEM_CHASSIS,1}{SBC_BLADE,.}*',
	    '*{SYSTEM_CHASSIS,.}{SBC_BLADE,.}',
	    '*{SYSTEM_CHASSIS,.}*{SBC_BLADE,.}',
	    '*{SYSTEM_CHASSIS,.}*{SBC_BLADE,.}*',
	    '{SYSTEM_CHASSIS,.}',
	    '{.,.}',
	    '*{.,.}',
	    '{.,.}*',
	    '*{.,.}*',
	    '*{.,.}*{.,.}',
	    '{.,.}*{.,.}*',
	    '{.,.}{.,.}*',
	    '*{.,.}{.,.}',
	    '*'
	   ]

entitypaths = ['{SYSTEM_CHASSIS,1}{SBC_BLADE,3}',
	       '{SYSTEM_CHASSIS,1}',
	       '{SYSTEM_CHASSIS,1}{SBC_BLADE,3}{ADD_IN_CARD,8}',
	       '{SYSTEM_CHASSIS,1}{PHYSICAL_SLOT,3}{SBC_BLADE,3}{ADD_IN_CARD,8}',
	       '{GROUP,4}{SYSTEM_CHASSIS,1}{PHYSICAL_SLOT,3}{SBC_BLADE,3}{ADD_IN_CARD,8}',
	       '{GROUP,4}{SYSTEM_CHASSIS,1}',
	       '{GROUP,4}{SYSTEM_CHASSIS,1}{SBC_BLADE,3}',
	       '{GROUP,4}{SYSTEM_CHASSIS,1}{SBC_BLADE,3}{ADD_IN_CARD,8}',
	       '{GROUP,4}{SYSTEM_CHASSIS,1}{PHYSICAL_SLOT,3}{SBC_BLADE,3}',
	       '{SBC_BLADE,3}',
	       '{SBC_BLADE,3}{ADD_IN_CARD,8}',
	       '{PHYSICAL_SLOT,4}{SBC_BLADE,3}',
	       '{PHYSICAL_SLOT,4}{SBC_BLADE,3}{ADD_IN_CARD,8}',
	       '{SYSTEM_CHASSIS,1}{PHYSICAL_SLOT,4}{SBC_BLADE,3}',
	       '{GROUP,2}',
	       '{GROUP,2}{SUBRACK,5}',
	       '{GROUP,7}{REMOTE,2}{SUBRACK,4}',
	       '{GROUP,7}{REMOTE,2}{SUBRACK,4}{BIOS,8}'
	      ]

results = [True, True, True, True, True, True, False, False, True, True, True,
           True, True, True, True, False, False, True, True, True, True, True,
           True, True, True, False, False, False, False, False, True, True,
           False, False, False, False, False, False, False, False, True, True,
           True, True, True, False, False, False, False, True, False, False,
           True, False, True, True, False, False, False, False, True, True,
           False, False, True, False, False, True, True, True, True, True,
           True, True, True, False, False, False, False, True, True, False,
           False, False, False, True, False, False, False, True, False, False,
           True, True, True, True, True, True, True, True, False, False, False,
           False, False, False, False, False, False, False, True, False, False,
           False, True, False, False, True, True, True, True, True, True, True,
           True, False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, True, True,
           True, True, True, True, True, True, False, False, False, False,
           False, False, False, False, True, True, True, True, True, True,
           True, False, False, True, True, True, True, True, True, True, True,
           False, False, False, False, False, False, False, False, False,
           False, True, True, False, False, True, False, False, True, True,
           True, True, True, True, True, True, False, False, False, False,
           False, False, False, False, True, True, True, False, False, True,
           True, False, False, True, True, True, True, True, True, True, True,
           False, False, False, False, False, False, False, True, True, True,
           True, False, False, False, False, False, True, True, True, True,
           False, False, False, False, True, False, False, False, False, False,
           False, False, False, False, False, True, False, False, False, False,
           False, False, True, True, True, True, True, True, True, True, False,
           False, False, False, False, False, False, False, True, True, True,
           False, False, False, False, False, False, True, True, True, True,
           True, True, True, True, False, False, False, False, False, False,
           False, False, False, False, True, False, False, False, False,
           False, False, True, True, True, True, True, True, True, True,
           False, False, False, False, True, True, False, False, True, True,
           True, False, False, True, True, False, False, True, True, True,
           True, True, True, True, True, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, True, True, True, True, False, False, False, False,
           True, False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, True, True,
           True, True, True, True, True, True, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, True, True, True, True, True, True,
           True, True, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False, True,
           True, True, True, True, True, True, True]

header = """
#!/usr/bin/env python
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

import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    """
     WARNING! This file is auto-magically generated by:
              %s
              Do not change this file manually. Update script instead
    """

    """
     This takes an entity path and an entity path's pattern,
     and knowing the proper result beforehand, checks if the
     pattern matches the entity path. If the proper result is
     achieved, the test passes.
    """
    def runTest(self):
        sys.argv[0]
        footer = """
        
if __name__=='__main__':
    unittest.main()
        """
        
        body = """
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):
        
    def runTest(self):
        ep_str = "%(e)s"
        epp_str = "%(p)s"
        epp=oh_entitypath_pattern()
        ep=SaHpiEntityPathT()
        error = SA_OK
        #SaHpiBoolT
        match = "%(m)s"

        error = oh_encode_entitypath(ep_str, ep)
        self.assertEqual  (error == SA_OK,True) 
        
        error = oh_compile_entitypath_pattern(epp_str, epp)
        self.assertEqual  (error == SA_OK,True) 
        
        self.assertEqual (oh_match_entitypath_pattern(epp, ep) != match,True)
        
        """
        
        m = 0
        for e in entitypaths:
            for p in patterns:
                testfile = open('epath_pattern_%03i.py' % m,'w')
                if not testfile:
                        print 'Error opening file'
                        sys.exit()
                if results[m]: match = SAHPI_TRUE
                else: match = SAHPI_FALSE
                vals = {'e': e, 'p': p, 'm': match}
                testfile.write(header+(body % vals)+footer)
                testfile.close()
                m += 1

if __name__=='__main__':
    unittest.main()
