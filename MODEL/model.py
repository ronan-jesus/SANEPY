# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ronan
#
# Created:     19/12/2016
# Copyright:   (c) Ronan 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import division

import numpy as np
from CALCULOS import calculos_Principais
from CALCULOS import estruturas_PVs
from AUXILIARES.menssagens import *
from AUXILIARES.ImportDXF_ezdxf import ImportaArquivoDXF, AbrirArquivo
from AUXILIARES.ExportaDXF_ezdxf import DXFExport
from ImportDXFCurvasNiveis import *
from AUXILIARES.Funcoes_de_Arquivos import *# salvaImagem
#from Funcoes_de_Arquivos import OnOpen
from ImportDXFCurvasNiveis import Terreno
from GRAFICOS.perfilLongitudinal import PerfilLongitudinal
from AUXILIARES.exportaExcel import ExportaEstruturaExcel
from collections import OrderedDict

class Model(object):
    
    def __init__(self):
        self.LINHAS = []
        self.onCommand = None        
        #IDs_PREDEFINIDOS PARA BOTOES
        #self.terreno = Terreno()
        self.ID_BTN_SELECIONAR = 301
        self.ID_BTN_BARRA = 302
        self.ID_BTN_NO = 303
        self.ID_BTN_EXCLUIR_BARRA = 304
        self.ID_BTN_EXCLUIR_NO = 305

        self.ID_MENU_ITEM_PORTICO3D = 401
        self.ID_MENU_ITEM_TRELICA3D = 402


        self.ID_MENU_ITEM_MOSTRAR_CARGASCONCENTRADAS = 501
        self.ID_MENU_ITEM_MOSTRAR_CARGASDISTRIBUIDAS = 502
        self.ID_MENU_ITEM_MOSTRAR_REACOESDEAPOIOS = 509

        self.ID_MENU_ITEM_MOSTRAR_ESFORCOSNORMAIS = 504
        self.ID_MENU_ITEM_MOSTRAR_ESFORCOSCORTANTEYY = 505
        self.ID_MENU_ITEM_MOSTRAR_ESFORCOSCORTANTEZZ = 510
        self.ID_MENU_ITEM_MOSTRAR_MOMENTOSFLETORESY = 506
        self.ID_MENU_ITEM_MOSTRAR_MOMENTOSFLETORESZ = 511
        self.ID_MENU_ITEM_MOSTRAR_MOMENTOSTORCORES = 507

        self.ID_MENU_ITEM_MOSTRAR_ESTRUTURA_DEFORMADA = 503
        self.ID_MENU_ITEM_MOSTRAR_ESTRUTURA_DEFORMADA = 503
        self.ID_MENU_ITEM_MOSTRAR_TEXTO_DESLOCAMENTOS = 508

        #CONSTANTES DE VISUALIZACAO
        self.MOSTRAR_NOS = True
        self.MOSTRAR_NUMERCAO_NOS = False
        self.MOSTRAR_RESTRICOES_NODAIS = True
        self.TAMANHO_DOS_NOS = 6
        self.TAMANHO_DOS_VINCULOS = 1.0

        self.MOSTRAR_BARRAS = True
        self.MOSTRAR_NUMERCAO_BARRAS = True
        self.MOSTRAR_EIXOS_BARRAS = True
        self.MOSTRAR_SECOES_BARRAS = False
        self.TAMANHO_EIXOS_BARRAS = 0.5
        self.MOSTRAR_EIXOS_GLOBAIS = True
        self.TAMANHO_EIXOS_GLOBAIS = 1
        self.POSICAO_EIXOS_GLOBAIS = [0,0,0]

        self.TAMANHO_CARGAS_DISTRIBUIDAS = 1
        self.TAMANHO_CARGAS_CONCENTRADAS = 1


        #VARIAVEIS DE CONTROLE DE DESENHO
        self.TIPO_ESTRUTURA = "TRELICA_ESPACIAL"
        self.COORDS_ATUAIS = [0.0, 0.0, 0.0]
        self.STATUS_BARRA = 1
        self.ON_BARRA = [-1, -1] #Nos de entrada da barra [No1, No2]
        self.TIPO_COORDS = "GLOBAL"  #Tipo de Coordenadas (GLOBAL OU RELATIVO)
        #MOSTRAR SOLICITACOES NOS ELEMENTOS
        self.MOSTRAR_PAINEL_PONTOSCOTAS = True
        self.MOSTRAR_PAINEL_ELEMENTOS = True
        self.MOSTRAR_REACOES_DE_APOIOS = False
        self.MOSTRAR_ESFORCOS_NORMAIS = False
        self.MOSTRAR_ESFORCOS_CORTANTES_Y = False
        self.MOSTRAR_ESFORCOS_CORTANTES_Z = False
        self.MOSTRAR_MOMENTOS_FLETORES_Y = False
        self.MOSTRAR_MOMENTOS_FLETORES_Z = False
        self.MOSTRAR_MOMENTOS_TORSORES = False
        self.MOSTRAR_ESTRUTURA_DEFORMADA = False
        self.MOSTRAR_ESTRUTURA_INDEFORMADA = False
        self.MOSTRAR_TEXTOS_DESLOCAMENTOS = True
        

        #COEFICIENTES PARA AUMENTAR A VISUALIZACAO NA JANELA DE DESENHO
        self.COEF_VISUALIZACAO_MOMENTOS = 1000

        #Flag para definicaoo da funcao atual de desenho (Selecionar, desenhar barra ou desenhar NO)
        self.FLAG_DESENHO = "SELECT"
        self.FLAG_SNAP = True
        #Variaveis
        self.Estrututura = None
        self.selected = []
        self.RecSelect = [None, None, None, None]
        self.selectedSnap = [None]

        self.materialEmUso = None
        self.secaoEmUso = None

        self.path_arquivo = None

        #Unidades de Medidas e Formatos
        self.UnidadeComprimento = "[m] - Metro"
        self.UnidadeForca = "[kN] - Kilo Newton"
        self.UnidadeAngulo = "Rad"
        self.FormatoComprimento = "x.xx"
        self.FormatoForca = "x.xx"
        self.FormatoAngulo = "x.xx"

        #Textos das Unidades de Medidas
        self._TextoUnidadeComprimento = "m"
        self._TextoUnidadeForca = "kN"
        self.TextoUnidadeTorque = "kN.m"
        self.TextoUnidadeCargaDistribuida = "kN/m"

        #Coeficientes para Transformar unidades em Metros
        self.coef_MedidaLinear = 1
        
        self.emDesenvolvimento = False    
        
        self.LISTA_PERFIS = []
        
        self.PERFIL = PerfilLongitudinal
        
        self.OBJETO_SELECIONADO = False
        self.ON_PERFIL = [False]
        
    def AbrirArquivoTxt(self, evt):
        if self.VerificaSeHaProjetoAberto():
            if self.ShowModalMessage(evt, "Deseja Salvar o Projeto Atual",
                                  "Aviso"):
                #print ("PATH = %s" %self.path_arquivo)
                salvaProjeto(self.Estrututura, evt, self.path_arquivo)
                self.CriaNovaEstrutura("PORTICO")
            else:
                self.CriaNovaEstrutura("PORTICO")
        else:
            self.CriaNovaEstrutura("PORTICO")
        
        arquivo = OnOpen(evt)
        
        self.Estrututura = arquivo[0]
        self.path_arquivo = arquivo[1]
        
        self.ConeCanvas.AtualizaTodasAsGlList()
        
    def AdicionaElementosListaSelecao(self, lista_elementos, evt):
        """Adiciona novos elementos selecionados na lista de selecao
           cumulativamente se o botao de controle crtl(cmd) estiver
           pressionado.
           
           Se o botao SHIFT estiver pressionado, faz a deselecao de elementos
           que estavam selecionados, ou seja na retira da lista de selecao a
           lista de elementos que foi passado como parametro para a funca.
           
           Se nao houver nenhum botao de controle pressionado, substitui toda
           a lista de selecao pela lista de selecao passada para a funcao.            
        """
        #self.VerificaCliqueBotaoEsquerdo()
        
        if evt.CmdDown():
            self.selected += lista_elementos            
            self.selected = map(list, OrderedDict.fromkeys(
                                            map(tuple, self.selected)).keys())
        elif evt.ShiftDown():
            if len([x for x in lista_elementos if x in self.selected])>0:
                self.selected = [x for x in self.selected \
                                                   if x not in lista_elementos]
        else:
            self.selected = lista_elementos
    
    def CalculaEstrutura(self):
        """ Chama as funcoes para calcular a Estrutura. Antes, faz as
            verificacoes necessarias para que a estrutura esteja em condicoes
            de ser processada sem erros.
        """
        if self.VerificaEstrutura() == False:
            self.Estrututura.CalculaEstrutura()
            if len(self.Estrututura.ERROS_ESTRUTURA) == 0:
                self.ConeCanvas.AtualizaTodasAsGlList()
            else:
                if 5001 in self.Estrututura.ERROS_ESTRUTURA:
                    tituloJanela = u"Nao Foi Possivel Processar o Calculo da Estrutura"
                    mes1 = u"Estrutura Instavel, verifique as condições de contorno \n\n"
                    mes2 = u"Verifique as vinculaçoes Externas e Internas da Estrutura \n"
                    mes = mes1+mes2
                    MostraMensagemErro(mes, tituloJanela)
        else:
            erros = self.VerificaEstrutura()
            mensagem = []
            if len(erros["ERRO_MATERIAL"]) > 0:
                mensagem.append(u"Barras sem definição de Material: " +str(erros["ERRO_MATERIAL"]))

            if len(erros["ERRO_SECAO"]) > 0:
                mensagem.append(u"Barras sem definição de Seção: " +str(erros["ERRO_SECAO"]))

            mes = u"MOTIVOS: \n\n"
            tituloJanela = u"Nao Foi Possivel Processar o Calculo da Estrutura"
            for iten in mensagem:
                mes += iten+"\n"+"\n"
            MostraMensagemErro(mes, tituloJanela)
            
    def ClickSelect(self, x, y, evt, canvas):
        """Select com o click simples do botao esquerdo do mouse
        """                
        if self.RecSelect[2:4] == [None, None]:
            canvas.pickRects(x, y, evt, retangulo=[])        
            
    def CriaBarra(self, ELEM_SELEC):
        """Cria barra com o click do botao direito do mouse
        """        
        try:
            if (len(ELEM_SELEC)==1 and ELEM_SELEC[0][0]==1):
                numPVselecionado = ELEM_SELEC[0][1]
                if (self.STATUS_BARRA == 1):
                    self.ON_BARRA[0] = numPVselecionado
                    self.STATUS_BARRA = 2
                elif (self.STATUS_BARRA == 2 and numPVselecionado != self.ON_BARRA[0]):
                    self.ON_BARRA[1] = numPVselecionado
                    self.STATUS_BARRA = 1
    
                    #Adiciona Barra na Estrutura
                    NO1, NO2 = self.ON_BARRA[0], self.ON_BARRA[1]
                    
                    pv1 = self.Estrututura.Dic_Lista_Pvs[NO1]
                    pv2 = self.Estrututura.Dic_Lista_Pvs[NO2]
                    
                    tubo_aux = calculos_Principais.Tubo([pv1,pv2])
                        
                    ################ OTIMIZAR ESTA ETAPA ####################
                    self.Estrututura.AdicionaTubo(tubo_aux)
                    self.Estrututura.Dic_Lista_Tubulacoes[tubo_aux.numero] = tubo_aux
                    self.PainelLateralDireito.AdicionaBarraTreeCtrl(tubo_aux)
                    
                    self.ConeCanvas.AtualizaDesenhoTubos()
                    self.ConeCanvas.AtualizaDesenhoEixosBarras()
                    self.LimpaSelecao()
                else:
                    self.selected = []
                    self.ON_BARRA = [-1, -1]
                
        except Exception as e:
            if self.emDesenvolvimento == True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
            else:
                pass
    
    def CriaNovaEstrutura(self, tipo_estrutura):
        if tipo_estrutura == "PORTICO":
            if hasattr(self, "Estrututura"):
                del(self.Estrututura)
                self.Estrututura = calculos_Principais.App() #ESTRUTURA DO ARQUIVO DE PORTICO ESPACIAL
                
                self.EnableAllButtons(True)
                self.TIPO_ESTRUTURA = "PORTICO_ESPACIAL"
                self.Estrututura.UnidadeComprimento = self.UnidadeComprimento
                self.Estrututura.UnidadeComprimento = self.UnidadeForca
                
                #self.IMPORTADXF(None, "C:\PROGRAMAS PYTHON\SANEPY\Projetos\SANEPY\ARQUIVOS/ficticea_esgoto.dxf")
            
            else:
                if self.emDesenvolvimento == True:
                    print ("ERRO AO CRIAR O ARQUIVO PORTICO")
                else:
                    pass
                

        self.path_arquivo = None
        self.ConeCanvas.AtualizaTodasAsGlList()
    
    def CriaPerfil(self, x_mundo, y_mundo):        
        NomePerfil = self.ON_PERFIL[1][0]
        pvInicio = int(self.ON_PERFIL[1][1])
        pvfinal = int(self.ON_PERFIL[1][2])
        
        _trechos = self.Estrututura.VerificaCaminho(pvInicio, pvsChegada=[pvfinal])
        
        _num = len(self.LISTA_PERFIS)+1
        
        newPerfil  = PerfilLongitudinal(self, [x_mundo, y_mundo], nomePerfil=NomePerfil, trechos=_trechos, num=_num)
        self.LISTA_PERFIS.append(newPerfil)
        self.ON_PERFIL = [False,[None, None, None]]        
        
    def DeselecionarElementosNaTreeCtrl(self, EstruturasDeselecionadas):
        """Tira da lista selecao os elementos selecionados na TreeCtrl de 
           exibicao dos elementos
        """
        itemsDeselecionar = []
        itemsDeselecionar += [[1, x] for x in EstruturasDeselecionadas["PVs"]]
        itemsDeselecionar += [[2, x] for x in EstruturasDeselecionadas["TRECHOS"]]
        
        for item in itemsDeselecionar:
            if item in self.selected:                
                self.selected.remove(item)   
        
        self.selected = [list(item) for item in set(tuple(row) for row in self.selected)]
        self.ConeCanvas.AtualizaDesenhoTodosElementos
        
    def DrawRetangulo(self, x1, y1, x2, y2):
        try:
            l = (x2-x1)

            xp1 = x1
            yp1 = y1

            xp2 = (x1+l)
            yp2 = (y1)

            xp3 = (x2)
            yp3 = (y2)

            xp4 = (x2-l)
            yp4 = (y2)

            return [[0,0],[xp1,yp1],[xp2,yp2],[xp3,yp3],[xp4,yp4]]
        except:
            pass

    def ExcluiElementosSelecionados(self, tipoelemento=None):
        listaTubos_selecionados = self.GetBarrasSelecionadas()
        listaPVs_selecionados = self.GetNosSelecionados()
        listaPerfis_selecionados = self.GetPerfisSelecionados()

        lista_tubos_excluir = []
        listaPVs_excluir = []
        
        if tipoelemento in ["BARRA","TUDO"]:
            for numTubo in listaTubos_selecionados:                
                lista_tubos_excluir.append(self.Estrututura.Dic_Lista_Tubulacoes[numTubo])
            
            self.Estrututura.ExcluirTubo(lista_tubos_excluir)
            self.LimpaSelecao()
            self.PainelLateralDireito.DeleteBarraTreeCtrl(self.Estrututura.LISTA_TUBULACOES)

        if tipoelemento in ["NO","TUDO"]:
            for pv in listaPVs_selecionados:                
                    listaPVs_excluir.append(self.Estrututura.Dic_Lista_Pvs[pv])
            self.Estrututura.ExcluirPv(listaPVs_excluir)
            self.PainelLateralDireito.DeleteNoTreeCtrl(self.Estrututura.LISTA_PVS)
            
        if tipoelemento in ["PERFIL","TUDO"]:
            for perfil in self.LISTA_PERFIS:
                if perfil.numero in listaPerfis_selecionados:
                    self.LISTA_PERFIS.remove(perfil) 
        
        self.ConeCanvas.AtualizaDesenhoTodosElementos()
        
    def Exporta2PNG(self, event):
        path = salvaImagem(event)
        self.ConeCanvas.Pyopengl2PNG(path)
     
    def ExportaDados(self, event):
        ExportaEstruturaExcel(self, self.Estrututura, event)
    
    def Get_Coef_MedidaLinear(self):
        """
        Retorna o coeficiente para transformar as medidas em Metros conforme
        a unidade de medida especificada
        """
        if  self.UnidadeComprimento == "[m] - Metro":
            return 1
        elif self.UnidadeComprimento == "[cm] - Centimetro":
            return 100
        elif self.UnidadeComprimento == "[mm] - milimetro":
            return 1000
        elif self.UnidadeComprimento == "[ft] - Pes":
            return 1/0.3048
        elif self.UnidadeComprimento == "[in] - Polegada":
            return 1/0.0254
    
    def Get_Coef_MedidaForca(self):
        """
        Retorna o coeficiente para transformar as medidas em Metros conforme
        a unidade de medida especificada
        """
        if self.UnidadeForca == "[kN] - Kilo Newton":
            return 1
        elif self.UnidadeForca == "[lb] - Libra":
            return 224.8089431
        elif self.UnidadeForca == "[klb] -Kilo Libra":
            return 0.2248089431
        elif self.UnidadeForca == "[N] - Newton":
            return 1000
        elif self.UnidadeForca == "[kgf] - Kilo Grama Forca":
            return 101.9716213
        elif self.UnidadeForca == "[Tonf] - Tonelada Forca":
            return 0.1019716213
            
    def GetBarrasSelecionadas(self):
        """Retorna uma lista com os numeros dos TRECHOS que estao na lista de
           selecao.
        """
        listaselecao = []
        if self.selected != None:
            for objeto in self.selected:
                if (len(objeto) == 4 and objeto[0] == 3 and objeto[2] == 2):                    
                    listaselecao.append(objeto[3])
                elif (len(objeto) == 2 and objeto[0] == 2):                    
                    listaselecao.append(objeto[1])
                    
        return set(listaselecao)
        #return [x[1] for x in self.selected if x[0] == 2]
            
    def GetNosSelecionados(self):
        """Retorna uma lista com os numeros dos PVs que estao na lista de
           selecao.
        """
        listaselecao = []
        if self.selected != None:
            for objeto in self.selected:
                if (len(objeto) == 4 and objeto[0] == 3 and objeto[2] == 1):
                    listaselecao.append(objeto[3])
                elif (len(objeto) == 2 and objeto[0] == 1):
                    listaselecao.append(objeto[1])
            
        return set(listaselecao)
        #return [x[1] for x in self.selected if x[0] == 1]    
        
    def GetPerfisSelecionados(self):
        """Retorna uma lista com os numeros dos Perfis que estao na lista de
           selecao.
        """
        listaselecao = []
        if self.selected != None:
            for objeto in self.selected:
                if (len(objeto) == 2 and objeto[0] == 3):
                    listaselecao.append(objeto[1])                
            
        return set(listaselecao)        
    
    def GetObjetoSelecionado(self, select):        
        for perfil in self.LISTA_PERFIS:
            if (perfil.numero == select[1]):
                return perfil
    
    def GetTypeSelection(self):
        selection = self.selected
        len_selection = len(selection)        
        
        if len_selection == 0:
            return "NADA"
        elif len_selection == 1:
            if (len(selection[0]) == 2 and selection[0][0] == 1):
                return "PV"
            elif (len(selection[0]) == 2 and selection[0][0] == 2):
                return "TRECHO"
            elif (len(selection[0]) == 3 and selection[0][2] == 1):
                return "PV_MOVER"
            elif (len(selection[0]) == 3 and selection[0][2] == 2):
                return "PV_ROTACIONAR"
            elif (len(selection[0]) == 3 and selection[0][2] == 3):
                return "LABEL_MOVER"
            elif (len(selection[0]) == 3 and selection[0][2] == 4):
                return "TICK_TOP_PV"
            elif (len(selection[0]) == 3 and selection[0][2] == 5):
                return "TICK_BOTTOM_PV"
        
        elif len_selection > 1:
            return "VARIOS_ELEMENTOS"
                
    def GetPerfilByNumber(self, numPerfil):
        """Retorna o objeto do tipo PERFIL que o numero seja igual ao parametro
           passado na funcao
        """
        for perfil in self.LISTA_PERFIS:
            if perfil.numero == numPerfil:
                return perfil        
        return None
    
    def IMPORTADXF(self, event, path=None):
        DXFExport(self)
        
        
