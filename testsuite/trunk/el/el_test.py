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

from openhpi import *
#from el_compare import *
import sys

#add_event(el, idx)
def el_compare(el1, el2):
    el_compare(el1,el2)

#define OH_ELTEST_MAX_ENTRIES 5

"""
/*      -*- linux-c -*-
 *
 * (C) Copyright IBM Corp. 2003, 2004, 2006
 * Copyright (c) 2003 by Intel Corp.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 * file and program are licensed under a BSD style license.  See
 * the Copying file included with the OpenHPI distribution for
 * full licensing terms.
 *
 * Authors:
 *      David Ashley <dashley@us.ibm.com>
 *      Renier Morales <renierm@users.sf.net>
 */
"""

# note: if OH_ELTEST_MAX_ENTRIES changes we may need additional members here 
#data[0] = ["Test data one","Test data two", "Test data three","Test data four","Test data five","Test data six","Test data seven","Test data eight","Test data nine","Test data ten"]

# add an SaHpiUserEventT event to the EL
# Note that the event data we use is just a string from the above array
def add_event(el, idx):

    data[0] = ["Test data one","Test data two", "Test data three","Test data four","Test data five","Test data six","Test data seven","Test data eight","Test data nine","Test data ten"]
    entry = fetchentry = oh_el_entry()
    event = SaHpiEventT()
    retc = SaErrorT()
    oldId = el.nextid
    next = prev = None

    if ((idx >= sizeof_data) / sizeof_char ):
        print "ERROR: idx invalid."
        return 1
            
    # add a single event 
    event.Source = 1
    event.EventType = SAHPI_ET_USER
    event.Timestamp = SAHPI_TIME_UNSPECIFIED
    event.Severity = SAHPI_DEBUG
    event.EventDataUnion.UserEvent.UserEventData.Data = data[idx]
    retc = oh_el_append(el, event, None, None)

    if (retc != SA_OK):
        print "ERROR: oh_el_add failed."
        return 1
        
    entry = el.list[len(el.list)]
    # check correct id 
    if (entry.event.EntryId != el.nextid - 1):
        print "ERROR: entry.EntryId invalid."
        return 1
    
    if (entry.event.Timestamp == 0):
        print "ERROR: entry.Timestamp invalid."
        return 1
        
    # inspect oh_el struct values 
        if(el.info.Enabled != TRUE):
            print "ERROR: el->info.Enabled invalid."
            return 1
       
        if(el.info.UpdateTimestamp != entry.event.Timestamp):
            print "ERROR: el->info.UpdateTimestamp invalid."
            return 1
        
        if(el.basetime != 0):
            print "ERROR: el->basetime invalid."
            return 1
        
        if(el.nextid != oldId + 1):
            print "ERROR: el->nextid invalid."
            return 1
        
        if(el.list == None):
            print "ERROR: el->list == None."
            return 1
        
        # now fetch the event and compare it 
        retc = oh_el_get(el, entry.event.EntryId, prev, next, fetchentry)
        if (retc != SA_OK):
            print "ERROR: oh_el_get failed."
            return 1
        
        if (entry.event.EntryId != fetchentry.event.EntryId):
            print "ERROR: entry->EntryId invalid."
            return 1
        
        if (prev != entry.event.EntryId - 1):
            if (prev != SAHPI_NO_MORE_ENTRIES):
                print "ERROR: prev invalid."
                return 1
                
        if (next != entry.event.EntryId + 1):
            if (next != SAHPI_NO_MORE_ENTRIES):
                print "ERROR: next invalid."
                return 1
            
        if (fetchentry.event.Timestamp == 0):
            print "ERROR: fetchentry->Timestamp invalid."
            return 1

        if (fetchentry.event.Event.Source != 1):
            print "ERROR: fetchentry->Event.Source invalid."
            return 1
        
        if (fetchentry.event.Event.EventType != SAHPI_ET_USER):
            print "ERROR: fetchentry->Event.EventType invalid."
            return 1
        
        if (fetchentry.event.Event.Timestamp != SAHPI_TIME_UNSPECIFIED):
            print "ERROR: fetchentry->Event.Timestamp invalid."
            return 1
        
        if (fetchentry.event.Event.Severity != SAHPI_DEBUG):
            print "ERROR: fetchentry->Event.Severity invalid."
            return 1
        
        if (fetchentry.event.Event.EventDataUnion.UserEvent.UserEventData.Data == data[idx]):
            print "ERROR: fetchentry->Event.EventDataUnion.UserEvent.UserEventData invalid."
            return 1
        return 0

