# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

ID_MENU_ITEM_PORTICO3D = 1000
ID_MENU_ITEM_TRELICA3D = 1001
ID_MENU_ITEM_MOSTRAR_PAINEL_PONTOSCOTAS = 1002
ID_MENU_ITEM_MOSTRAR_PAINELELEMENTOS = 1003
ID_MENU_ITEM_MOSTRAR_REACOESDEAPOIOS = 1004
ID_MENU_ITEM_MOSTRAR_ESFORCOSNORMAIS = 1005
ID_MENU_ITEM_MOSTRAR_ESFORCOSCORTANTEYY = 1006
ID_MENU_ITEM_MOSTRAR_ESFORCOSCORTANTEZZ = 1007
ID_MENU_ITEM_MOSTRAR_MOMENTOSFLETORESY = 1008
ID_MENU_ITEM_MOSTRAR_MOMENTOSFLETORESZ = 1009
ID_MENU_ITEM_MOSTRAR_MOMENTOSTORCORES = 1010
ID_MENU_ITEM_MOSTRAR_ESTRUTURA_DEFORMADA = 1011
ID_MENU_ITEM_MOSTRAR_TEXTO_DESLOCAMENTOS = 1012
ID_BTN_SELECIONAR = 1013
ID_BTN_BARRA = 1014
ID_BTN_NO = 1015
ID_BTN_EXCLUIR_BARRA = 1016
ID_BTN_EXCLUIR_NO = 1017
ID_MENU_ITEM_EDITAR_NOS = 1018
ID_MENU_ITEM_ELEMENTOS_NOS_RESTRICOES = 1019
ID_MENU_ITEM_ANALISES_EXPORTAR = 1020
ID_MENU_ITEM_MATERIAL_BARRAS = 1021
ID_MENU_ITEM_SECOES_BARRAS = 1022
ID_MENU_ITEM_CARGA_Y_BARRAS = 1023
ID_MENU_ITEM_CARGA_Z_BARRAS = 1024
ID_MENU_ITEM_INCLINACAO_BARRAS = 1025
ID_MENU_ITEM_INVERTER_SENTIDO_BARRAS = 1026
ID_MENU_OPCOES_HABILITAR_ELEMENTOS = 1027
ID_MENU_OPCOES_UNIDADES = 1028
ID_MENU_ITEM_MOSTRAR_ESTRUTURA_INDEFORMADA = 1029
ID_MENU_ITEM_SALVAR = 1030
ID_MENU_ITEM_ABRIR = 1031
ID_MENU_ITEM_FECHAR = 1032
ID_MENU_SOBRE_O_PROGRAMA = 1033
ID_MENU_ITEM_ROTULAR_BARRAS = 1034
ID_MENU_ITEM_EXPORTAR_PNG = 1035
ID_MENU_ITEM_IMPORTAR_DXF = 1036
ID_MENU_ITEM_CRIAR_PERFIL = 1037
ID_MENU_PROJETO_OPCOES_DO_PROJETO = 1038

###########################################################################
## Class Gui_principal
###########################################################################

