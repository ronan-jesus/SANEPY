# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

ID_BTN_SELECIONAR = 1013
ID_BTN_BARRA = 1014
ID_BTN_NO = 1015
ID_BTN_EXCLUIR_BARRA = 1016
ID_BTN_EXCLUIR_NO = 1017
ID_BTN_PERFIL = 1018

###########################################################################
## Class  ToolbarLateralEsuqerdo
###########################################################################

class  ToolbarLateralEsuqerdo ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.auiToolbarSelecao = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_DEFAULT_STYLE|wx.aui.AUI_TB_GRIPPER|wx.aui.AUI_TB_VERTICAL )
		self.auiToolbarSelecao.SetToolSeparation( 2 )
		self.auiToolbarSelecao.SetToolPacking( 5 )
		self.auiToolbarSelecao.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.btnToogleSelecionar = self.auiToolbarSelecao.AddTool( ID_BTN_SELECIONAR, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Selecionar", wx.EmptyString, None )

		self.btnToogleBarra = self.auiToolbarSelecao.AddTool( ID_BTN_BARRA, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Nova BARRA", u"Altera estado para inserir barras", None )

		self.btnToogleNo = self.auiToolbarSelecao.AddTool( ID_BTN_NO, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Novo NÓ", u"Abre janela para inserção de NÓS", None )

		self.auiToolbarSelecao.AddSeparator()

		self.auiToolbarSelecao.AddSeparator()

		self.btnToogleExcluirBarra = self.auiToolbarSelecao.AddTool( ID_BTN_EXCLUIR_BARRA, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Excluir Barras", u"Exclui todas as Barras Selecionadas", None )

		self.btnToogleExcluirNo = self.auiToolbarSelecao.AddTool( ID_BTN_EXCLUIR_NO, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Excluir NÓ", u"Exclui todos os NÓS selecionados", None )

		self.m_staticline1 = wx.StaticLine( self.auiToolbarSelecao, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.auiToolbarSelecao.AddControl( self.m_staticline1 )
		self.m_staticline2 = wx.StaticLine( self.auiToolbarSelecao, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.auiToolbarSelecao.AddControl( self.m_staticline2 )
		self.btnTooglePerfil = self.auiToolbarSelecao.AddTool( ID_BTN_PERFIL, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Desenha Perfil Longitudinal", wx.EmptyString, None )

		self.auiToolbarSelecao.Realize()

		bSizer1.Add( self.auiToolbarSelecao, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.SelecaoBtnLaterais, id = self.btnToogleSelecionar.GetId() )
		self.Bind( wx.EVT_TOOL, self.SelecaoBtnLaterais, id = self.btnToogleBarra.GetId() )
		self.Bind( wx.EVT_TOOL, self.SelecaoBtnLaterais, id = self.btnToogleNo.GetId() )
		self.Bind( wx.EVT_TOOL, self.SelecaoBtnLaterais, id = self.btnToogleExcluirBarra.GetId() )
		self.Bind( wx.EVT_TOOL, self.SelecaoBtnLaterais, id = self.btnToogleExcluirNo.GetId() )
		self.Bind( wx.EVT_TOOL, self.SelecaoBtnLaterais, id = self.btnTooglePerfil.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def SelecaoBtnLaterais( self, event ):
		event.Skip()







