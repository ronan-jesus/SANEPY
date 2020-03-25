# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 18:26:40 2018

@author: RONAN TEODORO
"""
from UI_propertGridTrechos import propGridTrechos
from AUXILIARES.util import truncaNumero

class JanelaPropTrechos(propGridTrechos):
    def __init__(self, parent, listaTrechos, acao=None):
        propGridTrechos.__init__(self, parent)
        self.parent = parent
        self.listaTrechos = listaTrechos
        #self.parent.Estrututura.CriaListaDeLigacoes()        
        
        self.parent.Estrututura.CalculaVazoesEntradas()#listaTrechos[0])#Calcula Vazoes
        self.parent.Estrututura.CalculaRemansoTrechos()#listaTrechos[0])#Calcula Remansos
        
        self.valoresAntigos = {}  #dicionario para armazenar valores antigos
        self.InicializaPropriedades()        

        self.Show()
        
    def InicializaPropriedades(self):
        """Inicializa todas as propriedades do propertyGrid ao abrir a janela
        """
        #Numero do trecho
        self.ptyGridItemNumero.Enable(False)
        self.ptyGridItemNumero.SetValue(self.listaTrechos[0].numero)
        #Nome do Trecho
        self.ptyGridItemNome.SetValue(self.listaTrechos[0].nomeTrecho)
        #Nome da Estrutura Inicial
        self.ptyGridItemEstruturaInicial.Enable(False)
        estruturaInicial = self.listaTrechos[0].PV1.nomePV + \
                                          str(self.listaTrechos[0].PV1.numero)
        self.ptyGridItemEstruturaInicial.SetValue(estruturaInicial)
        #Nome da Estrutura Final
        self.ptyGridItemEstruturaFinal.Enable(False)
        estruturaFinal = self.listaTrechos[0].PV2.nomePV + \
                                          str(self.listaTrechos[0].PV2.numero)
        self.ptyGridItemEstruturaFinal.SetValue(estruturaFinal)
        
        #Preenche lista de diametros
        #for diam in self.parent.DIAMETROS:
        for diam in self.listaTrechos[0].ListaDiametros():
            self.ptyGridItemDiametro.AddChoice(diam)        
        #Diamentro rela da tubulacao
        diam = self.listaTrechos[0].D
        #Cria a lista de diametros em ordem crescente por diametro
        listaDiametros = self.listaTrechos[0].ListaDiametros()
        #Cria o Dicionario diam:TextoDiametro
        textosDiamentros = self.listaTrechos[0].ListaTextosDiamentros()
        #Pega o texto do diametro pelo dicionario valor:Chave
        texto = textosDiamentros[diam]
        #pega o indice do diametro na lista de diametros pelo texto
        indice = listaDiametros.index(texto)
        #Seta o diametro da tubulacao no grid de propriedade        
        self.ptyGridItemDiametro.SetChoiceSelection(indice)
        #Usar Comprimento Automatico
        self.ptyGridItemComprAuto.SetValue(self.listaTrechos[0].comprimentoAuto)        
        #Comprimento do Trecho
        self.ptyGridItemComprimento.Enable(False)
        self.ptyGridItemComprimento.SetValue(round(self.listaTrechos[0].GetCompAutoTrecho(), 2))        
        #Comprimento Definido
        if self.listaTrechos[0].comprimentoAuto == False:
            self.ptyGridItemCompDefinido.Enable(True)            
        else:
            self.ptyGridItemCompDefinido.Enable(False)
        self.ptyGridItemCompDefinido.SetValue(self.listaTrechos[0].Ldefinido)  
        #Cota da Geratriz Inferior do Tubo Inicio do Trecho        
        CGII = self.listaTrechos[0].CGII
        self.ptyGridItemCotaGeratrizInferiorInicio.SetValue(CGII)
        #Cota da Geratriz Inferior do Tubo Final do Trecho        
        CGIF = self.listaTrechos[0].CGIF
        self.ptyGridItemCotaGeratrizInferiorFinal.SetValue(CGIF)
        #Cota da Geratriz Superior do Tubo Inicio do Trecho        
        CGSI = self.listaTrechos[0].CGSI
        self.ptyGridItemCotaGeratrizSuperiorInicio.SetValue(CGSI)
        #Cota da Geratriz Superior do Tubo Final do Trecho        
        CGSF = self.listaTrechos[0].CGSF
        self.ptyGridItemCotaGeratrizSuperiorFinal.SetValue(CGSF)
        #Declividade do terreno
        self.ptyGridItemDeclividaTerreno.Enable(False)
        declivTerreno = str(truncaNumero(self.listaTrechos[0].Iterreno, 4))+"%"
        self.ptyGridItemDeclividaTerreno.SetValue(declivTerreno)
        #Declividade do minima
        self.ptyGridItemDeclividaMinima.Enable(False)
        declivMinima = str(truncaNumero(self.listaTrechos[0].Iminima, 4))+"%"
        self.ptyGridItemDeclividaMinima.SetValue(declivMinima)
        #Declividade do trecho
        self.valoresAntigos["Iadotada"] = \
                            truncaNumero(self.listaTrechos[0].Iadotada, 4)*100
        
        declivTrecho = str(truncaNumero(self.listaTrechos[0].Iadotada*100, 4))\
                                                                           +"%"
        self.ptyGridItemDeclividaTrecho.SetValue(declivTrecho)
        #Desnivel do trecho
        desnivelTrecho = self.listaTrechos[0].Desnivel
        self.ptyGridItemDesnivel.SetValue(desnivelTrecho)
        #Contribuicao inicio de Plano
        taxaIniPlano = self.listaTrechos[0].TaxaInicial
        self.ptyGridItemContribInicioPlano.SetValue(taxaIniPlano)
        #Contribuicao final de Plano
        taxaFimPlano = self.listaTrechos[0].TaxaFinal
        self.ptyGridItemContribFimPlano.SetValue(taxaFimPlano)
        #Vazao Pontual no trecho
        Qpontual = self.listaTrechos[0].Qpontual
        self.ptyGridItemVazaoPontual.SetValue(Qpontual)
        #Contribuicao parasitaria
        taxaParasitaria = self.listaTrechos[0].TaxaInfiltracao
        self.ptyGridItemContribParasitaria.SetValue(taxaParasitaria)
        
        #Contribuicao total do trecho - Inicio
        self.ptyGridItemContribTotalInicio.Enable(True)
        contribTotalInicio = self.listaTrechos[0].ContribTotalInicio
        self.ptyGridItemContribTotalInicio.SetValue(contribTotalInicio)
        
        #Contribuicao total do trecho - Final
        self.ptyGridItemContribTotalFinal.Enable(True)
        contribTotalFinal = self.listaTrechos[0].ContribTotalFinal
        self.ptyGridItemContribTotalFinal.SetValue(contribTotalFinal) 
        
        #Vazao de entrada no trecjo - PV a montante - Inicio
        self.ptyGridItemVazaoEntradaInicio.Enable(True)
        vazaoEntradaInicio = self.listaTrechos[0].QentradaInicial
        self.ptyGridItemVazaoEntradaInicio.SetValue(vazaoEntradaInicio)
        
        #Vazao de saida no trecjo - PV a jusante - Inicio
        self.ptyGridItemVazaoSaidaInicio.Enable(True)
        vazaoSaidaInicio = self.listaTrechos[0].QsaidaInicial
        self.ptyGridItemVazaoSaidaInicio.SetValue(vazaoSaidaInicio)
      
        #Vazao de entrada no trecjo - PV a montante - Final
        self.ptyGridItemVazaoEntradaFinal.Enable(False)
        vazaoEntradaFinal = self.listaTrechos[0].QentradaFinal
        self.ptyGridItemVazaoEntradaFinal.SetValue(vazaoEntradaFinal)
        
        #Vazao de saida no trecjo - PV a jusante - Final
        self.ptyGridItemVazaoSaidaFinal.Enable(True)
        vazaoSaidaFinal = self.listaTrechos[0].QsaidaFinal
        self.ptyGridItemVazaoSaidaFinal.SetValue(vazaoSaidaFinal)
        
        #PROPRIEDADES HIDRAULICAS
        #Coeficiente de Manning
        self.ptyGridItemCoefManning.Enable(True)
        coefManning = self.listaTrechos[0].coefManning
        self.ptyGridItemCoefManning.SetValue(coefManning)
        
        #Velocidade no trecho para o inicio de plano
        self.ptyGridItemVelocidadeInicio.Enable(True)
        velocidadeTrechoInicio = self.listaTrechos[0].Vi
        self.ptyGridItemVelocidadeInicio.SetValue(velocidadeTrechoInicio)
        
        #Velocidade no trecho para o fim de plano
        self.ptyGridItemVelocidadeFinal.Enable(True)
        velocidadeTrechoFinal = self.listaTrechos[0].Vf
        self.ptyGridItemVelocidadeFinal.SetValue(velocidadeTrechoFinal)
        
        #Velocidade Critica do trecho para o inicio de plano
        self.ptyGridItemVelCriticaInicio.Enable(True)
        velocidadeCriticaInicio = self.listaTrechos[0].Vcritica_inicial
        self.ptyGridItemVelCriticaInicio.SetValue(velocidadeCriticaInicio)
        
        #Velocidade Critica do trecho para o final de plano
        self.ptyGridItemVelCriticaFinal.Enable(False)
        velocidadeCriticaFinal = self.listaTrechos[0].Vcritica_final
        self.ptyGridItemVelCriticaFinal.SetValue(velocidadeCriticaFinal)
        
        #Relaca Rh/D para o inicio de plano
        self.ptyGridItemRelacaoRh_D_inicial.Enable(False)
        relacao_Rh_D_inicio = self.listaTrechos[0].Rh_D_inicial
        self.ptyGridItemRelacaoRh_D_inicial.SetValue(relacao_Rh_D_inicio)
        
        #Relaca Rh/D para o final de plano
        self.ptyGridItemRelacaoRh_D_final.Enable(False)
        relacao_Rh_D_final = self.listaTrechos[0].Rh_D_final
        self.ptyGridItemRelacaoRh_D_final.SetValue(relacao_Rh_D_final)
        
        #Perimetro molhado para o inicio de Plano
        self.ptyGridItemPerimMolhadoInicio.Enable(False)
        perimetroMolhadoInicio = self.listaTrechos[0].PmInicial
        self.ptyGridItemPerimMolhadoInicio.SetValue(perimetroMolhadoInicio)

        #Perimetro molhado para o inicio de Plano
        self.ptyGridItemPerimMolhadoFinal.Enable(False)
        perimetroMolhadoFinal = self.listaTrechos[0].PmFinal
        self.ptyGridItemPerimMolhadoFinal.SetValue(perimetroMolhadoFinal)
        
        #Area molhada para o inicio de Plano
        self.ptyGridItemAreaMolhadaInicio.Enable(False)
        areaMolhadaInicial = self.listaTrechos[0].AmInicial
        self.ptyGridItemAreaMolhadaInicio.SetValue(areaMolhadaInicial)
        
        #Area molhada para o final de Plano
        self.ptyGridItemAreaMolhadaFinal.Enable(False)
        areaMolhadaFinal = self.listaTrechos[0].AmFinal
        self.ptyGridItemAreaMolhadaFinal.SetValue(areaMolhadaFinal)
        
        #Raio Hidraulico para o Inicio de Plano
        self.ptyGridItemRaioHidraulicoInicio.Enable(False)
        raioHidraulicoInicio = self.listaTrechos[0].RHinicial
        self.ptyGridItemRaioHidraulicoInicio.SetValue(raioHidraulicoInicio)

        #Raio Hidraulico para o final de Plano
        self.ptyGridItemRaioHidraulicoFinal.Enable(False)
        raioHidraulicoFinal = self.listaTrechos[0].RHfinal
        self.ptyGridItemRaioHidraulicoFinal.SetValue(raioHidraulicoFinal)
        
        #Altura Lamina de Agua para Inicio de PLano
        self.ptyGridItemAlturaLaminaInicio.Enable(False)
        alturaLaminaInicio = self.listaTrechos[0].Lamina_inicial
        self.ptyGridItemAlturaLaminaInicio.SetValue(alturaLaminaInicio)
        
        #Altura Lamina de Agua para Final de PLano
        self.ptyGridItemAlturaLaminaFinal.Enable(False)
        alturaLaminaFinal = self.listaTrechos[0].Lamina_final
        self.ptyGridItemAlturaLaminaFinal.SetValue(alturaLaminaFinal)
        
        #Cota da Lamina de Agua Montante (Apenas Final de Plano)
        self.ptyGridItemCotaLaminaMontante.Enable(False)
        cotaLaminaMontante = self.listaTrechos[0].CotaLaminaMontante
        self.ptyGridItemCotaLaminaMontante.SetValue(cotaLaminaMontante)
        
        #Cota da Lamina de Agua Jusante (Apenas Final de Plano)
        self.ptyGridItemCotaLaminaJusante.Enable(False)
        cotaLaminaJusante = self.listaTrechos[0].CotaLaminaJusante
        self.ptyGridItemCotaLaminaJusante.SetValue(cotaLaminaJusante)
        
        #Remanso (Apenas Final de Plano)
        self.ptyGridItemRemanso.Enable(False)
        remanso = self.listaTrechos[0].Remanso
        self.ptyGridItemRemanso.SetValue(remanso)
        
        #Altura do fundo do tubo no PV inicial do Trecho
        alturaInicioTrecho = self.listaTrechos[0].GetalturaInicioTrecho()
        self.ptyGridItemAlturaTuboInicioTrecho.SetValue(alturaInicioTrecho)
        
        #Altura do fundo do tubo no PV final do Trecho
        alturaFinalTrecho = self.listaTrechos[0].GetalturaFinalTrecho()
        self.ptyGridItemAlturaTuboFinalTrecho.SetValue(alturaFinalTrecho)
        
        #cobertura inicio do Trecho
        coberturaInicioTrecho = self.listaTrechos[0].coberturaInicioTrecho
        self.ptyGridItemCoberturaInicioTrecho.SetValue(coberturaInicioTrecho)
        
        #cobertura final do Trecho
        coberturaFinalTrecho = self.listaTrechos[0].coberturaFinalTrecho
        self.ptyGridItemCoberturaFinalTrecho.SetValue(coberturaFinalTrecho)
        

    # Sobrecarrega o metodo 'ModificaPropriedade' quando algo e alterado
    # na janela de propriedades do trecgo
    def ModificaPropriedade( self, event ):
        proprAlterada = event.GetPropertyName()
        valorAlterado = event.GetPropertyValue()
        
        if proprAlterada == u"Nome do Trecho":
            self.listaTrechos[0].nomeTrecho = valorAlterado        
        elif proprAlterada == u"Diâmetro do Trecho (mm)":           
            diam = event.GetProperty()
            D = self.listaTrechos[0].DIC_DIAMETROS[diam.GetValueString()]
            self.listaTrechos[0].SetDiametroTrecho(D)
        elif proprAlterada == u"Usar Comprimento Automatico":           
            self.listaTrechos[0].comprimentoAuto = valorAlterado
        elif proprAlterada == u"Comp do Trecho Definido (m)":           
            self.listaTrechos[0].Ldefinido = valorAlterado
        elif proprAlterada == u"Cota Geratriz Inferior Inicio (m)":
            self.listaTrechos[0].SetCGII(valorAlterado)
        elif proprAlterada == u"Cota Geratriz Inferior Final (m)":
            self.listaTrechos[0].SetCGIF(valorAlterado)
        elif proprAlterada == u"Cota Geratriz Superior Inicio (m)":
            self.listaTrechos[0].SetCGSI(valorAlterado)
        elif proprAlterada == "Cota Geratriz Superior Final (m)":
            self.listaTrechos[0].SetCGSF(valorAlterado)        
        elif proprAlterada == u"Declividade Minima (%)":
            pass
        elif proprAlterada == u"Declividade do Trecho (%)":
            valorAlterado = self.FormataDeclividade(valorAlterado)
            self.listaTrechos[0].SetDeclividade(valorAlterado)
        elif proprAlterada == u"Desnível (m)":
            self.listaTrechos[0].SetDesnivel(valorAlterado)
        elif proprAlterada == u"Contribuição Inicio de Plano (l/s.m)":
            self.listaTrechos[0].TaxaInicial = valorAlterado
        elif proprAlterada == u"Contribuição Final de Plano (l/s.m)":
            self.listaTrechos[0].TaxaFinal = valorAlterado
        elif proprAlterada == u"Vazão Pontual no Trecho (l/s)":
            self.listaTrechos[0].Qpontual = valorAlterado
        elif proprAlterada == u"Contribuição Parasitária (l/s.m)":
            self.listaTrechos[0].TaxaInfiltracao = valorAlterado
        elif proprAlterada == u"Contrib. Total do Trecho - Inicio (l/s)":
            pass
        elif proprAlterada == u"Contrib. Total do Trecho - Final (l/s)":
            pass
        elif proprAlterada == u"Vazão de Montante - Inicio (l/s)":
            pass
        elif proprAlterada == u"Vazão de Jusante - Inicio (l/s)":
            pass
        elif proprAlterada == u"Vazão de Montante - Final (l/s)":
            pass
        elif proprAlterada == u"Vazão de Jusante - Final (l/s)":
            pass
        elif proprAlterada == u"Coeficiente de Manning":
            self.listaTrechos[0].coefManning = valorAlterado
        elif proprAlterada == u"Velocidade Início de Plano (m/s)":
            pass
        elif proprAlterada == u"Velocidade Final de Plano (m/s)":
            pass
        elif proprAlterada == u"Perímetro Molhado Início":
            pass
        elif proprAlterada == u"Perimetro Molhado Final":
            pass
        elif proprAlterada == u"Área Molhada Início":
            pass
        elif proprAlterada == u"Área Molhada Final":
            pass
        elif proprAlterada == u"Raio Hidráulico Início":
            pass
        elif proprAlterada == u"Raio Hidráulico Final":
            pass
        elif proprAlterada == u"Altura Lâmina Água Inicio (m)":
            pass
        elif proprAlterada == u"Altura Lâmina Água Final (m)":
            pass
        elif proprAlterada == u"Altura Fundo Tubo Inicio Trecho (m)":
            self.listaTrechos[0].SetAlturaInicioTrecho(valorAlterado)
        elif proprAlterada == u"Altura Fundo Tubo Final Trecho (m)":
            self.listaTrechos[0].SetAlturaFinalTrecho(valorAlterado)
        elif proprAlterada == u"Cobertura no Inicio do Trecho (m)":
            self.listaTrechos[0].SetCoberturaInicioTrecho(valorAlterado)
        elif proprAlterada == u"Cobertura no Final do Trecho (m)":
            self.listaTrechos[0].SetCoberturaFinalTrecho(valorAlterado)
        
        self.parent.ConeCanvas.AtualizaTodasAsGlList()
        self.InicializaPropriedades() #reseta os valores apos mudanca
        #event.Skip()

    def FormataDeclividade(self, valorDecliv):
        """ Funcao para formatar a declividade inserida na janela de
            propriedades, pois tem caracteres do tipo float e strings
            
            Caso a funcao nao consiga formatar a string para float, devolve
            o valor antigo.
        """        
        if (valorDecliv.count('%') == 1 and valorDecliv[-1] == "%"):
            try:
                 valorDecliv = float(valorDecliv.split("%")[0])/100
                 return valorDecliv
            except:
                return float(self.valoresAntigos["Iadotada"])/100
        else:
            try:
                 valorDecliv = float(valorDecliv)/100
                 return valorDecliv
            except:
                return float(self.valoresAntigos["Iadotada"])/100
                
    
    def OnClose(self):
        pass
        #self.Destroy()