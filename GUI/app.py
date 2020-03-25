# -*- coding: utf-8 -*-
from __future__ import division


#from CamadaNegocios import CamadaDoModelo
from MODEL.model import *

from AUXILIARES.Funcoes_de_Arquivos import salvaProjeto


from janelaPropGridPVs import DlgGerenciaEstrutura
from janelaPropGridTrechos import JanelaPropTrechos
from janelaDadosDoProjeto import JanelaDadosDoProjeto
from TreeListCtrlPerfis import TreeListCtrlPerfil
from janelaCriaPerfil import JanelaCriaPerfil
from gui_principal import Gui_principal
from painelSelecaoEsquerdo import PainelSelecaoEsquerdo
from painelGerenciaPontos import PainelGerenciaPontos
from ArvoreDeSelecao import ArvoreSelecaoElementos
from janela_habilita_elementos import JanelaOpcoesVisualizacao
from janela_opcoes_unidades import JanelaOpcoesUnidades
from AUXILIARES.imagens_do_app import *
from sobre import *

from MODEL.pyopengl import ConeCanvas

import wx
import wx.adv
import wx.lib.agw.aui as aui

import time
# This working example of the use of OpenGL in the wxPython context
# was assembled in August 2012 from the GLCanvas.py file found in
# the wxPython docs-demo package, plus components of that package's
# run-time environment.

# Note that dragging the mouse rotates the view of the 3D cube or cone.

try:
    from wx import glcanvas
    haveGLCanvas = True
except ImportError:
    haveGLCanvas = False

try:
    # The Python OpenGL package can be found at
    # http://PyOpenGL.sourceforge.net/
    from OpenGL.GL import *
    from OpenGL.GLUT import *
    haveOpenGL = True
except ImportError:
    haveOpenGL = False

