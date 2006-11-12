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
Provides dependency information on requred versions and cflags
"""
__author__ = 'Renier Morales <renierm@users.sf.net>'

import sys, os, re

pkg_config_path = 'PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig:/opt/gnome/lib/pkgconfig'

def get_glib_cflags():
	"""Gets the cflags needed to use glib"""
	pkgcmd = os.popen(pkg_config_path +
                          ' pkg-config --cflags glib-2.0', 'r')
        pkgcmd_text = pkgcmd.read()
        pkgcmd.close()
	includes = pkgcmd_text.split()
	for x in range(len(includes)):
		includes[x] = includes[x][2:]
		
	return includes

def check_pkgcfg_ver(reqver_text, pkgname):
	"""Check for requried version using pkg-config"""
	reqver = map(int, reqver_text.split('.'))
	pkgcmd = os.popen(pkg_config_path +
                          ' pkg-config --modversion ' + pkgname, 'r')
	pkgcmd_text = pkgcmd.read()
	pkgcmd.close()
	match = re.search(r'^([0-9]+)\.([0-9]+)\.([0-9]+)', pkgcmd_text)
	if match:
		pkgver_str = match.groups()
		pkgver = map(int, pkgver_str)
		return check_ver(pkgver, reqver)
	else:
		return '<not found>'

def check_glibver(reqver_text):
	"""Check for required glib version"""
	return check_pkgcfg_ver(reqver_text, 'glib-2.0')

def check_openhpiver(reqver_text):
	"""Check for required OpenHPI version"""
	return check_pkgcfg_ver(reqver_text, 'openhpi')

def check_swigver(reqver_text):
	"""Check for required SWIG version"""
	reqver = map(int, reqver_text.split('.'))
	swigcmd = os.popen('PATH=$PATH:/usr/local/bin swig -version', 'r')
	swigcmd_text = swigcmd.read()
	swigcmd.close()
	match = re.search(r'\sSWIG\sVersion\s([0-9]+)\.([0-9]+)\.([0-9]+)',
			  swigcmd_text)
	if match:
		swigver_str = match.groups()
		swigver = map(int, swigver_str)
		return check_ver(swigver, reqver)
	else:
		return '<not found>'

def check_pythonver(reqver_text):
	"""Check for required Python version"""
	reqver = map(int, reqver_text.split('.'))
	pythonver = sys.version_info[:3]
	return check_ver(pythonver, reqver)

def check_ver(ver, reqver):
	if ver[0] < reqver[0]:
		return '.'.join(ver)
	elif ver[0] == reqver[0]:
		if ver[1] < reqver[1]:
			return '.'.join(ver)
		elif ver[1] == reqver[1]:
			if ver[2] < reqver[2]:
				return '.'.join(ver)
		
	return None

