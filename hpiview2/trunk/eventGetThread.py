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
        self.AddEvent()

    def run(self):
        global res
        global rdr
        global sid
        global timeout
        global event
        global listctrl

	print "Listening for Events .... "
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
                tbuff = oh_big_textbuffer()
                b=SaHpiTextBufferT()
                oh_decode_time(self.event.Timestamp, b)
                oh_decode_entitypath(self.rdr.Entity, tbuff)
                listctrl.Append([b.Data,tbuff.Data,oh_lookup_severity(self.event.Severity),oh_lookup_eventtype(self.event.EventType),str(self.event.EventDataUnion.DomainEvent.DomainId)])
##                oh_print_event(self.event, None, 4)
            else:
                tbuff = oh_big_textbuffer()
                b=SaHpiTextBufferT()
                oh_decode_time(self.event.Timestamp, b)
                oh_decode_entitypath(self.rdr.Entity, tbuff)
                listctrl.Append([b.Data,tbuff.Data,oh_lookup_severity(self.event.Severity),oh_lookup_eventtype(self.event.EventType),str(self.event.EventDataUnion.DomainEvent.DomainId)])

    def AddEvent(self):
        global sid
        # the event initialized
        event =  SaHpiEventT()

        # initialize the mandatory attributes
        event.EventType = SAHPI_ET_USER
        event.Source = SAHPI_UNSPECIFIED_RESOURCE_ID

        # initialize the attreibutes for the specific kind of event that is to be triggerred.

        sensorevt = SaHpiSensorEventT()
        sensorchangeevt = SaHpiSensorEnableChangeEventT()
        userevt = SaHpiUserEventT()

        sensorevt.SensorNum = 222
        sensorevt.SensorType = SAHPI_TEMPERATURE
        sensorevt.EventCategory = SAHPI_EC_THRESHOLD
        sensorevt.Assertion = True

        sensorchangeevt.SensorNum = 222
        sensorchangeevt.SensorEnable = True

        textbuffer = SaHpiTextBufferT()
        oh_append_textbuffer(textbuffer,"Custom Event")

        userevt.UserEventData = textbuffer


        ##event.EventDataUnion.SensorEvent = sensorevt
        ##event.EventDataUnion.SensorEnableChangeEvent = sensorchangeevt
        event.EventDataUnion.UserEvent = userevt


        error = saHpiEventAdd(sid, event)
        error = saHpiEventLogEntryAdd (sid , SAHPI_UNSPECIFIED_RESOURCE_ID , event)
        
        print "Added the Custom User Event onto the Events Stack"
