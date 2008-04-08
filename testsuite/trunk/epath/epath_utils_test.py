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

import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        #gchar *test_string, *expected_string;
        bigbuf=oh_big_textbuffer()
        ep=SaHpiEntityPathT()

        """
        oh_encode_entitypath - Null parameter testcase
        """
        expected_err = SA_ERR_HPI_INVALID_PARAMS

        err = oh_encode_entitypath(None, ep)
        
        self.assertEqual (err != expected_err,False)
        
        """
        oh_encode_entitypath - All blanks testcase
        """
        test_string = "       "
        expected_err = SA_ERR_HPI_INVALID_DATA

        err = oh_encode_entitypath(test_string, ep)
        self.assertEqual (err != expected_err,False)
        
        """
        oh_encode_entitypath - Begin junk testcase
        """
        test_string = "junk{SYSTEM_CHASSIS,11}{SUBBOARD_CARRIER_BLADE,9}"
        expected_err = SA_ERR_HPI_INVALID_DATA

        err = oh_encode_entitypath(test_string, ep)
        self.assertEqual (err != expected_err,False)
        
        """
        oh_encode_entitypath - Middle junk testcase
        """
        test_string = "{SYSTEM_CHASSIS,11}junk{SUBBOARD_CARRIER_BLADE,9}"
        expected_err = SA_ERR_HPI_INVALID_DATA

        err = oh_encode_entitypath(test_string, ep)
        self.assertEqual (err != expected_err,False)
        
        """
        oh_encode_entitypath - End junk testcase
        """
        test_string = "{SYSTEM_CHASSIS,11}{SUBBOARD_CARRIER_BLADE,9}junk"
        expected_err = SA_ERR_HPI_INVALID_DATA

        err = oh_encode_entitypath(test_string, ep)
        self.assertEqual (err != expected_err,False)

        """
        oh_encode_entitypath - No comma testcase
        """
        test_string = "{SYSTEM_CHASSIS.11}{SUBBOARD_CARRIER_BLADE,9}"
        expected_err = SA_ERR_HPI_INVALID_DATA

        err = oh_encode_entitypath(test_string, ep)
        self.assertEqual (err != expected_err,False)
        
        """
        oh_encode_entitypath - Bad HPI type testcase
        """
        test_string = "{SYSTEM_CHASSIS,11}{WRONG_HPI_TYPE,9}"
        expected_err = SA_ERR_HPI_INVALID_DATA

        err = oh_encode_entitypath(test_string, ep)
        self.assertEqual (err != expected_err,False)
        
        """
        oh_encode_entitypath - Bad HPI instance testcase
        """
        test_string = "{SYSTEM_CHASSIS,1abc1}{SYSTEM_SUB_CHASSIS,9}"
        expected_err = SA_ERR_HPI_INVALID_DATA

        err = oh_encode_entitypath(test_string, ep)
        self.assertEqual (err != expected_err,False)
        
        """
        oh_encode_entitypath - Extra parameters testcase
        """
        test_string = "{SYSTEM_CHASSIS,2}{SYSTEM_SUB_CHASSIS,9,2}"
        expected_err = SA_ERR_HPI_INVALID_DATA

        err = oh_encode_entitypath(test_string, ep)
        self.assertEqual (err != expected_err,False)
        
        """
        oh_encode_entitypath - Nominal testcase
        """
        test_string = "{SYSTEM_CHASSIS,1}{SUB_CHASSIS,2}"

        err = oh_encode_entitypath(test_string, ep)
        self.assertEqual (err!=None,True)
        
        oh_init_bigtext(bigbuf)
        err = oh_decode_entitypath(ep, bigbuf)
        self.assertEqual (err!=None,True)
        
        self.assertEqual (bigbuf.Data!= test_string,False)
        
        """
        oh_encode_entitypath - Blanks testcase
        """
        test_string = "  {SYSTEM_CHASSIS,  1111}  { CHASSIS_BACK_PANEL_BOARD  ,32 }  "
        expected_string = "{SYSTEM_CHASSIS,1111}{CHASSIS_BACK_PANEL_BOARD,32}"

        err = oh_encode_entitypath(test_string, ep)
        self.assertEqual (err!=None,True)
        
        oh_init_bigtext(bigbuf)
        err = oh_decode_entitypath(ep, bigbuf)
        self.assertEqual (err!=None,True)
        
        self.assertEqual (bigbuf.Data!= expected_string,False)
        
        """
        oh_decode_entitypath testcases
        """
        
        test_ep=SaHpiEntityPathT()

        oh_init_ep(test_ep)
        test_ep.Entry[0].EntityType = SAHPI_ENT_SUB_CHASSIS
        test_ep.Entry[0].EntityLocation = 109
        test_ep.Entry[1].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
        test_ep.Entry[1].EntityLocation = 112

        """
        oh_decode_entitypath  - Null testcase
        """
        expected_err = SA_ERR_HPI_INVALID_PARAMS

        
        err = oh_decode_entitypath(test_ep, None)
        self.assertEqual (err != expected_err,False)
    
        """
        * oh_decode_entitypath  - Bad instance testcase
        """
        test_ep.Entry[0].EntityLocation = 1234567
        
        expected_err = SA_ERR_HPI_INVALID_DATA

        err = oh_decode_entitypath(test_ep, bigbuf)
        self.assertEqual (err != expected_err,False)
        
        test_ep.Entry[0].EntityLocation = 109
        
        """
        oh_decode_entitypath  - Nominal testcase
        """
        expected_string = "{SYSTEM_CHASSIS,112}{SUB_CHASSIS,109}"
        
        oh_init_bigtext(bigbuf)
        oh_append_bigtext(bigbuf, test_string)
    
        err = oh_decode_entitypath(test_ep, bigbuf)
        self.assertEqual (err!=None,True)
        
        self.assertEqual (bigbuf.Data!= expected_string,False)
        
if __name__=='__main__':
    unittest.main()