# this struct encapsulates all the data for a system event log the log records themselves are stored in the el GList 
class oh_el ():
    basetime = None  # Time clock reference for this event log
    sysbasetime = None #The system time when the basetime was set
    nextid = None # id for next log entry
    gentimestamp = None # generate timestamp for entries.
    info = SaHpiEventLogInfoT ()  # Contains enabled state, overflow flag,timestamp of last update,and the max size for this log.
    list = []  # list of event log entries for prev and next lookups
        

# this structure encapsulates the actual log entry and its context 
class oh_el_entry ():
    event = SaHpiEventLogEntryT()
    rdr = SaHpiRdrT() # All 0's means no associated rdr
    res = SaHpiRptEntryT() # All 0's means no associated rpt

# allocate and initialize an EL 
def oh_el_create(size):

        el = oh_el()

        if (el != None):
            el.basetime = 0
            el.sysbasetime = 0
            el.nextid = SAHPI_OLDEST_ENTRY + 1
            el.gentimestamp = SAHPI_TRUE
            el.info.Entries = 0
            el.info.Size = size
            el.info.UserEventMaxSize = SAHPI_MAX_TEXT_BUFFER_LENGTH
            el.info.UpdateTimestamp = SAHPI_TIME_UNSPECIFIED
            el.info.CurrentTime = SAHPI_TIME_UNSPECIFIED
            el.info.Enabled = SAHPI_TRUE
            el.info.OverflowFlag = SAHPI_FALSE
            el.info.OverflowResetable = SAHPI_TRUE
            el.info.OverflowAction = SAHPI_EL_OVERFLOW_OVERWRITE
    
        el.list = None
        return el

# close and free all memory associated with an EL 
def oh_el_close(el):
    if (el == None) : 
        return SA_ERR_HPI_INVALID_PARAMS
    oh_el_clear(el)
    el = None
    return SA_OK

