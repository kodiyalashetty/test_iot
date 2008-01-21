#!/usr/bin/env python


import wx
import sys, os
from openhpi import *
from threading import *
import ResourcePref
import SensorPref
import ControlPref
import InventoryPref
import WatchDogPref
import ResEventLog
import PrefEvtLogTimestamp
import FrmHelpAbout
import eventGetThread
import CustomEvent

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
	ResourceTitles = ["EventLog","Event Log Timestamp", "Event Log Clear","-","Parameters Control", "Power", "Reset","-","Preferences"]     
	SensorTitles = ["Read Sensor","Preferences"]
	ControlTitles = ["Preferences"]
	WatchdogTitles = ["Reset Watchdog","Preferences"]
	InventoryTitles = ["Preferences"]
	ParametersControl = ["Set Default Parameters","Save Parameters","Restore"]
	Power = ["On","Off","Off/On"]
	Reset = ["Cold", "Warm", "Assert", "Deassert"]
	menu_type = ""
	eventgetthread = None
	tempsensnum = None
	tempresid = None
	dlist = [""]
	
	menu_title_by_id = {}
	menu_title_by_id1 = {}
		
	def __init__(self, fr):
			global frame
			global rdrlist
			frame = fr
			frame.Bind(wx.EVT_MENU, self.Menu_Session_Quit_Handler,id=101)
			frame.Bind(wx.EVT_MENU, self.About_Handler,id=109)
			frame.Bind(wx.EVT_TOOL, self.CLose_Button_Handler,id=201)   
			frame.Bind(wx.EVT_BUTTON, self.New_Session_Handler, frame.bitmap_button_2)
			frame.Bind(wx.EVT_BUTTON, self.Hide_Domain_Handler, frame.bitmap_button_1)
			frame.Bind(wx.EVT_TOGGLEBUTTON, self.Hide_Events_Handler, frame.button_1)
			frame.Bind(wx.EVT_TOGGLEBUTTON, self.Hide_Messages_Handler, frame.button_2)
			frame.Bind(wx.EVT_TOOL, self.Subscribe_Handler, id=203)
			frame.Bind(wx.EVT_LISTBOX_DCLICK, self.Set_TreeOnNewSession, frame.list_box_1)
			frame.Bind(wx.EVT_TREE_SEL_CHANGED, self.sys_activated, frame.tree_ctrl_1)
                        frame.Bind(wx.EVT_LISTBOX_DCLICK, self.New_Session_Handler, frame.list_box_1)   
##			frame.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.sys_collapsed, frame.tree_ctrl_1)
##			frame.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.sys_expanded, frame.tree_ctrl_1)
			frame.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.RightClickCb ,frame.tree_ctrl_1)
			frame.Bind(wx.EVT_TOOL, self.Domain_Discover ,id=202)
			rdrlist=[["x",0,0,0]]
                        frame.Layout()

##			self.New_Session_Handler(None)
                        self.GetDRTInfo()

	def openHpiSession(self):
			global sid
			error, sid = saHpiSessionOpen(SAHPI_UNSPECIFIED_DOMAIN_ID, None)
                        self.errorMsg(error ,"Session Opened","OpenHpiSession")
			return 

                        
	def discover(self):
                	global dinfo,sid

                        if(sid == None):
                                self.Msg("No Sessions Active")
                                return
			error = saHpiDiscover(sid)
			self.errorMsg(error ,"Domain Discovered","discover")
                        dinfo = SaHpiDomainInfoT()
                        error = saHpiDomainInfoGet(sid, dinfo)
                        self.errorMsg(error ,"Populated the Domain Info","discover")
                	return

	def SubscribeEvents(self):
        	global sid,frame,eventgetthread,tempsensnum,tempresid,dlist
        	
                if(sid != None):
                        error = saHpiSubscribe(sid)
                        self.errorMsg(error ,"Events Subscribed","SubscribeEvents")
                        CustomEvent.CustomEvent(sid)
                        eventgetthread =  eventGetThread.EventGetThread(frame.list_ctrl_1,sid,frame,self.dlist)
                        eventgetthread.setDaemon(True)
                        eventgetthread.start()
                return  

	def unSubscribeEvents(self):
                global sid,frame
                if(sid != None):
                        error = saHpiUnsubscribe(sid)
                        self.errorMsg(error ,"Events Unsubscribed","UnSubscribeEvents")
                        frame.list_ctrl_1.DeleteAllItems()
                        frame.Layout()
                return  

