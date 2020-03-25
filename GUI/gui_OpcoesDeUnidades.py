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
## Class GuiOpcoesUnidades
###########################################################################

class GuiOpcoesUnidades ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 485,493 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Unidades e Formatos" ), wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 4, 3, 0, 0 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Comprimento :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		cbx_UnidadeComprimentoChoices = [ u"[m] - Metro", u"[cm] - Centimetro", u"[mm] - milimetro", u"[ft] - Pes", u"[in] - Polegada" ]
		self.cbx_UnidadeComprimento = wx.ComboBox( self, wx.ID_ANY, u"[m] - Metro", wx.DefaultPosition, wx.DefaultSize, cbx_UnidadeComprimentoChoices, 0 )
		gSizer1.Add( self.cbx_UnidadeComprimento, 0, wx.ALL|wx.EXPAND, 5 )
		
		cbx_FormatoComprimentoChoices = [ u"x", u"x.x", u"x.xx", u"x.xxx", u"x.xxxx", u"x.xxxxx", u"x.xxxxxx" ]
		self.cbx_FormatoComprimento = wx.ComboBox( self, wx.ID_ANY, u"x.xx", wx.DefaultPosition, wx.DefaultSize, cbx_FormatoComprimentoChoices, 0 )
		gSizer1.Add( self.cbx_FormatoComprimento, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Força :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		cbx_UnidadeForcaChoices = [ u"[lb] - Libra", u"[klb] -Kilo Libra", u"[N] - Newton", u"[kN] - Kilo Newton", u"[kgf] - Kilo Grama Forca", u"[Tonf] - Tonelada Forca" ]
		self.cbx_UnidadeForca = wx.ComboBox( self, wx.ID_ANY, u"[kN] - Kilo Newton", wx.DefaultPosition, wx.DefaultSize, cbx_UnidadeForcaChoices, 0 )
		gSizer1.Add( self.cbx_UnidadeForca, 0, wx.ALL|wx.EXPAND, 5 )
		
		cbx_FormatoForcaChoices = [ u"x", u"x.x", u"x.xx", u"x.xxx", u"x.xxxx", u"x.xxxxx", u"x.xxxxxx" ]
		self.cbx_FormatoForca = wx.ComboBox( self, wx.ID_ANY, u"x.xx", wx.DefaultPosition, wx.DefaultSize, cbx_FormatoForcaChoices, 0 )
		gSizer1.Add( self.cbx_FormatoForca, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Ângulo :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		cbx_UnidadeAnguloChoices = [ u"[rad] - Radianos", u"[deg] - Graus", u"[grd] - Gradianos" ]
		self.cbx_UnidadeAngulo = wx.ComboBox( self, wx.ID_ANY, u"[rad] - Radianos", wx.DefaultPosition, wx.DefaultSize, cbx_UnidadeAnguloChoices, 0 )
		gSizer1.Add( self.cbx_UnidadeAngulo, 0, wx.ALL|wx.EXPAND, 5 )
		
		cbx_FormatoAnguloChoices = [ u"x", u"x.x", u"x.xx", u"x.xxx", u"x.xxxx", u"x.xxxxx", u"x.xxxxxx" ]
		self.cbx_FormatoAngulo = wx.ComboBox( self, wx.ID_ANY, u"x.xx", wx.DefaultPosition, wx.DefaultSize, cbx_FormatoAnguloChoices, 0 )
		gSizer1.Add( self.cbx_FormatoAngulo, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.AddSpacer( ( 0, 200), 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btn_ok, 0, wx.ALL, 5 )
		
		self.btn_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btn_cancel, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer6, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cbx_UnidadeComprimento.Bind( wx.EVT_COMBOBOX, self.SelecionaUnidade )
		self.cbx_FormatoComprimento.Bind( wx.EVT_COMBOBOX, self.SelecionaUnidade )
		self.cbx_UnidadeForca.Bind( wx.EVT_COMBOBOX, self.SelecionaUnidade )
		self.cbx_FormatoForca.Bind( wx.EVT_COMBOBOX, self.SelecionaUnidade )
		self.m_staticText3.Bind( wx.EVT_CHAR, self.OnClose )
		self.cbx_UnidadeAngulo.Bind( wx.EVT_COMBOBOX, self.SelecionaUnidade )
		self.cbx_FormatoAngulo.Bind( wx.EVT_COMBOBOX, self.SelecionaUnidade )
		self.btn_ok.Bind( wx.EVT_BUTTON, self.OnButton_OK )
		self.btn_cancel.Bind( wx.EVT_BUTTON, self.OnButton_Cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def SelecionaUnidade( self, event ):
		event.Skip()
	
	
	
	
	def OnClose( self, event ):
		event.Skip()
	
	
	
	def OnButton_OK( self, event ):
		event.Skip()
	
	def OnButton_Cancel( self, event ):
		event.Skip()
	

