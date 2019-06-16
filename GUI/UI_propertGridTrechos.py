# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.propgrid as pg

###########################################################################
## Class propGridTrechos
###########################################################################

class propGridTrechos ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PROPRIEDADES TRECHOS", pos = wx.DefaultPosition, size = wx.Size( 500,474 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_propertyGridManager1 = pg.PropertyGridManager(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_BOLD_MODIFIED|wx.propgrid.PG_DESCRIPTION|wx.propgrid.PG_SPLITTER_AUTO_CENTER|wx.propgrid.PG_TOOLBAR|wx.propgrid.PG_TOOLTIPS)
		self.m_propertyGridManager1.SetExtraStyle( wx.propgrid.PG_EX_NO_FLAT_TOOLBAR )

		self.m_propertyGridPage1 = self.m_propertyGridManager1.AddPage( u"TESTE1", wx.ArtProvider.GetBitmap( wx.ART_HELP_BOOK, wx.ART_TOOLBAR ) );
		self.ptyGridItemNumero1 = self.m_propertyGridPage1.Append( pg.PropertyCategory( u"Dados Gerais", u"Dados Gerais" ) )
		self.ptyGridItemNumero = self.m_propertyGridPage1.Append( pg.IntProperty( u"Número do Trecho", u"Número do Trecho" ) )
		self.ptyGridItemNome = self.m_propertyGridPage1.Append( pg.StringProperty( u"Nome do Trecho", u"Nome do Trecho" ) )
		self.ptyGridItemEstruturaInicial = self.m_propertyGridPage1.Append( pg.StringProperty( u"Estrutura Inicial", u"Estrutura Inicial" ) )
		self.ptyGridItemEstruturaFinal = self.m_propertyGridPage1.Append( pg.StringProperty( u"Estrutura Final", u"Estrutura Final" ) )
		self.m_propertyGridItem14 = self.m_propertyGridPage1.Append( pg.PropertyCategory( u"Dados Geometria", u"Dados Geometria" ) )
		self.ptyGridItemDiametro = self.m_propertyGridPage1.Append( pg.EnumProperty( u"Diâmetro do Trecho (mm)", u"Diâmetro do Trecho (mm)" ) )
		self.ptyGridItemComprAuto = self.m_propertyGridPage1.Append( pg.BoolProperty( u"Usar Comprimento Automatico", u"Usar Comprimento Automatico" ) )
		self.ptyGridItemComprimento = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Comp do Trecho Auto (m)", u"Comp do Trecho Auto (m)" ) )
		self.ptyGridItemCompDefinido = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Comp do Trecho Definido (m)", u"Comp do Trecho Definido (m)" ) )
		self.ptyGridItemCotaGeratrizInferiorInicio = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Cota Geratriz Inferior Inicio (m)", u"Cota Geratriz Inferior Inicio (m)" ) )
		self.ptyGridItemCotaGeratrizInferiorFinal = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Cota Geratriz Inferior Final (m)", u"Cota Geratriz Inferior Final (m)" ) )
		self.ptyGridItemCotaGeratrizSuperiorInicio = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Cota Geratriz Superior Inicio (m)", u"Cota Geratriz Superior Inicio (m)" ) )
		self.ptyGridItemCotaGeratrizSuperiorFinal = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Cota Geratriz Superior Final (m)", u"Cota Geratriz Superior Final (m)" ) )
		self.ptyGridItemDeclividaTerreno = self.m_propertyGridPage1.Append( pg.StringProperty( u"Declividade do Terreno (%)", u"Declividade do Terreno (%)" ) )
		self.ptyGridItemDeclividaMinima = self.m_propertyGridPage1.Append( pg.StringProperty( u"Declividade Minima (%)", u"Declividade Minima (%)" ) )
		self.ptyGridItemDeclividaTrecho = self.m_propertyGridPage1.Append( pg.StringProperty( u"Declividade do Trecho (%)", u"Declividade do Trecho (%)" ) )
		self.ptyGridItemDesnivel = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Desnível (m)", u"Desnível (m)" ) )
		self.m_propertyGridItem20 = self.m_propertyGridPage1.Append( pg.PropertyCategory( u"Vazões", u"Vazões" ) )
		self.ptyGridItemContribInicioPlano = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Contribuição Inicio de Plano (l/s.m)", u"Contribuição Inicio de Plano (l/s.m)" ) )
		self.ptyGridItemContribFimPlano = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Contribuição Final de Plano (l/s.m)", u"Contribuição Final de Plano (l/s.m)" ) )
		self.ptyGridItemVazaoPontual = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Vazão Pontual no Trecho (l/s)", u"Vazão Pontual no Trecho (l/s)" ) )
		self.ptyGridItemContribParasitaria = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Contribuição Parasitária (l/s.m)", u"Contribuição Parasitária (l/s.m)" ) )
		self.ptyGridItemContribTotalInicio = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Contrib. Total do Trecho - Inicio (l/s)", u"Contrib. Total do Trecho - Inicio (l/s)" ) )
		self.ptyGridItemContribTotalFinal = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Contrib. Total do Trecho - Final (l/s)", u"Contrib. Total do Trecho - Final (l/s)" ) )
		self.ptyGridItemVazaoEntradaInicio = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Vazão de Montante - Inicio (l/s)", u"Vazão de Montante - Inicio (l/s)" ) )
		self.ptyGridItemVazaoSaidaInicio = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Vazão de Jusante - Inicio (l/s)", u"Vazão de Jusante - Inicio (l/s)" ) )
		self.ptyGridItemVazaoEntradaFinal = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Vazão de Montante - Final (l/s)", u"Vazão de Montante - Final (l/s)" ) )
		self.ptyGridItemVazaoSaidaFinal = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Vazão de Jusante - Final (l/s)", u"Vazão de Jusante - Final (l/s)" ) )
		self.m_propertyGridItem25 = self.m_propertyGridPage1.Append( pg.PropertyCategory( u"Propriedades Hidráulicas", u"Propriedades Hidráulicas" ) )
		self.ptyGridItemCoefManning = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Coeficiente de Manning", u"Coeficiente de Manning" ) )
		self.ptyGridItemVelocidadeInicio = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Velocidade Início de Plano (m/s)", u"Velocidade Início de Plano (m/s)" ) )
		self.ptyGridItemVelocidadeFinal = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Velocidade Final de Plano (m/s)", u"Velocidade Final de Plano (m/s)" ) )
		self.ptyGridItemVelCriticaInicio = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Velocidade Crítica Início de Plano (m/s)", u"Velocidade Crítica Início de Plano (m/s)" ) )
		self.ptyGridItemVelCriticaFinal = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Velocidade Crítica Final de Plano (m/s)", u"Velocidade Crítica Final de Plano (m/s)" ) )
		self.ptyGridItemRelacaoRh_D_inicial = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Relação Rh/D Inicio", u"Relação Rh/D Inicio" ) )
		self.ptyGridItemRelacaoRh_D_final = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Relação Rh/D Final", u"Relação Rh/D Final" ) )
		self.ptyGridItemPerimMolhadoInicio = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Perímetro Molhado Início", u"Perímetro Molhado Início" ) )
		self.ptyGridItemPerimMolhadoFinal = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Perimetro Molhado Final", u"Perimetro Molhado Final" ) )
		self.ptyGridItemAreaMolhadaInicio = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Área Molhada Início", u"Área Molhada Início" ) )
		self.ptyGridItemAreaMolhadaFinal = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Área Molhada Final", u"Área Molhada Final" ) )
		self.ptyGridItemRaioHidraulicoInicio = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Raio Hidráulico Início", u"Raio Hidráulico Início" ) )
		self.ptyGridItemRaioHidraulicoFinal = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Raio Hidráulico Final", u"Raio Hidráulico Final" ) )
		self.ptyGridItemRelacao_H_D_Inicio = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Relação h/D Inicio (%)", u"Relação h/D Inicio (%)" ) )
		self.ptyGridItemRelacao_H_D_Final = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Relação h/D Final (%)", u"Relação h/D Final (%)" ) )
		self.ptyGridItemAlturaLaminaInicio = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Altura Lâmina Água Inicio (m)", u"Altura Lâmina Água Inicio (m)" ) )
		self.ptyGridItemAlturaLaminaFinal = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Altura Lâmina Água Final (m)", u"Altura Lâmina Água Final (m)" ) )
		self.ptyGridItemCotaLaminaMontante = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Cota Lâmina Água Montante (m)", u"Cota Lâmina Água Montante (m)" ) )
		self.ptyGridItemCotaLaminaJusante = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Cota Lâmina Água Jusante (m)", u"Cota Lâmina Água Jusante (m)" ) )
		self.ptyGridItemRemanso = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Remanso no Trecho (m)", u"Remanso no Trecho (m)" ) )
		self.Alturas = self.m_propertyGridPage1.Append( pg.PropertyCategory( u"Alturas e Coberturas", u"Alturas e Coberturas" ) )
		self.ptyGridItemAlturaTuboInicioTrecho = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Altura Fundo Tubo Inicio Trecho (m)", u"Altura Fundo Tubo Inicio Trecho (m)" ) )
		self.ptyGridItemAlturaTuboFinalTrecho = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Altura Fundo Tubo Final Trecho (m)", u"Altura Fundo Tubo Final Trecho (m)" ) )
		self.ptyGridItemCoberturaInicioTrecho = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Cobertura no Inicio do Trecho (m)", u"Cobertura no Inicio do Trecho (m)" ) )
		self.ptyGridItemCoberturaFinalTrecho = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Cobertura no Final do Trecho (m)", u"Cobertura no Final do Trecho (m)" ) )
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


