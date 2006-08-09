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
Display HPI events from the session queue

This is a port from the C version of hpievents over to Python.
The C version comes bundled with the OpenHPI package.

Author(s):
        Renier Morales <renierm@users.sf.net>
"""
import sys, os
from optparse import OptionParser
from openhpi import *

# Print version numbers
ohpiver = oHpiVersionGet()
ohpiver_str = os.path.basename(sys.argv[0]) + ' - OpenHPI %u.%u.%u' % (ohpiver >> 48,
	(ohpiver & 0x0000FFFF00000000) >> 32,
	(ohpiver & 0x00000000FFFF0000) >> 16)
print ohpiver_str
hpiver = saHpiVersionGet()
hpiver_str = 'SaHpi API Version is %x.0%d.0%d' % ((hpiver >> 16) + 9,
	(hpiver & 0x0000FF00) >> 8,
	 hpiver & 0x000000FF)
print hpiver_str; print ''

# Parse options
parser = OptionParser()
parser.add_option('-t',
                  '--timeout',
                  dest='timeout',
                  help='wait <seconds> for event. If BLOCK is specified, it will wait forever for an event.',
                  metavar='<seconds or BLOCK>')
parser.add_option('-d',
		  '--discover',
		  dest='discover',
		  help='call saHpiDiscover() after saHpiSubscribe()',
		  action='store_true',
		  default=False)
parser.add_option('-v',
		  '--verbose',
		  dest='verbose',
		  help='display debug messages',
		  action='store_true',
		  default=False)
options, args = parser.parse_args()

def dbg(format, vals=()):
	"""Prints message only if verbose is turned on"""
	if options.verbose:
		print format % vals

def errorout(format, error):
	"""Prints HPI error and exits"""
	if error != SA_OK:
		print format % oh_lookup_error(error)
		sys.exit(-1)

# Main()
Timeout = SAHPI_TIMEOUT_IMMEDIATE
if options.timeout:
	if options.timeout == 'BLOCK':
		Timeout = SAHPI_TIMEOUT_BLOCK
	else:
		Timeout = int(options.timeout) * 1000000000

print '*'*14, 'Timeout: [%u]' % Timeout, '*'*14
error, sid = saHpiSessionOpen(SAHPI_UNSPECIFIED_DOMAIN_ID, None)
errorout('saHpiSessionOpen: %s', error)

if (not options.discover):
	dbg('saHpiDiscover _before_ subscribing')
	error = saHpiDiscover(sid)
	errorout('saHpiDiscover: %s', error)

dbg('Subscribe to events')
error = saHpiSubscribe(sid)
errorout('saHpiSubscribe: %s', error)

if (options.discover):
	dbg('saHpiDiscover _after_ subscribing')
	error = saHpiDiscover(sid)
	errorout('saHpiDiscover after subscribe: %s', error)

dinfo = SaHpiDomainInfoT()
error = saHpiDomainInfoGet(sid, dinfo)
errorout('saHpiDomainInfoGet: %s', error)
print 'DomainInfo: UpdateCount = %u, UpdateTime = %u' % (dinfo.RptUpdateCount,
							 dinfo.RptUpdateTimestamp)

# Walk the RPT
eid = SAHPI_FIRST_ENTRY
res = SaHpiRptEntryT()
linfo = SaHpiEventLogInfoT()
error = SA_OK
while error == SA_OK and eid != SAHPI_LAST_ENTRY:
	print '*'*46
	error, nexteid = saHpiRptEntryGet(sid, eid, res)
	dbg('saHpiRptEntryGet: %s', oh_lookup_error(error))
	if error == SA_OK:
		rid = res.ResourceId
		dbg('Resource %u capabilities = %x', (rid, res.ResourceCapabilities))
		if res.ResourceCapabilities & SAHPI_CAPABILITY_EVENT_LOG:
			error = saHpiEventLogInfoGet(sid, rid, linfo)
			dbg('saHpiEventLogInfoGet: %s', oh_lookup_error(error))
			if error == SA_OK:
				oh_print_eventloginfo(linfo, 4)
		else:
			dbg('Resource doesn\'t have an event log')

		print 'rptentry[%u] tag: %s' % (rid, res.ResourceTag.Data)
		eid = nexteid
	
	print '*'*46

print 'Go and get the event...'
test_fail = 0
rdr = SaHpiRdrT()
event = SaHpiEventT()
while 1:
	rdr.RdrType = SAHPI_NO_RECORD
	error, qstatus = saHpiEventGet(sid, Timeout, event, rdr, res)
	if error != SA_OK:
		if error != SA_ERR_HPI_TIMEOUT:
			print 'ERROR during EventGet: %s' % oh_lookup_error(error)
			test_fail = 1
		else:
			if Timeout == SAHPI_TIMEOUT_BLOCK:
				print 'ERROR: Timeout while infinite wait'
				test_fail = 1
			elif Timeout != SAHPI_TIMEOUT_IMMEDIATE:
				print 'ERROR: Time, %u seconds, expired waiting for event' % options.timeout
				test_fail = 1

		break
	else:
		if rdr.RdrType == SAHPI_NO_RECORD:
			oh_print_event(event, None, 4)
		else:
			oh_print_event(event, rdr.Entity, 4)
	
if (test_fail == 0):
	print '\tTest PASSED'
else:
	print '\tTest FAILED'

dbg('Unsubscribe')
error = saHpiUnsubscribe(sid)
error = saHpiSessionClose(sid)