##    # Traversing through the RDRs and populating them in the List.
	def polpulateResAndRdrTypeData(self):
                global frame,sid , res , rdr
                global rdrlist,tempsensnum,tempresid
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

                        res = SaHpiRptEntryT()

                        error, nexteid = saHpiRptEntryGet(sid, eid, res)
                        self.errorMsg(error ,"","populateResAndRdrTypeData")

                        if error == SA_OK:
                                rid = res.ResourceId


                                if res.ResourceCapabilities & SAHPI_CAPABILITY_RDR:
                                
                                        while error1 == SA_OK and  erid != SAHPI_LAST_ENTRY:


                                                rdr = SaHpiRdrT()

                                                error1 , nextrdrid = saHpiRdrGet(sid , rid , erid , rdr)
                                                self.errorMsg(error1 ,"","populateResAndRdrTypeData")

                                                if(firstroot):
                                                        tbuff = oh_big_textbuffer()
                                                        oh_init_bigtext(tbuff)
                                                        oh_decode_entitypath(rdr.Entity, tbuff)
                                                        Id =frame.tree_ctrl_1.AddRoot(res.ResourceTag.Data,-1,-1,None)
                                                        frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetRootItem(),rootfont)
                                                        rdrlist.append([res.ResourceTag.Data,rdr,res,tbuff.Data ,"Resource",Id])
                                                        firstroot=False
                                                        tbuff = None

                                                if(addChildsToRoot):                
                                                        tbuff = oh_big_textbuffer()
                                                        oh_init_bigtext(tbuff)
                                                        oh_decode_entitypath(rdr.Entity, tbuff)
                                                        Id = frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),res.ResourceTag.Data,-1,-1,None)
                                                        frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),rootfont)
                                                        rdrlist.append([res.ResourceTag.Data,rdr,res,tbuff.Data ,"Resource",Id])
                                                        addChildsToRoot=False
                                                        tbuff = None

                                                if(first):
                                                        if(rdr.RdrType == SAHPI_SENSOR_RDR):
                                                                Id = frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),str(oh_lookup_sensortype(rdr.RdrTypeUnion.SensorRec.Type)) + " Sensor",-1,-1,None)            
                                                                #frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
                                                                rdrlist.append([str(oh_lookup_sensortype(rdr.RdrTypeUnion.SensorRec.Type)) + " Sensor",rdr,res ,"",rdr.RecordId , Id])
								tempsensnum = rdr.RdrTypeUnion.SensorRec.Num
								tempresid = res.ResourceId
							if(rdr.RdrType == SAHPI_CTRL_RDR):
                                                                Id = frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),str(oh_lookup_ctrltype(rdr.RdrTypeUnion.CtrlRec.Type)) + " Control",-1,-1,None)           
                                                                #frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
                                                                rdrlist.append([str(oh_lookup_ctrltype(rdr.RdrTypeUnion.CtrlRec.Type))+ " Control" ,rdr,res ,"",rdr.RecordId ,Id])
                                                        if(rdr.RdrType == SAHPI_WATCHDOG_RDR):
                                                                Id = frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"WatchDog  "+ str(rdr.RdrTypeUnion.WatchdogRec.WatchdogNum),-1,-1,None)           
                                                                #frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
                                                                rdrlist.append(["WatchDog  "+str(rdr.RdrTypeUnion.WatchdogRec.WatchdogNum) ,rdr,res ,"",rdr.RecordId ,Id])
                                                        if(rdr.RdrType == SAHPI_INVENTORY_RDR):
                                                                Id = frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Simulator Inv "+str(rdr.RdrType),-1,-1,None)         
                                                                #frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
                                                                rdrlist.append(["Simulator Inv "+str(rdr.RdrType),rdr,res,"",rdr.RecordId,Id])
                                                        if(rdr.RdrType == SAHPI_ANNUNCIATOR_RDR):
                                                                Id = frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Annunciator "+ str(rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum),-1,-1,None)           
                                                                #frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
                                                                rdrlist.append(["Annunciator "+ str(rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum),rdr,res,"",rdr.RecordId,Id])

                                                if(first == False):
                                                        if(rdr.RdrType == SAHPI_SENSOR_RDR):
                                                                Id = frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),str(oh_lookup_sensortype(rdr.RdrTypeUnion.SensorRec.Type)) + " Sensor",-1,-1,None)            
                                                                #frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
                                                                rdrlist.append([str(oh_lookup_sensortype(rdr.RdrTypeUnion.SensorRec.Type))+" Sensor",rdr,res,"",rdr.RecordId ,Id])
                                                        if(rdr.RdrType == SAHPI_CTRL_RDR):                      
                                                                Id = frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),str(oh_lookup_ctrltype(rdr.RdrTypeUnion.CtrlRec.Type)) + " Control",-1,-1,None)           
                                                                #frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
                                                                rdrlist.append([str(oh_lookup_ctrltype(rdr.RdrTypeUnion.CtrlRec.Type))+" Control",rdr,res,"",rdr.RecordId,Id])
                                                        if(rdr.RdrType == SAHPI_WATCHDOG_RDR):
                                                                Id = frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"WatchDog  "+ str(rdr.RdrTypeUnion.WatchdogRec.WatchdogNum),-1,-1,None)           
                                                                #frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
                                                                rdrlist.append(["WatchDog  "+str(rdr.RdrTypeUnion.WatchdogRec.WatchdogNum),rdr,res,"",rdr.RecordId,Id])
                                                        if(rdr.RdrType == SAHPI_INVENTORY_RDR):
                                                                Id = frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Simulator Inv "+str(rdr.RdrType),-1,-1,None)         
                                                                #frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
                                                                rdrlist.append(["Simulator Inv "+str(rdr.RdrType),rdr,res,"",rdr.RecordId,Id])
                                                        if(rdr.RdrType == SAHPI_ANNUNCIATOR_RDR):
                                                                Id = frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Annunciator "+ str(rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum),-1,-1,None)           
                                                                #frame.tree_ctrl_1.SetItemFont(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),font)
                                                                rdrlist.append(["Annunciator "+ str(rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum),rdr,res,"",rdr.RecordId,Id])

                                                erid = nextrdrid

                                else:
                                        self.Msg('Resource doesn\'t have RDR')

                        first = False
                        eid = nexteid
                        if(eid > 1):
                                addChildsToRoot=True
                
                        self.Msg('rptentry[%u] tag: %s' % (res.ResourceId, res.ResourceTag.Data))
                        self.resources.append(res.ResourceTag.Data)
                                        
                return  

	def popualateRDRData(self): 
        	return


