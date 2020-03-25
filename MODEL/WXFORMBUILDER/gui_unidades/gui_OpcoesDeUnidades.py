# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 485,493 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Unidades e Formatos" ), wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 4, 3, 0, 0 )
		
		self.m_staticText4 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Comprimento :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		m_comboBox3Choices = [ u"[m] - Metro", u"[cm] - Centímetro", u"[mm] - milímetro", u"[ft] - Pés", u"[in] - Polegada" ]
		self.m_comboBox3 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"[m] - Metro", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
		gSizer1.Add( self.m_comboBox3, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_comboBox21Choices = [ u"x", u"x.x", u"x.xx", u"x.xxx", u"x.xxxx", u"x.xxxxx", u"x.xxxxxx" ]
		self.m_comboBox21 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"x.xx", wx.DefaultPosition, wx.DefaultSize, m_comboBox21Choices, 0 )
		gSizer1.Add( self.m_comboBox21, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Força :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		m_comboBox1Choices = [ u"[lb] - Libra", u"[klb] -Kilo Libra", u"[N] - Newton", u"[kN] - Kilo Newton", u"[kgf] - Kilo Grama Força", u"[Tonf] - Tonelada Força" ]
		self.m_comboBox1 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"[kN] - Kilo Newton", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		gSizer1.Add( self.m_comboBox1, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_comboBox2Choices = [ u"x", u"x.x", u"x.xx", u"x.xxx", u"x.xxxx", u"x.xxxxx", u"x.xxxxxx" ]
		self.m_comboBox2 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"x.xx", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		gSizer1.Add( self.m_comboBox2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Ângulo :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		m_comboBox5Choices = [ u"[rad] - Radianos", u"[deg] - Graus", u"[grd] - Gradianos" ]
		self.m_comboBox5 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"[rad] - Radianos", wx.DefaultPosition, wx.DefaultSize, m_comboBox5Choices, 0 )
		gSizer1.Add( self.m_comboBox5, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_comboBox22Choices = [ u"x", u"x.x", u"x.xx", u"x.xxx", u"x.xxxx", u"x.xxxxx", u"x.xxxxxx" ]
		self.m_comboBox22 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"x.xx", wx.DefaultPosition, wx.DefaultSize, m_comboBox22Choices, 0 )
		gSizer1.Add( self.m_comboBox22, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer1, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_comboBox3.Bind( wx.EVT_COMBOBOX, self.SelecionaUnidade )
		self.m_comboBox21.Bind( wx.EVT_COMBOBOX, self.SelecionaUnidade )
		self.m_comboBox1.Bind( wx.EVT_COMBOBOX, self.SelecionaUnidade )
		self.m_comboBox2.Bind( wx.EVT_COMBOBOX, self.SelecionaUnidade )
		self.m_comboBox5.Bind( wx.EVT_COMBOBOX, self.SelecionaUnidade )
		self.m_comboBox22.Bind( wx.EVT_COMBOBOX, self.SelecionaUnidade )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def SelecionaUnidade( self, event ):
		event.Skip()
	
	
	
	
	
	

