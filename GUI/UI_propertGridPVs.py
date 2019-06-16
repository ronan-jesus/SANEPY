# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.propgrid as pg

###########################################################################
## Class propGridPVs
###########################################################################

class propGridPVs ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PROPRIEDADES ESTRUTURAS", pos = wx.DefaultPosition, size = wx.Size( 500,422 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_propertyGridManager1 = pg.PropertyGridManager(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_BOLD_MODIFIED|wx.propgrid.PG_DESCRIPTION|wx.propgrid.PG_SPLITTER_AUTO_CENTER|wx.propgrid.PG_TOOLBAR|wx.propgrid.PG_TOOLTIPS)
		self.m_propertyGridManager1.SetExtraStyle( wx.propgrid.PG_EX_NO_FLAT_TOOLBAR )

		self.m_propertyGridPage1 = self.m_propertyGridManager1.AddPage( u"TESTE1", wx.ArtProvider.GetBitmap( wx.ART_HELP_BOOK, wx.ART_TOOLBAR ) );
		self.Dados_Iniciais = self.m_propertyGridPage1.Append( pg.PropertyCategory( u"Dados Iniciais", u"Dados Iniciais" ) )
		self.ptyGridItemNomeEstrutura = self.m_propertyGridPage1.Append( pg.StringProperty( u"Nome da Estrutura", u"Nome da Estrutura" ) )
		self.ptyGridItemNumeroEstrutura = self.m_propertyGridPage1.Append( pg.IntProperty( u"Número da Estrutura", u"Número da Estrutura" ) )
		self.ptyGridItemPosicaoX = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Coordenada X (m)", u"Coordenada X (m)" ) )
		self.ptyGridItemPosicaoY = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Coordenada Y (m)", u"Coordenada Y (m)" ) )
		self.ptyGridItemAnguloRotacao = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Angulo Rotação ( ° dec)", u"Angulo Rotação ( ° dec)" ) )
		self.m_propertyGridItem53 = self.m_propertyGridPage1.Append( pg.PropertyCategory( u"Dados Gemétricos", u"Dados Gemétricos" ) )
		self.ptyGridItemTipoEstrutura = self.m_propertyGridPage1.Append( pg.EnumProperty( u"Tipo Estrutura", u"Tipo Estrutura" ) )
		self.ptyGridItemCotaTerreno = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Cota do Terreno (m)", u"Cota do Terreno (m)" ) )
		self.ptyGridItemCotaTampa = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Cota da Tampa (m)", u"Cota da Tampa (m)" ) )
		self.ptyGridItemCotaFundo = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Cota do Fundo (m)", u"Cota do Fundo (m)" ) )
		self.ptyGridItemAlturaEstrutura = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Altura da Estrutura (m)", u"Altura da Estrutura (m)" ) )
		bSizer4.Add( self.m_propertyGridManager1, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_propertyGridManager1.Bind( pg.EVT_PG_CHANGED, self.ModificaPropriedade )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ModificaPropriedade( self, event ):
		event.Skip()


