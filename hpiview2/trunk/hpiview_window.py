#!/usr/bin/env python

import wx
import sys

class Hpiview_Window(wx.Frame):


    def __init__(self, *args, **kwds):
    # begin wxGlade: Hpiview_Window.__init__
        kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.STAY_ON_TOP|wx.SYSTEM_MENU|wx.RESIZE_BORDER|wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        self.panel_1 = wx.Panel(self.notebook_1_pane_1, -1)
        # end wxGlade
        
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        self.SetMenuBar(self.frame_1_menubar)
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(101, "Quit", "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "Session")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.NewId(), "Clear log", "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "Edit")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.NewId(), "Discover", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.NewId(), "Load plugin", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.NewId(), "Unload plugin", "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "Action")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.NewId(), "About", "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "Help")

        # Menu Bar end
        self.frame_1_statusbar = self.CreateStatusBar(1, wx.ST_SIZEGRIP)

        # Tool Bar
        self.frame_1_toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL|wx.TB_FLAT|wx.TB_3DBUTTONS|wx.TB_TEXT|wx.TB_HORZ_LAYOUT|wx.TB_HORZ_TEXT)
        self.SetToolBar(self.frame_1_toolbar)
        self.frame_1_toolbar.AddLabelTool(wx.NewId(), "Close", wx.Bitmap("./images/close.bmp", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.frame_1_toolbar.AddLabelTool(wx.NewId(), "Discover", wx.Bitmap("./images/discover.bmp", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.frame_1_toolbar.AddLabelTool(wx.NewId(), "Subscribe events", wx.Bitmap("./images/unsubscribe events.bmp", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.frame_1_toolbar.AddLabelTool(wx.NewId(), "Get event", wx.Bitmap("./images/Get event.bmp", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")

        # Tool Bar end
        self.bitmap_button_1 = wx.BitmapButton(self, -1, wx.Bitmap("./images/Side toolbar1.bmp", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_2 = wx.BitmapButton(self, -1, wx.Bitmap("./images/Side toolbar2.bmp", wx.BITMAP_TYPE_ANY))
        self.list_box_1 = wx.ListBox(self, -1, choices=["DEFAULT"], style=wx.LB_SINGLE|wx.LB_HSCROLL)
        self.tree_ctrl_1 = wx.TreeCtrl(self.notebook_1_pane_1, -1, style=wx.TR_HAS_BUTTONS|wx.TR_NO_LINES|wx.TR_LINES_AT_ROOT|wx.TR_DEFAULT_STYLE|wx.SUNKEN_BORDER)
        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, -1, "", style=wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_LINEWRAP)
        self.bitmap_1 = wx.StaticBitmap(self, -1, wx.Bitmap("./images/Bottom toolbar1.bmp", wx.BITMAP_TYPE_ANY))
        self.button_1 = wx.Button(self, -1, "Messages", style=wx.BU_LEFT|wx.NO_BORDER)
        self.bitmap_2 = wx.StaticBitmap(self, -1, wx.Bitmap("./images/Bottom toolbar2.bmp", wx.BITMAP_TYPE_ANY))
        self.button_2 = wx.Button(self, -1, "Events", style=wx.BU_LEFT|wx.NO_BORDER)

        self.__set_properties()
        self.__do_layout()
        self.Layout()
        self.Centre()
  

    # initially clean up the window , ie having no elements
        self.list_box_1.Delete(self.list_box_1.GetSelection())
        self.tree_ctrl_1.DeleteAllItems()
        self.text_ctrl_1.Clear()
        self.notebook_1.Show(False)
    # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Hpiview_Window.__set_properties
        self.SetTitle("OpenHpi View")
        self.frame_1_statusbar.SetStatusWidths([100])
        # statusbar fields
        frame_1_statusbar_fields = ["ready"]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
            self.frame_1_toolbar.SetToolBitmapSize((32, 32))
            self.frame_1_toolbar.Realize()
            self.bitmap_button_1.SetToolTipString("Hide domain list")
            self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
            self.bitmap_button_2.SetToolTipString("Open new session")
            self.bitmap_button_2.SetSize(self.bitmap_button_2.GetBestSize())
            self.list_box_1.SetSelection(0)
            self.text_ctrl_1.SetMinSize((300, 543))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Hpiview_Window.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.bitmap_button_1, 0, wx.ALL, 5)
        sizer_2.Add(self.bitmap_button_2, 0, 0, 5)
        sizer_5.Add(sizer_2, 0, wx.ALL|wx.EXPAND, 0)
        sizer_5.Add(self.list_box_1, 4, wx.ALL|wx.EXPAND, 5)
        sizer_6.Add(self.tree_ctrl_1, 1, wx.EXPAND, 0)
        sizer_7.Add(self.text_ctrl_1, 0, 0, 0)
        self.panel_1.SetSizer(sizer_7)
        sizer_6.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.notebook_1_pane_1.SetSizer(sizer_6)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "DEFAULT")
        sizer_5.Add(self.notebook_1, 8, wx.EXPAND, 0)
        sizer_4.Add(sizer_5, 10, wx.EXPAND, 3)
        sizer_1.Add(self.bitmap_1, 0, 0, 0)
        sizer_1.Add(self.button_1, 0, 0, 0)
        sizer_1.Add(self.bitmap_2, 0, 0, 0)
        sizer_1.Add(self.button_2, 0, 0, 0)
        sizer_4.Add(sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_4)
        sizer_4.Fit(self)

        # end wxGlade
