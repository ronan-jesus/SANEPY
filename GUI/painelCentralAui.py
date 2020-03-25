# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 22:38:30 2018

@author: RONAN TEODORO
"""

import wx.lib.agw.aui as aui

class PainelCentralAui(aui.AuiManager):
    def __ini__(self):
        aui.AuiManager.__init__()
    
        self.Bind(aui.EVT_AUI_PANE_CLOSE, self.ClonePanel)
   
    def ClonePanel(self, event):
        print "FOI "*30
        