##     Displays the RDR Info when a particular RDR is clicked in the tree
	def sys_activated(self, event): # wxGlade: MyFrame.<event_handler>
                global frame,resources
                global rdrlist
                global sid
                reading = None
                evtState = None
                textbuffer = oh_big_textbuffer()
                error = SA_OK

                frame.text_ctrl_1.SetValue("")
                for ind in range(1,len(rdrlist)):

                                if(rdrlist[ind][0] == frame.tree_ctrl_1.GetItemText(frame.tree_ctrl_1.GetSelection()) and rdrlist[ind][5] == event.GetItem()):
                                        if(rdrlist[ind][4] == "Resource"):
                                                textbuffer = SaHpiTextBufferT()
                                                t1 = SaHpiTextBufferT()
                                                oh_append_textbuffer(textbuffer,"\n"+" ResourceID   \t\t\t" + str(rdrlist[ind][2].ResourceId)+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+" Entity Path  \t\t\t" + rdrlist[ind][3]+"\n")
                                                oh_decode_capabilities(rdrlist[ind][2].ResourceCapabilities,t1)
                                                frame.text_ctrl_1.SetValue(textbuffer.Data)
                                                frame.text_ctrl_1.SetValue(frame.text_ctrl_1.GetValue()+"\n"+" Capabilities \t\t\t" + t1.Data+"\n")
                                                textbuffer = SaHpiTextBufferT()
                                                oh_append_textbuffer(textbuffer,"\n"+" HotSwap Capabilities \t" + str(rdrlist[ind][2].HotSwapCapabilities)+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+" Resource Tag \t\t\t" + rdrlist[ind][2].ResourceTag.Data+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+" Severity     \t\t\t" + str(rdrlist[ind][2].ResourceSeverity)+"\n")
                                                frame.text_ctrl_1.SetValue(frame.text_ctrl_1.GetValue()+textbuffer.Data)
                                                return

                                        if(rdrlist[ind][1].RdrType==SAHPI_SENSOR_RDR):
                                                oh_init_bigtext(textbuffer)
                                                reading = SaHpiSensorReadingT()
                                                textbuffer = SaHpiTextBufferT()
                                                error ,evtState = saHpiSensorReadingGet(sid,rdrlist[ind][2].ResourceId,rdrlist[ind][1].RdrTypeUnion.SensorRec.Num,reading)
                                                self.errorMsg(error ,"Getting the Sensor Readings","sys_activated")
                                                oh_append_textbuffer(textbuffer,"\n"+" Type             \t\t"+"\tSensor \n")
                                                oh_append_textbuffer(textbuffer,"\n"+ " FRU Entity      \t\t"+self.GetBoolean(rdrlist[ind][1].IsFru)+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+" Sensor Type      \t\t"+str(oh_lookup_sensortype(rdrlist[ind][1].RdrTypeUnion.SensorRec.Type))+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+" Sensor Base Unit \t\t"+str(oh_lookup_sensorunits(rdrlist[ind][1].RdrTypeUnion.SensorRec.DataFormat.BaseUnits))+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+ " Sensor Control  \t\t"+self.GetBoolean(rdrlist[ind][1].RdrTypeUnion.SensorRec.EnableCtrl)+"\n")
                                                frame.text_ctrl_1.SetValue(textbuffer.Data)
                                                textbuffer = SaHpiTextBufferT()
                                                oh_append_textbuffer(textbuffer,"\n"+" Event Control    \t\t"+str(oh_lookup_sensoreventctrl(rdrlist[ind][1].RdrTypeUnion.SensorRec.EventCtrl))+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+" Min Value        \t\t"+str(rdrlist[ind][1].RdrTypeUnion.SensorRec.DataFormat.Range.Min.Value.SensorFloat64)+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+" Max Value        \t\t"+str(rdrlist[ind][1].RdrTypeUnion.SensorRec.DataFormat.Range.Max.Value.SensorFloat64)+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+" Nominal Value    \t\t"+str(rdrlist[ind][1].RdrTypeUnion.SensorRec.DataFormat.Range.Nominal.Value.SensorFloat64)+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+" Normal MinValue  \t\t"+str(rdrlist[ind][1].RdrTypeUnion.SensorRec.DataFormat.Range.NormalMin.Value.SensorFloat64)+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+" Normal MaxValue  \t\t"+str(rdrlist[ind][1].RdrTypeUnion.SensorRec.DataFormat.Range.NormalMax.Value.SensorFloat64)+"\n")
                                                frame.text_ctrl_1.SetValue(frame.text_ctrl_1.GetValue()+textbuffer.Data)
                                                return

                                        if(rdrlist[ind][1].RdrType==SAHPI_CTRL_RDR):
                                                ctrlState = SaHpiCtrlStateT()
                                                textbuffer = SaHpiTextBufferT()
                                                error, Mode = saHpiControlGet(sid,rdrlist[ind][2].ResourceId,rdrlist[ind][1].RdrTypeUnion.CtrlRec.Num,ctrlState)
                                                self.errorMsg(error ,"Getting the Control Readings","sys_activated")
                                                oh_append_textbuffer(textbuffer,"\n"+" Type\t\t\t\t"+"\tControl"+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+ " FRU Entity\t\t\t\t"+self.GetBoolean(rdrlist[ind][1].IsFru)+"\n")
                                                oh_append_textbuffer(textbuffer,"\n" +" Control Type\t\t\t\t"+str(oh_lookup_ctrltype(rdrlist[ind][1].RdrTypeUnion.CtrlRec.Type))+"\n")
                                                oh_append_textbuffer(textbuffer,"\n" +" Control Output Type\t\t" + str(oh_lookup_ctrloutputtype(rdrlist[ind][1].RdrTypeUnion.CtrlRec.OutputType))+"\n")
                                                oh_append_textbuffer(textbuffer,"\n" +" Control State Digital\t\t"+str(oh_lookup_ctrlstatedigital(ctrlState.StateUnion.Digital))+"\n")
                                                oh_append_textbuffer(textbuffer,"\n" +" Mode\t\t\t\t\t"+str(oh_lookup_ctrlmode(Mode))+"\n")
                                                frame.text_ctrl_1.SetValue(textbuffer.Data)
                                                self.GetControlInfo(frame.text_ctrl_1,rdrlist[ind][1].RdrTypeUnion.CtrlRec.Type,rdrlist,ind)
                                                return

                                        if(rdrlist[ind][1].RdrType==SAHPI_WATCHDOG_RDR):
                                                textbuffer = SaHpiTextBufferT()
                                                watchdogt = SaHpiWatchdogT()
                                                error = saHpiWatchdogTimerGet(sid,rdrlist[ind][2].ResourceId,rdrlist[ind][1].RdrTypeUnion.WatchdogRec.WatchdogNum,watchdogt)
                                                self.errorMsg(error ,"Getting the Watchdog Readings","sys_activated")
                                                oh_append_textbuffer(textbuffer,"\n"+ " Type            \t"+"\t\tWatchDog"+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+ " FRU Entity      \t\t"+self.GetBoolean(rdrlist[ind][1].IsFru)+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+ " Watch Dog Action    \t"+str(oh_lookup_watchdogaction(watchdogt.TimerAction))+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+ " Pre timer interrupt \t"+str(oh_lookup_watchdogpretimerinterrupt(watchdogt.PretimerInterrupt))+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+ " Timer use       \t\t"+str(oh_lookup_watchdogtimeruse(watchdogt.TimerUse))+"\n")
                                                frame.text_ctrl_1.SetValue(textbuffer.Data)
                                                return

                                        if(rdrlist[ind][1].RdrType==SAHPI_ANNUNCIATOR_RDR):
                                                textbuffer = SaHpiTextBufferT()
                                                annunt = SaHpiAnnouncementT()
                                                error = saHpiAnnunciatorGet(sid,rdrlist[ind][2].ResourceId,rdrlist[ind][1].RdrTypeUnion.AnnunciatorRec.AnnunciatorNum,SAHPI_FIRST_ENTRY,annunt)
                                                self.errorMsg(error ,"Getting the Annunciator Readings","sys_activated")
                                                oh_append_textbuffer(textbuffer,"\n"+" Type             \t"+"\t\tAnnunciator"+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+ " FRU Entity      \t\t"+self.GetBoolean(rdrlist[ind][1].IsFru)+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+" Annunciator Type     \t" + str(oh_lookup_annunciatortype(rdrlist[ind][1].RdrTypeUnion.AnnunciatorRec.AnnunciatorType))+"\n")
                                                frame.text_ctrl_1.SetValue(textbuffer.Data)
                                                return

                                        if(rdrlist[ind][1].RdrType==SAHPI_INVENTORY_RDR):
                                                textbuffer = SaHpiTextBufferT()
                                                idrinfo = SaHpiIdrInfoT()
                                                error = saHpiIdrInfoGet(sid,rdrlist[ind][2].ResourceId,rdrlist[ind][1].RdrType,idrinfo)
                                                self.errorMsg(error ,"Getting the Inventory Readings","sys_activated")
                                                oh_append_textbuffer(textbuffer,"\n"+" Type             \t\t\t"+"Inventory"+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+ " FRU Entity      \t\t"+self.GetBoolean(rdrlist[ind][1].IsFru)+"\n")
                                                oh_append_textbuffer(textbuffer,"\n"+ " Inventory's Persistent\t"+self.GetBoolean(rdrlist[ind][1].RdrTypeUnion.InventoryRec.Persistent)+"\n")                   
                                                frame.text_ctrl_1.SetValue(textbuffer.Data)
                                                return
				
	def sys_collapsed(self, event): # wxGlade: MyFrame.<event_handler>
		event.Skip()

	def sys_expanded(self, event): # wxGlade: MyFrame.<event_handler>
		event.Skip()

	def Menu_Session_Quit_Handler(self, event): # wxGlade: MyFrame.<event_handler>
                global frame,sid
                if(sid != -1):
                        self.Msg("closed")
                        saHpiSessionClose(sid)
                        frame.DestroyChildren()
                frame.Destroy()

	
	def Set_TreeOnNewSession(self, event): # wxGlade: MyFrame.<event_handler>
                global frame
                self.polpulateResAndRdrTypeData()


	def Domain_Discover(self, event): # wxGlade: MyFrame.<event_handler>
                global frame
                self.discover()

	
	def CLose_Button_Handler(self, event): # wxGlade: MyFrame.<event_handler>
                global frame
                global sid

                if(frame.list_box_1.GetSelection() == 0):
                        error = saHpiSessionClose(sid)
                        self.errorMsg(error,"Session Closed","Close_Button_Handler")
                        frame.tree_ctrl_1.DeleteAllItems()                        
                        frame.text_ctrl_1.Clear()
                        return
                else:
                        error = saHpiSessionClose(sid)
                        self.errorMsg(error,"Session Closed","Close_Button_Handler")   
                        frame.list_box_1.Delete(frame.list_box_1.GetSelection())
                        frame.tree_ctrl_1.DeleteAllItems()
                        frame.text_ctrl_1.Clear()
                        return
