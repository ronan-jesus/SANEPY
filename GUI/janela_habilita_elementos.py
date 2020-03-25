# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc
from gui_habilita_elementos import UI_JanelaOpcoesVisualizacoes

###########################################################################
## Class MyFrame2
###########################################################################

class JanelaOpcoesVisualizacao ( UI_JanelaOpcoesVisualizacoes ):
    def __init__( self, parent ):
        UI_JanelaOpcoesVisualizacoes.__init__ ( self, parent)
        self.parent = parent
        self.InicializaValores()
        self.Show()

    def InicializaValores(self):
        self.chb_mostrar_no.SetValue(self.parent.MOSTRAR_NOS)
        self.chb_mostrar_numeracao_nos.SetValue(self.parent.MOSTRAR_NUMERCAO_NOS)
        self.chb_mostrar_vinculos.SetValue(self.parent.MOSTRAR_RESTRICOES_NODAIS)
        self.txt_tamanhoNO.SetValue(str(self.parent.TAMANHO_DOS_NOS))
        self.txt_tamanhoVinculos.SetValue(str(self.parent.TAMANHO_DOS_VINCULOS))
        self.chb_mostrar_barra.SetValue(self.parent.MOSTRAR_BARRAS)
        self.chb_mostrar_numeracao_barras.SetValue(self.parent.MOSTRAR_NUMERCAO_BARRAS)
        self.chb_mostrar_eixos_barra.SetValue(self.parent.MOSTRAR_EIXOS_BARRAS)
        self.chb_mostrar_secoes_barra.SetValue(self.parent.MOSTRAR_SECOES_BARRAS)
        self.txt_tamanhoEixosBarra.SetValue(str(self.parent.TAMANHO_EIXOS_BARRAS))
        self.chb_mostrar_eixos_globais.SetValue(self.parent.MOSTRAR_EIXOS_GLOBAIS)
        self.txt_tamanhoEixosGlobais.SetValue(str(self.parent.TAMANHO_EIXOS_GLOBAIS))
        self.txt_tamanhoEixosGlobais.SetValue(str(self.parent.TAMANHO_EIXOS_GLOBAIS))
        self.txtPosGlobalX.SetValue(str(self.parent.POSICAO_EIXOS_GLOBAIS[0]))
        self.txtPosGlobalY.SetValue(str(self.parent.POSICAO_EIXOS_GLOBAIS[1]))
        self.txtPosGlobalZ.SetValue(str(self.parent.POSICAO_EIXOS_GLOBAIS[2]))
        self.txtPosGlobalZ.SetValue(str(self.parent.POSICAO_EIXOS_GLOBAIS[2]))
        self.chb_mostrarCargasDistribuidas.SetValue(self.parent.MOSTRAR_CARGAS_DISTRIBUIDAS)
        self.chb_mostrarCargasConcentradas.SetValue(self.parent.MOSTRAR_CARGAS_CONCENTRADAS)
        self.txt_tam_carga_distribuidas.SetValue(str(self.parent.TAMANHO_CARGAS_DISTRIBUIDAS))
        self.txt_tam_carga_concentradas.SetValue(str(self.parent.TAMANHO_CARGAS_CONCENTRADAS))
        
    def HabilitaVisualizacaoNos(self, event):
        """Habilita/Desabilita a visualizacao dos nos -> estado(True/False)"""
        self.parent.MOSTRAR_NOS = self.chb_mostrar_no.GetValue()
        
    def HabilitaVisualizacaoNumercaoNos(self, event):
        """Habilita/Desabilita a visualizacao da numercao nos -> estado(True/False)"""
        self.parent.MOSTRAR_NUMERCAO_NOS = self.chb_mostrar_numeracao_nos.GetValue()
    
    def HabilitaVisualizacaoVinculos(self, event):
        """Habilita/Desabilita a visualizacao dos 
        vinculos -> estado(True/False)"""
        self.parent.MOSTRAR_RESTRICOES_NODAIS = self.chb_mostrar_vinculos.GetValue()
        self.parent.ConeCanvas.AtualizaDesenhoRestricoesNodais() #Recria a GlLIst

    def SetTamanhoNo(self):
        """Seta o tamanho do NO na janela de visualizacao, a entrada e' em
           (pt) pontos do PyOpengl.
        """
        tamanhoNO = round(float(self.txt_tamanhoNO.GetValue()), 1)
        self.parent.TAMANHO_DOS_NOS = tamanhoNO
        self.parent.ConeCanvas.SetPointsSize() #Faz a alteracao no pyopengl
        
    def SetTamanhoVinculos(self):
        """Seta o tamanho dos Vinculos na janela de visualizacao, a entrada 
        e' em (m) pontos do PyOpengl.
        """
        tamanhoVinculo = round(float(self.txt_tamanhoVinculos.GetValue()), 1)
        self.parent.TAMANHO_DOS_VINCULOS = tamanhoVinculo
        self.parent.ConeCanvas.AtualizaDesenhoRestricoesNodais() #Recria a GlLIst
        self.parent.ConeCanvas.AtualizaDesenhoReacoes() #Recria a GlLIst
        self.parent.ConeCanvas.AtualizaDesenhoCargasConcentradas() #Recria a GlLIst
        
    def HabilitaVisualizacaoBarras(self, event):
        """Habilita/Desabilita a visualizacao das Barras 
        -> estado(True/False)
        """
        self.parent.MOSTRAR_BARRAS = self.chb_mostrar_barra.GetValue()
        
    def HabilitaVisualizacaoNumercaoBarras(self, event):
        """Habilita/Desabilita a visualizacao da numeracao Barras 
        -> estado(True/False)
        """
        self.parent.MOSTRAR_NUMERCAO_BARRAS = self.chb_mostrar_numeracao_barras.GetValue()
    
    def HabilitaVisualizacaoEixosBarras(self, event):
        """Habilita/Desabilita a visualizacao dos Eixos das Barras 
        -> estado(True/False)
        """
        self.parent.MOSTRAR_EIXOS_BARRAS = self.chb_mostrar_eixos_barra.GetValue()
        
    def HabilitaVisualizacaoSecoesBarras(self, event):
        """Habilita/Desabilita a visualizacao das Secoes das Barras 
        -> estado(True/False)
        """
        self.parent.MOSTRAR_SECOES_BARRAS = self.chb_mostrar_secoes_barra.GetValue()
        
    def SetTamanhoEixosBarras(self):
        """Seta o tamanho dos Eixos XYZ das barras
            a CONSTANTE TAMANHO_EIXOS_BARRAS controla o tamanho a unidade
            esta em metros
        """
        tamanhoEixos = round(float(self.txt_tamanhoEixosBarra.GetValue()), 2)
        self.parent.TAMANHO_EIXOS_BARRAS = tamanhoEixos
        self.parent.ConeCanvas.AtualizaDesenhoEixosBarras() #Recria a GlLIst

    def HabilitaVisualizacaoEixosGlobais(self, event):
        """Habilita/Desabilita a visualizacao dos Eixos Globais 
        -> estado(True/False)
        """
        self.parent.MOSTRAR_EIXOS_GLOBAIS = self.chb_mostrar_eixos_globais.GetValue()
    
    def SetTamanhoEixosGlobais(self):
        """"Seta o tamanho dos Eixos GLOBAIS a CONSTANTE TAMANHO_EIXOS_GLOBAIS
            que esta em MODEL controla o tamanho, a unidade esta em metros.
        """
        tamanhoEixos = round(float(self.txt_tamanhoEixosGlobais.GetValue()), 2)
        self.parent.TAMANHO_EIXOS_GLOBAIS = tamanhoEixos
        self.parent.ConeCanvas.AtualizaDesenhoEixosGlobais() #Recria a GlLIst
        
    def SetPosicaoEixosGlobais(self):
        """"Seta a posicao dos Eixos GLOBAIS a CONSTANTE POSICAO_EIXOS_GLOBAIS
            que esta em MODEL controla a posicao, a unidade esta em metros.
        """
        pos_x_Eixos = round(float(self.txtPosGlobalX.GetValue()), 2)
        pos_y_Eixos = round(float(self.txtPosGlobalY.GetValue()), 2)
        pos_z_Eixos = round(float(self.txtPosGlobalZ.GetValue()), 2)
        self.parent.POSICAO_EIXOS_GLOBAIS = [pos_x_Eixos,pos_y_Eixos,pos_z_Eixos]
        self.parent.ConeCanvas.AtualizaDesenhoEixosGlobais() #Recria a GlLIst

    
    def HabilitaVisualizacaoCargasDistribuidas(self, event):
        """Habilita/Desabilita a visualizacao das Cargas distribuidas 
        -> estado(True/False)
        """
        self.parent.MOSTRAR_CARGAS_DISTRIBUIDAS = self.chb_mostrarCargasDistribuidas.GetValue()
        
    def HabilitaVisualizacaoCargasConcentradas(self, event):
        """Habilita/Desabilita a visualizacao das Cargas dConcentradas 
        -> estado(True/False)
        """
        self.parent.MOSTRAR_CARGAS_CONCENTRADAS = self.chb_mostrarCargasConcentradas.GetValue()
        
    def SetTamCargaDistribuidas(self):
        """"Seta o tamanho das cargas distribuidas da janela de desenho
            que esta em MODEL controla o tamanho, a unidade esta em metros.
        """
        tamanho = float(self.txt_tam_carga_distribuidas.GetValue())
        self.parent.TAMANHO_CARGAS_DISTRIBUIDAS = tamanho
        self.parent.ConeCanvas.AtualizaDesenhoCargasDistribuidas() #Recria a GlLIst
        
    def SetTamCargaConcentradas(self):
        """"Seta o tamanho das cargas concentradas da janela de desenho
            que esta em MODEL controla o tamanho, a unidade esta em metros.
        """
        tamanho = float(self.txt_tam_carga_concentradas.GetValue())
        self.parent.TAMANHO_CARGAS_CONCENTRADAS = tamanho
        self.parent.ConeCanvas.AtualizaDesenhoCargasConcentradas() #Recria a GlLIst
        
    def OnClickButtonOK(self, event):
        self.SetTamanhoNo()
        self.SetTamanhoVinculos()
        self.SetTamanhoEixosBarras()
        self.SetTamanhoEixosGlobais()
        self.SetPosicaoEixosGlobais()
        self.SetTamCargaDistribuidas()
        self.SetTamCargaConcentradas()
        self.Destroy()

    def OnClickButtonCancel(self, event):
        self.Destroy()