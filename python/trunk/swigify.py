#!/usr/bin/env python
#
# (C) Copyright IBM Corp. 2006
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. This
# file and program are licensed under a BSD style license. See
# the Copying file included with the OpenHPI distribution for
# full licensing terms.
#
"""
Filter a given header file into a clean swig interface file

This script takes the name of a header file as argument, and
produces a clean interface file ready to be parsed by SWIG. The
output file will be sent to standard output.

This script does two things to clean a header file into a
SWIG-ready interface file:
1. Eliminate the gcc __attribute__* directives. These confuse
   SWIG (at version 1.3.29).
2. Convert typecasted #define-s to const globals. Typecasted
   #define-s get dropped by SWIG (at version 1.3.29).
3. Remove #warning lines (not implemented).
4. Convert macro 'functions' into function prototypes
   (not implemented).
5. Strip out unnecessary global struct arrays (not implemented).

You won't need to call this script often at all. Only if the
header file for which you are creating a swig interface changes,
then this script will help you to quickly create a new swig
interface file for it.
"""
__author__ = 'Renier Morales <renierm@users.sf.net>'

import sys, re

header_file = open(sys.argv[1], 'r')
header_content = header_file.read()
header_file.close()

header_content = re.sub(r' __attribute__\(.+\)([^()])', r'\1',header_content)
header_content = re.sub(r'#define ([A-Z0-9_]+)[ \t\\\n]+\((\w+)\)[ ]*([-A-Za-z0-9_() +]+)', r'const \2 \1 = \3;', header_content)
print header_content

