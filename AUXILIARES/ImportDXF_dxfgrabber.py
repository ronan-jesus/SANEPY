# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:00:27 2017

@author: RONAN TEODORO
"""
import os
import wx
import ezdxf
import dxfgrabber

import numpy as np
import timeit

def AbrirArquivo(event, tipo_arq):
        """
        Funcao para abrir dialogo de selecao de arquivo para abertura, carrega um arquivo
        gravado com cPickle
        """
        dlg = wx.FileDialog(event.GetEventObject().GetParent(), message="Abrir Arquivo...", defaultDir=os.getcwd(),
                            defaultFile="", style=wx.OPEN)

        # Call the dialog as a model-dialog so we're required to choose Ok or Cancel
        if dlg.ShowModal() == wx.ID_OK:
            # User has selected something, get the path, set the window's title to the path
            filename = dlg.GetPath()

        dlg.Destroy() # we don't need the dialog any more so we ask it to clean-up

        return filename
            
def ImportaArquivoDXF(path):
    ###########################
    start = timeit.default_timer() #Inicia contagem do tempo
    ###########################
    
    dwg = dxfgrabber.readfile(path)
    
    listaNOStoImport = []
    listaBARRAStoImport = []
    
    all_lines = [entity for entity in dwg.entities if entity.dxftype == 'LINE']
    
    for e in all_lines:
        no1 = None
        no2 = None        
        if  [round(e.start[0], 8), round(e.start[1], 8), round(e.start[2], 8)] not in listaNOStoImport:  
            listaNOStoImport.append([round(e.start[0], 8), round(e.start[1], 8), round(e.start[2], 8)])
            no1 = len(listaNOStoImport)-1
        else:
            no1 = listaNOStoImport.index([round(e.start[0], 8), round(e.start[1], 8), round(e.start[2], 8)])
        
        if [round(e.end[0], 8), round(e.end[1], 8), round(e.end[2], 8)] not in listaNOStoImport:            
            listaNOStoImport.append([round(e.end[0], 8), round(e.end[1], 8), round(e.end[2], 8)])
            no2 = len(listaNOStoImport)-1
        else:
            no2 = listaNOStoImport.index([round(e.end[0], 8), round(e.end[1], 8), round(e.end[2], 8)])
            
        listaBARRAStoImport.append([no1, no2])
        
    
    listaNOStoImport = np.array(listaNOStoImport)        
    _listaNOStoImport = np.unique(listaNOStoImport, axis=0)
    print "Quantidade Total de Pontos  == %s" %len(_listaNOStoImport)
    
    arquivo = open('TEST_DXF.txt', 'w') #GRAVA OS DADOS NO ARQUIVO TEXTO
    arquivo.write("%s\n" %listaBARRAStoImport) #GRAVA OS DADOS NO ARQUIVO TEXTO
    arquivo.close() #GRAVA OS DADOS NO ARQUIVO TEXTO
    
    ###########################
    stop = timeit.default_timer()
    print "Finalizou a abertura do arquivo - Tempo de %s segundos" %(stop - start)
    ###########################
    
    return listaNOStoImport, listaBARRAStoImport