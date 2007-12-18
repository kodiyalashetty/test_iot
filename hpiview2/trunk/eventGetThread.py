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
    frame = None
    dlist = [""]

    def __init__(self,lstctrl,sessionid,frm,domainlist):
        global listctrl,sid,frame,dlist
        Thread.__init__(self)
        listctrl = lstctrl
        frame = frm
        sid=sessionid
        dlist = domainlist
        self.AddEvent()

    def run(self):
        global res
        global rdr
        global sid
        global timeout
        global event
        global listctrl
        global dlist

	self.Msg("Listening for Events .... ")
        self.rdr.RdrType = SAHPI_NO_RECORD
        error, qstatus = saHpiEventGet(sid, self.timeout, self.event, self.rdr, self.res)
        if error != SA_OK:
            if error != SA_ERR_HPI_TIMEOUT:
                self.Msg('ERROR during EventGet: %s' % oh_lookup_error(error))
            else:
                if self.timeout == SAHPI_TIMEOUT_BLOCK:
                    self.Msg('ERROR: Timeout while infinite wait')
                elif self.timeout != SAHPI_TIMEOUT_IMMEDIATE:
                    self.Msg('ERROR: Time, %u seconds, expired waiting for event' % options.timeout)
        else:
            for ind in range(1,len(dlist)):
                if(self.event.EventDataUnion.DomainEvent.DomainId == dlist[ind].DomainId):
                    dname = dlist[ind].DomainTag.Data
            if self.rdr.RdrType == SAHPI_NO_RECORD:
                tbuff = oh_big_textbuffer()
                b=SaHpiTextBufferT()
                oh_decode_time(self.event.Timestamp, b)
                oh_decode_entitypath(self.rdr.Entity, tbuff)
                listctrl.Append([b.Data,tbuff.Data,oh_lookup_severity(self.event.Severity),oh_lookup_eventtype(self.event.EventType),dname])
##                oh_print_event(self.event, None, 4)
            else:
                tbuff = oh_big_textbuffer()
                b=SaHpiTextBufferT()
                oh_decode_time(self.event.Timestamp, b)
                oh_decode_entitypath(self.rdr.Entity, tbuff)
                listctrl.Append([b.Data,tbuff.Data,oh_lookup_severity(self.event.Severity),oh_lookup_eventtype(self.event.EventType),dname])

    def AddEvent(self):
        global sid
        # the event initialized
        event =  SaHpiEventT()

        # initialize the mandatory attributes
        event.EventType = SAHPI_ET_USER
        event.Source = SAHPI_UNSPECIFIED_RESOURCE_ID

        # initialize the attributes for the specific kind of event that is to be triggerred.

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


##        event.EventDataUnion.SensorEvent = sensorevt
##        event.EventDataUnion.SensorEnableChangeEvent = sensorchangeevt
        event.EventDataUnion.UserEvent = userevt


        error = saHpiEventAdd(sid, event)
        error = saHpiEventLogEntryAdd (sid , SAHPI_UNSPECIFIED_RESOURCE_ID , event)
        
        self.Msg("Added the Custom User Event onto the Events Stack")

    def Msg(self , message):
        global frame
        frame.text_ctrl_2.SetValue(frame.text_ctrl_2.GetValue()+"\r\n"+message)
