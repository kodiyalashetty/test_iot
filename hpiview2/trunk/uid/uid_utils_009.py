#!/usr/bin/env python

from openhpi import *
import unittest

class TestSequence(unittest.TestCase):
    
    def test(self):
        ep = SaHpiEntityPathT()
        
        oh_init_ep(ep)
        
        self.assertEqual(oh_uid_initialize(),0)
        
        self.assertEqual(not (oh_uid_from_entity_path(ep)), False)
         
        self.assertEqual(not (oh_uid_remove(0)), False)
              
if __name__=='__main__':
    unittest.main()   
