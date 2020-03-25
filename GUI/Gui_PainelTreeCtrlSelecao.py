# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc

###########################################################################
## Class PainelTreeCtrlSelecao
###########################################################################

class PainelTreeCtrlSelecao ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.tctrl_ArvoreSelecaoElementos = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer5.Add( self.tctrl_ArvoreSelecaoElementos, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
	
	def __del__( self ):
		pass
	

