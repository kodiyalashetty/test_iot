#!/usr/bin/env python

import wx
import sys, os
from openhpi import *


class Hpiview_Callbacks:

    frame = None
    sid = None
    dinfo = None
    Status = None	    	
    res = None
    rdr = None		
    rdrlist = None
		
    def __init__(self, fr):
	global frame
	global rdrlist
	frame = fr
	frame.Bind(wx.EVT_MENU, self.Menu_Session_Quit_Handler)
	frame.Bind(wx.EVT_TOOL, self.CLose_Button_Handler)   
	frame.Bind(wx.EVT_BUTTON, self.New_Session_Handler, frame.bitmap_button_2)
	frame.Bind(wx.EVT_BUTTON, self.Hide_Domain_Handler, frame.bitmap_button_1)	
	frame.Bind(wx.EVT_LISTBOX_DCLICK, self.Set_TreeOnNewSession, frame.list_box_1)
	frame.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.sys_activated, frame.tree_ctrl_1)	
	frame.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.sys_collapsed, frame.tree_ctrl_1)
	frame.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.sys_expanded, frame.tree_ctrl_1)	
	rdrlist=[["x",0,0,0]]

    def openHpiSession(self):
	global sid
	error, sid = saHpiSessionOpen(SAHPI_UNSPECIFIED_DOMAIN_ID, None)
	print "Session opened"
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
	global frame,sid , res , rdr ,rdrlist
	first = True
	firstroot = True
	addChildsToRoot = False
	tbuff = None
	textbuffer = oh_big_textbuffer()
    	res = SaHpiRptEntryT()
    	rdr = SaHpiRdrT()
	eid = SAHPI_FIRST_ENTRY
	error = SA_OK
	error1 = SA_OK
	while error == SA_OK and eid != SAHPI_LAST_ENTRY:

		erid = SAHPI_FIRST_ENTRY

		error, nexteid = saHpiRptEntryGet(sid, eid, res)

		if error == SA_OK:
			rid = res.ResourceId


			if res.ResourceCapabilities & SAHPI_CAPABILITY_RDR:
			
				while error1 == SA_OK and  erid != SAHPI_LAST_ENTRY:

					error1 , nextrdrid = saHpiRdrGet(sid , rid , erid , rdr)

					if(firstroot):
						tbuff = oh_big_textbuffer()
						oh_init_bigtext(tbuff)
						oh_decode_entitypath(rdr.Entity, tbuff)
						frame.tree_ctrl_1.AddRoot(tbuff.Data,-1,-1,None)
						firstroot=False
						tbuff = None

					if(addChildsToRoot):				
						tbuff = oh_big_textbuffer()
						oh_init_bigtext(tbuff)
						oh_decode_entitypath(rdr.Entity, tbuff)
						frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),tbuff.Data,-1,-1,None)
						addChildsToRoot=False
						tbuff = None

					if(first):
						if(rdr.RdrType == SAHPI_SENSOR_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),str(oh_lookup_sensortype(rdr.RdrTypeUnion.SensorRec.Type)) + " Sensor",-1,-1,None)			
							rdrlist.append([str(oh_lookup_sensortype(rdr.RdrTypeUnion.SensorRec.Type)) + " Sensor",rdr.RdrTypeUnion.SensorRec.Num,rid,rdr.RdrType])
						if(rdr.RdrType == SAHPI_CTRL_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),str(oh_lookup_ctrltype(rdr.RdrTypeUnion.CtrlRec.Type)) + " Control",-1,-1,None)			
							rdrlist.append([str(oh_lookup_ctrltype(rdr.RdrTypeUnion.CtrlRec.Type))+ " Control",rdr.RdrTypeUnion.CtrlRec.Num,rid,rdr.RdrType])
						if(rdr.RdrType == SAHPI_WATCHDOG_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"WatchDog # "+ str(rdr.RdrTypeUnion.WatchdogRec.WatchdogNum),-1,-1,None)			
							rdrlist.append(["WatchDog # "+str(rdr.RdrTypeUnion.WatchdogRec.WatchdogNum),rdr.RdrTypeUnion.WatchdogRec.WatchdogNum,rid,rdr.RdrType])
						if(rdr.RdrType == SAHPI_INVENTORY_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),str(rdr.RdrType),-1,-1,None)			
							rdrlist.append([str(rdr.RdrType),rdr.RdrType,rid,rdr.RdrType])
						if(rdr.RdrType == SAHPI_ANNUNCIATOR_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Annunciator #"+ str(rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum),-1,-1,None)			
							rdrlist.append(["Annunciator #"+ str(rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum),rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum,rid,rdr.RdrType])

					if(first == False):
						if(rdr.RdrType == SAHPI_SENSOR_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),str(oh_lookup_sensortype(rdr.RdrTypeUnion.SensorRec.Type)) + " Sensor",-1,-1,None)			
							rdrlist.append([str(oh_lookup_sensortype(rdr.RdrTypeUnion.SensorRec.Type))+" Sensor",rdr.RdrTypeUnion.SensorRec.Num,rid,rdr.RdrType])
						if(rdr.RdrType == SAHPI_CTRL_RDR):						
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),str(oh_lookup_ctrltype(rdr.RdrTypeUnion.CtrlRec.Type)) + " Control",-1,-1,None)			
							rdrlist.append([str(oh_lookup_ctrltype(rdr.RdrTypeUnion.CtrlRec.Type))+" Control",rdr.RdrTypeUnion.CtrlRec.Num,rid,rdr.RdrType])
						if(rdr.RdrType == SAHPI_WATCHDOG_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"WatchDog # "+ str(rdr.RdrTypeUnion.WatchdogRec.WatchdogNum),-1,-1,None)			
							rdrlist.append(["WatchDog # "+str(rdr.RdrTypeUnion.WatchdogRec.WatchdogNum),rdr.RdrTypeUnion.WatchdogRec.WatchdogNum,rid,rdr.RdrType])
						if(rdr.RdrType == SAHPI_INVENTORY_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),str(rdr.RdrType),-1,-1,None)			
							rdrlist.append([str(rdr.RdrType),rdr.RdrType,rid,rdr.RdrType])
						if(rdr.RdrType == SAHPI_ANNUNCIATOR_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Annunciator #"+ str(rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum),-1,-1,None)			
							rdrlist.append(["Annunciator #"+ str(rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum),rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum,rid,rdr.RdrType])

					erid = nextrdrid
		

			else:
				dbg('Resource doesn\'t have RDR')

		first = False
		eid = nexteid
		if(eid > 1):
			addChildsToRoot=True
	
		print 'rptentry[%u] tag: %s' % (res.ResourceId, res.ResourceTag.Data)

	return	

    def popualateRDRData(self):	
	return

    def dbg(format, vals=()):
	"""Prints message only if verbose is turned on"""
	if options.verbose:
		print format % vals

    def errorout(format, error):
	"""Prints HPI error and exits"""
	if error != SA_OK:
		print format % oh_lookup_error(error)
		sys.exit(-1)

    def sys_activated(self, event): # wxGlade: MyFrame.<event_handler>
	global frame
	global rdrlist
	global sid
	reading = None
	evtState = None
	textbuffer = oh_big_textbuffer()
	error = SA_OK
	frame.text_ctrl_1.ChangeValue(frame.tree_ctrl_1.GetItemText(frame.tree_ctrl_1.GetSelection()))
	for ind in range(0,len(rdrlist)):
		if(rdrlist[ind][0] == frame.text_ctrl_1.GetValue()):
			if(rdrlist[ind][3]==SAHPI_SENSOR_RDR):
				oh_init_bigtext(textbuffer)
				reading = SaHpiSensorReadingT()
				textbuffer = SaHpiTextBufferT()
				error ,evtState = saHpiSensorReadingGet(sid,rdrlist[ind][2],rdrlist[ind][1],reading)
				oh_decode_sensorreading(reading,rdr.RdrTypeUnion.SensorRec.DataFormat,textbuffer)
				oh_append_textbuffer(textbuffer,"\n"+"Type \t"+str(oh_lookup_sensortype(reading.Type))+"\n"+str(reading.Value.SensorBuffer))
				oh_append_textbuffer(textbuffer,"Sensor Type \t"+str(oh_lookup_sensorreadingtype(reading.Type))+"\n")
				oh_append_textbuffer(textbuffer,str(oh_lookup_sensorunits(rdr.RdrTypeUnion.SensorRec.DataFormat.BaseUnits))+"\n")
				oh_append_textbuffer(textbuffer,"Event Control \t"+str(oh_lookup_sensoreventctrl(rdr.RdrTypeUnion.SensorRec.EventCtrl))+"\n")
				oh_append_textbuffer(textbuffer,"Min Value \t"+str(rdr.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Value.SensorFloat64)+"\n")
				oh_append_textbuffer(textbuffer,"Max Value \t"+str(rdr.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Value.SensorFloat64)+"\n")
				oh_append_textbuffer(textbuffer,"Nominal Value \t"+str(rdr.RdrTypeUnion.SensorRec.DataFormat.Range.Nominal.Value.SensorFloat64)+"\n")
				oh_append_textbuffer(textbuffer,"Normal MinValue \t"+str(rdr.RdrTypeUnion.SensorRec.DataFormat.Range.NormalMin.Value.SensorFloat64)+"\n")
				oh_append_textbuffer(textbuffer,"Normal MaxValue \t"+str(rdr.RdrTypeUnion.SensorRec.DataFormat.Range.NormalMax.Value.SensorFloat64)+"\n")
				frame.text_ctrl_1.ChangeValue(textbuffer.Data)

    def sys_collapsed(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `sys_collapsed' not implemented!"
        event.Skip()

    def sys_expanded(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `sys_expanded' not implemented!"
        event.Skip()

    def Menu_Session_Quit_Handler(self, event): # wxGlade: MyFrame.<event_handler>
	global frame
	global sid
        print "Event handler `Menu_Session_Quit_Handler' not implemented"
	saHpiSessionClose(sid)
        frame.DestroyChildren()
	frame.Destroy()
	#event.Skip(True)
    
    def Set_TreeOnNewSession(self, event): # wxGlade: MyFrame.<event_handler>
	global frame
	self.polpulateResAndRdrTypeData()

    
    def CLose_Button_Handler(self, event): # wxGlade: MyFrame.<event_handler>
	global frame
	global sid
	#error = saHpiSessionClose(sid)
	frame.list_box_1.Delete(frame.list_box_1.GetSelection())
        frame.tree_ctrl_1.DeleteAllItems()
        frame.text_ctrl_1.Clear()
        frame.notebook_1.Show(False)
	#event.Skip(True)
    
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
	self.openHpiSession()
	self.polpulateResAndRdrTypeData()
