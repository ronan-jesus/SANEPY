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
## Class UI_JanelaOpcoesVisualizacoes
###########################################################################

class UI_JanelaOpcoesVisualizacoes ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Opcoes de Visualizacao", pos = wx.DefaultPosition, size = wx.Size( 674,404 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 2, 3, 0, 0 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"NÓS" ), wx.VERTICAL )
		
		sbSizer1.SetMinSize( wx.Size( 200,250 ) ) 
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.chb_mostrar_no = wx.CheckBox( self, wx.ID_ANY, u"Mostrar NOS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chb_mostrar_no.SetValue(True) 
		bSizer9.Add( self.chb_mostrar_no, 0, wx.ALL, 5 )
		
		self.chb_mostrar_numeracao_nos = wx.CheckBox( self, wx.ID_ANY, u"Mostrar Numeração", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chb_mostrar_numeracao_nos.SetValue(True) 
		bSizer9.Add( self.chb_mostrar_numeracao_nos, 0, wx.ALL, 5 )
		
		self.chb_mostrar_vinculos = wx.CheckBox( self, wx.ID_ANY, u"Mostrar Vinculação", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chb_mostrar_vinculos.SetValue(True) 
		bSizer9.Add( self.chb_mostrar_vinculos, 0, wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Tamanho dos NÓS (pt)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer10.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.txt_tamanhoNO = wx.TextCtrl( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer10.Add( self.txt_tamanhoNO, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer10, 0, 0, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Tamanho dos Vinculos (m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		bSizer14.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		self.txt_tamanhoVinculos = wx.TextCtrl( self, wx.ID_ANY, u"0.5", wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer14.Add( self.txt_tamanhoVinculos, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		bSizer71.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer71, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( sbSizer1, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"BARRAS" ), wx.VERTICAL )
		
		sbSizer2.SetMinSize( wx.Size( 200,250 ) ) 
		bSizer81 = wx.BoxSizer( wx.VERTICAL )
		
		self.chb_mostrar_barra = wx.CheckBox( self, wx.ID_ANY, u"Mostrar Barras", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chb_mostrar_barra.SetValue(True) 
		bSizer81.Add( self.chb_mostrar_barra, 0, wx.ALL, 5 )
		
		self.chb_mostrar_numeracao_barras = wx.CheckBox( self, wx.ID_ANY, u"Mostrar Numeração", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chb_mostrar_numeracao_barras.SetValue(True) 
		bSizer81.Add( self.chb_mostrar_numeracao_barras, 0, wx.ALL, 5 )
		
		self.chb_mostrar_eixos_barra = wx.CheckBox( self, wx.ID_ANY, u"Mostrar Eixos XYZ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chb_mostrar_eixos_barra.SetValue(True) 
		bSizer81.Add( self.chb_mostrar_eixos_barra, 0, wx.ALL, 5 )
		
		self.chb_mostrar_secoes_barra = wx.CheckBox( self, wx.ID_ANY, u"Mostrar Secoes das Barras", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chb_mostrar_secoes_barra.SetValue(True) 
		bSizer81.Add( self.chb_mostrar_secoes_barra, 0, wx.ALL, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Tamanho dos Eixos (m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer91.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.txt_tamanhoEixosBarra = wx.TextCtrl( self, wx.ID_ANY, u"0.1", wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer91.Add( self.txt_tamanhoEixosBarra, 0, wx.ALL, 5 )
		
		
		bSizer81.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		
		sbSizer2.Add( bSizer81, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( sbSizer2, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer101 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"ÁREA DE DESENHO" ), wx.VERTICAL )
		
		sbSizer3.SetMinSize( wx.Size( 200,-1 ) ) 
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.chb_mostrar_eixos_globais = wx.CheckBox( self, wx.ID_ANY, u"Mostrar Eixos Globais", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chb_mostrar_eixos_globais.SetValue(True) 
		bSizer11.Add( self.chb_mostrar_eixos_globais, 0, wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Tamanho dos Eixos (m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer13.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.txt_tamanhoEixosGlobais = wx.TextCtrl( self, wx.ID_ANY, u"1.0", wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer13.Add( self.txt_tamanhoEixosGlobais, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer13, 0, wx.EXPAND, 5 )
		
		bSizer131 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txtPosicaoEixosGlobais = wx.StaticText( self, wx.ID_ANY, u"Eixos Globais XYZ (m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtPosicaoEixosGlobais.Wrap( -1 )
		bSizer131.Add( self.txtPosicaoEixosGlobais, 0, wx.ALL, 5 )
		
		self.txtPosGlobalX = wx.TextCtrl( self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
		bSizer131.Add( self.txtPosGlobalX, 0, wx.TOP|wx.BOTTOM, 5 )
		
		self.txtPosGlobalY = wx.TextCtrl( self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
		bSizer131.Add( self.txtPosGlobalY, 0, wx.TOP|wx.BOTTOM, 5 )
		
		self.txtPosGlobalZ = wx.TextCtrl( self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
		bSizer131.Add( self.txtPosGlobalZ, 0, wx.TOP|wx.BOTTOM, 5 )
		
		
		bSizer11.Add( bSizer131, 0, 0, 5 )
		
		
		sbSizer3.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		bSizer101.Add( sbSizer3, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer101, 1, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"CARGAS" ), wx.VERTICAL )
		
		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.chb_mostrarCargasDistribuidas = wx.CheckBox( self, wx.ID_ANY, u"Mostrar Cargas Distribuídas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chb_mostrarCargasDistribuidas.SetValue(True) 
		bSizer161.Add( self.chb_mostrarCargasDistribuidas, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( bSizer161, 1, wx.EXPAND, 5 )
		
		bSizer1611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.chb_mostrarCargasConcentradas = wx.CheckBox( self, wx.ID_ANY, u"Mostrar Cargas Concentradas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chb_mostrarCargasConcentradas.SetValue(True) 
		bSizer1611.Add( self.chb_mostrarCargasConcentradas, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( bSizer1611, 1, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Tamanho Cargas Distri (m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer16.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.txt_tam_carga_distribuidas = wx.TextCtrl( self, wx.ID_ANY, u"1.0", wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer16.Add( self.txt_tam_carga_distribuidas, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		bSizer162 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Tamanho Cargas Conc (m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		bSizer162.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		self.txt_tam_carga_concentradas = wx.TextCtrl( self, wx.ID_ANY, u"1.0", wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer162.Add( self.txt_tam_carga_concentradas, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( bSizer162, 1, wx.EXPAND, 5 )
		
		
		bSizer15.Add( sbSizer4, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		dlg_button = wx.StdDialogButtonSizer()
		self.dlg_buttonOK = wx.Button( self, wx.ID_OK )
		dlg_button.AddButton( self.dlg_buttonOK )
		self.dlg_buttonCancel = wx.Button( self, wx.ID_CANCEL )
		dlg_button.AddButton( self.dlg_buttonCancel )
		dlg_button.Realize();
		
		bSizer5.Add( dlg_button, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.chb_mostrar_no.Bind( wx.EVT_CHECKBOX, self.HabilitaVisualizacaoNos )
		self.chb_mostrar_numeracao_nos.Bind( wx.EVT_CHECKBOX, self.HabilitaVisualizacaoNumercaoNos )
		self.chb_mostrar_vinculos.Bind( wx.EVT_CHECKBOX, self.HabilitaVisualizacaoVinculos )
		self.chb_mostrar_barra.Bind( wx.EVT_CHECKBOX, self.HabilitaVisualizacaoBarras )
		self.chb_mostrar_numeracao_barras.Bind( wx.EVT_CHECKBOX, self.HabilitaVisualizacaoNumercaoBarras )
		self.chb_mostrar_eixos_barra.Bind( wx.EVT_CHECKBOX, self.HabilitaVisualizacaoEixosBarras )
		self.chb_mostrar_secoes_barra.Bind( wx.EVT_CHECKBOX, self.HabilitaVisualizacaoSecoesBarras )
		self.chb_mostrar_eixos_globais.Bind( wx.EVT_CHECKBOX, self.HabilitaVisualizacaoEixosGlobais )
		self.chb_mostrarCargasDistribuidas.Bind( wx.EVT_CHECKBOX, self.HabilitaVisualizacaoCargasDistribuidas )
		self.chb_mostrarCargasConcentradas.Bind( wx.EVT_CHECKBOX, self.HabilitaVisualizacaoCargasConcentradas )
		self.dlg_buttonCancel.Bind( wx.EVT_BUTTON, self.OnClickButtonCancel )
		self.dlg_buttonOK.Bind( wx.EVT_BUTTON, self.OnClickButtonOK )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def HabilitaVisualizacaoNos( self, event ):
		event.Skip()
	
	def HabilitaVisualizacaoNumercaoNos( self, event ):
		event.Skip()
	
	def HabilitaVisualizacaoVinculos( self, event ):
		event.Skip()
	
	def HabilitaVisualizacaoBarras( self, event ):
		event.Skip()
	
	def HabilitaVisualizacaoNumercaoBarras( self, event ):
		event.Skip()
	
	def HabilitaVisualizacaoEixosBarras( self, event ):
		event.Skip()
	
	def HabilitaVisualizacaoSecoesBarras( self, event ):
		event.Skip()
	
	def HabilitaVisualizacaoEixosGlobais( self, event ):
		event.Skip()
	
	def HabilitaVisualizacaoCargasDistribuidas( self, event ):
		event.Skip()
	
	def HabilitaVisualizacaoCargasConcentradas( self, event ):
		event.Skip()
	
	def OnClickButtonCancel( self, event ):
		event.Skip()
	
	def OnClickButtonOK( self, event ):
		event.Skip()
	

