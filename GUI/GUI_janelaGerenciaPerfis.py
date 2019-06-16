# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class JanelaGerenciaPerfis
###########################################################################

class JanelaGerenciaPerfis ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sanepy - Gerenciamento de Perfil", pos = wx.DefaultPosition, size = wx.Size( 667,387 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelInformation = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )


		bSizer3.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self.panelInformation, wx.ID_ANY, u"Nome:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txt_NomePerfil = wx.TextCtrl( self.panelInformation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.txt_NomePerfil, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self.panelInformation, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txt_DescricaoPerfil = wx.TextCtrl( self.panelInformation, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,60 ), wx.TE_MULTILINE )
		bSizer3.Add( self.txt_DescricaoPerfil, 0, wx.ALL|wx.EXPAND, 5 )


		self.panelInformation.SetSizer( bSizer3 )
		self.panelInformation.Layout()
		bSizer3.Fit( self.panelInformation )
		self.m_notebook1.AddPage( self.panelInformation, u"Informações", False )
		self.panelElevacoes = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.panelElevacoes, wx.ID_ANY, u"Elevações" ), wx.VERTICAL )

		gSizer1 = wx.GridSizer( 3, 3, 0, 0 )


		gSizer1.Add( ( 0, 0), 0, 0, 5 )

		self.m_staticText5 = wx.StaticText( self.sbSizer1.GetStaticBox(), wx.ID_ANY, u"Início:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gSizer1.Add( self.m_staticText5, 0, wx.ALIGN_BOTTOM|wx.LEFT, 5 )

		self.m_staticText6 = wx.StaticText( self.sbSizer1.GetStaticBox(), wx.ID_ANY, u"Final:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gSizer1.Add( self.m_staticText6, 0, wx.ALIGN_BOTTOM|wx.LEFT, 5 )

		self.btrad_Automatico = wx.RadioButton( self.sbSizer1.GetStaticBox(), wx.ID_ANY, u"Automático", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btrad_Automatico, 0, wx.ALL, 5 )

		self.txt_ElevInicioAuto = wx.TextCtrl( self.sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txt_ElevInicioAuto, 0, wx.ALL, 5 )

		self.txt_ElevFinalAuto = wx.TextCtrl( self.sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txt_ElevFinalAuto, 0, wx.ALL, 5 )

		self.btrad_Definido = wx.RadioButton( self.sbSizer1.GetStaticBox(), wx.ID_ANY, u"Definido Pelo Usuário", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btrad_Definido, 0, wx.ALL, 5 )

		self.txt_ElevInicioDefinido = wx.TextCtrl( self.sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_ElevInicioDefinido.Enable( False )

		gSizer1.Add( self.txt_ElevInicioDefinido, 0, wx.ALL, 5 )

		self.txt_ElevFinalDefinido = wx.TextCtrl( self.sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_ElevFinalDefinido.Enable( False )

		gSizer1.Add( self.txt_ElevFinalDefinido, 0, wx.ALL, 5 )


		self.sbSizer1.Add( gSizer1, 0, wx.EXPAND, 5 )


		bSizer6.Add( self.sbSizer1, 0, 0, 5 )

		self.sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.panelElevacoes, wx.ID_ANY, u"Escalas" ), wx.VERTICAL )

		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )

		self.m_staticText7 = wx.StaticText( self.sbSizer4.GetStaticBox(), wx.ID_ANY, u"Escala Horizontal:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.txt_escalaHorizontal = wx.TextCtrl( self.sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_escalaHorizontal.Enable( False )

		gSizer2.Add( self.txt_escalaHorizontal, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self.sbSizer4.GetStaticBox(), wx.ID_ANY, u"Escala Vertical:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.txt_escalaVertical = wx.TextCtrl( self.sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.txt_escalaVertical, 0, wx.ALL, 5 )


		self.sbSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )


		bSizer6.Add( self.sbSizer4, 0, 0, 5 )


		self.panelElevacoes.SetSizer( bSizer6 )
		self.panelElevacoes.Layout()
		bSizer6.Fit( self.panelElevacoes )
		self.m_notebook1.AddPage( self.panelElevacoes, u"Elevações e Escalas", True )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.boxSizerElementos = wx.BoxSizer( wx.VERTICAL )


		self.m_panel3.SetSizer( self.boxSizerElementos )
		self.m_panel3.Layout()
		self.boxSizerElementos.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"Trechos e Estruturas", False )

		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer1.Add( m_sdbSizer1, 0, wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btrad_Automatico.Bind( wx.EVT_RADIOBUTTON, self.OnRadioButtomElevacoes )
		self.btrad_Definido.Bind( wx.EVT_RADIOBUTTON, self.OnRadioButtomElevacoes )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.OnCancelButton )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.OnOkButton )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnRadioButtomElevacoes( self, event ):
		event.Skip()


	def OnCancelButton( self, event ):
		event.Skip()

	def OnOkButton( self, event ):
		event.Skip()


