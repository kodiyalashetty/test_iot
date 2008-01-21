#!/usr/bin/env python

from openhpi import *
import unittest

class TestSequence(unittest.TestCase):
    def test(self):
        ep = SaHpiEntityPathT()
        rep = SaHpiEntityPathT()
        
        self.assertEqual(oh_uid_initialize(),0)
        
        oh_init_ep(ep)
        id = oh_uid_from_entity_path(ep)
        
        self.assertEqual(oh_entity_path_lookup(id, rep), 0)
        self.assertEqual(oh_cmp_ep(ep, rep), 1)
        
if __name__=='__main__':
        unittest.main()        
        
        
