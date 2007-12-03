#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.5 on Fri Sep 28 17:23:42 2007 from /home/jayshree/frames/InventoryPref.wxg

import wx

class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog1.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        self.sizer_3_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "FRU data")
        self.sizer_2_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "Inventory info")
        self.label_8 = wx.StaticText(self.notebook_1_pane_1, -1, "Inventory name")
        self.label_9 = wx.StaticText(self.notebook_1_pane_1, -1, "FRU inventory entity")
        self.label_10 = wx.StaticText(self.notebook_1_pane_1, -1, "Inventory persistant")
        self.label_11 = wx.StaticText(self.notebook_1_pane_1, -1, "Inventory update counter")
        self.label_12 = wx.StaticText(self.notebook_1_pane_1, -1, "Number of areas")
        self.label_13 = wx.StaticText(self.notebook_1_pane_1, -1, "Read only")
        self.label_14 = wx.StaticText(self.notebook_1_pane_1, -1, "Inventory fields")
        self.button_6 = wx.Button(self.notebook_1_pane_1, -1, "View")
        self.list_ctrl_1 = wx.ListCtrl(self.notebook_1_pane_2, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.button_7 = wx.Button(self.notebook_1_pane_2, -1, "Add area")
        self.button_8 = wx.Button(self.notebook_1_pane_2, -1, "Remove area")
        self.list_ctrl_2 = wx.ListCtrl(self.notebook_1_pane_2, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.button_9 = wx.Button(self.notebook_1_pane_2, -1, "Add")
        self.button_10 = wx.Button(self.notebook_1_pane_2, -1, "Remove")
        self.button_11 = wx.Button(self.notebook_1_pane_2, -1, "Set")
        self.button_4 = wx.Button(self, -1, "OK")
        self.button_5 = wx.Button(self, -1, "Cancel")

        self.__set_properties()
        self.__do_layout()
	# Binding the OK and Cancel buttons to the methods 
	self.Bind(wx.EVT_BUTTON, self.Ok_Button_Handler, self.button_4)
	self.Bind(wx.EVT_BUTTON, self.Cancel_Button_Handler, self.button_5)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog1.__set_properties
        self.SetTitle("Inventory Preferences")
	self.SetSize((400,500))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog1.__do_layout
        grid_sizer_5 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_6 = wx.FlexGridSizer(1, 3, 0, 0)
        grid_sizer_10 = wx.FlexGridSizer(2, 1, 0, 0)
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.HORIZONTAL)
        grid_sizer_11 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_12 = wx.FlexGridSizer(3, 1, 0, 0)
        grid_sizer_13 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_14 = wx.FlexGridSizer(3, 1, 0, 0)
        grid_sizer_7 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_9 = wx.FlexGridSizer(1, 2, 0, 0)
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.VERTICAL)
        grid_sizer_8 = wx.FlexGridSizer(6, 1, 0, 0)
        grid_sizer_8.Add(self.label_8, 0, 0, 0)
        grid_sizer_8.Add(self.label_9, 0, 0, 0)
        grid_sizer_8.Add(self.label_10, 0, 0, 0)
        grid_sizer_8.Add(self.label_11, 0, 0, 0)
        grid_sizer_8.Add(self.label_12, 0, 0, 0)
        grid_sizer_8.Add(self.label_13, 0, 0, 0)
        sizer_2.Add(grid_sizer_8, 1, wx.EXPAND, 0)
        grid_sizer_7.Add(sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_9.Add(self.label_14, 0, 0, 0)
        grid_sizer_9.Add(self.button_6, 0, 0, 0)
        grid_sizer_9.AddGrowableRow(0)
        grid_sizer_9.AddGrowableCol(0)
        grid_sizer_7.Add(grid_sizer_9, 1, wx.EXPAND, 0)
        self.notebook_1_pane_1.SetSizer(grid_sizer_7)
        grid_sizer_7.AddGrowableRow(0)
        grid_sizer_7.AddGrowableCol(0)
        grid_sizer_11.Add(self.list_ctrl_1, 2, wx.EXPAND, 0)
        grid_sizer_12.Add(self.button_7, 0, 0, 0)
        grid_sizer_12.Add(self.button_8, 0, 0, 0)
        grid_sizer_13.Add(self.list_ctrl_2, 1, wx.EXPAND, 0)
        grid_sizer_14.Add(self.button_9, 0, 0, 0)
        grid_sizer_14.Add(self.button_10, 0, 0, 0)
        grid_sizer_14.Add(self.button_11, 0, 0, 0)
        grid_sizer_14.AddGrowableRow(0)
        grid_sizer_14.AddGrowableCol(0)
        grid_sizer_13.Add(grid_sizer_14, 1, wx.EXPAND, 0)
        grid_sizer_13.AddGrowableRow(0)
        grid_sizer_13.AddGrowableCol(0)
        grid_sizer_12.Add(grid_sizer_13, 1, wx.EXPAND, 0)
        grid_sizer_12.AddGrowableRow(0)
        grid_sizer_12.AddGrowableCol(0)
        grid_sizer_11.Add(grid_sizer_12, 1, wx.EXPAND, 0)
        grid_sizer_11.AddGrowableRow(0)
        grid_sizer_11.AddGrowableCol(0)
        grid_sizer_10.Add(grid_sizer_11, 1, wx.EXPAND, 0)
        grid_sizer_10.Add(sizer_3, 1, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetSizer(grid_sizer_10)
        grid_sizer_10.AddGrowableRow(0)
        grid_sizer_10.AddGrowableCol(0)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "General")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "FRU")
        grid_sizer_5.Add(self.notebook_1, 1, wx.EXPAND, 0)
        grid_sizer_6.Add((170, 20), 0, 0, 0)
        grid_sizer_6.Add(self.button_4, 0, 0, 0)
        grid_sizer_6.Add(self.button_5, 0, 0, 0)
        grid_sizer_6.AddGrowableRow(0)
        grid_sizer_6.AddGrowableCol(0)
        grid_sizer_5.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        self.SetSizer(grid_sizer_5)
        grid_sizer_5.Fit(self)
        grid_sizer_5.AddGrowableRow(0)
        grid_sizer_5.AddGrowableCol(0)
        self.Layout()
        self.Centre()
        # end wxGlade
    
    def Ok_Button_Handler(self, event): # wxGlade: MyFrame.<event_handler>
	print "destroy the child frame"	
	self.Destroy()
		
    def Cancel_Button_Handler(self, event): # wxGlade: MyFrame.<event_handler>
	self.Destroy()
# end of class MyDialog1