#        path =  AbrirArquivo(event, "*dxf")
#        self.dadosDXF = ImportaArquivoDXF(path)    
#        self.PopulaTreeCtrl()
#        self.Regeneration()

    def InsereNoEstrutura(self):
        coordNo = list(self.COORDS_ATUAIS)
        if self.TIPO_COORDS == "GLOBAL":
            pass
        elif self.TIPO_COORDS == "RELATIVO":
            if (self.selectedSnap[0] == None or len(self.Estrututura.LISTA_PVS) == 0):
                if len(self.Estrututura.LISTA_PVS) != 0:
                    return #Caso a estrutura nao contenha NOS encerra o fluxo da
                           #da funcao pois nao foi clicado em um NO (Relativo)
            else:
                NO_Snap = self.Estrututura.Dic_Lista_Pvs[self.selectedSnap[0]]
                coordNo = np.add(coordNo, NO_Snap.pos)

        #VERIFICA QUAL O TIPO DA ESTRUTURA - PARA VER SE VAI USAR NO DE PORTICO OU DE TRELICA
        ################ INICIO OTIMIZAR ESTA ETAPA #################################
        if self.TIPO_ESTRUTURA == "PORTICO_ESPACIAL":
            no_aux = calculos_Principais.NO(coordNo, [self.UnidadeComprimento,
                                                    self.UnidadeForca])       
        ################ FINAL OTIMIZAR ESTA ETAPA #################################

        self.Estrututura.AdicionaNO(no_aux)
        self.Estrututura.Dic_Lista_Pvs[no_aux.numero] = no_aux
        
        if no_aux.numero != None:
            self.PainelLateralDireito.AdicionaNOTreeCtrl(no_aux)
    
    def InserePV(self, x, y):
        if hasattr(self, "terreno"):
            ct = self.terreno.Get_Z(x,y)
        else:
            ct = 0.0
            
        coordPv = np.array([x, y, 0])        
        pv_aux = estruturas_PVs.PV_Retangular(coordPv, CT=ct)
        self.Estrututura.AdicionaPV(pv_aux)
        self.Estrututura.Dic_Lista_Pvs[pv_aux.numero] = pv_aux
        self.PainelLateralDireito.AdicionaNOTreeCtrl(pv_aux)
    
    def InverteSentidoBarras(self):
        """ Faz a inversao do sentidos das barras selecionadas
            Chamando a funcao InverteDirecaoBarra() de cada barra da lista"""
        trechosSelecionados = self.GetBarrasSelecionadas()
        for trecho in self.Estrututura.LISTA_TUBULACOES:
            if trecho.numero+1000 in trechosSelecionados:
                trecho.InverteDirecaoTubo()

        self.ConeCanvas.AtualizaDesenhoTubos()
    
    def LimpaSelecao(self):
        """ Esvazia Lista de Selecao Atual"""
        self.selected = []
        self.ON_BARRA = [-1, -1]
        self.OBJETO_SELECIONADO = False
        self.Estrututura.PV.LimpaStatus()
        self.Estrututura.TRECHO.LimpaStatus()
        self.ConeCanvas.AtualizaDesenhoTodosElementos()
        
    def Regeneration(self):
       self.ConeCanvas.AtualizaTodasAsGlList()
       self.ConeCanvas.ParametrosVizualizacao()
    
    def PopulaTreeCtrl(self):
        """Faz o preenchimento da TreeCtrl no Painel Laretal Direito, com os
           Grupos de elementos
        """
        self.PainelLateralDireito.CriaTreeCrlt(self.Estrututura.LISTA_PVS, self.Estrututura.LISTA_TUBULACOES)
        
    def SelecionaelementosNaTreeCtrl(self, EstruturasSelecionadas):
        """Coloca na lista de selecao os elementos selecionadas na TreeCtrl
           de exibicao dos elementos
        """
        if len(EstruturasSelecionadas["PVs"]) != 0:
            self.selected += [[1, x] for x in EstruturasSelecionadas["PVs"]]
        
        if len(EstruturasSelecionadas["TRECHOS"]) != 0:
            self.selected += [[2, x] for x in EstruturasSelecionadas["TRECHOS"]]        
        
        self.selected = [list(item) for item in set(tuple(row) for row in self.selected)]
        
        self.ConeCanvas.AtualizaDesenhoTodosElementos()
        
    def SetCoeficienteVisualizacaoMomentos(self, coefiente):
        """Seta o valor do coeficiente de Visualizacao dos Momentos fletores,
        apos chama a alteracao dos desenhos (glList(id_momentoFletor))
        """
        self.COEF_VISUALIZACAO_MOMENTOS = coefiente
        #Atualiza os desenhos dos diagramas dos momentos fletores
        if self.MOSTRAR_MOMENTOS_FLETORES_Y == True:
            self.ConeCanvas.AtualizaDesenhoDiagramasFletoresY()
        if self.MOSTRAR_MOMENTOS_FLETORES_Z == True:    
            self.ConeCanvas.AtualizaDesenhoDiagramasFletoresZ()
        if self.MOSTRAR_ESFORCOS_CORTANTES_Y == True:
            self.ConeCanvas.AtualizaDesenhoEsforcosCortantesY()
        if self.MOSTRAR_ESFORCOS_CORTANTES_Z == True:
            self.ConeCanvas.AtualizaDesenhoEsforcosCortantesZ()
        if self.MOSTRAR_ESTRUTURA_DEFORMADA == True:
            self.ConeCanvas.AtualizaDesenhoDeformada()
        
        self.ConeCanvas.ParametrosVizualizacao()
    
    def SetTextoUnidadeComprimento(self):
        """
        Seta o texto da unidade de comprimento conforme a
        unidade de medida especificada
        """
        if  self.UnidadeComprimento == "[m] - Metro":
            self._TextoUnidadeComprimento = "m"
        elif self.UnidadeComprimento == "[cm] - Centimetro":
            self._TextoUnidadeComprimento = "cm"
        elif self.UnidadeComprimento == "[mm] - milimetro":
            self._TextoUnidadeComprimento = "mm"
        elif self.UnidadeComprimento == "[ft] - Pes":
            self._TextoUnidadeComprimento = "ft"
        elif self.UnidadeComprimento == "[in] - Polegada":
            self._TextoUnidadeComprimento = "in"
    
    def SetUnidades_e_Formatos(self, UnidCompr, UnidForca, UnidAngulo,
                               FormCompr, FormForca, FormAngulo):
        """SETA NO MODELO OS TIPOS DE UNIDADES E FORMATOS UTILIZADOS NA
           EXIBICAO DOS DADOS.

           UnidCompr -> string
           UnidForca -> string
           UnidAngulo -> string
           FormCompr -> string
           FormForca -> string
           FormAngulo -> string
        """
        self.UnidadeComprimento = UnidCompr
        self.UnidadeForca = UnidForca
        self.UnidadeAngulo = UnidAngulo
        self.FormatoComprimento = FormCompr
        self.FormatoForca = FormForca
        self.FormatoAngulo = FormAngulo

        #verificar o codigo a abaixo pois foi apenas uma gambiarra
        self.Estrututura.UnidadeComprimento = self.UnidadeComprimento
        self.Estrututura.UnidadeForca = self.UnidadeForca
        try:
            for no in self.Estrututura.LISTA_PVS:
                no.UnidadeComprimento = self.UnidadeComprimento
                no.UnidadeForca = self.UnidadeForca
            for barra in self.Estrututura.LISTA_BARRAS:
                barra.UnidadeComprimento = self.UnidadeComprimento
                barra.UnidadeForca = self.UnidadeForca
        except:
            pass
        #verificar o codigo a cima pois foi apenas uma gambiarra

        #Atualiza A Janela de Desenho para mostrar as unidades certas
        self.ConeCanvas.AtualizaTodasAsGlList()    
    
    
    
    def SetTextoUnidadeForca(self):
        """
        Seta o texto da unidade de Forca conforme a
        unidade de medida especificada
        """
        if self.UnidadeForca == "[kN] - Kilo Newton":
            self._TextoUnidadeForca = "kN"
        elif self.UnidadeForca == "[lb] - Libra":
            self._TextoUnidadeForca = "lb"
        elif self.UnidadeForca == "[klb] -Kilo Libra":
            self._TextoUnidadeForca = "klb"
        elif self.UnidadeForca == "[N] - Newton":
            self._TextoUnidadeForca = "N"
        elif self.UnidadeForca == "[kgf] - Kilo Grama Forca":
            self._TextoUnidadeForca = "kgf"
        elif self.UnidadeForca == "[Tonf] - Tonelada Forca":
            self._TextoUnidadeForca = "Tonf"
    @property
    def TextoUnidadeComprimento(self):
        self.SetTextoUnidadeComprimento()
        return self._TextoUnidadeComprimento
    
    @property
    def TextoUnidadeForca(self):
        self.SetTextoUnidadeForca()
        return self._TextoUnidadeForca
        
    def VerificaSelecao(self):
        """ Verifica se a selecao foi apenas por CLIQUE ou se foi pelo 
            RETANGULO de selecao.
            
            Se for CLIQUE returna uma lista vazia, se for RETANGULO, retorna
            uma lista com as coordenadas dos vertices do retangulo de selecao.
            
            xp1, xp2, xp3, xp4 = coordenadas da janela pontos 1, 2, 3 e 4
            yp1, yp2, yp3, yp4 = coordenadas da janela pontos 1, 2, 3 e 4
            
            return CLIQUE = []
            
            ou
            
            return RETANGULO = [[0,0],[xp1,yp1],[xp2,yp2],[xp3,yp3],[xp4,yp4]]            
            
        """
        
        if self.FLAG_DESENHO == "SELECT":
            if self.RecSelect[2] == None:
                return []
            elif self.RecSelect[2] != None:
                retangulo_de_selecao = self.DrawRetangulo(*self.RecSelect)
                return retangulo_de_selecao
        else:
            return []

    def VerificaCliqueBotaoDireito(self, evt):
        if (self.selected != None and len(self.selected)==1):
            if self.selected[0][0] == 1:
                self.GerenciaEstruturas(evt, [self.selected[0][1]])
            elif self.selected[0][0] == 2:
                barraselecionada = self.selected[0][1]
                self.GerenciaTrecho(evt, [barraselecionada])
    
    def VerificaClickButtonRightDown(self, ELEM_SELEC, x, y, evt):
        if (len(ELEM_SELEC[0])==2):
            if ELEM_SELEC[0][0] == 1:
                self.GerenciaEstruturas(evt, [ELEM_SELEC[0][1]])

            elif ELEM_SELEC[0][0] == 2:
                barraselecionada = ELEM_SELEC[0][1]
                self.GerenciaTrecho(evt, [barraselecionada])

            elif ELEM_SELEC[0][0] == 3:
                perfilSelecionado = ELEM_SELEC[0][1]
                self.GerenciaPerfis(evt, [perfilSelecionado])
        
        elif (len(ELEM_SELEC[0])==4 or len(ELEM_SELEC[0])==5):
            if ELEM_SELEC[0][2] == 1:
                self.GerenciaEstruturas(evt, [ELEM_SELEC[0][3]])

            elif ELEM_SELEC[0][2] == 2:
                barraselecionada = ELEM_SELEC[0][3]
                self.GerenciaTrecho(evt, [barraselecionada])
                
    def CliqueBtnEsquerdoDown(self, ELEM_SELEC, mouse_x, mouse_y):            
        if self.onCommand !=None:
            x, y = self.ConeCanvas.GetCoordMundo(mouse_x, mouse_y)
            self.onCommand.InicializaLinha([x/100, y/100, 0])
        
        #Verifica se tem algum elemento no SNAP
        if len(self.selectedSnap) !=0:
            pos = self.GetPositionElemSelect(self.selectedSnap[0])
        else:
            pos = False
        
        if pos == False:
            pass
        else:
            mouse_x, mouse_y = self.ConeCanvas.GetCoordTela(pos[0], pos[1])
        
        status = self.Estrututura.PV.StatusModificar() + \
                 self.Estrututura.TRECHO.StatusModificar() + \
                 self.PERFIL.StatusModificar()   
                
        if any(status):
            if self.Estrututura.PV.PVMover !=False:           
                PV = self.Estrututura.Dic_Lista_Pvs[self.Estrututura.PV.PVMover] 
                x, y = self.ConeCanvas.GetCoordMundo(mouse_x, mouse_y)
                PV.pos[0] = x
                PV.pos[1] = y
                self.Estrututura.PV.PVMover = False
                #Atualiza, pois foi mudado os elementos
                for perfil in self.LISTA_PERFIS:
                    perfil.InicializaDados()
            elif self.Estrututura.PV.PVRotacionar !=False:           
                PV = self.Estrututura.Dic_Lista_Pvs[self.Estrututura.PV.PVRotacionar] 
                x, y = self.ConeCanvas.GetCoordMundo(mouse_x, mouse_y)
                PV.AlteraAnguloRotacao(x, y, True)
                self.Estrututura.PV.PVRotacionar = False
            elif self.Estrututura.PV.PVLabelArrastar !=False:           
                PV = self.Estrututura.Dic_Lista_Pvs[self.Estrututura.PV.PVLabelArrastar] 
                x, y = self.ConeCanvas.GetCoordMundo(mouse_x, mouse_y)
                PV.Label.AlteraPosicaoLabel(x, y)
                self.Estrututura.PV.PVLabelArrastar = False
            elif self.Estrututura.PV.PVTick_top !=False:           
                PV = self.Estrututura.Dic_Lista_Pvs[self.Estrututura.PV.PVTick_top]                
                self.OBJETO_SELECIONADO.TickAlteraCotaTampa(PV, mouse_x, mouse_y)                
                self.Estrututura.PV.PVTick_top = False
                self.ConeCanvas.AtualizaDesenhoPerfis() #Atualiza desenho Perfis
            elif self.Estrututura.PV.PVTick_bottom !=False:           
                PV = self.Estrututura.Dic_Lista_Pvs[self.Estrututura.PV.PVTick_bottom]                
                self.OBJETO_SELECIONADO.TickAlteraCotaFundo(PV, mouse_x, mouse_y)                
                self.Estrututura.PV.PVTick_bottom = False
                self.ConeCanvas.AtualizaDesenhoPerfis() #Atualiza desenho Perfis
            
            #PERFIS
            elif self.PERFIL.PERFIL_MOV !=False:
                self.OBJETO_SELECIONADO.SetPosPerfil(mouse_x, mouse_y)                
                self.PERFIL.PERFIL_MOV = False
                self.ConeCanvas.AtualizaDesenhoPerfis() #Atualiza desenho Perfis
            #TRECHOS
            elif self.Estrututura.TRECHO.TUBOTick_inicio_top !=False:
                TRECHO = self.Estrututura.Dic_Lista_Tubulacoes[self.Estrututura.TRECHO.TUBOTick_inicio_top]                
                self.OBJETO_SELECIONADO.TickAlteraCGSI(TRECHO, mouse_x, mouse_y)                
                self.Estrututura.TRECHO.TUBOTick_inicio_top = False
                self.ConeCanvas.AtualizaDesenhoPerfis() #Atualiza desenho Perfis
            elif self.Estrututura.TRECHO.TUBOTick_inicio_bottom !=False:           
                TRECHO = self.Estrututura.Dic_Lista_Tubulacoes[self.Estrututura.TRECHO.TUBOTick_inicio_bottom]                
                self.OBJETO_SELECIONADO.TickAlteraCGII(TRECHO, mouse_x, mouse_y)                
                self.Estrututura.TRECHO.TUBOTick_inicio_bottom = False
                self.ConeCanvas.AtualizaDesenhoPerfis() #Atualiza desenho Perfis
            elif self.Estrututura.TRECHO.TUBOTick_middle !=False:           
                TRECHO = self.Estrututura.Dic_Lista_Tubulacoes[self.Estrututura.TRECHO.TUBOTick_middle]                
                self.OBJETO_SELECIONADO.TickAlteraCMIDDLE(TRECHO, mouse_x, mouse_y)                
                self.Estrututura.TRECHO.TUBOTick_middle = False
                self.ConeCanvas.AtualizaDesenhoPerfis() #Atualiza desenho Perfis
            elif self.Estrututura.TRECHO.TUBOTick_final_top !=False:           
                TRECHO = self.Estrututura.Dic_Lista_Tubulacoes[self.Estrututura.TRECHO.TUBOTick_final_top]                
                self.OBJETO_SELECIONADO.TickAlteraCGSF(TRECHO, mouse_x, mouse_y)                
                self.Estrututura.TRECHO.TUBOTick_final_top = False
                self.ConeCanvas.AtualizaDesenhoPerfis() #Atualiza desenho Perfis
            elif self.Estrututura.TRECHO.TUBOTick_final_bottom !=False:           
                TRECHO = self.Estrututura.Dic_Lista_Tubulacoes[self.Estrututura.TRECHO.TUBOTick_final_bottom]                
                self.OBJETO_SELECIONADO.TickAlteraCGIF(TRECHO, mouse_x, mouse_y)                
                self.Estrututura.TRECHO.TUBOTick_final_bottom = False
                self.ConeCanvas.AtualizaDesenhoPerfis() #Atualiza desenho Perfis
            self.OBJETO_SELECIONADO = False            
        else:
            if (ELEM_SELEC == None or len(ELEM_SELEC) == 0 ):
                pass
            elif len(ELEM_SELEC[0]) == 2:
                if (ELEM_SELEC[0][0] == 3): #Perfil Selecionado
                    self.OBJETO_SELECIONADO = self.GetObjetoSelecionado(ELEM_SELEC[0])
            elif len(ELEM_SELEC[0]) == 3:
                if ELEM_SELEC[0][0] == 3: #Elemento dentro de Perfil
                    if ELEM_SELEC[0][2] == 1:
                        self.PERFIL.PERFIL_MOV = ELEM_SELEC[0][1]
                elif ELEM_SELEC[0][0] == 1: #Elemento dentro de PV
                    if ELEM_SELEC[0][2] == 1: #PVMOVER
                        self.Estrututura.PV.PVMover = ELEM_SELEC[0][1]                    
                    elif ELEM_SELEC[0][2] == 2: #PVRotacionar
                        self.Estrututura.PV.PVRotacionar = ELEM_SELEC[0][1]                    
                    elif ELEM_SELEC[0][2] == 3: #PVLabelArrastar
                        self.Estrututura.PV.PVLabelArrastar = ELEM_SELEC[0][1]                    
            elif len(ELEM_SELEC[0]) == 4:
                self.ConeCanvas.AtualizaDesenhoPerfis()
            elif len(ELEM_SELEC[0]) == 5:
                self.OBJETO_SELECIONADO = self.LISTA_PERFIS[ELEM_SELEC[0][1]-1]
                if ELEM_SELEC[0][0] == 3: #Clicado em cima de um  PERFIL
                    if ELEM_SELEC[0][2] == 1: #Clicado em um objeto do PV no perfil 
                        if ELEM_SELEC[0][4] == 4: #Clicado no TICK_TOP do PV
                            self.Estrututura.PV.PVTick_top = ELEM_SELEC[0][3]
                        elif ELEM_SELEC[0][4] == 5: #Clicado no TICK_BOTTOM do PV
                            self.Estrututura.PV.PVTick_bottom = ELEM_SELEC[0][3]
                    elif ELEM_SELEC[0][2] == 2: #Clicado em um objeto do TUBO no perfil 
                        if ELEM_SELEC[0][4] == 4: #Clicado no TICK_TOP_INICIO do TUBO
                            self.Estrututura.TRECHO.TUBOTick_inicio_top = ELEM_SELEC[0][3]
                        elif ELEM_SELEC[0][4] == 5: #Clicado no TICK_BOTTOM_INICIO do TUBO
                            self.Estrututura.TRECHO.TUBOTick_inicio_bottom = ELEM_SELEC[0][3]
                        elif ELEM_SELEC[0][4] == 6: #Clicado no TICK_MIDDLE_MEIO do TUBO
                            self.Estrututura.TRECHO.TUBOTick_middle = ELEM_SELEC[0][3]
                        elif ELEM_SELEC[0][4] == 7: #Clicado no TICK_TOP_FINAL do TUBO
                            self.Estrututura.TRECHO.TUBOTick_final_top = ELEM_SELEC[0][3]
                        elif ELEM_SELEC[0][4] == 8: #Clicado no TICK_BOTTOM_FINAL do TUBO
                            self.Estrututura.TRECHO.TUBOTick_final_bottom = ELEM_SELEC[0][3]
    
    def VerificaSeHaNosSelecionados(self):
        if len([x for x in self.selected if x <= 1000])>0:
            return True
        else:
            return False

    def VerificaSeHaBarrasSelecionadas(self):
        if len([x for x in self.selected if x > 1000])>0:
            return True
        else:
            return False
    

    def ViewLeft(self):
        x_max = max([no.pos[0] for no in  self.Estrututura.LISTA_PVS])
        x_min = min([no.pos[0] for no in  self.Estrututura.LISTA_PVS])

        y_max = max([no.pos[1] for no in  self.Estrututura.LISTA_PVS])
        y_min = min([no.pos[1] for no in  self.Estrututura.LISTA_PVS])

        z_max = max([no.pos[2] for no in  self.Estrututura.LISTA_PVS])
        z_min = min([no.pos[2] for no in  self.Estrututura.LISTA_PVS])

        self.ConeCanvas.Camera.SetCameraLeft(x_max, x_min, y_max, y_min, z_max, z_min)

    def ViewRight(self):
        x_max = max([no.pos[0] for no in  self.Estrututura.LISTA_PVS])
        x_min = min([no.pos[0] for no in  self.Estrututura.LISTA_PVS])

        y_max = max([no.pos[1] for no in  self.Estrututura.LISTA_PVS])
        y_min = min([no.pos[1] for no in  self.Estrututura.LISTA_PVS])

        z_max = max([no.pos[2] for no in  self.Estrututura.LISTA_PVS])
        z_min = min([no.pos[2] for no in  self.Estrututura.LISTA_PVS])

        self.ConeCanvas.Camera.SetCameraRight(x_max, x_min, y_max, y_min, z_max, z_min)

    def ViewFront(self):
        x_max = max([no.pos[0] for no in  self.Estrututura.LISTA_PVS])
        x_min = min([no.pos[0] for no in  self.Estrututura.LISTA_PVS])

        y_max = max([no.pos[1] for no in  self.Estrututura.LISTA_PVS])
        y_min = min([no.pos[1] for no in  self.Estrututura.LISTA_PVS])

        z_max = max([no.pos[2] for no in  self.Estrututura.LISTA_PVS])
        z_min = min([no.pos[2] for no in  self.Estrututura.LISTA_PVS])

        self.ConeCanvas.Camera.SetCameraFront(x_max, x_min, y_max, y_min, z_max, z_min)

    def ViewBack(self):
        x_max = max([no.pos[0] for no in  self.Estrututura.LISTA_PVS])
        x_min = min([no.pos[0] for no in  self.Estrututura.LISTA_PVS])

        y_max = max([no.pos[1] for no in  self.Estrututura.LISTA_PVS])
        y_min = min([no.pos[1] for no in  self.Estrututura.LISTA_PVS])

        z_max = max([no.pos[2] for no in  self.Estrututura.LISTA_PVS])
        z_min = min([no.pos[2] for no in  self.Estrututura.LISTA_PVS])

        self.ConeCanvas.Camera.SetCameraBack(x_max, x_min, y_max, y_min, z_max, z_min)

    def ViewTop(self):
        x_max = max([no.pos[0] for no in  self.Estrututura.LISTA_PVS])
        x_min = min([no.pos[0] for no in  self.Estrututura.LISTA_PVS])

        y_max = max([no.pos[1] for no in  self.Estrututura.LISTA_PVS])
        y_min = min([no.pos[1] for no in  self.Estrututura.LISTA_PVS])

        z_max = max([no.pos[2] for no in  self.Estrututura.LISTA_PVS])
        z_min = min([no.pos[2] for no in  self.Estrututura.LISTA_PVS])

        self.ConeCanvas.Camera.SetCameraTop(x_max, x_min, y_max, y_min, z_max, z_min)

    def ViewBottom(self):
        x_max = max([no.pos[0] for no in  self.Estrututura.LISTA_PVS])
        x_min = min([no.pos[0] for no in  self.Estrututura.LISTA_PVS])

        y_max = max([no.pos[1] for no in  self.Estrututura.LISTA_PVS])
        y_min = min([no.pos[1] for no in  self.Estrututura.LISTA_PVS])

        z_max = max([no.pos[2] for no in  self.Estrututura.LISTA_PVS])
        z_min = min([no.pos[2] for no in  self.Estrututura.LISTA_PVS])

        self.ConeCanvas.Camera.SetCameraBottom(x_max, x_min, y_max, y_min, z_max, z_min)

    
    def GetPositionElemSelect(self, ELEM_SELECT):
        if (ELEM_SELECT != None and len(ELEM_SELECT) == 5):
            if ELEM_SELECT[0] == 3: #Elemento dentro de Perfil
                objeto = self.LISTA_PERFIS[ELEM_SELECT[1]-1]
                return objeto.GetPosElemTick(ELEM_SELECT)
        else:
            return False
    
    def VerificaSeHaProjetoAberto(self):
        if self.Estrututura != None:
            return True
        else:
            return False   

    def VerificaEstrutura(self):
        """ Verifica se as barras estao com todas as caracteristicas inserias
            para que a estrutura possa ser calculada
        """
        listaNumBarrasComErro = {"ERRO_MATERIAL":[], "ERRO_SECAO":[]}
        for barra in self.Estrututura.LISTA_BARRAS:
            if barra.Material == None:
                listaNumBarrasComErro["ERRO_MATERIAL"].append(barra.numero)
            else:
                pass

            if barra.Secao == None:
                listaNumBarrasComErro["ERRO_SECAO"].append(barra.numero)
            else:
                pass

        if (len(listaNumBarrasComErro["ERRO_MATERIAL"]) == 0 and
                                  len(listaNumBarrasComErro["ERRO_SECAO"])==0):
            return False
        else:
            return listaNumBarrasComErro

      

    
       
    
      
    
        
    