##                frame.notebook_1.Show(False)
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
                global dinfo

                if(frame.list_box_1.GetCount() > 0 and frame.list_box_1.GetSelection() == wx.NOT_FOUND):
                        return

                self.openHpiSession()                       
                frame.tree_ctrl_1.DeleteAllItems()
                self.polpulateResAndRdrTypeData()

                frame.notebook_1.Show(True)
                frame.Layout()

	def Hide_Events_Handler(self,event):
                global frame
                if(frame.button_1.GetValue()):
                        frame.window_1.Show(True)
                        frame.window_1.SetSashPosition(1,True);
                        frame.window_1_pane_1.Show(False)
                        frame.window_1_pane_2.Show(True)
                else:
                        frame.window_1.Show(False)
                        frame.window_1_pane_1.Show(False)
                        frame.window_1_pane_2.Show(False)
                #frame.window_1.Unsplit(frame.window_1.GetWindow1())
                frame.Layout()
	
	def Hide_Messages_Handler(self,event):
                global frame
                if(frame.button_2.GetValue()):
                        frame.window_1.Show(True)
                        frame.window_1.SetSashPosition(1005,True);                        

                        frame.window_1_pane_2.Show(False)
                        frame.window_1_pane_1.Show(True)
                else:
                        frame.window_1.Show(False)
                        frame.window_1_pane_2.Show(False)
                        frame.window_1_pane_1.Show(False)
                #frame.window_1.Unsplit(frame.window_1.GetWindow2())
                frame.Layout()

	def RightClickCb( self, event ):

                global frame,item_clicked,resources

                # record what was clicked
                
                item_clicked = frame.tree_ctrl_1.GetItemText(event.GetItem())

                self.menu_titles={}
                self.menu_title_by_id={}

                self.selectTitle(item_clicked)
                
                for title in self.menu_titles:
                  self.menu_title_by_id[ wx.NewId() ] = title

                ### 2. Launcher creates wxMenu. ###
                menu = wx.Menu()
                for (id,title) in self.menu_title_by_id.items():
                        ### 3. Launcher packs menu with Append. ###
                        if(title == "-"):
                          menu.AppendSeparator()    
                        else:   
                                if(title == "Parameters Control"):
                                        self.menu_title_by_id1={}
                                        for title1 in self.ParametersControl:
                                          self.menu_title_by_id1[ wx.NewId() ] = title1
                                        menu1 = wx.Menu()
                                        for (id,title1) in self.menu_title_by_id1.items():
                                             menu1.Append( id, title1 )
                                        menu.AppendMenu( id, title , menu1 )

                                else:
                                        if(title == "Power"):
                                                self.menu_title_by_id1={}
                                                for title1 in self.Power:
                                                    self.menu_title_by_id1[ wx.NewId() ] = title1
                                                menu1 = wx.Menu()
                                                for (id,title1) in self.menu_title_by_id1.items():
                                                    menu1.Append( id, title1 )
                                                menu.AppendMenu( id, title , menu1 )

                                        else:
                                                if(title == "Reset"):
                                                        self.menu_title_by_id1={}
                                                        for title1 in self.Reset:
                                                          self.menu_title_by_id1[ wx.NewId() ] = title1
                                                        menu1 = wx.Menu()
                                                        for (id,title1) in self.menu_title_by_id1.items():
                                                          menu1.Append( id, title1 )
                                                        menu.AppendMenu( id, title , menu1 )
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
		self.Msg('Perform "%(operation)s" on "%(target)s."' % vars())

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

