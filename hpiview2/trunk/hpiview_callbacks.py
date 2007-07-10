#!/usr/bin/env python

import wx
import sys, os
from optparse import OptionParser
from openhpi import *


class Hpiview_Callbacks:

    frame = None
    sid = None
    dinfo = None
    Status = None	    	
    res = None
    rdr = None

    def openHpiSession(self):
	global sid
	error, sid = saHpiSessionOpen(SAHPI_UNSPECIFIED_DOMAIN_ID, None)
	return 
		
    def discover(self):
	global dinfo
	error = saHpiDiscover(sid)
	dinfo = SaHpiDomainInfoT()
	error = saHpiDomainInfoGet(sid, dinfo)
	return

    def SubscribeEvents(self):
	global sid
	error = saHpiSubscribe(sid)
	return	

    def unSubscribeEvents(self):
	global sid
	error = saHpiUnsubscribe(sid)
	return	

    def polpulateResAndRdrTypeData(self):
	global frame
	global sid
	global res
	global rdr
    	res = SaHpiRptEntryT()
    	rdr = SaHpiRdrT()

	error = SA_OK
	error1 = SA_OK
	while error == SA_OK and eid != SAHPI_LAST_ENTRY:

		erid = SAHPI_FIRST_ENTRY

		print 'rptentry[%u] tag: %s' % (res.ResourceId, res.ResourceTag.Data)

		error, nexteid = saHpiRptEntryGet(sid, eid, res)

		if error == SA_OK:
			rid = res.ResourceId

			if res.ResourceCapabilities & SAHPI_CAPABILITY_RDR:
				
				while error1 == SA_OK and  erid != SAHPI_LAST_ENTRY:

					error1 , nextrdrid = saHpiRdrGet(sid , rid , erid , rdr)
				
					oh_print_rdr(rdr, 4)
		
					erid = nextrdrid
		

			else:
				dbg('Resource doesn\'t have RDR')


			eid = nexteid
	return	

    def popualateRDRData(self):	


    def dbg(format, vals=()):
	"""Prints message only if verbose is turned on"""
	if options.verbose:
		print format % vals

    def errorout(format, error):
	"""Prints HPI error and exits"""
	if error != SA_OK:
		print format % oh_lookup_error(error)
		sys.exit(-1)

    def setFrame(self, mainFrame):
	global frame 
	frame = mainFrame

    def sys_activated(self, event): # wxGlade: MyFrame.<event_handler>
        #print "Event handler `sys_activated' not implemented!"
	global frame


    def sys_collapsed(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `sys_collapsed' not implemented!"
        event.Skip()

    def sys_expanded(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `sys_expanded' not implemented!"
        event.Skip()

    def Menu_Session_Quit_Handler(self, event): # wxGlade: MyFrame.<event_handler>
	global frame
        #print "Event handler `Menu_Session_Quit_Handler' not implemented"
        frame.DestroyChildren()
	frame.Destroy()
	#event.Skip(True)

    def CLose_Button_Handler(self, event): # wxGlade: MyFrame.<event_handler>
	global frame
	global sid
	error = saHpiSessionClose(sid)
        frame.list_box_1.Delete(frame.list_box_1.GetSelection())
        frame.tree_ctrl_1.DeleteAllItems()
        frame.text_ctrl_1.Clear()
        frame.notebook_1.Show(False)
 
    def Set_TreeOnNewSession(self, event): # wxGlade: MyFrame.<event_handler>
	global frame
	polpulateResAndRdrTypeData()

    
    def Hide_Domain_Handler(self, event): # wxGlade: MyFrame.<event_handler>
	global frame
        if(frame.list_box_1.IsShown() == False):
            frame.list_box_1.Show(show=True)
        else:
	    if(frame.list_box_1.IsShown() == True):
	    	frame.list_box_1.Show(show=False)

    def New_Session_Handler(self, event): # wxGlade: MyFrame.<event_handler>
	global frame
        frame.tree_ctrl_1.DeleteAllItems()
	if(frame.list_box_1.GetCount() < 1):
	        frame.list_box_1.Insert("DEFAULT",frame.list_box_1.GetCount(),None)
        frame.notebook_1.Show(True)
