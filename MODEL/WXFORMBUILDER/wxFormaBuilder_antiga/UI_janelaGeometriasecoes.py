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
## Class ChangeDepthDialog
###########################################################################

class ChangeDepthDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Definição de Material", pos = wx.DefaultPosition, size = wx.Size( 342,462 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		Vbox1 = wx.BoxSizer( wx.VERTICAL )
		
		Hbox1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl_material = wx.StaticText( self, wx.ID_ANY, u"MATERIAL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_material.Wrap( -1 )
		Hbox1.Add( self.lbl_material, 1, wx.ALL, 5 )
		
		
		Vbox1.Add( Hbox1, 0, wx.EXPAND, 5 )
		
		Hbox2 = wx.BoxSizer( wx.HORIZONTAL )
		
		listboxChoices = [ wx.EmptyString ]
		self.listbox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,150 ), listboxChoices, 0 )
		Hbox2.Add( self.listbox, 0, wx.ALL, 5 )
		
		Vbox2 = wx.BoxSizer( wx.VERTICAL )
		
		self.btn_novo = wx.Button( self, wx.ID_ANY, u"Novo", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vbox2.Add( self.btn_novo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn_excluir = wx.Button( self, wx.ID_ANY, u"Excluir", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vbox2.Add( self.btn_excluir, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn_modificar = wx.Button( self, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vbox2.Add( self.btn_modificar, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn_usar = wx.Button( self, wx.ID_ANY, u"Usar", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vbox2.Add( self.btn_usar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Hbox2.Add( Vbox2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vbox1.Add( Hbox2, 1, wx.EXPAND, 5 )
		
		Hbox3 = wx.BoxSizer( wx.HORIZONTAL )
		
		Vbox3 = wx.BoxSizer( wx.VERTICAL )
		
		Hbox_nomeSecao = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl_nome_material = wx.StaticText( self, wx.ID_ANY, u"Nome :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_nome_material.Wrap( -1 )
		self.lbl_nome_material.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 72, 90, 90, False, wx.EmptyString ) )
		
		Hbox_nomeSecao.Add( self.lbl_nome_material, 0, wx.ALL, 5 )
		
		self.txtNomeMaterial = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		Hbox_nomeSecao.Add( self.txtNomeMaterial, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		Vbox3.Add( Hbox_nomeSecao, 1, wx.EXPAND, 5 )
		
		Hbox4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl_E = wx.StaticText( self, wx.ID_ANY, u"        E :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_E.Wrap( -1 )
		self.lbl_E.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 72, 90, 90, False, wx.EmptyString ) )
		
		Hbox4.Add( self.lbl_E, 0, wx.ALL, 5 )
		
		self.txtModElasticidade = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		Hbox4.Add( self.txtModElasticidade, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		Vbox3.Add( Hbox4, 1, wx.EXPAND, 5 )
		
		Hbox5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl_G = wx.StaticText( self, wx.ID_ANY, u"        G :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_G.Wrap( -1 )
		self.lbl_G.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 72, 90, 90, False, wx.EmptyString ) )
		
		Hbox5.Add( self.lbl_G, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.txtModElasticidadeTransversal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		Hbox5.Add( self.txtModElasticidadeTransversal, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		Vbox3.Add( Hbox5, 1, wx.EXPAND, 5 )
		
		
		Hbox3.Add( Vbox3, 1, 0, 5 )
		
		Vbox4 = wx.BoxSizer( wx.VERTICAL )
		
		
		Vbox4.AddSpacer( ( 0, 30), 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn_salvar = wx.Button( self, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_salvar.Enable( False )
		
		Vbox4.Add( self.btn_salvar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn_cancela_edicao = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_cancela_edicao.Enable( False )
		
		Vbox4.Add( self.btn_cancela_edicao, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Hbox3.Add( Vbox4, 1, 0, 5 )
		
		
		Vbox1.Add( Hbox3, 1, 0, 5 )
		
		Hbox8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_ok = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hbox8.Add( self.btn_ok, 0, wx.ALL, 5 )
		
		self.btn_cancela = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hbox8.Add( self.btn_cancela, 0, wx.ALL, 5 )
		
		
		Vbox1.Add( Hbox8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( Vbox1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.listbox.Bind( wx.EVT_LISTBOX, self.SelectListBox )
		self.btn_novo.Bind( wx.EVT_BUTTON, self.NovoMaterial )
		self.btn_excluir.Bind( wx.EVT_BUTTON, self.ExcluirMaterial )
		self.btn_modificar.Bind( wx.EVT_BUTTON, self.ModificarMaterial )
		self.btn_usar.Bind( wx.EVT_BUTTON, self.UsarMaterial )
		self.btn_salvar.Bind( wx.EVT_BUTTON, self.SalvaMaterial )
		self.btn_cancela_edicao.Bind( wx.EVT_BUTTON, self.CancelaEdicao )
		self.btn_ok.Bind( wx.EVT_BUTTON, self.SalvaAlteracoes )
		self.btn_cancela.Bind( wx.EVT_BUTTON, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def SelectListBox( self, event ):
		event.Skip()
	
	def NovoMaterial( self, event ):
		event.Skip()
	
	def ExcluirMaterial( self, event ):
		event.Skip()
	
	def ModificarMaterial( self, event ):
		event.Skip()
	
	def UsarMaterial( self, event ):
		event.Skip()
	
	def SalvaMaterial( self, event ):
		event.Skip()
	
	def CancelaEdicao( self, event ):
		event.Skip()
	
	def SalvaAlteracoes( self, event ):
		event.Skip()
	
	def OnClose( self, event ):
		event.Skip()
	