##     Displays preferences of the selected resource
	def ShowResInfo(self, selection):
                global item_clicked
                frm = ResourcePref.MyDialog(frame,-1,"")
                for ind in range(1,len(rdrlist)):
                         if(rdrlist[ind][0] == item_clicked):
                                frm.label_1.SetLabel(frm.label_1.GetLabel() + " :\t" + str(rdrlist[ind][2].ResourceInfo.AuxFirmwareRev))
                                frm.label_2.SetLabel(frm.label_2.GetLabel() + " :\t" + str(rdrlist[ind][2].ResourceInfo.FirmwareMinorRev))
                                frm.label_3.SetLabel(frm.label_3.GetLabel() + " :\t" + str(rdrlist[ind][2].ResourceInfo.FirmwareMajorRev))
                                frm.label_4.SetLabel(frm.label_4.GetLabel() + "\t\t\t\t:\t" + str(rdrlist[ind][2].ResourceInfo.ProductId))
                                frm.label_5.SetLabel(frm.label_5.GetLabel() + "\t\t:\t" + str(rdrlist[ind][2].ResourceInfo.ManufacturerId))
                                frm.label_6.SetLabel(frm.label_6.GetLabel() + "\t\t:\t" + str(rdrlist[ind][2].ResourceInfo.DeviceSupport))
                                frm.label_7.SetLabel(frm.label_7.GetLabel() + "\t\t:\t" + str(rdrlist[ind][2].ResourceInfo.SpecificVer))
                                frm.label_8.SetLabel(frm.label_8.GetLabel() + "\t\t:\t" + str(rdrlist[ind][2].ResourceInfo.ResourceRev))
                                break
                frm.ShowModal()

##     Displays Event log information for the selected resource
	def ShowEvtLog(self, selection):
                global item_clicked
                frm = ResEventLog.MyDialog(frame,-1,"")
                for ind in range(1,len(rdrlist)):
                         if(rdrlist[ind][0] == item_clicked):
                                info = SaHpiEventLogInfoT()
                                error = saHpiEventLogInfoGet(sid,rdrlist[ind][2].ResourceId,info)
                                self.errorMsg(error ,"Getting the EL","ShowEvtLog")
                                frm.label_1.SetLabel(frm.label_1.GetLabel() + "\t\t:\t" + str(info.Entries))
                                frm.label_2.SetLabel(frm.label_2.GetLabel() + "\t\t\t:\t" + str(info.Size))
                                frm.label_3.SetLabel(frm.label_3.GetLabel() + "\t:\t" + str(info.UserEventMaxSize))
                                b = SaHpiTextBufferT()
                                oh_decode_time(info.UpdateTimestamp,b)
                                frm.label_4.SetLabel(frm.label_4.GetLabel() + "\t:\t" + b.Data)
                                b = SaHpiTextBufferT()
                                oh_decode_time(info.CurrentTime,b)
                                frm.label_5.SetLabel(frm.label_5.GetLabel() + "\t:\t" + b.Data)
                                frm.label_6.SetLabel(frm.label_6.GetLabel() + "\t\t:\t" + self.GetBoolean(info.OverflowFlag))
                                frm.label_7.SetLabel(frm.label_7.GetLabel() + "\t\t:\t" + self.GetBoolean(info.OverflowResetable))
                                if(info.OverflowAction == 0):
                                        frm.label_8.SetLabel(frm.label_8.GetLabel() + ":\t" + "Drop")
                                else:
                                        frm.label_8.SetLabel(frm.label_8.GetLabel() + ":\t" + "Overwrite")
                                frm.checkbox_1.SetValue(info.Enabled)
				break
                frm.ShowModal()

