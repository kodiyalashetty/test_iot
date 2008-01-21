#!/usr/bin/env python

from openhpi import *
import unittest

class TestSequence(unittest.TestCase):
    def test(self):
        ep = SaHpiEntityPathT()
        
        
        self.assertEqual(oh_uid_initialize(),0)
        
        oh_init_ep(ep)
        id = oh_uid_from_entity_path(ep)
        rid = oh_uid_from_entity_path(ep)
        
        self.assertEqual((id != rid), 0)
        
        
if __name__=='__main__':
        unittest.main()        
        
