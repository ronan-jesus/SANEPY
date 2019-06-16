# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 21:38:55 2018

@author: RONAN TEODORO

ALGORITMO REPONSAVEL POR ABRIR O ARQUIVO 'TabelaIndicesGeometricos' E CRIAR
A LISTA COM OS DADOS GEOMETRICOS DO DIMENSIONAMENTO HIDRAULICOS DOS TUBOS
EM ESCOAMENTO LIVRE. A FUNCAO
"""

def CriaTabelaIndices():
    """ Cria a tabela de indices geometricos dos tubos. O retorno e uma lista
        de listas com os indices [h/D, Ø, A/D², R/D,Pm/D, Qh/QD, Vh/VD].

    """
    try:
        arq = "ARQUIVOS\TabelaIndicesGeometricos.txt"
        arquivo = open(arq, "r")
    except:
        arq = "..\ARQUIVOS\TabelaIndicesGeometricos.txt"
        arquivo = open(arq, "r")
        
    
    
    INDICES = []
    for linha in arquivo.readlines():
        l = []
        for valor in linha.rstrip("\n").split("	"):
            l.append(valor)
        INDICES.append(l)
    
    return INDICES