##     Displays preferences of the Sensor RDR
	def ShowSensorInfo(self, selection):
                global item_clicked
                frm = SensorPref.MyDialog(frame,-1,"")
                for ind in range(1,len(rdrlist)):
                        if(rdrlist[ind][0] == item_clicked):
                                reading = SaHpiSensorReadingT()
                                error ,evtState = saHpiSensorReadingGet(sid,rdrlist[ind][2].ResourceId,rdrlist[ind][1].RdrTypeUnion.SensorRec.Num,reading)
                                self.errorMsg(error ,"Getting the sensor readings", "ShowSensorInfo")
                                frm.label_1.SetLabel(frm.label_1.GetLabel() + "\t\t:\t" + "Sensor")
                                frm.label_2.SetLabel(frm.label_2.GetLabel() + "\t\t:\t" + str(oh_lookup_sensortype(rdrlist[ind][1].RdrTypeUnion.SensorRec.Type)))
                                if(rdrlist[ind][1].RdrTypeUnion.SensorRec.EnableCtrl==0):
                                        frm.label_3.SetLabel(frm.label_3.GetLabel() + "\t:\t" + "False")
                                        frm.label_11.SetLabel(frm.label_11.GetLabel() + "\t:\t" + "False")
                                else:
                                        frm.label_3.SetLabel(frm.label_3.GetLabel() + "\t:\t" + "True")
                                        frm.label_11.SetLabel(frm.label_11.GetLabel() + "\t:\t" + "True")
                                frm.label_4.SetLabel(frm.label_4.GetLabel() + "\t:\t" + str(oh_lookup_sensorunits(rdrlist[ind][1].RdrTypeUnion.SensorRec.DataFormat.BaseUnits)))
                                frm.label_5.SetLabel(frm.label_5.GetLabel() + "\t\t\t:\t" + str(rdrlist[ind][1].RdrTypeUnion.SensorRec.DataFormat.Range.Min.Value.SensorFloat64))
                                frm.label_6.SetLabel(frm.label_6.GetLabel() + "\t\t:\t" + str(rdrlist[ind][1].RdrTypeUnion.SensorRec.DataFormat.Range.Max.Value.SensorFloat64))
                                frm.label_7.SetLabel(frm.label_7.GetLabel() + "\t:\t" + str(rdrlist[ind][1].RdrTypeUnion.SensorRec.DataFormat.Range.NormalMin.Value.SensorFloat64))
                                frm.label_8.SetLabel(frm.label_8.GetLabel() + "\t:\t" + str(rdrlist[ind][1].RdrTypeUnion.SensorRec.DataFormat.Range.NormalMax.Value.SensorFloat64))
                                frm.label_9.SetLabel(frm.label_9.GetLabel() + "\t\t:\t" + str(rdrlist[ind][1].RdrTypeUnion.SensorRec.DataFormat.Range.Nominal.Value.SensorFloat64))
                                frm.label_10.SetLabel(frm.label_10.GetLabel() + "\t\t:\t" + str(oh_lookup_eventcategory(rdrlist[ind][1].RdrTypeUnion.SensorRec.Category)))
                                frm.label_12.SetLabel(frm.label_12.GetLabel() + "\t:\t" + str(rdrlist[ind][1].RdrTypeUnion.SensorRec.Events))
                                sensorthresholds = SaHpiSensorThresholdsT()
                                error = saHpiSensorThresholdsGet(sid,rdrlist[ind][2].ResourceId,rdrlist[ind][1].RdrTypeUnion.SensorRec.Num,sensorthresholds)
                                self.errorMsg(error ,"Getting the sensor thresholds","ShowSensorInfo")
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
                
##     Displays preferences of the Inventory RDR
	def ShowInvInfo(self, selection):
                global item_clicked
                frm = InventoryPref.MyDialog(frame,-1,"")
                for ind in range(1,len(rdrlist)):
                        if(rdrlist[ind][0] == item_clicked):
                                idrinfo = SaHpiIdrInfoT()
                                error = saHpiIdrInfoGet(sid,rdrlist[ind][2].ResourceId,rdrlist[ind][1].RdrTypeUnion.InventoryRec.IdrId,idrinfo)
                                self.errorMsg(error ,"Getting the Inventory readings","ShowInvInfo")
                                frm.label_8.SetLabel(frm.label_8.GetLabel() + "\t\t\t:\t " + item_clicked)
                                frm.label_9.SetLabel(frm.label_9.GetLabel() + "\t\t:\t " + self.GetBoolean(rdrlist[ind][1].IsFru))
                                frm.label_10.SetLabel(frm.label_10.GetLabel() + "\t\t:\t " + self.GetBoolean(rdrlist[ind][1].RdrTypeUnion.InventoryRec.Persistent))
                                frm.label_11.SetLabel(frm.label_11.GetLabel() + "\t:\t " + str(idrinfo.UpdateCount))
                                frm.label_12.SetLabel(frm.label_12.GetLabel() + "\t\t\t:\t " + str(idrinfo.NumAreas))
                                frm.label_13.SetLabel(frm.label_13.GetLabel() + "\t\t\t\t:\t " + self.GetBoolean(idrinfo.ReadOnly))
                                self.GetInvAreaInfo(frm ,idrinfo,rdrlist[ind][2].ResourceId,rdrlist[ind][1].RdrTypeUnion.InventoryRec.IdrId)
                                break

                frm.ShowModal()

