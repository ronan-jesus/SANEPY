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
## Class UI_janelageometria
###########################################################################

class UI_janelageometria ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Definição de Seções", pos = wx.DefaultPosition, size = wx.Size( 560,507 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		Vbox1 = wx.BoxSizer( wx.VERTICAL )
		
		Hbox1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl_secoes = wx.StaticText( self, wx.ID_ANY, u"SEÇÕES", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_secoes.Wrap( -1 )
		Hbox1.Add( self.lbl_secoes, 1, wx.ALL, 5 )
		
		
		Vbox1.Add( Hbox1, 0, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		Hbox2 = wx.BoxSizer( wx.VERTICAL )
		
		Vbox2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_novo = wx.Button( self, wx.ID_ANY, u"Novo", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		Vbox2.Add( self.btn_novo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn_excluir = wx.Button( self, wx.ID_ANY, u"Excluir", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		Vbox2.Add( self.btn_excluir, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn_modificar = wx.Button( self, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		Vbox2.Add( self.btn_modificar, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn_usar = wx.Button( self, wx.ID_ANY, u"Usar", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		Vbox2.Add( self.btn_usar, 0, wx.ALL, 5 )
		
		
		Hbox2.Add( Vbox2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		listbox_secoesChoices = []
		self.listbox_secoes = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,150 ), listbox_secoesChoices, 0 )
		Hbox2.Add( self.listbox_secoes, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.btn_salvar = wx.Button( self, wx.ID_ANY, u"SALVAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_salvar.Enable( False )
		
		bSizer11.Add( self.btn_salvar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn_cancelar = wx.Button( self, wx.ID_ANY, u"CANCELAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_cancelar.Enable( False )
		
		bSizer11.Add( self.btn_cancelar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Hbox2.Add( bSizer11, 0, wx.TOP|wx.ALIGN_RIGHT, 80 )
		
		
		bSizer25.Add( Hbox2, 1, 0, 5 )
		
		
		bSizer24.Add( bSizer25, 0, wx.EXPAND, 5 )
		
		self.bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"   Tipo :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer10.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		cbox_tipoChoices = [ u"Retangular", u"Circular", u"Perfil I", u"Secao Generica" ]
		self.cbox_tipo = wx.ComboBox( self, wx.ID_ANY, u"Retangular", wx.DefaultPosition, wx.Size( 100,-1 ), cbox_tipoChoices, 0 )
		bSizer10.Add( self.cbox_tipo, 1, wx.ALL, 5 )
		
		
		self.bSizer15.Add( bSizer10, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Nome :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer9.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.txt_NomeSecao = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.txt_NomeSecao, 1, wx.ALL, 5 )
		
		
		self.bSizer15.Add( bSizer9, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer24.Add( self.bSizer15, 1, wx.EXPAND, 5 )
		
		
		Vbox1.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		Hbox8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_ok = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hbox8.Add( self.btn_ok, 0, wx.ALL, 5 )
		
		self.btn_cancelar2 = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hbox8.Add( self.btn_cancelar2, 0, wx.ALL, 5 )
		
		
		Vbox1.Add( Hbox8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( Vbox1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_novo.Bind( wx.EVT_BUTTON, self.NovaSecao )
		self.btn_excluir.Bind( wx.EVT_BUTTON, self.ExcluirSecao )
		self.btn_modificar.Bind( wx.EVT_BUTTON, self.ModificaSecao )
		self.btn_usar.Bind( wx.EVT_BUTTON, self.UsarSecao )
		self.listbox_secoes.Bind( wx.EVT_LISTBOX, self.SelectListBox )
		self.btn_salvar.Bind( wx.EVT_BUTTON, self.SalvaSecao )
		self.btn_cancelar.Bind( wx.EVT_BUTTON, self.CancelaEdicao )
		self.cbox_tipo.Bind( wx.EVT_COMBOBOX, self.cbx_tipo_selecionado )
		self.btn_ok.Bind( wx.EVT_BUTTON, self.SalvaAlteracoes )
		self.btn_cancelar2.Bind( wx.EVT_BUTTON, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def NovaSecao( self, event ):
		event.Skip()
	
	def ExcluirSecao( self, event ):
		event.Skip()
	
	def ModificaSecao( self, event ):
		event.Skip()
	
	def UsarSecao( self, event ):
		event.Skip()
	
	def SelectListBox( self, event ):
		event.Skip()
	
	def SalvaSecao( self, event ):
		event.Skip()
	
	def CancelaEdicao( self, event ):
		event.Skip()
	
	def cbx_tipo_selecionado( self, event ):
		event.Skip()
	
	def SalvaAlteracoes( self, event ):
		event.Skip()
	
	def OnClose( self, event ):
		event.Skip()
	

