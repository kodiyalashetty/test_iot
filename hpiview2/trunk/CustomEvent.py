#!/usr/bin/env python

from openhpi import *


class CustomEvent:

    def __init__(self,sid):

        event =  SaHpiEventT()

        # initialize the mandatory attributes
        event.EventType = SAHPI_ET_USER
        event.Source = SAHPI_UNSPECIFIED_RESOURCE_ID

        # initialize the attributes for the specific kind of event that is to be triggerred.

        userevt = SaHpiUserEventT()

        textbuffer = SaHpiTextBufferT()
        oh_append_textbuffer(textbuffer,"Custom Event")

        userevt.UserEventData = textbuffer


        event.EventDataUnion.UserEvent = userevt


        error = saHpiEventAdd(sid, event)
        error = saHpiEventLogEntryAdd (sid , SAHPI_UNSPECIFIED_RESOURCE_ID , event)
        