##     Displays preferences of the Watchdog RDR
	def ShowWatchDogInfo(self, selection):
                global item_clicked
                frm = WatchDogPref.MyDialog(frame,-1,"")
                for ind in range(1,len(rdrlist)):
                        if(rdrlist[ind][0] == item_clicked):
                                watchdog = SaHpiWatchdogT()
                                error = saHpiWatchdogTimerGet(sid,rdrlist[ind][2].ResourceId,rdrlist[ind][1].RdrTypeUnion.WatchdogRec.WatchdogNum,watchdog)
                                self.errorMsg(error ,"Getting the Watchdog readings","ShowWatchDogInfo")
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

##     Displays preferences of the Control RDR
	def ShowControlInfo(self, selection):
                global item_clicked
                frm = ControlPref.MyDialog(frame,-1,"")
                for ind in range(1,len(rdrlist)):
                        if(rdrlist[ind][0] == item_clicked):
                                ctrlState = SaHpiCtrlStateT()
                                error, Mode = saHpiControlGet(sid,rdrlist[ind][2].ResourceId,rdrlist[ind][1].RdrTypeUnion.CtrlRec.Num,ctrlState)
                                self.errorMsg(error ,"Getting the Control readings","ShowControlInfo")
                                self.GetControlInfo(frm,rdrlist[ind][1].RdrTypeUnion.CtrlRec.Type,rdrlist,ind)
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
                if(self.resources.index(item)>0):
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
                frm.list_ctrl_1.InsertColumn(6,"Inventory Areas",format=wx.LIST_FORMAT_LEFT,width=100)
                frm.list_ctrl_1.InsertStringItem(6,str(1))
                while error == SA_OK and AreaId != SAHPI_LAST_ENTRY:
                        error , nextAreaId = saHpiIdrAreaHeaderGet(sid,rid,idrid, AreaType ,AreaId, Header)
                        self.errorMsg(error ,"Getting the Inventory Area info","GetInvAreaInfo")
                        frm.list_ctrl_1.SetStringItem(AreaId,AreaId,str(oh_lookup_idrareatype(Header.Type)))
                        frm.list_ctrl_2.InsertColumn(Header.NumFields,"Inventory Fields",format=wx.LIST_FORMAT_LEFT,width=100)
                        frm.list_ctrl_2.InsertStringItem(Header.NumFields,str(1))
                        while error1 == SA_OK and FieldId != SAHPI_LAST_ENTRY:
                                error1 , nextFieldId =  saHpiIdrFieldGet(sid,rid,idrid,AreaId,SAHPI_IDR_FIELDTYPE_UNSPECIFIED,FieldId,Field)
                                self.errorMsg(error1 ,"Getting the Inventory field info","GetInvAreaInfo")
                                frm.list_ctrl_2.SetStringItem(FieldId,FieldId,str(oh_lookup_idrfieldtype(Field.Type)))
                                FieldId = nextFieldId
                        AreaId = nextAreaId

	def Subscribe_Handler(self , event):
              global frame
              if(frame.frame_2_toolbar.FindById(203).IsToggled()):
                        self.SubscribeEvents()
              else:
                        self.unSubscribeEvents()

	def About_Handler(self, event):
                frm = FrmHelpAbout.frmHelpAbout(frame,-1,"")        
                frm.ShowModal()

	def GetControlInfo(self, frm, ctrltype, rdrlist, ind):
                ctrlState = SaHpiCtrlStateT()
                error, Mode = saHpiControlGet(sid,rdrlist[ind][2].ResourceId,rdrlist[ind][1].RdrTypeUnion.CtrlRec.Num,ctrlState)

                if ( isinstance(frm ,wx.Dialog)):
                        frm.label_1.SetLabel(frm.label_1.GetLabel() + "\t\t\t\t" + str(oh_lookup_ctrltype(rdrlist[ind][1].RdrTypeUnion.CtrlRec.Type)))
                        frm.label_2.SetLabel(frm.label_2.GetLabel() + "\t\t\t" + self.GetBoolean(rdrlist[ind][1].RdrTypeUnion.CtrlRec.WriteOnly))
                        frm.label_3.SetLabel(frm.label_3.GetLabel() + "\t\t\t" + str(oh_lookup_ctrloutputtype(rdrlist[ind][1].RdrTypeUnion.CtrlRec.OutputType)))
                        frm.label_4.SetLabel(frm.label_4.GetLabel() + "\t\t\t\t" + str(oh_lookup_ctrlmode(Mode)))
                        frm.label_5.SetLabel(frm.label_5.GetLabel() + "\t\t" + self.GetBoolean(rdrlist[ind][1].RdrTypeUnion.CtrlRec.DefaultMode.ReadOnly))

                if(isinstance(frm ,wx.Dialog)):
                        if(ctrltype == 0 ):
                                frm.label_6.SetLabel(frm.label_6.GetLabel() + "\t\t" + str(oh_lookup_ctrlstatedigital(ctrlState.StateUnion.Digital)))

                        if(ctrltype == 1 ):
                                frm.label_6.SetLabel(frm.label_6.GetLabel() + "\t\t" + str(ctrlState.StateUnion.Discrete))

                        if(ctrltype == 2 ):
                                frm.label_6.SetLabel(frm.label_6.GetLabel() + "\t\t" + str(ctrlState.StateUnion.Analog))
                                frm.label_21.SetLabel("Min Control State Value\t\t" + str(rdrlist[ind][1].RdrTypeUnion.CtrlRec.TypeUnion.Analog.Min))
                                frm.label_22.SetLabel("Max Control State Value\t\t" + str(rdrlist[ind][1].RdrTypeUnion.CtrlRec.TypeUnion.Analog.Max))

                        if(ctrltype == 3 ):
                                frm.label_6.SetLabel(frm.label_6.GetLabel() + "\t\t" + str(ctrlState.StateUnion.Stream.Stream))

                        if(ctrltype == 4 ):
                                frm.label_6.SetLabel(frm.label_6.GetLabel() + "\t\t" + ctrlState.StateUnion.Text.Text.Data)
                                frm.label_21.SetLabel("Max Chars per line\t\t\t" + str(rdrlist[ind][1].RdrTypeUnion.CtrlRec.TypeUnion.Text.MaxChars))
                                frm.label_22.SetLabel("Max number of lines\t\t" + str(rdrlist[ind][1].RdrTypeUnion.CtrlRec.TypeUnion.Text.MaxLines))
                                frm.label_23.SetLabel("Control default line\t\t\t" + str(ctrlState.StateUnion.Text.Line))

                        if(ctrltype == 192 ):
                                frm.label_6.SetLabel(frm.label_6.GetLabel() + "\t\t" + str(ctrlState.StateUnion.Oem.Body))
                                frm.label_21.SetLabel("Control Manufacturer Id\t\t" + str(ctrlState.StateUnion.Oem.MId))
                                frm.label_22.SetLabel("Oem Configuration data\t\t" + str(rdrlist[ind][1].RdrTypeUnion.CtrlRec.TypeUnion.Oem.ConfigData))

                        return

                if(isinstance(frm ,wx.TextCtrl)):

                        if(ctrltype == 0):
                                frm.SetValue(frm.GetValue() + "\n Control default state\t\t" + str(oh_lookup_ctrlstatedigital(ctrlState.StateUnion.Digital))+ "\n")

                        if(ctrltype == 1):
                                frm.SetValue(frm.GetValue()+ "\n Control default state\t\t" + str(ctrlState.StateUnion.Discrete)+ "\n")

                        if(ctrltype == 2):
                                frm.SetValue(frm.GetValue()+"\n Control default state\t\t" + str(ctrlState.StateUnion.Analog)+ "\n")
                                frm.SetValue(frm.GetValue()+"\n Min Control State Value\t\t" + str(rdrlist[ind][1].RdrTypeUnion.CtrlRec.TypeUnion.Analog.Min)+ "\n")
                                frm.SetValue(frm.GetValue()+"\n Max Control State Value\t" + str(rdrlist[ind][1].RdrTypeUnion.CtrlRec.TypeUnion.Analog.Max)+ "\n")

                        if(ctrltype == 3):
                                frm.SetValue(frm.GetValue()+ "\n Control default state\t\t" + str(ctrlState.StateUnion.Stream.Stream)+ "\n")

                        if(ctrltype == 4):
                                frm.SetValue(frm.GetValue()+"\n Control default state\t\t" + ctrlState.StateUnion.Text.Text.Data + "\n")
                                frm.SetValue(frm.GetValue()+"\n Max Chars per line\t\t\t" + str(rdrlist[ind][1].RdrTypeUnion.CtrlRec.TypeUnion.Text.MaxChars)+ "\n")
                                frm.SetValue(frm.GetValue()+"\n Max number of lines\t\t" + str(rdrlist[ind][1].RdrTypeUnion.CtrlRec.TypeUnion.Text.MaxLines)+ "\n")
                                frm.SetValue(frm.GetValue()+"\n Control default line\t\t\t" + str(ctrlState.StateUnion.Text.Line)+ "\n")

                        if(ctrltype == 5):
                                frm.SetValue(frm.GetValue()+"\n Control default state\t\t" + str(ctrlState.StateUnion.Oem.Body)+ "\n")
                                frm.SetValue(frm.GetValue()+"\n Control Manufacturer Id\t\t" + str (ctrlState.StateUnion.Oem.MId)+ "\n")
                                frm.SetValue(frm.GetValue()+"\n Oem Configuration data\t\t" + str (rdrlist[ind][1].RdrTypeUnion.CtrlRec.TypeUnion.Oem.ConfigData)+ "\n")
                        return 
		

	def GetEventInfo(self,rdrlist,rdrtype,rdrclicked):
                global frame,sid
                res=None
                rdr=None
                for ind in range(1,len(rdrlist)):
                        if(rdrlist[ind][0] == rdrclicked):
                                rdr = rdrlist[ind][1]
                                res = rdrlist[ind][2]
                                event = SaHpiEventT()
                                error = saHpiEventGet(sid, SAHPI_TIMEOUT_IMMEDIATE, event, rdr, res)
                                textbuffer = SaHpiTextBufferT()
                                oh_append_textbuffer(textbuffer," Type : " + str(event.EventType))
                                frame.text_ctrl_1.SetValue(frame.text_ctrl_1.GetValue()+textbuffer.Data)
                                break

        def Msg(self , message):
                global frame
                frame.text_ctrl_2.SetValue(frame.text_ctrl_2.GetValue()+"\r"+message)

        def errorMsg(self , err , msg , methodname):
                if err != SA_OK:
                        self.Msg (oh_lookup_error(err))
                        print "Error : " + methodname + " : " + oh_lookup_error(err)
                else:
                        if(msg != ""):
                                self.Msg(msg)

        def StatusMsg(self , message):
                global frame
                frame.statusbar.SetStatusText(message)
        

        def GetDRTInfo(self):
                global dlist,frame

                error, sid = saHpiSessionOpen(SAHPI_UNSPECIFIED_DOMAIN_ID, None)
                if error == SA_OK:
                        eid = SAHPI_FIRST_ENTRY
                        
                        error1 = SA_OK
                        while error1 == SA_OK and eid != SAHPI_LAST_ENTRY:

                                drtentry = SaHpiDrtEntryT()

                                error1, nextentry = saHpiDrtEntryGet(sid, eid, drtentry)
                                domaininfo = SaHpiDomainInfoT()
                                error2 = saHpiDomainInfoGet(sid, domaininfo)
                                self.errorMsg(error ,"Domain Discovered","GetDRTInfo")
                                self.dlist.append(domaininfo)
                                frame.list_box_1.Insert(domaininfo.DomainTag.Data,frame.list_box_1.GetCount(),None)
                                        
                                eid = nextentry
                else:
                        print "No available domain"
                error = saHpiSessionClose(sid)
