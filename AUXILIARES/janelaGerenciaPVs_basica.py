# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc

###########################################################################
## Class DlgGerenciaPV_basic
###########################################################################

class DlgGerenciaPV_basic ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edição de Estrutura", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		VBox1 = wx.BoxSizer( wx.VERTICAL )

		HBox1 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl_numeroEstrutura = wx.StaticText( self, wx.ID_ANY, u"Numero Estrutura", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_numeroEstrutura.Wrap( -1 )

		HBox1.Add( self.lbl_numeroEstrutura, 0, wx.ALL, 5 )

		self.txt_numeroPV = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_numeroPV.Enable( False )

		HBox1.Add( self.txt_numeroPV, 0, wx.ALL, 5 )


		VBox1.Add( HBox1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		HBox11 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl_nomeEstrutura = wx.StaticText( self, wx.ID_ANY, u"Nome Estrutura", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_nomeEstrutura.Wrap( -1 )

		HBox11.Add( self.lbl_nomeEstrutura, 0, wx.ALL, 5 )

		self.txt_nomePV = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_nomePV.Enable( False )

		HBox11.Add( self.txt_nomePV, 0, wx.ALL, 5 )


		VBox1.Add( HBox11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer2 = wx.FlexGridSizer( 3, 4, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

		self.lbl_pos_x = wx.StaticText( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_pos_x.Wrap( -1 )

		fgSizer2.Add( self.lbl_pos_x, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 10 )

		self.lbl_pos_y = wx.StaticText( self, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_pos_y.Wrap( -1 )

		fgSizer2.Add( self.lbl_pos_y, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 10 )

		self.lbl_pos_z = wx.StaticText( self, wx.ID_ANY, u"Z", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_pos_z.Wrap( -1 )

		fgSizer2.Add( self.lbl_pos_z, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 10 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 0 )

		self.lbl_unidade_x = wx.StaticText( self, wx.ID_ANY, u"(m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_unidade_x.Wrap( -1 )

		fgSizer2.Add( self.lbl_unidade_x, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.lbl_unidade_y = wx.StaticText( self, wx.ID_ANY, u"(m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_unidade_y.Wrap( -1 )

		fgSizer2.Add( self.lbl_unidade_y, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.lbl_unidade_z = wx.StaticText( self, wx.ID_ANY, u"(m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_unidade_z.Wrap( -1 )

		fgSizer2.Add( self.lbl_unidade_z, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.lbl_posicao = wx.StaticText( self, wx.ID_ANY, u"Posiçao", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_posicao.Wrap( -1 )

		fgSizer2.Add( self.lbl_posicao, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.LEFT|wx.RIGHT, 5 )

		self.txt_pos_x = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,25 ), 0 )
		self.txt_pos_x.Enable( False )

		fgSizer2.Add( self.txt_pos_x, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 5 )

		self.txt_pos_y = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,25 ), 0 )
		self.txt_pos_y.Enable( False )

		fgSizer2.Add( self.txt_pos_y, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 5 )

		self.txt_pos_z = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,25 ), 0 )
		self.txt_pos_z.Enable( False )

		fgSizer2.Add( self.txt_pos_z, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 5 )


		VBox1.Add( fgSizer2, 0, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		VBox1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.lbl_tipoEstrutura = wx.StaticText( self, wx.ID_ANY, u"Tipo Estrutura:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_tipoEstrutura.Wrap( -1 )

		fgSizer4.Add( self.lbl_tipoEstrutura, 0, wx.ALL, 5 )

		cbx_tipoEstruturaChoices = [ u"PV - Poço de Visita", u"CP - Caixa de Passagem", u"TIL - Terminal de Inspeção e Limpeza", u"IT - Terminal de Inspeção" ]
		self.cbx_tipoEstrutura = wx.ComboBox( self, wx.ID_ANY, u"PV - Poço de Visita", wx.DefaultPosition, wx.DefaultSize, cbx_tipoEstruturaChoices, 0 )
		self.cbx_tipoEstrutura.SetSelection( 0 )
		fgSizer4.Add( self.cbx_tipoEstrutura, 0, wx.ALL, 5 )


		bSizer9.Add( fgSizer4, 1, wx.EXPAND, 5 )


		VBox1.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )

		self.lbl_cotaTerreno = wx.StaticText( self, wx.ID_ANY, u"Cota do Terreno:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_cotaTerreno.Wrap( -1 )

		gSizer1.Add( self.lbl_cotaTerreno, 0, wx.ALL, 5 )

		self.txt_cotaTerreno = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txt_cotaTerreno, 0, wx.ALL, 5 )

		self.lbl_unid_cotaTerreno = wx.StaticText( self, wx.ID_ANY, u"(m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_unid_cotaTerreno.Wrap( -1 )

		gSizer1.Add( self.lbl_unid_cotaTerreno, 0, wx.ALL, 5 )

		self.lbl_cotaTampa = wx.StaticText( self, wx.ID_ANY, u"Cota da Tampa:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_cotaTampa.Wrap( -1 )

		gSizer1.Add( self.lbl_cotaTampa, 0, wx.ALL, 5 )

		self.txt_cotaTampa = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txt_cotaTampa, 0, wx.ALL, 5 )

		self.lbl_unid_cotaTampa = wx.StaticText( self, wx.ID_ANY, u"(m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_unid_cotaTampa.Wrap( -1 )

		gSizer1.Add( self.lbl_unid_cotaTampa, 0, wx.ALL, 5 )

		self.lbl_cotaFundo = wx.StaticText( self, wx.ID_ANY, u"Cota do Fundo:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_cotaFundo.Wrap( -1 )

		gSizer1.Add( self.lbl_cotaFundo, 0, wx.ALL, 5 )

		self.txt_cotaFundo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txt_cotaFundo, 0, wx.ALL, 5 )

		self.lbl_unid_cotaFundo = wx.StaticText( self, wx.ID_ANY, u"(m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_unid_cotaFundo.Wrap( -1 )

		gSizer1.Add( self.lbl_unid_cotaFundo, 0, wx.ALL, 5 )

		self.lbl_alturaPV = wx.StaticText( self, wx.ID_ANY, u"Altura do PV:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_alturaPV.Wrap( -1 )

		gSizer1.Add( self.lbl_alturaPV, 0, wx.ALL, 5 )

		self.txt_Altura = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.txt_Altura, 0, wx.ALL, 5 )

		self.lbl_unid_cotaAltura = wx.StaticText( self, wx.ID_ANY, u"(m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_unid_cotaAltura.Wrap( -1 )

		gSizer1.Add( self.lbl_unid_cotaAltura, 0, wx.ALL, 5 )


		bSizer23.Add( gSizer1, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		VBox1.Add( bSizer23, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		HBox4 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_ok = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		HBox4.Add( self.btn_ok, 0, wx.ALL, 5 )

		self.btn_cancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		HBox4.Add( self.btn_cancelar, 0, wx.ALL, 5 )


		VBox1.Add( HBox4, 0, wx.ALIGN_CENTER, 5 )


		self.SetSizer( VBox1 )
		self.Layout()
		VBox1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.txt_pos_x.Bind( wx.EVT_TEXT, self.OnTextPosX )
		self.txt_pos_y.Bind( wx.EVT_TEXT, self.OnTextPosY )
		self.txt_pos_z.Bind( wx.EVT_TEXT, self.OnTextPosZ )
		self.txt_cotaTerreno.Bind( wx.EVT_KILL_FOCUS, self.AlteraCotaTerreno )
		self.txt_cotaTampa.Bind( wx.EVT_KILL_FOCUS, self.AlteraCotaTampa )
		self.txt_cotaFundo.Bind( wx.EVT_KILL_FOCUS, self.AlteraCotaFundo )
		self.txt_Altura.Bind( wx.EVT_KILL_FOCUS, self.AlteraAltura )
		self.btn_ok.Bind( wx.EVT_BUTTON, self.OnButtonOK )
		self.btn_cancelar.Bind( wx.EVT_BUTTON, self.OnButtonCancelar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnTextPosX( self, event ):
		event.Skip()

	def OnTextPosY( self, event ):
		event.Skip()

	def OnTextPosZ( self, event ):
		event.Skip()

	def AlteraCotaTerreno( self, event ):
		event.Skip()

	def AlteraCotaTampa( self, event ):
		event.Skip()

	def AlteraCotaFundo( self, event ):
		event.Skip()

	def AlteraAltura( self, event ):
		event.Skip()

	def OnButtonOK( self, event ):
		event.Skip()

	def OnButtonCancelar( self, event ):
		event.Skip()


