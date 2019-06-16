# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from UI_propertGridPVs import propGridPVs
from AUXILIARES.util import truncaNumero
###########################################################################
## Class DlgGerenciaNO
###########################################################################

class DlgGerenciaEstrutura( propGridPVs ):
    def __init__( self, parent, listaPvs, acao=None ):
        propGridPVs.__init__ ( self, parent)
        self.parent = parent
        self.listaPvs = listaPvs        
        self.ACAO = acao
        
        self.valoresAntigos = {}  #dicionario para armazenar valores antigos
        self.InicializaPropriedades() 
        self.Show()        
        
    def InicializaPropriedades(self):
        """Inicializa todas as propriedades do propertyGrid ao abrir a janela
        """
        #Nome da Estrutura
        self.ptyGridItemNomeEstrutura.Enable(True)
        self.ptyGridItemNomeEstrutura.SetValue(self.listaPvs[0].nomePV)
        
        #Numero da Estrutura
        self.ptyGridItemNumeroEstrutura.Enable(False)
        self.ptyGridItemNumeroEstrutura.SetValue(self.listaPvs[0].numero)
        
        #Coordenada X da Estrutura
        self.ptyGridItemPosicaoX.Enable(True)
        self.ptyGridItemPosicaoX.SetValue(self.listaPvs[0].pos[0])
        
        #Coordenada Y da Estrutura
        self.ptyGridItemPosicaoY.Enable(True)
        self.ptyGridItemPosicaoY.SetValue(self.listaPvs[0].pos[1])
        
        #Angulo Rotacao do PV
        self.ptyGridItemAnguloRotacao.Enable(True)
        self.ptyGridItemAnguloRotacao.SetValue(self.listaPvs[0].AngloRotacao)
        
        #Tipo da Estrutura
        self.ptyGridItemTipoEstrutura.Enable(True)
        #Preenche lista de Estruturas
        for estrutura in self.listaPvs[0].ESTRUTURAS:
            self.ptyGridItemTipoEstrutura.AddChoice(estrutura)        
        #Seta a estrutura no grid de propriedade        
        self.ptyGridItemTipoEstrutura.SetChoiceSelection(0)
        
        #Cota do Terreno
        self.ptyGridItemCotaTerreno.Enable(True)
        self.ptyGridItemCotaTerreno.SetValue(self.listaPvs[0].CotaTerreno)
        
        #Cota da Tampa
        self.ptyGridItemCotaTampa.Enable(True)
        self.ptyGridItemCotaTampa.SetValue(self.listaPvs[0].CotaTampa)
        
        #Cota do Fundo
        self.ptyGridItemCotaFundo.Enable(True)
        self.ptyGridItemCotaFundo.SetValue(self.listaPvs[0].CotaFundo)
        
        #Altura da estrutura
        self.ptyGridItemAlturaEstrutura.Enable(True)
        self.ptyGridItemAlturaEstrutura.SetValue(self.listaPvs[0].AlturaPv)
        
    # Sobrecarrega o metodo 'ModificaPropriedade' quando algo e alterado
    # na janela de propriedades da Estrutura
    def ModificaPropriedade( self, event ):
        proprAlterada = event.GetPropertyName()
        valorAlterado = event.GetPropertyValue()
        
        if proprAlterada == u"Nome da Estrutura":
            self.listaPvs[0].SetNomeEstrutura(valorAlterado)
        elif proprAlterada == u"Número da Estrutura":           
            pass
        elif proprAlterada == u"Coordenada X (m)":           
            self.listaPvs[0].SetCoordenadaX(valorAlterado)
        elif proprAlterada == u"Coordenada Y (m)":           
            self.listaPvs[0].SetCoordenadaY(valorAlterado)
        elif proprAlterada == u"Angulo Rotação ( ° dec)":           
            self.listaPvs[0].SetAnguloRotacao(valorAlterado)
        elif proprAlterada == u"Tipo Estrutura":           
            pass
        elif proprAlterada == u"Cota do Terreno (m)":           
            self.listaPvs[0].SetCotaTerreno(valorAlterado)
        elif proprAlterada == u"Cota da Tampa (m)":           
            self.listaPvs[0].SetCotaTampa(valorAlterado)
        elif proprAlterada == u"Cota do Fundo (m)":           
            self.listaPvs[0].SetCotaFundo(valorAlterado)
        elif proprAlterada == u"Altura da Estrutura (m)":
            self.listaPvs[0].SetAlturaEstrutura(valorAlterado)
        
        self.InicializaPropriedades() #reseta os valores apos mudanca
        #event.Skip()    

    def FinalizaAlteracoes(self):
        pass