class Gui_principal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1025,442 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.arquivo = wx.Menu()
		self.menu_abrir_novo = wx.MenuItem( self.arquivo, ID_MENU_ITEM_PORTICO3D, u"Novo", wx.EmptyString, wx.ITEM_NORMAL )
		self.arquivo.Append( self.menu_abrir_novo )

		self.item_salvar = wx.MenuItem( self.arquivo, ID_MENU_ITEM_SALVAR, u"Salvar Arquivo", wx.EmptyString, wx.ITEM_NORMAL )
		self.arquivo.Append( self.item_salvar )

		self.item_abrir = wx.MenuItem( self.arquivo, ID_MENU_ITEM_ABRIR, u"Abrir Arquivo", wx.EmptyString, wx.ITEM_NORMAL )
		self.arquivo.Append( self.item_abrir )

		self.item_fechar = wx.MenuItem( self.arquivo, ID_MENU_ITEM_FECHAR, u"Fechar", wx.EmptyString, wx.ITEM_NORMAL )
		self.arquivo.Append( self.item_fechar )

		self.m_menubar2.Append( self.arquivo, u"Arquivo" )

		self.menu_projeto = wx.Menu()
		self.item_opcoes_opcoesProjeto = wx.MenuItem( self.menu_projeto, ID_MENU_PROJETO_OPCOES_DO_PROJETO, u"Opções de Projeto", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_projeto.Append( self.item_opcoes_opcoesProjeto )

		self.item_opcoes_habilitar_visualizacao_elementos = wx.MenuItem( self.menu_projeto, ID_MENU_OPCOES_HABILITAR_ELEMENTOS, u"Habilitar/Desabilitar Elementos", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_projeto.Append( self.item_opcoes_habilitar_visualizacao_elementos )

		self.item_opcoes_unidades = wx.MenuItem( self.menu_projeto, ID_MENU_OPCOES_UNIDADES, u"Unidades e Formatos", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_projeto.Append( self.item_opcoes_unidades )

		self.m_menubar2.Append( self.menu_projeto, u"Projeto" )

		self.visualizar = wx.Menu()
		self.paineis = wx.Menu()
		self.mostrar_painel_pontosCotas = wx.MenuItem( self.paineis, ID_MENU_ITEM_MOSTRAR_PAINEL_PONTOSCOTAS, u"Pontos de Cotas", wx.EmptyString, wx.ITEM_CHECK )
		self.paineis.Append( self.mostrar_painel_pontosCotas )
		self.mostrar_painel_pontosCotas.Check( True )

		self.mostrar_painel_elementos = wx.MenuItem( self.paineis, ID_MENU_ITEM_MOSTRAR_PAINELELEMENTOS, u"Elementos", wx.EmptyString, wx.ITEM_CHECK )
		self.paineis.Append( self.mostrar_painel_elementos )
		self.mostrar_painel_elementos.Check( True )

		self.visualizar.AppendSubMenu( self.paineis, u"Paineis" )

		self.reacoes = wx.Menu()
		self.mostrar_reacoes_apoios = wx.MenuItem( self.reacoes, ID_MENU_ITEM_MOSTRAR_REACOESDEAPOIOS, u"Reações nos Apoios", wx.EmptyString, wx.ITEM_CHECK )
		self.reacoes.Append( self.mostrar_reacoes_apoios )

		self.visualizar.AppendSubMenu( self.reacoes, u"Reações" )

		self.solicitacoes = wx.Menu()
		self.normal = wx.MenuItem( self.solicitacoes, ID_MENU_ITEM_MOSTRAR_ESFORCOSNORMAIS, u"Esforço Normal", wx.EmptyString, wx.ITEM_CHECK )
		self.solicitacoes.Append( self.normal )

		self.cortante_y = wx.MenuItem( self.solicitacoes, ID_MENU_ITEM_MOSTRAR_ESFORCOSCORTANTEYY, u"Esforço Cortante em Y", wx.EmptyString, wx.ITEM_CHECK )
		self.solicitacoes.Append( self.cortante_y )

		self.cortante_z = wx.MenuItem( self.solicitacoes, ID_MENU_ITEM_MOSTRAR_ESFORCOSCORTANTEZZ, u"Esforço Cortante em Z", wx.EmptyString, wx.ITEM_CHECK )
		self.solicitacoes.Append( self.cortante_z )

		self.momento_y = wx.MenuItem( self.solicitacoes, ID_MENU_ITEM_MOSTRAR_MOMENTOSFLETORESY, u"Momentos Fletores em Y", wx.EmptyString, wx.ITEM_CHECK )
		self.solicitacoes.Append( self.momento_y )

		self.momento_z = wx.MenuItem( self.solicitacoes, ID_MENU_ITEM_MOSTRAR_MOMENTOSFLETORESZ, u"Momentos Fletores em Z", wx.EmptyString, wx.ITEM_CHECK )
		self.solicitacoes.Append( self.momento_z )

		self.torcor = wx.MenuItem( self.solicitacoes, ID_MENU_ITEM_MOSTRAR_MOMENTOSTORCORES, u"Momentos Torçores", wx.EmptyString, wx.ITEM_CHECK )
		self.solicitacoes.Append( self.torcor )

		self.visualizar.AppendSubMenu( self.solicitacoes, u"Solicitações" )

		self.deformacoes = wx.Menu()
		self.estrutura_deformada = wx.MenuItem( self.deformacoes, ID_MENU_ITEM_MOSTRAR_ESTRUTURA_DEFORMADA, u"Estrutura Deformada", wx.EmptyString, wx.ITEM_CHECK )
		self.deformacoes.Append( self.estrutura_deformada )

		self.estrutura_indeformada = wx.MenuItem( self.deformacoes, ID_MENU_ITEM_MOSTRAR_ESTRUTURA_INDEFORMADA, u"Estrutura Indeformada", wx.EmptyString, wx.ITEM_CHECK )
		self.deformacoes.Append( self.estrutura_indeformada )

		self.deslocamentos_nodais = wx.MenuItem( self.deformacoes, ID_MENU_ITEM_MOSTRAR_TEXTO_DESLOCAMENTOS, u"Deslocamentos Nodais", wx.EmptyString, wx.ITEM_CHECK )
		self.deformacoes.Append( self.deslocamentos_nodais )

		self.visualizar.AppendSubMenu( self.deformacoes, u"Deformações" )

		self.m_menubar2.Append( self.visualizar, u"Visualizar" )

		self.menu_elementos = wx.Menu()
		self.submenu_nos = wx.Menu()
		self.item_nos_atribuir_forcas = wx.MenuItem( self.submenu_nos, ID_MENU_ITEM_EDITAR_NOS , u"Atribuir Forças", wx.EmptyString, wx.ITEM_NORMAL )
		self.submenu_nos.Append( self.item_nos_atribuir_forcas )

		self.item_nos_atribuir_retricoes = wx.MenuItem( self.submenu_nos, ID_MENU_ITEM_ELEMENTOS_NOS_RESTRICOES, u"Definir Restrições", wx.EmptyString, wx.ITEM_NORMAL )
		self.submenu_nos.Append( self.item_nos_atribuir_retricoes )

		self.menu_elementos.AppendSubMenu( self.submenu_nos, u"Nós" )

		self.submenu_barras = wx.Menu()
		self.item_barras_atribuir_material = wx.MenuItem( self.submenu_barras, ID_MENU_ITEM_MATERIAL_BARRAS, u"Atribuir Material", wx.EmptyString, wx.ITEM_NORMAL )
		self.submenu_barras.Append( self.item_barras_atribuir_material )

		self.item_barras_atribuir_secao = wx.MenuItem( self.submenu_barras, ID_MENU_ITEM_SECOES_BARRAS, u"Atribuir Seção", wx.EmptyString, wx.ITEM_NORMAL )
		self.submenu_barras.Append( self.item_barras_atribuir_secao )

		self.item_barras_atribuir_carga_y = wx.MenuItem( self.submenu_barras, ID_MENU_ITEM_CARGA_Y_BARRAS, u"Atribuir Carregamento Eixo Y", wx.EmptyString, wx.ITEM_NORMAL )
		self.submenu_barras.Append( self.item_barras_atribuir_carga_y )

		self.item_barras_atribuir_carga_z = wx.MenuItem( self.submenu_barras, ID_MENU_ITEM_CARGA_Z_BARRAS, u"Atribuir Carregamento Eixo Z", wx.EmptyString, wx.ITEM_NORMAL )
		self.submenu_barras.Append( self.item_barras_atribuir_carga_z )

		self.item_barras_atribuir_inclinacao_secao = wx.MenuItem( self.submenu_barras, ID_MENU_ITEM_INCLINACAO_BARRAS, u"Atribuir Inclinação da Seção", wx.EmptyString, wx.ITEM_NORMAL )
		self.submenu_barras.Append( self.item_barras_atribuir_inclinacao_secao )

		self.item_barras_inverter_sentido_barra = wx.MenuItem( self.submenu_barras, ID_MENU_ITEM_INVERTER_SENTIDO_BARRAS, u"Inverter Sentido", wx.EmptyString, wx.ITEM_NORMAL )
		self.submenu_barras.Append( self.item_barras_inverter_sentido_barra )

		self.item_barras_rotular_barra = wx.MenuItem( self.submenu_barras, ID_MENU_ITEM_ROTULAR_BARRAS, u"Rotular  Conexões", wx.EmptyString, wx.ITEM_NORMAL )
		self.submenu_barras.Append( self.item_barras_rotular_barra )

		self.menu_elementos.AppendSubMenu( self.submenu_barras, u"Barras" )

		self.submenu_perfis = wx.Menu()
		self.item_perfis_criar_perfil = wx.MenuItem( self.submenu_perfis, ID_MENU_ITEM_CRIAR_PERFIL, u"Criar Perfil", wx.EmptyString, wx.ITEM_NORMAL )
		self.submenu_perfis.Append( self.item_perfis_criar_perfil )

		self.menu_elementos.AppendSubMenu( self.submenu_perfis, u"Perfis" )

		self.m_menubar2.Append( self.menu_elementos, u"Elementos" )

		self.menu_elementos_exportar = wx.Menu()
		self.submenu_exportar = wx.MenuItem( self.menu_elementos_exportar, ID_MENU_ITEM_ANALISES_EXPORTAR, u"Exportar -> Excel", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_elementos_exportar.Append( self.submenu_exportar )

		self.menu_item_exportar_PNG = wx.MenuItem( self.menu_elementos_exportar, ID_MENU_ITEM_EXPORTAR_PNG, u"Exportar -> Imagem PNG", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_elementos_exportar.Append( self.menu_item_exportar_PNG )

		self.menu_elementos_exportar.AppendSeparator()

		self.menu_item_importar_dxf = wx.MenuItem( self.menu_elementos_exportar, ID_MENU_ITEM_IMPORTAR_DXF, u"Importar -> DXF", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_elementos_exportar.Append( self.menu_item_importar_dxf )

		self.m_menubar2.Append( self.menu_elementos_exportar, u"Ferramentas" )

		self.menu_sobre = wx.Menu()
		self.item_sobre_o_programa = wx.MenuItem( self.menu_sobre, ID_MENU_SOBRE_O_PROGRAMA, u"Sobre o Programa", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_sobre.Append( self.item_sobre_o_programa )

		self.m_menubar2.Append( self.menu_sobre, u"Sobre" )

		self.SetMenuBar( self.m_menubar2 )

		self.toolbar = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.toolbar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		self.salvar = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Salvar Projeto", u"Salva o projeto atual", None )

		self.abrir = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Abrir Projeto", u"Abre janela de busca de arquivo", None )

		self.toolbar.AddSeparator()

		self.gerenciaModE = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Definir Materiais", u"Abre janela de gerenciamento de materiais", None )

		self.gerenciaSecoes_I = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Definir Seções", u"Abre janela de gerenciamento de seções", None )

		self.toolbar.AddSeparator()

		self.mostraNormal = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Mostrar Esforços Normais", u"Altera visualização da estrutura para visualização dos esforços normais nas barras", None )

		self.mostraCortante = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Mostrar Esforços Cortantes", u"Altera visualização da estrutura para visualização dos esforços cortantes nas barras", None )

		self.mostraFletor = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Mostrar Momentos Fletores", u"Altera visualização da estrutura para visualização dos esforços dos momentos fletores nas barras", None )

		self.mostraTorcor = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Mostrar Momentos Torsores", u"Altera visualização da estrutura para visualização dos momentos torsores nas barras", None )

		self.toolbar.AddSeparator()

		self.pan = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Alterar Mouse para PAN", u"Altera o enquadramento da tela para ser arrastado com o mouse", None )

		self.zoomAll = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Dar ZoomAll", u"Enquadra toda a estrutura na porção de tela visivel", None )

		self.orbit = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Alterar Mouse para Orbit", u"Altera o enquadramento da tela para girar com o arraste do mouse", None )

		self.toolbar.AddSeparator()

		self.seta_calcular = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Calcular Estrutura", u"Faz a verificação e cálculo da estrutura em análise", None )

		self.txt_min_coef = wx.TextCtrl( self.toolbar, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.toolbar.AddControl( self.txt_min_coef )
		self.m_slider1 = wx.Slider( self.toolbar, wx.ID_ANY, 50, 0, 1000, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		self.toolbar.AddControl( self.m_slider1 )
		self.txt_max_coef = wx.TextCtrl( self.toolbar, wx.ID_ANY, u"1000", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.toolbar.AddControl( self.txt_max_coef )
		self.btn_vista_esquerda = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Visualizar Estrutura a Esquerda", u"Altera camera para visualizar a estrutura na parte esquerda", None )

		self.m_tool15 = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Visualizar Estrutura a Direita", u"Altera camera para visualizar a estrutura na parte direita", None )

		self.m_tool16 = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Visualizar Estrutura de Frente", u"Altera camera para visualizar a estrutura na parte da frente", None )

		self.m_tool17 = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Visualizar Estrutura de Trás", u"Altera camera para visualizar a estrutura na parte de trás", None )

		self.m_tool18 = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Visualizar de cima", u"Altera camera para visualizar a estrutura na parte de cima", None )

		self.m_tool19 = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"visualizar de baixo", u"Altera camera para visualizar a estrutura na parte de baixo", None )

		self.toolbar.Realize()


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.Bind( wx.EVT_MENU, self.MenuItemselect, id = self.menu_abrir_novo.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuItemselect, id = self.item_salvar.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuItemselect, id = self.item_abrir.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuItemselect, id = self.item_fechar.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_opcoes_opcoesProjeto.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_opcoes_habilitar_visualizacao_elementos.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_opcoes_unidades.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCheckselect, id = self.mostrar_painel_pontosCotas.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCheckselect, id = self.mostrar_painel_elementos.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCheckselect, id = self.mostrar_reacoes_apoios.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCheckselect, id = self.normal.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCheckselect, id = self.cortante_y.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCheckselect, id = self.cortante_z.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCheckselect, id = self.momento_y.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCheckselect, id = self.momento_z.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCheckselect, id = self.torcor.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCheckselect, id = self.estrutura_deformada.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCheckselect, id = self.estrutura_indeformada.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCheckselect, id = self.deslocamentos_nodais.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_nos_atribuir_forcas.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_nos_atribuir_retricoes.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_barras_atribuir_material.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_barras_atribuir_secao.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_barras_atribuir_carga_y.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_barras_atribuir_carga_z.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_barras_atribuir_inclinacao_secao.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_barras_inverter_sentido_barra.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_barras_rotular_barra.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_perfis_criar_perfil.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.submenu_exportar.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.menu_item_exportar_PNG.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.menu_item_importar_dxf.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuElementosSelected, id = self.item_sobre_o_programa.GetId() )
		self.Bind( wx.EVT_TOOL, self.SalvaArquivo, id = self.salvar.GetId() )
		self.Bind( wx.EVT_TOOL, self.Abre_Arquivo, id = self.abrir.GetId() )
		self.Bind( wx.EVT_TOOL, self.GerenciaMateriais, id = self.gerenciaModE.GetId() )
		self.Bind( wx.EVT_TOOL, self.GerenciaSecoes, id = self.gerenciaSecoes_I.GetId() )
		self.Bind( wx.EVT_TOOL, self.MostrarEsforcosNormais, id = self.mostraNormal.GetId() )
		self.Bind( wx.EVT_TOOL, self.MostrarEsforcosCortantes, id = self.mostraCortante.GetId() )
		self.Bind( wx.EVT_TOOL, self.MostrarMomentosFletores, id = self.mostraFletor.GetId() )
		self.Bind( wx.EVT_TOOL, self.MostrarMomentosTorsores, id = self.mostraTorcor.GetId() )
		self.Bind( wx.EVT_TOOL, self.SelecionaModoPan, id = self.pan.GetId() )
		self.Bind( wx.EVT_TOOL, self.ZoomAll, id = self.zoomAll.GetId() )
		self.Bind( wx.EVT_TOOL, self.Calcula, id = self.seta_calcular.GetId() )
		self.txt_min_coef.Bind( wx.EVT_KILL_FOCUS, self.AtualizaCoefVisualizacao )
		self.m_slider1.Bind( wx.EVT_SCROLL, self.OnSliderBarra )
		self.txt_max_coef.Bind( wx.EVT_KILL_FOCUS, self.AtualizaCoefVisualizacao )
		self.Bind( wx.EVT_TOOL, self.ViewCameraLeft, id = self.btn_vista_esquerda.GetId() )
		self.Bind( wx.EVT_TOOL, self.ViewCameraRight, id = self.m_tool15.GetId() )
		self.Bind( wx.EVT_TOOL, self.ViewCameraFront, id = self.m_tool16.GetId() )
		self.Bind( wx.EVT_TOOL, self.ViewCameraBack, id = self.m_tool17.GetId() )
		self.Bind( wx.EVT_TOOL, self.ViewCameraTop, id = self.m_tool18.GetId() )
		self.Bind( wx.EVT_TOOL, self.ViewCameraBottom, id = self.m_tool19.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def MenuItemselect( self, event ):
		event.Skip()




	def MenuElementosSelected( self, event ):
		event.Skip()



	def OnCheckselect( self, event ):
		event.Skip()


























	def SalvaArquivo( self, event ):
		event.Skip()

	def Abre_Arquivo( self, event ):
		event.Skip()

	def GerenciaMateriais( self, event ):
		event.Skip()

	def GerenciaSecoes( self, event ):
		event.Skip()

	def MostrarEsforcosNormais( self, event ):
		event.Skip()

	def MostrarEsforcosCortantes( self, event ):
		event.Skip()

	def MostrarMomentosFletores( self, event ):
		event.Skip()

	def MostrarMomentosTorsores( self, event ):
		event.Skip()

	def SelecionaModoPan( self, event ):
		event.Skip()

	def ZoomAll( self, event ):
		event.Skip()

	def Calcula( self, event ):
		event.Skip()

	def AtualizaCoefVisualizacao( self, event ):
		event.Skip()

	def OnSliderBarra( self, event ):
		event.Skip()


	def ViewCameraLeft( self, event ):
		event.Skip()

	def ViewCameraRight( self, event ):
		event.Skip()

	def ViewCameraFront( self, event ):
		event.Skip()

	def ViewCameraBack( self, event ):
		event.Skip()

	def ViewCameraTop( self, event ):
		event.Skip()

	def ViewCameraBottom( self, event ):
		event.Skip()