# append a new entry to the EL 
def oh_el_append(el,event,rdr,res):
    entry = oh_el_entry()
    tv =_timeval()
    cursystime = SaHpiTimeT()
    # check for valid el params and state
    if (el == None or event == None):
        return SA_ERR_HPI_INVALID_PARAMS
    else :
        if(el.info.Enabled == False and event.EventType != SAHPI_ET_USER):
            return SA_ERR_HPI_INVALID_REQUEST
    # alloc the new entry 
        entry = oh_el_entry()
        if (entry == None):
            el.info.OverflowFlag = True
            return SA_ERR_HPI_OUT_OF_SPACE
        
        if (rdr):
            entry.rdr = rdr
        if (res):
            entry.res = res

        # if necessary, wrap the el entries 
        if (el.info.Size != OH_EL_MAX_SIZE and  len(el.list) == el.info.Size):
            el.list = None
            el.list = g_list_delete_link(el.list, el.list)
            el.info.OverflowFlag = SAHPI_TRUE
        
        # Set the event log entry id and timestamp 
        entry.event.EntryId = el.nextid + 1
        if (el.gentimestamp):
        	gettimeofday(tv, None)
            #cursystime = (tv.tv_sec * 1000000000 + tv.tv_usec * 1000)
            #el.info.UpdateTimestamp = el.basetime + (cursystime - el.sysbasetime)
        else:
            el.info.UpdateTimestamp = event.Timestamp
        
        # Setting time based on the event to have some sense of what the current time is going to be when providing the el info.
        oh_el_timeset(el, event.Timestamp)
        entry.event.Timestamp = el.info.UpdateTimestamp

        # append the new entry 
        entry.event.Event = event
        el.list.append(entry)
        return SA_OK
    
    #prepend a new entry to the EL 
    def oh_el_prepend(el,event,rdr,res):
        node = []
        entry = oh_el_entry()
        tv = timeval()
        cursystime = SaHpiTimeT()

        # check for valid el params and state 
        if (el == None or event == None):
            return SA_ERR_HPI_INVALID_PARAMS
        else:
            if (el.info.Enabled == False and event.EventType != SAHPI_ET_USER):
                return SA_ERR_HPI_INVALID_REQUEST
        
        # see if el is full 
        if (el.info.Size != OH_EL_MAX_SIZE and  g_list_length(el.list) == el.info.Size):
            return SA_ERR_HPI_OUT_OF_SPACE
        
        # alloc the new entry 
        entry = oh_el_entry()
        if (entry == None):
            el.info.OverflowFlag = True
        return SA_ERR_HPI_OUT_OF_SPACE
        
        if (rdr):
            entry.rdr = rdr
        if (res):
            entry.res = res

        #Since we are adding entries in reverse order we have to renumber existing entries
        node = el.list 
        while node:
            tmpentry = node.data
            tmpentry.event.EntryId = tmpentry.event.EntryId + 1
            node = node.next
        el.nextid = el.nextid+1

        # prepare & prepend the new entry 
        entry.event.EntryId = SAHPI_OLDEST_ENTRY + 1
        if (el.gentimestamp):
            gettimeofday(tv, None)
            #cursystime = (SaHpiTimeT) tv.tv_sec * 1000000000 + tv.tv_usec * 1000
            #el.info.UpdateTimestamp = el.basetime + (cursystime - el.sysbasetime)
        else:
            el.info.UpdateTimestamp = event.Timestamp
    
        # Setting time based on the event to have some sense of what the current time is going to be when providing the el info.
        oh_el_timeset(el, event.Timestamp)
        entry.event.Timestamp = el.info.UpdateTimestamp

        # prepend the new entry to the list 
        entry.event.Event = event
        el.list = g_list_prepend(el.list, entry)
        return SA_OK

        # clear all EL entries 
    def oh_el_clear(el):
        GList *node
        if (el == None):
            return SA_ERR_HPI_INVALID_PARAMS
    
    # free the data for every element in the list 
    node = el.list
    while node:
        g_free(node.data)
        node = node.next
    
    # free the list nodes
        g_list_free(el.list)
        
    # reset the control structure 
        el.info.OverflowFlag = SAHPI_FALSE
        el.info.UpdateTimestamp = SAHPI_TIME_UNSPECIFIED
        el.info.Entries = 0
        el.nextid = SAHPI_OLDEST_ENTRY + 1 # always start at 1
        el.list = None
        return SA_OK

    # get an EL entry 
def  oh_el_get(el,entryid,prev,next,entry):
    eid = SaHpiEventLogEntryIdT()
    node = []
    elentry = oh_el_entry()

    if (not el or not prev or not next or not entry or entryid == SAHPI_NO_MORE_ENTRIES):
        return SA_ERR_HPI_INVALID_PARAMS
    
    if (g_list_length(el.list) == 0):
        return SA_ERR_HPI_NOT_PRESENT

    # FIXME: There is a bug here because this does not take into account the case when oh_el_prepend would have been used. In such case the
    #OLDEST entry would technically not be the first one in the list.
    #To be continued...
    #-- Renier Morales (08/30/06)

    if (entryid == SAHPI_OLDEST_ENTRY):
        node = g_list_first(el.list)
    else :
        if (entryid == SAHPI_NEWEST_ENTRY):
		node = g_list_last(el.list)
	if (node):
		elentry = node.data
		eid = elentry.event.EntryId
	else:
		eid = entryid
	
    node = el.list
    while node:    
        elentry = node.data
        if (eid == elentry.event.EntryId):
            entry = elentry
            if (node.prev):
                elentry = node.prev.data
                prev = elentry.event.EntryId
            else :
				prev = SAHPI_NO_MORE_ENTRIES
            if (node.next):
                elentry = node.next.data
                next = elentry.event.EntryId
            else :
				next = SAHPI_NO_MORE_ENTRIES
            return SA_OK
            node = node.next
	return SA_ERR_HPI_NOT_PRESENT