#----------------------------------------------------------------------
class App(Gui_principal, Model):
    def __init__(self, parent):        
        
        Gui_principal.__init__(self, parent)
        Model.__init__(self)        
        
        self.ConeCanvas = ConeCanvas(self)
        self.painelGerenciaPontos = PainelGerenciaPontos(self)
        
        
        self.PainelLateralDireito = ArvoreSelecaoElementos(self)
        self.toolbar_lateral = PainelSelecaoEsquerdo(self)
        
        
        self._mgr = aui.AuiManager()
        self._mgr.SetManagedWindow(self)       
        
        
        
        self._mgr.AddPane(self.PainelLateralDireito, aui.AuiPaneInfo().Right().Caption("Painel Elementos"))
        self._mgr.AddPane(self.toolbar_lateral, aui.AuiPaneInfo().Left().Caption("Painel de Selecao"))
        self._mgr.AddPane(self.painelGerenciaPontos, aui.AuiPaneInfo().Bottom().Caption("Pontos de Cotas"))
        self._mgr.AddPane(self.ConeCanvas, aui.AuiPaneInfo().CenterPane())
        
        pl = self._mgr.GetPane(self.PainelLateralDireito)
        pl.name = "painelLateralDireito"
        
        pl = self._mgr.GetPane(self.painelGerenciaPontos)
        pl.name = "painelGerenciaPontos"
        
        pl = self._mgr.GetPane(self.toolbar_lateral)
        pl.name = "painelLateralEsquerdo"
        
        self._mgr.Bind(aui.EVT_AUI_PANE_CLOSE, self.ClosePanels)
        
        
        
        
                
                
        #self.Show()
        
        #self.CallSplashScreem()

        
        
        
        self.SetImagensdDoApp()
        
        self.Centre()
        self.Show()
        
        self.Maximize(True)

        self.EnableAllButtons(False)
        
        self._mgr.Update()
        
        #self.splash.Destroy()
    
    def ClosePanels(self, event):
        namePanel = event.GetPane().name
        if namePanel == "painelLateralDireito":
            pass            
        elif namePanel == "painelGerenciaPontos":
            self.mostrar_painel_pontosCotas.Check(False)
            self.MOSTRAR_PAINEL_PONTOSCOTAS = False
        elif namePanel == "painelLateralEsquerdo":
            pass
        
    def CallSplashScreem(self):
        bitmap = wx.Bitmap('IMGs/image.png')
        self.splash = wx.adv.SplashScreen(bitmap, wx.adv.SPLASH_CENTER_ON_SCREEN|wx.adv.SPLASH_TIMEOUT,5000, self)
        self.splash.Show()
        
        time.sleep(5)        
        self.SetIcone()
        
    def SetIcone(self):
        """Define o ICONE da Janela do programa
        """        
        favicon = icone.GetIcon()
        wx.Frame.SetIcon(self, favicon)        
    
    def SetImagensdDoApp(self):
        """Define Todas as imagens da JanelaPrincipal do programa
        """
        self.toolbar.SetToolNormalBitmap(self.salvar.GetId(), icon_salvar.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.abrir.GetId(), icon_abrir.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.gerenciaModE.GetId(), icon_mod_elasticidade.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.gerenciaSecoes_I.GetId(), icon_iniercia.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.mostraNormal.GetId(), icon_normal.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.mostraCortante.GetId(), icon_cortante.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.mostraFletor.GetId(), icon_momento.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.mostraTorcor.GetId(), icones_momento_torcor_TCC_32x32.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.pan.GetId(), icon_pan_32x32.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.zoomAll.GetId(), icon_expandAll_32x32.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.orbit.GetId(), icon_orbit_32x32.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.seta_calcular.GetId(), icone_seta_calcular_32x32.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.btn_vista_esquerda.GetId(), vista_esquerda.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.m_tool15.GetId(), icon_vista_direita.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.m_tool16.GetId(), icone_vista_frontal.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.m_tool17.GetId(), icone_vista_posterior.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.m_tool18.GetId(), icone_vista_superior.GetBitmap())
        self.toolbar.SetToolNormalBitmap(self.m_tool19.GetId(), icone_vista_baixo.GetBitmap())
        
        #self.toolbar_lateral.auiToolbarSelecao.SetToolBitmap(1013, icon_seta_selecionar_32x32.GetBitmap())
        self.toolbar_lateral.auiToolbarSelecao.SetToolBitmap(1013, wx.Bitmap( u"IMGs/icone_setaSelecionar_sanepy.png", wx.BITMAP_TYPE_ANY ))
        #self.toolbar_lateral.auiToolbarSelecao.SetToolBitmap(1014, icon_barra_32x32.GetBitmap())
        self.toolbar_lateral.auiToolbarSelecao.SetToolBitmap(1014, wx.Bitmap( u"IMGs/icone_trecho_sanepy.png", wx.BITMAP_TYPE_ANY ))
        #self.toolbar_lateral.auiToolbarSelecao.SetToolBitmap(1015, icon_no_32x32.GetBitmap())
        self.toolbar_lateral.auiToolbarSelecao.SetToolBitmap(1015, wx.Bitmap( u"IMGs/icone_pv_sanepy.png", wx.BITMAP_TYPE_ANY ))
        #self.toolbar_lateral.auiToolbarSelecao.SetToolBitmap(1016, icone_excluir_barra_32x32.GetBitmap())
        self.toolbar_lateral.auiToolbarSelecao.SetToolBitmap(1016, wx.Bitmap( u"IMGs/icone_excluirTrecho_sanepy.png", wx.BITMAP_TYPE_ANY ))
        #self.toolbar_lateral.auiToolbarSelecao.SetToolBitmap(1017, icone_excluir_no_32x32.GetBitmap())
        self.toolbar_lateral.auiToolbarSelecao.SetToolBitmap(1017, wx.Bitmap( u"IMGs/icone_excluirPv_sanepy.png", wx.BITMAP_TYPE_ANY ))
        self.toolbar_lateral.auiToolbarSelecao.SetToolBitmap(1018, wx.Bitmap( u"IMGs/icone_perfil_sanepy.png", wx.BITMAP_TYPE_ANY ))
    
    def ShowModalMessage(self, event, mensagem, titulo_janela):
        dlg = wx.MessageDialog(None, mensagem , titulo_janela,
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        result = dlg.ShowModal() == wx.ID_YES
        dlg.Destroy()
        return result



    def MenuItemselect( self, event ):
        Id_Selecionado =  event.GetId()
        if Id_Selecionado == 1000:
            if self.VerificaSeHaProjetoAberto():
                if self.ShowModalMessage(event, "Deseja Salvar o Projeto Atual",
                                      "Aviso"):
                    #print ("PATH = %s" %self.path_arquivo)
                    salvaProjeto(self.Estrututura, event, self.path_arquivo)
                    self.CriaNovaEstrutura("PORTICO")
                else:
                    self.CriaNovaEstrutura("PORTICO")
            else:
                self.CriaNovaEstrutura("PORTICO")       
        
        elif Id_Selecionado == 1030:
            try:
                if self.VerificaSeHaProjetoAberto():
                    if self.ShowModalMessage(event, "Deseja Salvar o Projeto Atual",
                                          "Aviso"):
                        #print ("PATH = %s" %self.path_arquivo)
                        salvaProjeto(self.Estrututura, event, self.path_arquivo)
                        self.CriaNovaEstrutura("PORTICO")
                    else:
                        self.CriaNovaEstrutura("PORTICO")
                else:
                    self.CriaNovaEstrutura("PORTICO")
            except:
                #SE NAO HOUVER, NAO FAZ NADA
                pass
            
        elif Id_Selecionado == 1031:
            try:
               self.Abre_Arquivo(event) 
            except:
                pass
            
        elif Id_Selecionado == 1032:
            try:
               self.Destroy()
            except:
                pass            

    def OnCheckselect(self, evt):
        Id_Selecionado =  evt.GetId()

        #VERIFICA SE ESTA SELECIONADO PARA MOSTRAR PAINEL PONTOSCOTAS
        if Id_Selecionado == 1002:
            if self.mostrar_painel_pontosCotas.IsChecked():
                self.MOSTRAR_PAINEL_PONTOSCOTAS = True
                pl = self._mgr.GetPane(self.painelGerenciaPontos) 
                pl.Show()                 
                self._mgr.Update()
            else:
                self.MOSTRAR_PAINEL_PONTOSCOTAS = False
                pl = self._mgr.GetPane(self.painelGerenciaPontos) 
                pl.Hide()                 
                self._mgr.Update()

        #VERIFICA SE ESTA SELECIONADO PARA MOSTRAR CARGAS DISTRIBUIDAS
        elif Id_Selecionado == 1003:
            if self.mostrar_painel_elementos.IsChecked():
                self.painelGerenciaPontos.Hide()
                self.MOSTRAR_PAINEL_ELEMENTOS = True
            else:
                self.MOSTRAR_PAINEL_ELEMENTOS = False


        #VERIFICA SE ESTA SELECIONADO PARA MOSTRAR REACOES_DE_APOIOS
        elif Id_Selecionado == 1004:
            if self.mostrar_reacoes_apoios.IsChecked():
                self.MOSTRAR_REACOES_DE_APOIOS = True
            else:
                self.MOSTRAR_REACOES_DE_APOIOS = False


        #VERIFICA SE ESTA SELECIONADO PARA MOSTRAR ESFORCOS_NORMAIS
        elif Id_Selecionado == 1005:
            if self.normal.IsChecked():
                self.MOSTRAR_ESFORCOS_NORMAIS = True
            else:
                self.MOSTRAR_ESFORCOS_NORMAIS = False


        #VERIFICA SE ESTA SELECIONADO PARA MOSTRAR ESFORCOS_CORTANTES_Y
        elif Id_Selecionado == 1006:
            if self.cortante_y.IsChecked():
                self.MOSTRAR_ESFORCOS_CORTANTES_Y = True
            else:
                self.MOSTRAR_ESFORCOS_CORTANTES_Y = False


        #VERIFICA SE ESTA SELECIONADO PARA MOSTRAR ESFORCOS_CORTANTES_Z
        elif Id_Selecionado == 1007:
            if self.cortante_z.IsChecked():
                self.MOSTRAR_ESFORCOS_CORTANTES_Z = True
            else:
                self.MOSTRAR_ESFORCOS_CORTANTES_Z = False


        #VERIFICA SE ESTA SELECIONADO PARA MOSTRAR MOMENTOS_FLETORES_Y
        elif Id_Selecionado == 1008:
            if self.momento_y.IsChecked():
                self.MOSTRAR_MOMENTOS_FLETORES_Y = True
            else:
                self.MOSTRAR_MOMENTOS_FLETORES_Y = False

        #VERIFICA SE ESTA SELECIONADO PARA MOSTRAR MOMENTOS_FLETORES_Z
        elif Id_Selecionado == 1009:
            if self.momento_z.IsChecked():
                self.MOSTRAR_MOMENTOS_FLETORES_Z = True
            else:
                self.MOSTRAR_MOMENTOS_FLETORES_Z = False

        #VERIFICA SE ESTA SELECIONADO PARA MOSTRAR MOMENTOS_TORSORES
        elif Id_Selecionado == 1010:
            if self.torcor.IsChecked():
                self.MOSTRAR_MOMENTOS_TORSORES = True
            else:
                self.MOSTRAR_MOMENTOS_TORSORES = False


        #VERIFICA SE ESTA SELECIONADO PARA MOSTRAR ESTRUTURA_DEFORMADA
        elif Id_Selecionado == 1011:
            if self.estrutura_deformada.IsChecked():
                self.MOSTRAR_ESTRUTURA_DEFORMADA = True
            else:
                self.MOSTRAR_ESTRUTURA_DEFORMADA = False
                
        #VERIFICA SE ESTA SELECIONADO PARA MOSTRAR ESTRUTURA_INDEFORMADA
        elif Id_Selecionado == 1029:
            if self.estrutura_indeformada.IsChecked():
                self.MOSTRAR_ESTRUTURA_INDEFORMADA = True
                print (self.MOSTRAR_ESTRUTURA_INDEFORMADA)
            else:
                self.MOSTRAR_ESTRUTURA_INDEFORMADA = False
                print (self.MOSTRAR_ESTRUTURA_INDEFORMADA)

        #VERIFICA SE ESTA SELECIONADO PARA MOSTRAR TEXTOS_DESLOCAMENTOS
        elif Id_Selecionado == 1012:
            if self.deslocamentos_nodais.IsChecked():
                self.MOSTRAR_TEXTOS_DESLOCAMENTOS = True
            else:
                self.MOSTRAR_TEXTOS_DESLOCAMENTOS = False

        evt.Skip()

    def MenuElementosSelected( self, event):
        Id_Selecionado =  event.GetId()
        if Id_Selecionado == 1018:
            self.ExportaDados(event)
#            if self.VerificaSeHaNosSelecionados() == True:
#                try: #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DE GERENCIAMENTO DE NOS
#                    #SE TIVER ALGUMA INSTANCIA, FECHA
#                    self.JanelaGerenciaNo.OnClose()
#                except:
#                    #SE NAO HOUVER, NAO FAZ NADA
#                    pass
#
#                #ABRE UMA NOVA JANELA DE GERENCIAMENTO DE NOS
#                self.JanelaGerenciaNo = self.GerenciaNo(event, self.GetNosSelecionados(), "FORCAS")

        elif Id_Selecionado == 1019:
            if self.VerificaSeHaNosSelecionados() == True:
                try: #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DE GERENCIAMENTO DE NOS
                    #SE TIVER ALGUMA INSTANCIA, FECHA
                    self.JanelaGerenciaNo.OnClose()
                except:
                    #SE NAO HOUVER, NAO FAZ NADA
                    pass

                #ABRE UMA NOVA JANELA DE GERENCIAMENTO DE NOS
                self.JanelaGerenciaNo = self.GerenciaNo(event, self.GetNosSelecionados(), "RESTRICOES")

        elif Id_Selecionado == 1020:
            self.ExportaDados(event)
        
        

        elif Id_Selecionado == 1021:
            #ABRE UMA NOVA JANELA DE GERENCIAMENTO DE BARRAS
            self.GerenciaTrecho(event, self.GetBarrasSelecionadas(),"MATERIAL")

        elif Id_Selecionado == 1022:
            #ABRE UMA NOVA JANELA DE GERENCIAMENTO DE BARRAS
            self.GerenciaTrecho(event, self.GetBarrasSelecionadas(),"SECAO")

        elif Id_Selecionado == 1023:
            #ABRE UMA NOVA JANELA DE GERENCIAMENTO DE BARRAS
            self.GerenciaTrecho(event, self.GetBarrasSelecionadas(),"CARGA_Y")

        elif Id_Selecionado == 1024:
            #ABRE UMA NOVA JANELA DE GERENCIAMENTO DE BARRAS
            self.GerenciaTrecho(event, self.GetBarrasSelecionadas(),"CARGA_Z")

        elif Id_Selecionado == 1025:
            #ABRE UMA NOVA JANELA DE GERENCIAMENTO DE BARRAS
            self.GerenciaTrecho(event, self.GetBarrasSelecionadas(),"ALPHA")
            
        elif Id_Selecionado == 1034:
            #ABRE UMA NOVA JANELA DE GERENCIAMENTO DE BARRAS
            self.GerenciaTrecho(event, self.GetBarrasSelecionadas(),"ROTULAR")

        elif Id_Selecionado == 1026:
            #INVERTE O SENTIDO DAS BARRAS SELECIONADAS
            self.InverteSentidoBarras()

        elif Id_Selecionado == 1027:
            #ABRE JANELA DE OPCOES DE VISUALIZACAO
            JanelaOpcoesVisualizacao(self)
            
        elif Id_Selecionado == 1028:
            #ABRE JANELA DE OPCOES DE UNIDADES E FORMATOS
            try:
                #SE HOUVER ALGUMA INSTANCIA, FECHA
                self.JanelaOpcoesUnidades.OnClose()
            except:
                #SE NAO HOUVER, NAO FAZ NADA
                pass
    
            #ABRE UMA NOVA JANELA DE OPCOES E UNIDADES
            self.dlg_OpcoesUnidades = JanelaOpcoesUnidades(self)
        
        elif Id_Selecionado == 1033:
            #ABRE JANELA DE OPCOES DE UNIDADES E FORMATOS
            try:
                #SE HOUVER ALGUMA INSTANCIA, FECHA
                self.JanelaSobre.OnClose()
            except:
                #SE NAO HOUVER, NAO FAZ NADA
                pass
    
            #ABRE UMA NOVA JANELA DE OPCOES E UNIDADES
            self.JanelaSobre = AboutDlg(None)
            self.JanelaSobre.Show()

        elif Id_Selecionado == 1035:
            self.Exporta2PNG(event)
            
        elif Id_Selecionado == 1036:
            self.IMPORTADXF(event)
            
        elif Id_Selecionado == 1037:
            self.ON_PERFIL = [True,[None, None, None]]
            self.CriaJanelaPerfil()
            
        elif Id_Selecionado == 1038:
            print ("kkkkk")
            self.janelaDadosProjeto =  JanelaDadosDoProjeto(self)
            self.janelaDadosProjeto.Show()
            
    def OnSliderBarra(self, evt):
        """
        Funcao para pegar o valor da sliderBar para mostrar a escala da estrutura deformada e setar
        o coeficiente que a estrutura deformada devera ser mostrada
        """
        self.SetCoeficienteVisualizacaoMomentos(self.m_slider1.GetValue())

    def Calcula(self, evt):
        """
        Funcao para chamar a rotina de calculo da Estrutura.
        """        
        self.CalculaEstrutura()

    def SalvaArquivo(self, event):
        print ("Estauhxijahoucmowiioenhc")
        salvaProjeto(self.Estrututura, event, self.path_arquivo)
        
        event.Skip()

    def Abre_Arquivo(self, evt):
        """
        Funcao para abri o arquivo com a estrutura salva, utiliza o cPikle.
        """        
        self.AbrirArquivoTxt(evt)
        evt.Skip()        
        
    def SelecaoBtnLaterais(self, evt):
        """
        Funcao para gerenciar os ToggleButtons Laterais, onde se encontram os botoes
        selecionar, novoNo, novaBarra, exluirNo, excluirBarra,ect.
        """
        if evt.GetId() == 1013:
            self.FLAG_DESENHO = "SELECT"
            self.ConeCanvas.SetCursor(wx.Cursor(wx.CURSOR_DEFAULT))            
        elif evt.GetId() == 1014:
            self.FLAG_DESENHO = "BARRA"
            self.ConeCanvas.SetCursor(wx.Cursor(wx.CURSOR_DEFAULT))            
            
            print ("HABILITADO PARA DESENAR BARRAS")
            #Desabilita a janela de insercao de nos, caso esteja aberto
            #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DE INSERCAO DE COORDENADAS
            try:
                #SE TIVER ALGUMA INSTANCIA, FECHA
                self.dlg_insertCoord.OnClose()             

            except:
                #SE NAO HOUVER, NAO FAZ NADA
                pass


        elif evt.GetId() == 1015:
            self.FLAG_DESENHO = "NO"
            image = Crosshair_Cursor_Link.GetImage()
            image.SetOption(wx.IMAGE_OPTION_CUR_HOTSPOT_X, 14)
            image.SetOption(wx.IMAGE_OPTION_CUR_HOTSPOT_Y, 14)            
            self.ConeCanvas.SetCursor(wx.Cursor(image))

            #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DE INSERCAO DE COORDENADAS
            try:
                #SE TIVER ALGUMA INSTANCIA, FECHA
                self.dlg_insertCoord.OnClose()

            except:
                #SE NAO HOUVER, NAO FAZ NADA
                pass

        elif evt.GetId() == 1016:
            #Exclui apenas as BARRAS selecionadas            
            self.ExcluiElementosSelecionados("BARRA")
            
            
            

        elif evt.GetId() == 1017:
            #Exclui apenas os NOS selecionados
            self.ExcluiElementosSelecionados("NO")

        self.ConeCanvas.SetFocus()

    def ZoomAll(self, event):
        """
        Funcao para reenquadrar a estrutura no centro da tela novamente
        """
        print ("ZOOL ALL")
        self.ConeCanvas.ZoomAll(event)
        self.ConeCanvas.ParametrosVizualizacao()

    def GerenciaMateriais(self, evt):
        """
        Funcao que chama a Janela de Gerenciar Materiais, para criar ou editar novos materiais
        """
        #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DA JANELA DE GERENCIAMENTO DE MATERIAIS
        try:
            #SE TIVER ALGUMA INSTANCIA, FECHA
            self.janelaMateriais.OnClose(evt)
        except:
            #SE NAO HOUVER, NAO FAZ NADA
            pass

        self.janelaMateriais = ChangeDepthDialog(self )

    def GerenciaSecoes(self, evt):
        """
        Funcao que chama a Janela de Gerenciar Secoes, para criar ou editar novas SECOES.
        """
        #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DA JANELA DE GERENCIAMENTO DE SECOES
        try:
            #SE HOUVER ALGUMA INSTANCIA, FECHA
            self.dlg_gerenciaSecoes.OnClose(evt)
        except:
            #SE NAO HOUVER, NAO FAZ NADA
            pass

        self.dlg_gerenciaSecoes = dlgDefineGeometria(self)        

    def GerenciaTrecho(self, evt, trechoSelecionado, acao=None):
        """
        Funcao que chama a Janela de Gerenciar Trechos, para gerenciar
        os atributos dos trechos selecionadas.
        """
        #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DA JANELA DE GERENCIAMENTO DE BARRA
        try:
            #SE HOUVER ALGUMA INSTANCIA, FECHA
            self.propertyTrechos.OnClose()
        except:
            #SE NAO HOUVER, NAO FAZ NADA
            pass
        
        lista_trechos = []
        if len(trechoSelecionado) == 1:
            lista_trechos.append(
                   self.Estrututura.Dic_Lista_Tubulacoes[trechoSelecionado[0]])

        else:
            for trechoSel in trechoSelecionado:
                lista_trechos.append(
                   self.Estrututura.Dic_Lista_Tubulacoes[trechoSel])
                
        #ABRE UMA NOVA JANELA DE GERENCIAMENTO DE BARRAS
        self.propertyTrechos = JanelaPropTrechos(self, lista_trechos, acao)

    def GerenciaEstruturas(self, evt, PVsSelecionado, acao=None):
        """
        Funcao que chama a Janela de Gerenciar PVs, para gerenciar
        os atributos dos PVs selecionados.
        """
        #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DA JANELA DE GERENCIAMENTO
        #DE ESTRUTURAS        
        
        print ("PVsSelecionado = %s" %PVsSelecionado)
        try:
            #SE HOUVER ALGUMA INSTANCIA, FECHA
            self.DlgGerenciaEstrutura.OnClose()
        except:
            #SE NAO HOUVER, NAO FAZ NADA
            pass

        if len(PVsSelecionado)==1:
            numero_pv = PVsSelecionado[0]
            pv = self.Estrututura.Dic_Lista_Pvs[numero_pv]       
            #ABRE UMA NOVA JANELA DE GERENCIAMENTO DE BARRAS
            self.DlgGerenciaEstrutura = DlgGerenciaEstrutura(self, [pv], acao)
        elif len(PVsSelecionado)>1:
            lista_pvs = []
            for pvSel in PVsSelecionado:
                for pv in self.Estrututura.LISTA_PVS:
                    if pv.numero == noSel:
                        lista_pvs.append(pv)
            
            #ABRE UMA NOVA JANELA DE GERENCIAMENTO DE BARRAS
            self.DlgGerenciaEstrutura = DlgGerenciaEstrutura(self, lista_nos, acao)
    
    def GerenciaPerfis(self, evt, perfilSelecionado):        
        try:
            #SE HOUVER ALGUMA INSTANCIA, FECHA
            self.janelaGerenciaPerfil.OnClose()
        except:
            #SE NAO HOUVER, NAO FAZ NADA
            pass

        if len(perfilSelecionado)==1:
            numero_Perfil = perfilSelecionado[0]
            perfil = self.GetPerfilByNumber(numero_Perfil)       
            #ABRE UMA NOVA JANELA DE GERENCIAMENTO DE BARRAS
            self.janelaGerenciaPerfil = TreeListCtrlPerfil(self, perfil)
        

    def CriaJanelaPerfil(self):
        """
        Funcao que chama a Janela de Criar, Perfil"""
        #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DE CRIAR PERFIL
        try:
            #SE TIVER ALGUMA INSTANCIA, FECHA
            self.janeCriaPerfil.OnClose(evt)
        except:
            #SE NAO HOUVER, NAO FAZ NADA
            pass

        self.janeCriaPerfil = JanelaCriaPerfil(self)        
        
    def SelecionaModoPan(self, evt):
        self.FLAG_DESENHO = "PAN"
        evt.Skip()

    def MostrarEsforcosNormais( self, event ):
        self.MOSTRAR_CARGAS_CONCENTRADAS = False
        self.MOSTRAR_CARGAS_DISTRIBUIDAS = False
        self.MOSTRAR_REACOES_DE_APOIOS = False        
        self.MOSTRAR_ESFORCOS_NORMAIS = True
        self.MOSTRAR_ESFORCOS_CORTANTES_Y = False
        self.MOSTRAR_ESFORCOS_CORTANTES_Z = False
        self.MOSTRAR_MOMENTOS_FLETORES_Y = False
        self.MOSTRAR_MOMENTOS_FLETORES_Z = False
        self.MOSTRAR_MOMENTOS_TORSORES = False
        self.MOSTRAR_ESTRUTURA_DEFORMADA = False
        self.MOSTRAR_ESTRUTURA_INDEFORMADA = False
        self.MOSTRAR_TEXTOS_DESLOCAMENTOS = False
        
        self.mostrar_cargas_concentradas.Check(False)
        self.mostrar_cargas_distribuidas.Check(False)
        self.mostrar_reacoes_apoios.Check(False)
        self.normal.Check(True)
        self.cortante_y.Check(False)
        self.cortante_z.Check(False)
        self.momento_y.Check(False)
        self.momento_z.Check(False)
        self.torcor.Check(False)
        self.estrutura_deformada.Check(False)
        self.estrutura_indeformada.Check(False)
        self.deslocamentos_nodais.Check(False)
        
        event.Skip()
	
    def MostrarEsforcosCortantes( self, event ):
        self.MOSTRAR_CARGAS_CONCENTRADAS = False
        self.MOSTRAR_CARGAS_DISTRIBUIDAS = False
        self.MOSTRAR_REACOES_DE_APOIOS = False        
        self.MOSTRAR_ESFORCOS_NORMAIS = False
        self.MOSTRAR_ESFORCOS_CORTANTES_Y = True
        self.MOSTRAR_ESFORCOS_CORTANTES_Z = True
        self.MOSTRAR_MOMENTOS_FLETORES_Y = False
        self.MOSTRAR_MOMENTOS_FLETORES_Z = False
        self.MOSTRAR_MOMENTOS_TORSORES = False
        self.MOSTRAR_ESTRUTURA_DEFORMADA = False
        self.MOSTRAR_ESTRUTURA_INDEFORMADA = False
        self.MOSTRAR_TEXTOS_DESLOCAMENTOS = False
        
        self.mostrar_cargas_concentradas.Check(False)
        self.mostrar_cargas_distribuidas.Check(False)
        self.mostrar_reacoes_apoios.Check(False)
        self.normal.Check(False)
        self.cortante_y.Check(True)
        self.cortante_z.Check(True)
        self.momento_y.Check(False)
        self.momento_z.Check(False)
        self.torcor.Check(False)
        self.estrutura_deformada.Check(False)
        self.estrutura_indeformada.Check(False)
        self.deslocamentos_nodais.Check(False)
        
        event.Skip()
	
    def MostrarMomentosFletores( self, event ):
        self.MOSTRAR_CARGAS_CONCENTRADAS = False
        self.MOSTRAR_CARGAS_DISTRIBUIDAS = False
        self.MOSTRAR_REACOES_DE_APOIOS = False        
        self.MOSTRAR_ESFORCOS_NORMAIS = False
        self.MOSTRAR_ESFORCOS_CORTANTES_Y = False
        self.MOSTRAR_ESFORCOS_CORTANTES_Z = False
        self.MOSTRAR_MOMENTOS_FLETORES_Y = True
        self.MOSTRAR_MOMENTOS_FLETORES_Z = True
        self.MOSTRAR_MOMENTOS_TORSORES = False
        self.MOSTRAR_ESTRUTURA_DEFORMADA = False
        self.MOSTRAR_ESTRUTURA_INDEFORMADA = False
        self.MOSTRAR_TEXTOS_DESLOCAMENTOS = False
        
        self.mostrar_cargas_concentradas.Check(False)
        self.mostrar_cargas_distribuidas.Check(False)
        self.mostrar_reacoes_apoios.Check(False)
        self.normal.Check(False)
        self.cortante_y.Check(False)
        self.cortante_z.Check(False)
        self.momento_y.Check(True)
        self.momento_z.Check(True)
        self.torcor.Check(False)
        self.estrutura_deformada.Check(False)
        self.estrutura_indeformada.Check(False)
        self.deslocamentos_nodais.Check(False)
        event.Skip()
	
    def MostrarMomentosTorsores( self, event ):
        self.MOSTRAR_CARGAS_CONCENTRADAS = False
        self.MOSTRAR_CARGAS_DISTRIBUIDAS = False
        self.MOSTRAR_REACOES_DE_APOIOS = False        
        self.MOSTRAR_ESFORCOS_NORMAIS = False
        self.MOSTRAR_ESFORCOS_CORTANTES_Y = False
        self.MOSTRAR_ESFORCOS_CORTANTES_Z = False
        self.MOSTRAR_MOMENTOS_FLETORES_Y = False
        self.MOSTRAR_MOMENTOS_FLETORES_Z = False
        self.MOSTRAR_MOMENTOS_TORSORES = True
        self.MOSTRAR_ESTRUTURA_DEFORMADA = False
        self.MOSTRAR_ESTRUTURA_INDEFORMADA = False
        self.MOSTRAR_TEXTOS_DESLOCAMENTOS = False
        
        self.mostrar_cargas_concentradas.Check(False)
        self.mostrar_cargas_distribuidas.Check(False)
        self.mostrar_reacoes_apoios.Check(False)
        self.normal.Check(False)
        self.cortante_y.Check(False)
        self.cortante_z.Check(False)
        self.momento_y.Check(False)
        self.momento_z.Check(False)
        self.torcor.Check(True)
        self.estrutura_deformada.Check(False)
        self.estrutura_indeformada.Check(False)
        self.deslocamentos_nodais.Check(False)
        event.Skip()


    def ViewCameraTop(self, evt):
        self.ViewTop()
        evt.Skip()

    def EnableAllButtons(self, Flag=True):
        """
        Funcao que habilita e desabilita todos os botoes da janela
        Caso nao seja passado nenhuma FLAG, entao adota TRUE e habilita todos.
        """
        #DESABILITA OS BOTOES DA TOOLBAR
        self.toolbar.EnableTool(self.salvar.GetId(), Flag)
        self.toolbar.EnableTool(self.abrir.GetId(), Flag)
        self.toolbar.EnableTool(self.gerenciaModE.GetId(), Flag)
        self.toolbar.EnableTool(self.gerenciaSecoes_I.GetId(), Flag)
        self.toolbar.EnableTool(self.mostraNormal.GetId(), Flag)
        self.toolbar.EnableTool(self.mostraCortante.GetId(), Flag)
        self.toolbar.EnableTool(self.mostraFletor.GetId(), Flag)
        self.toolbar.EnableTool(self.mostraTorcor.GetId(), Flag)
        self.toolbar.EnableTool(self.pan.GetId(), Flag)
        self.toolbar.EnableTool(self.zoomAll.GetId(), Flag)
        self.toolbar.EnableTool(self.orbit.GetId(), False)
        self.toolbar.EnableTool(self.seta_calcular.GetId(), Flag)

        if Flag == True:
            #HABILITA OS BOTOES DA LATERAL ESQUERDA
            self.toolbar_lateral.auiToolbarSelecao.EnableTool(self.toolbar_lateral.btnToogleSelecionar.GetId(), Flag)
            self.toolbar_lateral.auiToolbarSelecao.EnableTool(self.toolbar_lateral.btnToogleBarra.GetId(), Flag)
            self.toolbar_lateral.auiToolbarSelecao.EnableTool(self.toolbar_lateral.btnToogleNo.GetId(), Flag)
            self.toolbar_lateral.auiToolbarSelecao.EnableTool(self.toolbar_lateral.btnToogleExcluirBarra.GetId(), Flag)
            self.toolbar_lateral.auiToolbarSelecao.EnableTool(self.toolbar_lateral.btnToogleExcluirNo.GetId(), Flag)
            self.toolbar_lateral.auiToolbarSelecao.EnableTool(self.toolbar_lateral.btnTooglePerfil.GetId(), Flag)
        elif Flag == False:
            #DESABILITA OS BOTOES DA LATERAL ESQUERDA
            self.toolbar_lateral.auiToolbarSelecao.EnableTool(self.toolbar_lateral.btnToogleSelecionar.GetId(), Flag)
            self.toolbar_lateral.auiToolbarSelecao.EnableTool(self.toolbar_lateral.btnToogleBarra.GetId(), Flag)
            self.toolbar_lateral.auiToolbarSelecao.EnableTool(self.toolbar_lateral.btnToogleNo.GetId(), Flag)
            self.toolbar_lateral.auiToolbarSelecao.EnableTool(self.toolbar_lateral.btnToogleExcluirBarra.GetId(), Flag)
            self.toolbar_lateral.auiToolbarSelecao.EnableTool(self.toolbar_lateral.btnToogleExcluirNo.GetId(), Flag)
            self.toolbar_lateral.auiToolbarSelecao.EnableTool(self.toolbar_lateral.btnTooglePerfil.GetId(), Flag)
        
        self._mgr.Update()
            
    def AtualizaCoefVisualizacao( self, event ):
        self.m_slider1.SetMin(int(self.txt_min_coef.GetValue()))
        self.m_slider1.SetMax(int(self.txt_max_coef.GetValue()))
        event.Skip()
    
    def OnClose(self, event):
        if self.ShowModalMessage(event, "Tem certeza que deseja encerrar o \
                                            programa ?", "Atencao"):
            self.Destroy()
        
if __name__ == '__main__':
    app = wx.App(False)
    App(None)
    app.MainLoop()
