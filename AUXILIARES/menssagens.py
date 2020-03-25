# -*- coding: utf-8 -*-
"""
Created on Fri Dec 08 04:18:12 2017

@author: RONAN TEODORO
"""

import wx

def MostraMensagemErro(menssagemDeErro, titulo):
    wx.MessageBox(menssagemDeErro, titulo, wx.OK | wx.ICON_INFORMATION)