#!/usr/bin/env python


import wx
import sys, os
from openhpi import *
import ResourcePref
import SensorPref
import ControlPref
import InventoryPref
import WatchDogPref
import ResEventLog
import PrefEvtLogTimestamp

class Hpiview_Callbacks:

    frame = None
    sid = None
    dinfo = None
    Status = None	    	
    res = None
    rdr = None		
    rdrlist = None
    rdrevtlist = None
    item_clicked = None	
    menu_titles = {}
    resources = [""]
    ResourceTitles = ["EventLog","Event Log Timestamp", "Event Log Clear","-","Parameter Control", "Power", "reset","-","Preferences"] 	
    SensorTitles = ["Read Sensor","Preferences"]
    ControlTitles = ["Preferences"]
    WatchdogTitles = ["Reset Watchdog","Preferences"]
    InventoryTitles = ["Preferences"]
    menu_type = ""	
	
    menu_title_by_id = {}
		
    def __init__(self, fr):
	global frame
	global rdrlist
	frame = fr
	frame.Bind(wx.EVT_MENU, self.Menu_Session_Quit_Handler,id=101)
	frame.Bind(wx.EVT_TOOL, self.CLose_Button_Handler,id=201)   
	frame.Bind(wx.EVT_BUTTON, self.New_Session_Handler, frame.bitmap_button_2)
	frame.Bind(wx.EVT_BUTTON, self.Hide_Domain_Handler, frame.bitmap_button_1)
	frame.Bind(wx.EVT_BUTTON, self.Hide_Events_Handler, frame.bitmap_button_3)
	frame.Bind(wx.EVT_BUTTON, self.Hide_Messages_Handler, frame.bitmap_button_4)
	frame.Bind(wx.EVT_LISTBOX_DCLICK, self.Set_TreeOnNewSession, frame.list_box_1)
	frame.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.sys_activated, frame.tree_ctrl_1)	
	frame.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.sys_collapsed, frame.tree_ctrl_1)
	frame.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.sys_expanded, frame.tree_ctrl_1)
	frame.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.RightClickCb ,frame.tree_ctrl_1)
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
	rdr1 = SaHpiRdrT()
	eid = SAHPI_FIRST_ENTRY
	error = SA_OK
	error1 = SA_OK
	error2 = SA_OK
	event = SaHpiEventT()
	rid=None
	font = wx.Font(pointSize=10, family=wx.FONTFAMILY_DEFAULT,style=wx.FONTSTYLE_ITALIC, weight=wx.FONTWEIGHT_LIGHT)
	rootfont = wx.Font(pointSize=10, family=wx.FONTFAMILY_DEFAULT,style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_BOLD)
	while error == SA_OK and eid != SAHPI_LAST_ENTRY:

		erid = SAHPI_FIRST_ENTRY

		error, nexteid = saHpiRptEntryGet(sid, eid, res)

		if error == SA_OK:
			rid = res.ResourceId


			if res.ResourceCapabilities & SAHPI_CAPABILITY_RDR:
			
				while error1 == SA_OK and  erid != SAHPI_LAST_ENTRY:

					error1 , nextrdrid = saHpiRdrGet(sid , rid , erid , rdr)
					Timeout = SAHPI_TIMEOUT_IMMEDIATE
					tempres = SaHpiRptEntryT()
					temprdr = SaHpiRdrT()
					error2, qstatus = saHpiEventGet(sid, Timeout, event, temprdr, tempres)

					if(firstroot):
						tbuff = oh_big_textbuffer()
						oh_init_bigtext(tbuff)
						oh_decode_entitypath(rdr.Entity, tbuff)
						frame.tree_ctrl_1.AddRoot(res.ResourceTag.Data,-1,-1,None)
						frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetRootItem(),rootfont)
						rdrlist.append([res.ResourceTag.Data,res.ResourceId,res.ResourceEntity,res.ResourceCapabilities,res.HotSwapCapabilities,res.ResourceTag.Data,res.ResourceSeverity,res.ResourceInfo,tbuff.Data])
						firstroot=False
						tbuff = None

					if(addChildsToRoot):				
						tbuff = oh_big_textbuffer()
						oh_init_bigtext(tbuff)
						oh_decode_entitypath(rdr.Entity, tbuff)
						frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),res.ResourceTag.Data,-1,-1,None)
						frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),rootfont)
						rdrlist.append([res.ResourceTag.Data,res.ResourceId,res.ResourceEntity,res.ResourceCapabilities,res.HotSwapCapabilities,res.ResourceTag.Data,res.ResourceSeverity,res.ResourceInfo,tbuff.Data])
						addChildsToRoot=False
						tbuff = None

					if(first):
						if(rdr.RdrType == SAHPI_SENSOR_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),str(oh_lookup_sensortype(rdr.RdrTypeUnion.SensorRec.Type)) + " Sensor",-1,-1,None)			
							#frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
							rdrlist.append([str(oh_lookup_sensortype(rdr.RdrTypeUnion.SensorRec.Type)) + " Sensor",rdr.RdrTypeUnion.SensorRec.Num,rid,rdr.RdrType,rdr.RdrTypeUnion.SensorRec.DataFormat,rdr.RdrTypeUnion.SensorRec.DataFormat.BaseUnits,rdr.RdrTypeUnion.SensorRec.Type,rdr.RdrTypeUnion.SensorRec.EnableCtrl,rdr.RdrTypeUnion.SensorRec.EventCtrl,rdr.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Value.SensorFloat64,rdr.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Value.SensorFloat64,rdr.RdrTypeUnion.SensorRec.DataFormat.Range.Nominal.Value.SensorFloat64,rdr.RdrTypeUnion.SensorRec.DataFormat.Range.NormalMin.Value.SensorFloat64,rdr.RdrTypeUnion.SensorRec.DataFormat.Range.NormalMax.Value.SensorFloat64,rdr.IsFru,rdr.RdrTypeUnion.SensorRec.Category])
						if(rdr.RdrType == SAHPI_CTRL_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),str(oh_lookup_ctrltype(rdr.RdrTypeUnion.CtrlRec.Type)) + " Control",-1,-1,None)			
							#frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
							rdrlist.append([str(oh_lookup_ctrltype(rdr.RdrTypeUnion.CtrlRec.Type))+ " Control",rdr.RdrTypeUnion.CtrlRec.Num,rid,rdr.RdrType,rdr.RdrTypeUnion.CtrlRec.Type,rdr.RdrTypeUnion.CtrlRec.OutputType,rdr.IsFru,rdr.RdrTypeUnion.CtrlRec.DefaultMode.Mode,rdr.RdrTypeUnion.CtrlRec.WriteOnly,rdr.RdrTypeUnion.CtrlRec.DefaultMode.ReadOnly])
						if(rdr.RdrType == SAHPI_WATCHDOG_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"WatchDog  "+ str(rdr.RdrTypeUnion.WatchdogRec.WatchdogNum),-1,-1,None)			
							#frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
							rdrlist.append(["WatchDog  "+str(rdr.RdrTypeUnion.WatchdogRec.WatchdogNum),rdr.RdrTypeUnion.WatchdogRec.WatchdogNum,rid,rdr.RdrType,rdr.IsFru])
						if(rdr.RdrType == SAHPI_INVENTORY_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Simulator Inv "+str(rdr.RdrType),-1,-1,None)			
							#frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
							rdrlist.append(["Simulator Inv "+str(rdr.RdrType),rdr.RdrType,rid,rdr.RdrType,rdr.IsFru,rdr.RdrTypeUnion.InventoryRec.Persistent,rdr.RdrTypeUnion.InventoryRec.IdrId])
						if(rdr.RdrType == SAHPI_ANNUNCIATOR_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Annunciator "+ str(rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum),-1,-1,None)			
							#frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
							rdrlist.append(["Annunciator "+ str(rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum),rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum,rid,rdr.RdrType,rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorType,rdr.IsFru])

					if(first == False):
						if(rdr.RdrType == SAHPI_SENSOR_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),str(oh_lookup_sensortype(rdr.RdrTypeUnion.SensorRec.Type)) + " Sensor",-1,-1,None)			
							#frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
							rdrlist.append([str(oh_lookup_sensortype(rdr.RdrTypeUnion.SensorRec.Type))+" Sensor",rdr.RdrTypeUnion.SensorRec.Num,rid,rdr.RdrType,rdr.RdrTypeUnion.SensorRec.DataFormat,rdr.RdrTypeUnion.SensorRec.DataFormat.BaseUnits,rdr.RdrTypeUnion.SensorRec.Type,rdr.RdrTypeUnion.SensorRec.EnableCtrl,rdr.RdrTypeUnion.SensorRec.EventCtrl,rdr.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Value.SensorFloat64,rdr.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Value.SensorFloat64,rdr.RdrTypeUnion.SensorRec.DataFormat.Range.Nominal.Value.SensorFloat64,rdr.RdrTypeUnion.SensorRec.DataFormat.Range.NormalMin.Value.SensorFloat64,rdr.RdrTypeUnion.SensorRec.DataFormat.Range.NormalMax.Value.SensorFloat64,rdr.IsFru,rdr.RdrTypeUnion.SensorRec.Category])
						if(rdr.RdrType == SAHPI_CTRL_RDR):						
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),str(oh_lookup_ctrltype(rdr.RdrTypeUnion.CtrlRec.Type)) + " Control",-1,-1,None)			
							#frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
							rdrlist.append([str(oh_lookup_ctrltype(rdr.RdrTypeUnion.CtrlRec.Type))+" Control",rdr.RdrTypeUnion.CtrlRec.Num,rid,rdr.RdrType,rdr.RdrTypeUnion.CtrlRec.Type,rdr.RdrTypeUnion.CtrlRec.OutputType,rdr.IsFru,rdr.RdrTypeUnion.CtrlRec.DefaultMode,rdr.RdrTypeUnion.CtrlRec.WriteOnly])
						if(rdr.RdrType == SAHPI_WATCHDOG_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"WatchDog  "+ str(rdr.RdrTypeUnion.WatchdogRec.WatchdogNum),-1,-1,None)			
							#frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
							rdrlist.append(["WatchDog  "+str(rdr.RdrTypeUnion.WatchdogRec.WatchdogNum),rdr.RdrTypeUnion.WatchdogRec.WatchdogNum,rid,rdr.RdrType,rdr.IsFru])
						if(rdr.RdrType == SAHPI_INVENTORY_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Simulator Inv "+str(rdr.RdrType),-1,-1,None)			
							#frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
							rdrlist.append(["Simulator Inv "+str(rdr.RdrType),rdr.RdrType,rid,rdr.RdrType,rdr.IsFru,rdr.RdrTypeUnion.InventoryRec.Persistent,rdr.RdrTypeUnion.InventoryRec.IdrId])
						if(rdr.RdrType == SAHPI_ANNUNCIATOR_RDR):
							frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Annunciator "+ str(rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum),-1,-1,None)			
							#frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
							rdrlist.append(["Annunciator "+ str(rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum),rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum,rid,rdr.RdrType,rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorType,rdr.IsFru])

					erid = nextrdrid
		

			else:
				dbg('Resource doesn\'t have RDR')

		first = False
		eid = nexteid
		if(eid > 1):
			addChildsToRoot=True
	
		print 'rptentry[%u] tag: %s' % (res.ResourceId, res.ResourceTag.Data)
		self.resources.append(res.ResourceTag.Data)
				
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
	global frame,resources
	global rdrlist
	global sid
	reading = None
	evtState = None
	textbuffer = oh_big_textbuffer()
	error = SA_OK
	frame.text_ctrl_1.SetValue(frame.tree_ctrl_1.GetItemText(frame.tree_ctrl_1.GetSelection()))
	for ind in range(0,len(rdrlist)):
		if(rdrlist[ind][0] == frame.text_ctrl_1.GetValue()):
			if(rdrlist[ind][3]==SAHPI_SENSOR_RDR):
				oh_init_bigtext(textbuffer)
				reading = SaHpiSensorReadingT()
				textbuffer = SaHpiTextBufferT()
				error ,evtState = saHpiSensorReadingGet(sid,rdrlist[ind][2],rdrlist[ind][1],reading)
				oh_append_textbuffer(textbuffer,"\n"+" Type 			\t"+"Sensor \n")
				if(rdrlist[ind][14]==0):
					oh_append_textbuffer(textbuffer,"\n"+" FRU Entity 		\t"+ "False" +"\n")
				else:
					oh_append_textbuffer(textbuffer,"\n"+" FRU Entity 		\t"+ "True" +"\n")
				oh_append_textbuffer(textbuffer,"\n"+" Sensor Type 		\t"+str(oh_lookup_sensortype(rdrlist[ind][6]))+"\n")
				oh_append_textbuffer(textbuffer,"\n"+" Sensor Base Unit 	\t"+str(oh_lookup_sensorunits(rdrlist[ind][5]))+"\n")
				if(rdrlist[ind][7]==0):
					oh_append_textbuffer(textbuffer,"\n"+" Sensor Control 	\t"+ "False" +"\n")
				else:
					oh_append_textbuffer(textbuffer,"\n"+" Sensor Control 	\t"+ "True" +"\n")
				frame.text_ctrl_1.SetValue(textbuffer.Data)
				textbuffer = SaHpiTextBufferT()
				oh_append_textbuffer(textbuffer,"\n"+" Event Control 	\t"+str(oh_lookup_sensoreventctrl(rdrlist[ind][8]))+"\n")
				oh_append_textbuffer(textbuffer,"\n"+" Min Value 		\t"+str(rdrlist[ind][9])+"\n")
				oh_append_textbuffer(textbuffer,"\n"+" Max Value 		\t"+str(rdrlist[ind][10])+"\n")
				oh_append_textbuffer(textbuffer,"\n"+" Nominal Value 	\t"+str(rdrlist[ind][11])+"\n")
				oh_append_textbuffer(textbuffer,"\n"+" Normal MinValue 	\t"+str(rdrlist[ind][12])+"\n")
				oh_append_textbuffer(textbuffer,"\n"+" Normal MaxValue 	\t"+str(rdrlist[ind][13])+"\n")
				frame.text_ctrl_1.SetValue(frame.text_ctrl_1.GetValue()+textbuffer.Data)
				continue
			if(rdrlist[ind][3]==SAHPI_CTRL_RDR):
				ctrlState = SaHpiCtrlStateT()
				textbuffer = SaHpiTextBufferT()
				error ,Mode = saHpiControlGet(sid,rdrlist[ind][2],rdrlist[ind][1],ctrlState)
				oh_append_textbuffer(textbuffer,"\n"+" Type 			\t"+"Control"+"\n")
				if(rdrlist[ind][6]==0):
					oh_append_textbuffer(textbuffer,"\n"+" FRU Entity 		\t"+ "False" +"\n")
				else:
					oh_append_textbuffer(textbuffer,"\n"+" FRU Entity 		\t"+ "True" +"\n")
				oh_append_textbuffer(textbuffer,"\n" +" Control Type 		\t"+str(oh_lookup_ctrltype(rdrlist[ind][4]))+"\n")
				oh_append_textbuffer(textbuffer,"\n" +" Control Output Type \t" + str(oh_lookup_ctrloutputtype(rdrlist[ind][5]))+"\n")
				oh_append_textbuffer(textbuffer,"\n" +" Control State Digital\t"+str(oh_lookup_ctrlstatedigital(ctrlState.StateUnion.Digital))+"\n")
				oh_append_textbuffer(textbuffer,"\n" +" Mode 			\t"+str(oh_lookup_ctrlmode(Mode))+"\n")
				frame.text_ctrl_1.SetValue(textbuffer.Data)
				continue
			if(rdrlist[ind][3]==SAHPI_WATCHDOG_RDR):
				textbuffer = SaHpiTextBufferT()
				watchdogt = SaHpiWatchdogT()
				error = saHpiWatchdogTimerGet(sid,rdrlist[ind][2],rdrlist[ind][1],watchdogt)
				oh_append_textbuffer(textbuffer,"\n"+ " Type 			\t"+"WatchDog"+"\n")
				if(rdrlist[ind][4]==0):
					oh_append_textbuffer(textbuffer,"\n"+" FRU Entity 		\t"+ "False" +"\n")
				else:
					oh_append_textbuffer(textbuffer,"\n"+" FRU Entity 		\t"+ "True" +"\n")
				oh_append_textbuffer(textbuffer,"\n"+ " Watch Dog Action 	\t"+str(oh_lookup_watchdogaction(watchdogt.TimerAction))+"\n")
				oh_append_textbuffer(textbuffer,"\n"+ " Pre timer interrupt \t"+str(oh_lookup_watchdogpretimerinterrupt(watchdogt.PretimerInterrupt))+"\n")
				oh_append_textbuffer(textbuffer,"\n"+ " Timer use 		\t"+str(oh_lookup_watchdogtimeruse(watchdogt.TimerUse))+"\n")
				frame.text_ctrl_1.SetValue(textbuffer.Data)
				continue
			if(rdrlist[ind][3]==SAHPI_ANNUNCIATOR_RDR):
				textbuffer = SaHpiTextBufferT()
				annunt = SaHpiAnnouncementT()
				error = saHpiAnnunciatorGet(sid,rdrlist[ind][2],rdrlist[ind][1],SAHPI_FIRST_ENTRY,annunt)
				oh_append_textbuffer(textbuffer,"\n"+" Type 			\t"+"Annunciator"+"\n")
				if(rdrlist[ind][5]==0):
					oh_append_textbuffer(textbuffer,"\n"+" FRU Entity 		\t"+ "False" +"\n")
				else:
					oh_append_textbuffer(textbuffer,"\n"+" FRU Entity 		\t"+ "True" +"\n")
				oh_append_textbuffer(textbuffer,"\n"+" Annunciator Type 	\t" + str(oh_lookup_annunciatortype(rdrlist[ind][4]))+"\n")
				frame.text_ctrl_1.SetValue(textbuffer.Data)
				continue
			if(rdrlist[ind][3]==SAHPI_INVENTORY_RDR):
				textbuffer = SaHpiTextBufferT()
				idrinfo = SaHpiIdrInfoT()
				error = saHpiIdrInfoGet(sid,rdrlist[ind][2],rdrlist[ind][1],idrinfo)
				oh_append_textbuffer(textbuffer,"\n"+" Type 			\t"+"Inventory"+"\n")
				if(rdrlist[ind][4]==0):
					oh_append_textbuffer(textbuffer,"\n"+" FRU Entity 		\t"+ "False" +"\n")
				else:
					oh_append_textbuffer(textbuffer,"\n"+" FRU Entity 		\t"+ "True" +"\n")
				if(rdrlist[ind][5]==0):
					oh_append_textbuffer(textbuffer,"\n"+" Inventory's Persistent \t"+ "False" +"\n")
				else:
					oh_append_textbuffer(textbuffer,"\n"+" Inventory's Persistent \t"+ "True" +"\n")
				frame.text_ctrl_1.SetValue(textbuffer.Data)
				continue

  			textbuffer = SaHpiTextBufferT()
  			t1 = SaHpiTextBufferT()
			oh_append_textbuffer(textbuffer,"\n"+" ResourceID	\t" + str(rdrlist[ind][1])+"\n")
			oh_append_textbuffer(textbuffer,"\n"+" Entity Path 	\t" + rdrlist[ind][8]+"\n")
			oh_decode_capabilities(rdrlist[ind][3],t1)
			frame.text_ctrl_1.SetValue(textbuffer.Data)
			frame.text_ctrl_1.SetValue(frame.text_ctrl_1.GetValue()+"\n"+" Capabilities	\t" + t1.Data+"\n")
			textbuffer = SaHpiTextBufferT()
			oh_append_textbuffer(textbuffer,"\n"+" HotSwap Capabilities \t" + str(rdrlist[ind][4])+"\n")
			oh_append_textbuffer(textbuffer,"\n"+" Resource Tag	\t" + rdrlist[ind][5]+"\n")
			oh_append_textbuffer(textbuffer,"\n"+" Severity		\t" + str(rdrlist[ind][6])+"\n")
			frame.text_ctrl_1.SetValue(frame.text_ctrl_1.GetValue()+textbuffer.Data)
				
    def sys_collapsed(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `sys_collapsed' not implemented!"
        event.Skip()

    def sys_expanded(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `sys_expanded' not implemented!"
        event.Skip()

    def Menu_Session_Quit_Handler(self, event): # wxGlade: MyFrame.<event_handler>
	global frame,sid
	if(sid != None):
		print "closed"
		saHpiSessionClose(sid)
        frame.DestroyChildren()
	frame.Destroy()

    
    def Set_TreeOnNewSession(self, event): # wxGlade: MyFrame.<event_handler>
	global frame
	self.polpulateResAndRdrTypeData()

    
    def CLose_Button_Handler(self, event): # wxGlade: MyFrame.<event_handler>
	global frame
	global sid
	error = saHpiSessionClose(sid)
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
	frame.Layout()
	self.openHpiSession()
	self.polpulateResAndRdrTypeData()

    def Hide_Events_Handler(self,event):
	global frame
	frame.window_1.Unsplit(frame.window_1.GetWindow1())
	frame.window_2.Unsplit(frame.window_2.GetWindow2())
	
    def Hide_Messages_Handler(self,event):
	global frame
	frame.window_1.Unsplit(frame.window_1.GetWindow1())
	frame.window_2.Unsplit(frame.window_2.GetWindow1())

    def RightClickCb( self, event ):

	global frame,item_clicked,resources

        # record what was clicked
	
        item_clicked = frame.tree_ctrl_1.GetItemText(event.GetItem())

	self.menu_titles={}
	self.menu_title_by_id={}

	self.selectTitle(item_clicked)
	
	for title in self.menu_titles:
	  self.menu_title_by_id[ wx.NewId() ] = title

	print item_clicked
 
        ### 2. Launcher creates wxMenu. ###
        menu = wx.Menu()
        for (id,title) in self.menu_title_by_id.items():
            ### 3. Launcher packs menu with Append. ###
	    if(title == "-"):
	      menu.AppendSeparator()	
	    else:	
              menu.Append( id, title )
            ### 4. Launcher registers menu handlers with EVT_MENU, on the menu. ###
            wx.EVT_MENU( menu, id, self.MenuSelectionCb )
 
        ### 5. Launcher displays menu with call to PopupMenu, invoked on the source component, passing event's GetPoint. ###
        frame.tree_ctrl_1.PopupMenu( menu, event.GetPoint() )

    def MenuSelectionCb( self, event ):

        # do something
        operation = self.menu_title_by_id[ event.GetId() ]
        target    = self.item_clicked
        print 'Perform "%(operation)s" on "%(target)s."' % vars()

	if(self.menu_type == "Resource" and operation == self.ResourceTitles[len(self.ResourceTitles)-1]):
		self.ShowResInfo(self.item_clicked)
	if(self.menu_type == "Resource" and operation == self.ResourceTitles[0]):
		self.ShowEvtLog(self.item_clicked)
	if(self.menu_type == "Resource" and operation == self.ResourceTitles[1]):
		frm = PrefEvtLogTimestamp.MyFrame(frame,-1,"")
		frm.Show()
	if(self.menu_type == "Sensor" and operation == self.SensorTitles[len(self.SensorTitles)-1]):
		self.ShowSensorInfo(self.item_clicked)
	if(self.menu_type == "Control" and operation == self.ControlTitles[len(self.ControlTitles)-1]):
		self.ShowControlInfo(self.item_clicked)
	if(self.menu_type == "Inventory" and operation == self.InventoryTitles[len(self.InventoryTitles)-1]):
		self.ShowInvInfo(self.item_clicked)
	if(self.menu_type == "WatchDog" and operation == self.WatchdogTitles[len(self.WatchdogTitles)-1]):
		self.ShowWatchDogInfo(self.item_clicked)

    def ShowResInfo(self, selection):
	global item_clicked
	frm = ResourcePref.MyDialog(frame,-1,"")
	print item_clicked
	for ind in range(0,len(rdrlist)):
		 if(rdrlist[ind][0] == item_clicked):
			frm.label_1.SetLabel(frm.label_1.GetLabelText() + " : " + str(rdrlist[ind][7].AuxFirmwareRev))
			frm.label_2.SetLabel(frm.label_2.GetLabelText() + " : " + str(rdrlist[ind][7].FirmwareMinorRev))
			frm.label_3.SetLabel(frm.label_3.GetLabelText() + " : " + str(rdrlist[ind][7].FirmwareMajorRev))
			frm.label_4.SetLabel(frm.label_4.GetLabelText() + " : " + str(rdrlist[ind][7].ProductId))
			frm.label_5.SetLabel(frm.label_5.GetLabelText() + " : " + str(rdrlist[ind][7].ManufacturerId))
			frm.label_6.SetLabel(frm.label_6.GetLabelText() + " : " + str(rdrlist[ind][7].DeviceSupport))
			frm.label_7.SetLabel(frm.label_7.GetLabelText() + " : " + str(rdrlist[ind][7].SpecificVer))
			frm.label_8.SetLabel(frm.label_8.GetLabelText() + " : " + str(rdrlist[ind][7].ResourceRev))
	frm.ShowModal()

    def ShowEvtLog(self, selection):
	global item_clicked
	frm = ResEventLog.MyDialog(frame,-1,"")
	for ind in range(0,len(rdrlist)):
		 if(rdrlist[ind][0] == item_clicked):
			info = SaHpiEventLogInfoT()
			error = saHpiEventLogInfoGet(sid,rdrlist[ind][1],info)
			frm.label_1.SetLabel(frm.label_1.GetLabelText() + " : " + str(info.Entries))
			frm.label_2.SetLabel(frm.label_2.GetLabelText() + " : " + str(info.Size))
			frm.label_3.SetLabel(frm.label_3.GetLabelText() + " : " + str(info.UserEventMaxSize))
			b = SaHpiTextBufferT()
			oh_decode_time(info.UpdateTimestamp,b)
			frm.label_4.SetLabel(frm.label_4.GetLabelText() + " : " + b.Data)
			b = SaHpiTextBufferT()
			oh_decode_time(info.CurrentTime,b)
			frm.label_5.SetLabel(frm.label_5.GetLabelText() + " : " + b.Data)
			frm.label_6.SetLabel(frm.label_6.GetLabelText() + " : " + self.GetBoolean(info.OverflowFlag))
			frm.label_7.SetLabel(frm.label_7.GetLabelText() + " : " + self.GetBoolean(info.OverflowResetable))
			if(info.OverflowAction == 0):
				frm.label_8.SetLabel(frm.label_8.GetLabelText() + " : " + "Drop")
			else:
				frm.label_8.SetLabel(frm.label_8.GetLabelText() + " : " + "Overwrite")
			print info.Enabled
			frm.checkbox_1.SetValue(info.Enabled)
	frm.ShowModal()

    def ShowSensorInfo(self, selection):
	global item_clicked
	frm = SensorPref.MyDialog(frame,-1,"")
	print item_clicked
	for ind in range(0,len(rdrlist)):
		if(rdrlist[ind][0] == item_clicked):
			reading = SaHpiSensorReadingT()
			error ,evtState = saHpiSensorReadingGet(sid,rdrlist[ind][2],rdrlist[ind][1],reading)
			frm.label_1.SetLabel(frm.label_1.GetLabelText() + " : " + "Sensor")
			frm.label_2.SetLabel(frm.label_2.GetLabelText() + " : " + str(oh_lookup_sensortype(rdrlist[ind][6])))
			if(rdrlist[ind][7]==0):
				frm.label_3.SetLabel(frm.label_3.GetLabelText() + " : " + "False")
				frm.label_11.SetLabel(frm.label_11.GetLabelText() + " : " + "False")
			else:
				frm.label_3.SetLabel(frm.label_3.GetLabelText() + " : " + "True")
				frm.label_11.SetLabel(frm.label_11.GetLabelText() + " : " + "True")
			frm.label_4.SetLabel(frm.label_4.GetLabelText() + " : " + str(oh_lookup_sensorunits(rdrlist[ind][5])))
			frm.label_5.SetLabel(frm.label_5.GetLabelText() + " : " + str(rdrlist[ind][9]))
			frm.label_6.SetLabel(frm.label_6.GetLabelText() + " : " + str(rdrlist[ind][10]))
			frm.label_7.SetLabel(frm.label_7.GetLabelText() + " : " + str(rdrlist[ind][12]))
			frm.label_8.SetLabel(frm.label_8.GetLabelText() + " : " + str(rdrlist[ind][13]))
			frm.label_9.SetLabel(frm.label_9.GetLabelText() + " : " + str(rdrlist[ind][11]))
			frm.label_10.SetLabel(frm.label_10.GetLabelText() + " : " + str(oh_lookup_eventcategory(rdrlist[ind][14])))
			frm.label_12.SetLabel(frm.label_12.GetLabelText() + " : " + str(rdrlist[ind][15]))
			sensorthresholds = SaHpiSensorThresholdsT()
			error = saHpiSensorThresholdsGet(sid,rdrlist[ind][2],rdrlist[ind][1],sensorthresholds)	
			print 'sensor threshold value' % (sensorthresholds.PosThdHysteresis)
			frm.spin_ctrl_6.SetValue(sensorthresholds.NegThdHysteresis.Value.SensorFloat64)
			frm.spin_ctrl_1.SetValue(sensorthresholds.PosThdHysteresis.Value.SensorFloat64)
			frm.spin_ctrl_2.SetValue(sensorthresholds.UpCritical.Value.SensorFloat64)
			frm.spin_ctrl_3.SetValue(sensorthresholds.UpMajor.Value.SensorFloat64)
			frm.spin_ctrl_7.SetValue(sensorthresholds.UpMinor.Value.SensorFloat64)
			frm.spin_ctrl_4.SetValue(sensorthresholds.LowCritical.Value.SensorFloat64)		
			frm.spin_ctrl_5.SetValue(sensorthresholds.LowMajor.Value.SensorFloat64)
			frm.spin_ctrl_8.SetValue(sensorthresholds.LowMinor.Value.SensorFloat64)
			break
	frm.ShowModal()
	
    def ShowInvInfo(self, selection):
	global item_clicked
	frm = InventoryPref.MyDialog(frame,-1,"")
	print item_clicked
	for ind in range(0,len(rdrlist)):
		if(rdrlist[ind][0] == item_clicked):
			idrinfo = SaHpiIdrInfoT()
			error = saHpiIdrInfoGet(sid,rdrlist[ind][2],rdrlist[ind][6],idrinfo)
			frm.label_8.SetLabel(frm.label_8.GetLabelText() + " : " + item_clicked)
			frm.label_9.SetLabel(frm.label_9.GetLabelText() + " : " + self.GetBoolean(rdrlist[ind][4]))
			frm.label_10.SetLabel(frm.label_10.GetLabelText() + " : " + self.GetBoolean(rdrlist[ind][5]))
			frm.label_11.SetLabel(frm.label_11.GetLabelText() + " : " + str(idrinfo.UpdateCount))
			frm.label_12.SetLabel(frm.label_12.GetLabelText() + " : " + str(idrinfo.NumAreas))
			frm.label_13.SetLabel(frm.label_13.GetLabelText() + " : " + self.GetBoolean(idrinfo.ReadOnly))
			self.GetInvAreaInfo(frm ,idrinfo,rdrlist[ind][2],rdrlist[ind][6])
			break

	frm.ShowModal()

    def ShowWatchDogInfo(self, selection):
	global item_clicked
	frm = WatchDogPref.MyDialog(frame,-1,"")
	print item_clicked
	for ind in range(0,len(rdrlist)):
		if(rdrlist[ind][0] == item_clicked):
			watchdog = SaHpiWatchdogT()
			error = saHpiWatchdogTimerGet(sid,rdrlist[ind][2],rdrlist[ind][1],watchdog)
			frm.checkbox_2.SetValue(watchdog.Log)
			frm.checkbox_3.SetValue(watchdog.Running)
			frm.combo_box_5.SetSelection(watchdog.TimerUse)
			frm.combo_box_6.SetSelection(watchdog.TimerAction)
			frm.combo_box_7.SetSelection(watchdog.PretimerInterrupt)
			frm.spin_ctrl_3.SetValue(watchdog.PreTimeoutInterval)
			frm.spin_ctrl_4.SetValue(watchdog.InitialCount)
			frm.spin_ctrl_5.SetValue(watchdog.PresentCount)
			self.GetWatchDogTimerExpFlags(frm ,watchdog.TimerUseExpFlags)
			break

	frm.ShowModal()

    #def ShowIdrAreaInfo(self):	

    def ShowControlInfo(self, selection):
	global item_clicked
	frm = ControlPref.MyDialog(frame,-1,"")
	for ind in range(0,len(rdrlist)):
		if(rdrlist[ind][0] == item_clicked):
			#textbuffer = oh_init_bigtext(textbuffer)
			ctrlState = SaHpiCtrlStateT()
			error ,Mode = saHpiControlGet(sid,rdrlist[ind][2],rdrlist[ind][1],ctrlState)
			frm.label_1.SetLabel(frm.label_1.GetLabelText() + " : " + str(oh_lookup_ctrltype(rdrlist[ind][4])))
			frm.label_2.SetLabel(frm.label_2.GetLabelText() + " : " + self.GetBoolean(rdrlist[ind][8]))
			frm.label_3.SetLabel(frm.label_3.GetLabelText() + " : " + str(oh_lookup_ctrloutputtype(rdrlist[ind][5])))
			frm.label_4.SetLabel(frm.label_4.GetLabelText() + " : " + str(oh_lookup_ctrlmode(Mode)))
			frm.label_5.SetLabel(frm.label_5.GetLabelText() + " : " + self.GetBoolean(rdrlist[ind][9]))
			frm.label_6.SetLabel(frm.label_6.GetLabelText() + " : " + str(oh_lookup_ctrlstatedigital(ctrlState.StateUnion.Digital)))
			break
	frm.ShowModal()

    def GetBoolean(self, val):
	if(val == 1):
		return "True"
	if(val == 0):
		return "False"

    def selectTitle(self,item):
	if(item.find("Sensor") > 0):
	   self.menu_titles = self.SensorTitles	
	   self.menu_type="Sensor"	
	   return	
	if(item.find("Control") > 0):
	   self.menu_titles = self.ControlTitles	
	   self.menu_type="Control"	
	   return
	if(item.find("Dog") > 0):
	   self.menu_titles = self.WatchdogTitles	
	   self.menu_type="WatchDog"	
	   return
	if(item.find("Inv") > 0):
	   self.menu_titles = self.InventoryTitles	
	   self.menu_type="Inventory"	
	   return
	if(self.resources.index(item_clicked) > 0):
	   self.menu_titles = self.ResourceTitles
	   self.menu_type="Resource"	
	   return	

    def GetWatchDogTimerExpFlags(self, frm ,expFlags):

	if((expFlags & SAHPI_WATCHDOG_EXP_BIOS_FRB2) == 1):
		frm.checkbox_4.SetValue(True)
	if((expFlags & SAHPI_WATCHDOG_EXP_BIOS_POST) == 1):
		frm.checkbox_5.SetValue(True)
	if((expFlags & SAHPI_WATCHDOG_EXP_OS_LOAD) == 1):
		frm.checkbox_6.SetValue(True)
	if((expFlags & SAHPI_WATCHDOG_EXP_SMS_OS) == 1):
		frm.checkbox_7.SetValue(True)
	if((expFlags & SAHPI_WATCHDOG_EXP_OEM) == 1):
		frm.checkbox_8.SetValue(True)

    def GetInvAreaInfo(self, frm , idrinfo ,rid ,idrid):
	AreaId = SAHPI_FIRST_ENTRY
	Header = SaHpiIdrAreaHeaderT()
	AreaType = SAHPI_IDR_AREATYPE_UNSPECIFIED
	error = SA_OK
	error1 = SA_OK
	FieldId = SAHPI_FIRST_ENTRY
	Field = SaHpiIdrFieldT()
	frm.list_ctrl_1.InsertColumn(6,"Inventory Areas",format=wx.LIST_FORMAT_LEFT,width=-1)
	frm.list_ctrl_1.InsertStringItem(6,str(1))
	while error == SA_OK and AreaId != SAHPI_LAST_ENTRY:
		error , nextAreaId = saHpiIdrAreaHeaderGet(sid,rid,idrid, AreaType ,AreaId, Header)
		frm.list_ctrl_1.SetStringItem(AreaId,AreaId,str(oh_lookup_idrareatype(Header.Type)))
		frm.list_ctrl_2.InsertColumn(Header.NumFields,"Inventory Fields",format=wx.LIST_FORMAT_LEFT,width=-1)
		frm.list_ctrl_2.InsertStringItem(Header.NumFields,str(1))
		while error1 == SA_OK and FieldId != SAHPI_LAST_ENTRY:
			error1 , nextFieldId =  saHpiIdrFieldGet(sid,rid,idrid,AreaId,SAHPI_IDR_FIELDTYPE_UNSPECIFIED,FieldId,Field)
			frm.list_ctrl_2.SetStringItem(FieldId,FieldId,str(oh_lookup_idrfieldtype(Field.Type)))
			print str(oh_lookup_idrfieldtype(Field.Type)) + Field.Field.Data
			FieldId = nextFieldId
		print "-"
		AreaId = nextAreaId
		
