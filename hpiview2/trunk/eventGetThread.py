#!/usr/bin/env python

from threading import *
from openhpi import *
import thread

class EventGetThread(Thread):

    eid = SAHPI_FIRST_ENTRY
    res = SaHpiRptEntryT()
    linfo = SaHpiEventLogInfoT()
    error = SA_OK
    timeout = SAHPI_TIMEOUT_BLOCK
    sid = None

    rdr = SaHpiRdrT()
    event = SaHpiEventT()
    rptentry = SaHpiRptEntryT()

    listctrl = None

    def __init__(self,lstctrl,sessionid):
        global listctrl,sid
        Thread.__init__(self)
        listctrl = lstctrl
        sid=sessionid

    def run(self):
	print "Listening for Events .... "
	thread.start_new_thread (self.CatchEvent,())


    def CatchEvent(self):
        global res
        global rdr
        global sid
        global timeout
        global event
        self.rdr.RdrType = SAHPI_NO_RECORD
        error, qstatus = saHpiEventGet(sid, self.timeout, self.event, self.rdr, self.res)
        if error != SA_OK:
            if error != SA_ERR_HPI_TIMEOUT:
                print 'ERROR during EventGet: %s' % oh_lookup_error(error)
            else:
                if self.timeout == SAHPI_TIMEOUT_BLOCK:
                    print 'ERROR: Timeout while infinite wait'
                elif self.timeout != SAHPI_TIMEOUT_IMMEDIATE:
                    print 'ERROR: Time, %u seconds, expired waiting for event' % options.timeout
        else:
            if self.rdr.RdrType == SAHPI_NO_RECORD:
                oh_print_event(self.event, None, 4)
            else:
##                    oh_print_event(event, rdr.Entity, 4)
                b=SaHpiTextBufferT()
                oh_decode_time(self.event.Timestamp, b)
                oh_init_bigtext(tbuff)
                oh_decode_entitypath(self.rdr.Entity, tbuff)
                self.listctrl.append([b.Data,tbuff.Data,oh_lookup_severity(self.event.Severity),oh_lookup_eventtype(self.event.EventType),str(self.event.EventDataUnion.DomainEvent.DomainId)])