# get EL info 
def oh_el_info(el, info):
    tv = timeval()
    cursystime = SaHpiTimeT()

    if (el == None or info == None):
        return SA_ERR_HPI_INVALID_PARAMS
        info = el.info
        info.Entries = g_list_length(el.list)
        gettimeofday(tv, None)
        #cursystime = (SaHpiTimeT) tv.tv_sec * 1000000000 + tv.tv_usec * 1000
        #info.CurrentTime = el.basetime + (cursystime - el.sysbasetime)
        return SA_OK

# reset EL overflowflag 
def oh_el_overflowreset(el):
    if (el == None):
        return SA_ERR_HPI_INVALID_PARAMS
	if (el.info.OverflowResetable):
        	el.info.OverflowFlag = SAHPI_FALSE
		return SA_OK
	else:
		return SA_ERR_HPI_INVALID_CMD
	
def oh_el_overflowset(el, flag):
	if (not el) :
            return SA_ERR_HPI_INVALID_PARAMS
	el.info.OverflowFlag = flag
	return SA_OK

# write a EL entry list to a file 
def oh_el_map_to_file(el,filename):
    file = None
    node = []
    if (el == None or filename == None):
        return SA_ERR_HPI_INVALID_PARAMS
        file = open(filename, O_WRONLY | O_CREAT | O_TRUNC, 0660 )
        if (file < 0):
            print "EL file '%s' could not be opened" + filename
            return SA_ERR_HPI_ERROR
                   
	node = el.list
    while node:
        if (write(file, node.data, sizeof_oh_el_entry) != sizeof_oh_el_entry):
			print "Couldn't write to file '%s'." + filename
			close(file)
        return SA_ERR_HPI_ERROR
        if (close(file) != 0):
            print "Couldn't close file '%s'." + filename
            return SA_ERR_HPI_ERROR
        return SA_OK
        node = node.next

# read a EL entry list from a file
def oh_el_map_from_file(el, filename):
    entry = oh_el_entry()

    # check el params and state */
    if (el == None or filename == None):
        return SA_ERR_HPI_INVALID_PARAMS
    else :
        if (el.info.Enabled == False):
            return SA_ERR_HPI_INVALID_REQUEST
            file = open(filename, O_RDONLY)
        if (file < 0):
            print "EL file '%s' could not be opened" + filename
            return SA_ERR_HPI_ERROR
        oh_el_clear(el) # ensure list is empty
        while (read(file, entry, sizeof_oh_el_entry) == sizeof_oh_el_entry):
            elentry = oh_el_entry()
            el.nextid = entry.event.EntryId
            el.nextid = el.nextid + 1
            elentry = entry
            el.list = g_list_append(el.list, elentry)

        if (close(file) != 0):
            print "Couldn't close file '%s'." + filename
            return SA_ERR_HPI_ERROR
        
        return SA_OK

# set the EL timestamp offset 
    def oh_el_timeset(el, timestamp):
        tv = timeval()
        if (el == None or timestamp == SAHPI_TIME_UNSPECIFIED):
            return SA_ERR_HPI_INVALID_PARAMS
        
        gettimeofday(tv, None)
        el.sysbasetime = tv.tv_sec * 1000000000 + tv.tv_usec * 1000
        el.basetime = timestamp
        return SA_OK

# set the timestamp generate flag 
    def oh_el_setgentimestampflag(el, flag):
        if (el == None):
            return SA_ERR_HPI_INVALID_PARAMS
            el.gentimestamp = flag
            return SA_OK

    def oh_el_enableset(el, flag):
        if (not el):
            return SA_ERR_HPI_INVALID_PARAMS
            el.info.Enabled = flag
            return SA_OK

