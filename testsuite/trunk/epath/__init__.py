#!/usr/bin/env python
"""
Run all tests cases according to the test file pattern.
"""
import os, re, unittest

try:
	restore_dir = os.getcwd()
	os.chdir(__path__[0])
except NameError:
	restore_dir = None

test_pattern = re.compile('^[a-z]{1}.*\.py$')
	
# Compile list of tests to run based on file pattern
test_files = []
for t in os.listdir(os.curdir):
	if t.startswith('gen_'): continue # Skip generators
	if test_pattern.search(t):
		test_files.append(t)

# Import all test cases found and add to a test suite for running.
suite = unittest.TestSuite()
test_files.sort()
for t in test_files:
	test = __import__(t[:-3]) # remove '.py' ending for import call
	try:
	    suite.addTest(test.TestSequence())
	except:
	    print t; raise

# Run test suite
unittest.TextTestRunner().run(suite)

if restore_dir: os.chdir(restore_dir)
