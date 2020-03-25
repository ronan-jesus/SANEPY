# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.propgrid as pg

###########################################################################
## Class MeuPainel
###########################################################################

class MeuPainel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 454,469 ), style = wx.TAB_TRAVERSAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_propertyGrid1 = pg.PropertyGrid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DEFAULT_STYLE|wx.propgrid.PG_SPLITTER_AUTO_CENTER)
		self.m_propertyGridItem12 = self.m_propertyGrid1.Append( pg.PropertyCategory( u"Dados Gerais", u"Dados Gerais" ) ) 
		self.m_propertyGridItem8 = self.m_propertyGrid1.Append( pg.IntProperty( u"Número do Trecho", u"Número do Trecho" ) ) 
		self.m_propertyGridItem10 = self.m_propertyGrid1.Append( pg.StringProperty( u"Nome do Trecho", u"Nome do Trecho" ) ) 
		self.m_propertyGridItem9 = self.m_propertyGrid1.Append( pg.StringProperty( u"Estrutura Inicial", u"Estrutura Inicial" ) ) 
		self.m_propertyGridItem11 = self.m_propertyGrid1.Append( pg.StringProperty( u"Estrutura Final", u"Estrutura Final" ) ) 
		self.m_propertyGridItem13 = self.m_propertyGrid1.Append( pg.FloatProperty( u"Comprimento do Trecho (m)", u"Comprimento do Trecho (m)" ) ) 
		self.m_propertyGridItem14 = self.m_propertyGrid1.Append( pg.PropertyCategory( u"Dados Geometria", u"Dados Geometria" ) ) 
		self.ptyGridItemDiametro = self.m_propertyGrid1.Append( pg.EnumProperty( u"Diâmetro do Trecho (mm)", u"Diâmetro do Trecho (mm)" ) ) 
		self.m_propertyGridItem15 = self.m_propertyGrid1.Append( pg.FloatProperty( u"Cota Geratriz Inferior Inicio (m) ", u"Cota Geratriz Inferior Inicio (m) " ) ) 
		self.m_propertyGridItem16 = self.m_propertyGrid1.Append( pg.FloatProperty( u"Cota Geratriz Inferior Final (m)", u"Cota Geratriz Inferior Final (m)" ) ) 
		self.m_propertyGridItem17 = self.m_propertyGrid1.Append( pg.FloatProperty( u"Cota Geratriz Superior Inicio (m)", u"Cota Geratriz Superior Inicio (m)" ) ) 
		self.m_propertyGridItem18 = self.m_propertyGrid1.Append( pg.FloatProperty( u"Cota Geratriz Superior Final (m)", u"Cota Geratriz Superior Final (m)" ) ) 
		self.m_propertyGridItem19 = self.m_propertyGrid1.Append( pg.FloatProperty( u"Declividade do Trecho", u"Declividade do Trecho" ) ) 
		self.m_propertyGridItem20 = self.m_propertyGrid1.Append( pg.PropertyCategory( u"Vazões", u"Vazões" ) ) 
		self.m_propertyGridItem21 = self.m_propertyGrid1.Append( pg.FloatProperty( u"Contribuição Inicio de Plano (l/s.m)", u"Contribuição Inicio de Plano (l/s.m)" ) ) 
		self.m_propertyGridItem22 = self.m_propertyGrid1.Append( pg.FloatProperty( u"Contribuição Final de Plano (l/s.m)", u"Contribuição Final de Plano (l/s.m)" ) ) 
		self.m_propertyGridItem24 = self.m_propertyGrid1.Append( pg.FloatProperty( u"Contribuição Total no Trecho (l/s)", u"Contribuição Total no Trecho (l/s)" ) ) 
		self.m_propertyGridItem23 = self.m_propertyGrid1.Append( pg.FloatProperty( u"Vazão de Entrada - Montante (l/s)", u"Vazão de Entrada - Montante (l/s)" ) ) 
		self.m_propertyGridItem25 = self.m_propertyGrid1.Append( pg.FloatProperty( u"Vazão de Saida - Jusante (l/s)", u"Vazão de Saida - Jusante (l/s)" ) ) 
		bSizer4.Add( self.m_propertyGrid1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
	
	def __del__( self ):
		pass
	

