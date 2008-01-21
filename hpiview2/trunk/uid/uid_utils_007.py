#!/usr/bin/env python

from openhpi import *
import unittest

class TestSequence(unittest.TestCase):
    iid = [0,1,2,3,4,5,6,7,8,9,10]
    
    def test(self):
        ep = SaHpiEntityPathT()
        self.assertEqual(oh_uid_initialize(),0)
        
        oh_init_ep(ep)
        
        for i in range (0, 10):
            ep.Entry[0].EntityLocation = i
            self.iid[i] = oh_uid_from_entity_path(ep)
            
        for i in range (0, 10):
            ep.Entry[0].EntityLocation = i
            ep.Entry[1].EntityType = 0
            rid = oh_uid_lookup(ep)
            self.assertEqual((rid != self.iid[i]), 0)
        
              
if __name__=='__main__':
    unittest.main()   
