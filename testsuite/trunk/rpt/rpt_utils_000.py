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
from openhpi import *
import r

def objcmp(obj1, obj2):
	"""
	Compare two object instances and return True if they are equivalent
	"""

	# Check that the two objects are instances of a class
	if not repr(type(obj1)).startswith('<class ') or not repr(type(obj2)).startswith('<class '):
		print 'Object check failed: not a class'
		print obj1
		print obj2
		return False

	# Check that the two objects are instances of the same class
	if repr(obj1.__class__) != repr(obj2.__class__):
		print 'Class check failed "%s" != "%s"' % (repr(obj1.__class__), repr(obj2.__class_))
		return False
	
	for attr in dir(obj1): # Compare objects attribute by attribute
		# Disregard special python/swig attributes
		if attr.startswith('_') or repr(type(getattr(obj1,attr))) == "<type 'PySwigObject'>":
			continue
		
		# If the attribute is an object instance, compare them recursively 
		if repr(type(getattr(obj1, attr))).startswith('<class '):
			if not objcmp(getattr(obj1, attr), getattr(obj2, attr)):
				return False
		# If the attribute is a sequence or dictionary,
		# compare elements side by side recursively
		elif type(getattr(obj1, attr)) in [TupleType, ListType, DictType]:
			if len(getattr(obj1, attr)) != len(getattr(obj2, attr)):
				return False

			for e1, e2 in zip(getattr(obj1, attr), getattr(obj2, attr)):
				if not objcmp(e1, e2): return False
				
		# If the attribute is a native type (e.g. number or string)
		# then do normal comparison.
		else:
			if getattr(obj1, attr) != getattr(obj2, attr):
				print 'Attribute check failed obj1.%s != obj2.%s' % (attr, attr)
				return False
	
	return True

class TestSequence(unittest.TestCase):
       
    """
    runTest : Starting with an empty RPTable, adds 1 resource to it
    and tries to fetch it by the ResourceId and compare it against
    the original resource. A failed comparison means the test
    failed, otherwise the test passed.
 
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):

        rpttable = RPTable()
        
        oh_init_rpt(rpttable)
        
        self.assertEqual(oh_add_resource(rpttable, r.rptentries[0], None, 0), 0)
        
        tmpentry = oh_get_resource_by_id(rpttable, r.rptentries[0].ResourceId)
        
        self.assertEqual(tmpentry != None, True)

        self.assertEqual(objcmp(r.rptentries[0], tmpentry), True)
        
if __name__=='__main__':
        unittest.main()        
        
        
