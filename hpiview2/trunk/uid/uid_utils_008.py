#!/usr/bin/env python

from openhpi import *
import unittest

class TestSequence(unittest.TestCase):
       
    def test(self):
                
        self.assertEqual(oh_uid_initialize(),0)
        self.assertEqual(oh_uid_from_entity_path(None),0)
                      
if __name__=='__main__':
        unittest.main()   
