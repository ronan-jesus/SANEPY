# -*- coding: utf-8 -*-

import wx
from toolBarPainelEsquerdo import ToolbarLateralEsuqerdo
from AUXILIARES.imagens_do_app import *
from AUXILIARES.commandLinha import commandLine

class PainelSelecaoEsquerdo(ToolbarLateralEsuqerdo):
    def __init__(self, parent):
        ToolbarLateralEsuqerdo.__init__(self, parent)
        
        self.parent = parent
            
    def SelecaoBtnLaterais(self, event):
        """
        Funcao para gerenciar os Botoes Laterais, onde se encontram os botoes
        selecionar, novoPV, novoTrecho, exluirPV, excluirTrecho,ect.
        """
        if event.GetId() == 1013:
            self.parent.FLAG_DESENHO = "SELECT"
            self.parent.ConeCanvas.SetCursor(wx.Cursor(wx.CURSOR_DEFAULT))            
        elif event.GetId() == 1014:
            self.parent.FLAG_DESENHO = "BARRA"
            self.parent.ConeCanvas.SetCursor(wx.Cursor(wx.CURSOR_DEFAULT))            
            
            #Desabilita a janela de insercao de nos, caso esteja aberto
            #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DE INSERCAO DE COORDENADAS
            try:
                #SE TIVER ALGUMA INSTANCIA, FECHA
                self.parent.dlg_insertCoord.OnClose()             

            except:
                #SE NAO HOUVER, NAO FAZ NADA
                pass


        elif event.GetId() == 1015:
            self.parent.FLAG_DESENHO = "NO"
            self.parent.ConeCanvas.SetCursor(wx.Cursor(wx.CURSOR_CROSS))

            #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DE INSERCAO DE COORDENADAS
            try:
                #SE TIVER ALGUMA INSTANCIA, FECHA
                self.parent.dlg_insertCoord.OnClose()

            except:
                #SE NAO HOUVER, NAO FAZ NADA
                pass

        elif event.GetId() == 1016:
            self.parent.onCommand = commandLine(self.parent)
            
            #Exclui apenas as BARRAS selecionadas
            self.parent.ExcluiElementosSelecionados("BARRA")

        elif event.GetId() == 1017:
            #Exclui apenas os NOS selecionados
            self.parent.ExcluiElementosSelecionados("NO")
        
        
        elif event.GetId() == 1018:
            #Desabilita a janela de insercao de nos, caso esteja aberto
            #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DE INSERCAO DE COORDENADAS
            try:
                #SE TIVER ALGUMA INSTANCIA, FECHA
                self.parent.propertyTrechos.OnClose()             

            except:
                #SE NAO HOUVER, NAO FAZ NADA
                pass
            
            #VERIFICA SE JA HA UMA INSTANCIA DA JANELA DE INSERCAO DE COORDENADAS
            try:
                #SE TIVER ALGUMA INSTANCIA, FECHA
                self.DlgGerenciaEstrutura.OnClose()

            except:
                #SE NAO HOUVER, NAO FAZ NADA
                pass
            
            
            #Exclui apenas os NOS selecionados
            self.parent.ON_PERFIL = [True,[None, None, None]]
            self.parent.CriaJanelaPerfil()

        #self.parent.ConeCanvas.SetFocus()
        
        
#ID_MENU_ITEM_MOSTRAR_CARGASCONCENTRADAS - ID_MENU_ITEM_MOSTRAR_PAINEL_PONTOSCOTAS
#ID_MENU_ITEM_MOSTRAR_CARGASDISTRIBUIDAS - ID_MENU_ITEM_MOSTRAR_PAINELELEMENTOS