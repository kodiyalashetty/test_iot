#!/usr/bin/env python

import wx
import sys

class Hpiview_Callbacks:

    frame = None

    def setFrame(self, mainFrame):
	global frame 
	frame = mainFrame

    def sys_activated(self, event): # wxGlade: MyFrame.<event_handler>
        #print "Event handler `sys_activated' not implemented!"
	global frame
        frame.text_ctrl_1.ChangeValue(frame.tree_ctrl_1.GetItemText(frame.tree_ctrl_1.GetSelection()))
	if(frame.text_ctrl_1.GetValue()=="SYSTEM_CHASIS #1"):
		frame.text_ctrl_1.ChangeValue("ResourceID			1\nEntity path			{SYSTEM CHASIS #1}\n					resource\n					deasserts\n					watchdog\n					control\n					annuciator\nCapabilities			power\n					reset\n					inventory_data\n					event_log\n					RDR\n					sensor\nHotSwapCapabalities	none\nResourceTag		Chasis 1\nSeverity				critical\nResource reset state	deassert")
        event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Planar Temperature Sensor"):
		frame.text_ctrl_1.ChangeValue("Type 					sensor		\n\nFRU entity				true					\nSensor type				temperature				\nEvent category			threshold				\nSensor control			false					\nSensor event control		event control not supported		\nSensor base unit			F(degree farenheit)			\nModifier base unit		unspecified unit			\nModifier use unit			none					\nMin value					40.000(F)				\nMax value					125.000(F)				\nNormal min value				90.000(F)				\nNormal max value			110.000(F)				\nNominal value				100.000(F)")
        event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Planar CPU area temperature sensor"):
		frame.text_ctrl_1.ChangeValue("Type 					sensor		\n\nFRU entity				true					\nSensor type				temperature				\nEvent category			threshold				\nSensor control			false					\nSensor event control		event control not supported		\nSensor base unit			F(degree farenheit)			\nModifier base unit		unspecified unit			\nModifier use unit			none					\nMin value					40.000(F)				\nMax value					125.000(F)				\nNormal min value				90.000(F)				\nNormal max value			110.000(F)				\nNominal value				100.000(F)")
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Digital Control"):
		frame.text_ctrl_1.ChangeValue("Type					control \n\nFRU entity				false \n\nControl type				digital \n\nWrite only control		false \n\nControl output type		led \n\nDefault mode			auto \n\nRead only mode			true \n\nControl default state		on")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Discrete Control"):
		frame.text_ctrl_1.ChangeValue("Type					control \n\nFRU entity				false \n\nControl type				discrete \n\nWrite only control		false \n\nControl output type		led \n\nDefault mode			auto \n\nRead only mode			true \n\nControl default state		1")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Analog Control"):
		frame.text_ctrl_1.ChangeValue("Type					control \n\nFRU entity				false \n\nControl type				analog \n\nWrite only control		false \n\nControl output type		audible \n\nDefault mode			auto \n\nRead only mode			true \n\nMin control state value	0 \n\nMax control state value	10 \n\nDefault control state value	0")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Stream Control"):
		frame.text_ctrl_1.ChangeValue("Type					control \n\nFRU entity				false \n\nControl type				stream \n\nWrite only control		false \n\nControl output type		led \n\nDefault mode			auto \n\nRead only mode			true \n\nControl default state	")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Text Control"):
		frame.text_ctrl_1.ChangeValue("Type					control \n\nFRU entity				false \n\nControl type				text \n\nWrite only control		false \n\nControl output type		lcd display\n\nDefault mode			auto \n\nRead only mode			true \n\nMaximum of chars per line	10 \n\nMaximum of lines			2 \n\nControl default line		0\n\nControl default state		unknown")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Oem Control"):
		frame.text_ctrl_1.ChangeValue("Type					control \n\nFRU entity				false \n\nControl type				oem type \n\nWrite only control		false \n\nControl output type		led \n\nDefault mode			auto \n\nRead only mode			true \n\nOem configuration data	\n\nControl default state		ok")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Annuciator 1"):
		frame.text_ctrl_1.ChangeValue("Type				annuciator \n\nFRU entity			false ")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Watchdog 1"):
		frame.text_ctrl_1.ChangeValue("Type				watchdog \n\nFRU entity			false ")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Simulator Inv 1"):
		frame.text_ctrl_1.ChangeValue("Type					inventory \n\nFRU entity				false \n\nInventory's persistent		false ")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="PROCESSOR #1"):
		frame.text_ctrl_1.ChangeValue("ResourceID			2\n\nEntity path			{SYSTEM CHASIS #1}{PROCESSOR #1}\n\n					resource\n\n					deasserts\n\nCapabilities			RDR\n\n					sensor\n\nHotSwapCapabalities	none\n\nResourceTag		CPU 1\n\nSeverity				major")
        event.Skip()
	if(frame.text_ctrl_1.GetValue()=="CPU temperature sensor"):
		frame.text_ctrl_1.ChangeValue("Type 					sensor		\n\nFRU entity				true					\nSensor type				temperature				\nEvent category			threshold				\nSensor control			false					\nSensor event control		event control not supported		\nSensor base unit			C(degree Celsius)			\nModifier base unit		unspecified unit			\nModifier use unit			none					\nMin value					0.000(C)		\nMax value					125.000(C) ")
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="DISC_DRIVE #1"):
		frame.text_ctrl_1.ChangeValue("ResourceID			3\n\nEntity path			{SYSTEM CHASIS #1}{DISC_DRIVE #1}\n\n					resource\n\n					deasserts\n\nCapabilities			RDR\n\n					sensor\n\nHotSwapCapabalities	none\n\nResourceTag		DASD 1 1\n\nSeverity				major")
        event.Skip()
	if(frame.text_ctrl_1.GetValue()=="DASD temperature sensor"):
		frame.text_ctrl_1.ChangeValue("Type 					sensor		\n\nFRU entity				true					\nSensor type				temperature				\nEvent category			threshold				\nSensor control			false					\nSensor event control		event control not supported		\nSensor base unit			C(degree Celsius)			\nModifier base unit		unspecified unit			\nModifier use unit			none					\nMin value					0.000(C)		\nMax value					125.000(C) ")
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="DISC_DRIVE #2"):
		frame.text_ctrl_1.ChangeValue("ResourceID			3\n\nEntity path			{SYSTEM CHASIS #1}{DISC_DRIVE #2}\n					resource\n					deasserts\n					managed_hotswap\n					watchdog\n					control\n					FRU \nCapabilities			annuciator\n					power\n 					reset\n					inventory_data\n					event_log\n 					RDR\n					sensor\n\nHotSwapCapabalities	none\n\nResourceTag		HS DASD 1 2\n\nSeverity				major\n\nResource reset state	deassert")	
        event.Skip()
	if(frame.text_ctrl_1.GetValue()=="HS DASD temperature sensor 1"):
		frame.text_ctrl_1.ChangeValue("Type 					sensor		\n\nFRU entity				true					\nSensor type				temperature				\nEvent category			threshold				\nSensor control			false					\nSensor event control		event control not supported		\nSensor base unit			F(degree farenheit)			\nModifier base unit		unspecified unit			\nModifier use unit			none					\nMin value					40.000(F)				\nMax value					125.000(F)				\nNormal min value				90.000(F)				\nNormal max value			110.000(F)				\nNominal value				100.000(F)")
        event.Skip()
	if(frame.text_ctrl_1.GetValue()=="HS DASD temperature sensor 2"):
		frame.text_ctrl_1.ChangeValue("Type 					sensor		\n\nFRU entity				true					\nSensor type				temperature				\nEvent category			threshold				\nSensor control			false					\nSensor event control		event control not supported		\nSensor base unit			F(degree farenheit)			\nModifier base unit		unspecified unit			\nModifier use unit			none					\nMin value					40.000(F)				\nMax value					125.000(F)				\nNormal min value				90.000(F)				\nNormal max value			110.000(F)				\nNominal value				100.000(F)")
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Digital Control"):
		frame.text_ctrl_1.ChangeValue("Type					control \n\nFRU entity				false \n\nControl type				digital \n\nWrite only control		false \n\nControl output type		led \n\nDefault mode			auto \n\nRead only mode			true \n\nControl default state		on")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Discrete Control"):
		frame.text_ctrl_1.ChangeValue("Type					control \n\nFRU entity				false \n\nControl type				discrete \n\nWrite only control		false \n\nControl output type		led \n\nDefault mode			auto \n\nRead only mode			true \n\nControl default state		1")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Analog Control"):
		frame.text_ctrl_1.ChangeValue("Type					control \n\nFRU entity				false \n\nControl type				analog \n\nWrite only control		false \n\nControl output type		audible \n\nDefault mode			auto \n\nRead only mode			true \n\nMin control state value	0 \n\nMax control state value	10 \n\nDefault control state value	0")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Stream Control"):
		frame.text_ctrl_1.ChangeValue("Type					control \n\nFRU entity				false \n\nControl type				stream \n\nWrite only control		false \n\nControl output type		led \n\nDefault mode			auto \n\nRead only mode			true \n\nControl default state	")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Text Control"):
		frame.text_ctrl_1.ChangeValue("Type					control \n\nFRU entity				false \n\nControl type				text \n\nWrite only control		false \n\nControl output type		lcd display\n\nDefault mode			auto \n\nRead only mode			true \n\nMaximum of chars per line	10 \n\nMaximum of lines			2 \n\nControl default line		0\n\nControl default state		unknown")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Oem Control"):
		frame.text_ctrl_1.ChangeValue("Type					control \n\nFRU entity				false \n\nControl type				oem type \n\nWrite only control		false \n\nControl output type		led \n\nDefault mode			auto \n\nRead only mode			true \n\nOem configuration data	\n\nControl default state		ok")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Annuciator 2"):
		frame.text_ctrl_1.ChangeValue("Type				annuciator \n\nFRU entity			false ")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Watchdog 2"):
		frame.text_ctrl_1.ChangeValue("Type				watchdog \n\nFRU entity			false ")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Simulator HS DASD Inv 1"):
		frame.text_ctrl_1.ChangeValue("Type					inventory \n\nFRU entity				false \n\nInventory's persistent		false ")	
	event.Skip()
	if(frame.text_ctrl_1.GetValue()=="FAN #1"):
		frame.text_ctrl_1.ChangeValue("ResourceID			5\n\nEntity path			{SYSTEM CHASIS #1}{FAN #1}\n\n					resource\n\n					deasserts\n\nCapabilities			RDR\n\n					sensor\n\nHotSwapCapabalities	none\n\nResourceTag		FAN 1\n\nSeverity				major")
        event.Skip()
	if(frame.text_ctrl_1.GetValue()=="Blower fan speed - percent of maximum RPM"):
		frame.text_ctrl_1.ChangeValue("Type 					sensor		\n\nFRU entity				true					\nSensor type				fan				\nEvent category			predictive_fail				\nSensor control			false					\nSensor event control		event control not supported		\nSensor base unit			%			\nModifier base unit		%			\nModifier use unit			none					\nMin value					0.000(%)				\nMax value					100.000(%) ")
	event.Skip()
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
        frame.list_box_1.Delete(frame.list_box_1.GetSelection())
        frame.tree_ctrl_1.DeleteAllItems()
        frame.text_ctrl_1.Clear()
        frame.notebook_1.Show(False)
 
    def Set_TreeOnNewSession(self, event): # wxGlade: MyFrame.<event_handler>
	global frame
        frame.tree_ctrl_1.AddRoot("SYSTEM_CHASIS #1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Planar Temperature Sensor",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Planar CPU area temperature sensor",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Digital Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Discrete Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Analog Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Stream Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Text Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Oem Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Annuciator 1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Watchdog 1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Simulator Inv 1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"PROCESSOR #1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"CPU temperature sensor",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"DISC_DRIVE #1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"DASD temperature sensor",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"DISC_DRIVE #2",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"HS DASD temperature sensor 1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"HS DASD temperature sensor 2",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Digital Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Discrete Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Analog Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Stream Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Text Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Oem Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Annuciator 2",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Watchdog 2",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Simulator HS DASD Inv 1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"FAN #1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Blower fan speed - percent of maximum RPM",-1,-1,None)
        event.Skip()
    
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
        frame.tree_ctrl_1.AddRoot("SYSTEM_CHASIS #1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Planar Temperature Sensor",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Planar CPU area temperature sensor",-1,-1,None)
	print "ddd"
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Digital Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Discrete Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Analog Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Stream Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Text Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Oem Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Annuciator 1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Watchdog 1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"Simulator Inv 1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"PROCESSOR #1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"CPU temperature sensor",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"DISC_DRIVE #1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"DASD temperature sensor",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"DISC_DRIVE #2",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"HS DASD temperature sensor 1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"HS DASD temperature sensor 2",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Digital Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Discrete Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Analog Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Stream Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Text Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Oem Control",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Annuciator 2",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Watchdog 2",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Simulator HS DASD Inv 1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetRootItem(),"FAN #1",-1,-1,None)
        frame.tree_ctrl_1.AppendItem(frame.tree_ctrl_1.GetLastChild(frame.tree_ctrl_1.GetRootItem()),"Blower fan speed - percent of maximum RPM",-1,-1,None)
