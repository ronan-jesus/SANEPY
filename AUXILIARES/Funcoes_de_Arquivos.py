# -*- coding: utf-8 -*-
import os
import wx
import timeit

try:
    import cPickle as pickle
except:
    import pickle

def salvaProjeto(estrutura, event, caminho=None):    
    """
    Funcao responsavel por abrir a janela de salvamento, escolhe o nome e local
    do arquivo, apos faz o salvamento do arquivo contento a classe ESTRUTURA
    a classe /e salva inteira com o cPickle
    """
    if caminho == None:
        dlg = wx.FileDialog(event.GetEventObject().GetParent(), "Save project as...", os.getcwd(), "", "*.txt", wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        result = dlg.ShowModal()
        inFile = dlg.GetPath()
        dlg.Destroy()

        if result == wx.ID_OK:  #Botao salvar foi pressionado            
            # Abra o arquivo (leitura)
            
            
            with open(inFile, 'wb') as arquivo:                
                pickle.dump(estrutura,arquivo)
                arquivo.close()

            #Salva caminho do arquivo salvo, para salvar automaticamente
            #Ou apenas salvar, sem abrir o dialogo de SALVAR COMO.            
            if event.GetEventObject().GetParent():
                event.GetEventObject().GetParent().path_arquivo = inFile
            else:
                event.GetEventObject().path_arquivo = inFile
            return True

        elif result == wx.ID_CANCEL:    #Qualque um dos botoes cancelar ou fechar janela
            return False
    else:
        # Abra o arquivo (leitura)
        with open(inFile, 'wb') as arquivo:      
            pickle.dump(estrutura,arquivo)
            arquivo.close()


def OnOpen(event):
        """
        Funcao para abrir dialogo de selecao de arquivo para abertura, carrega um arquivo
        gravado com cPickle
        """
        dlg = wx.FileDialog(event.GetEventObject().GetParent(), message="Abrir Arquivo...", defaultDir=os.getcwd(),
                            defaultFile="", style=wx.FD_OPEN)

        # Call the dialog as a model-dialog so we're required to choose Ok or Cancel
        if dlg.ShowModal() == wx.ID_OK:
            start = timeit.default_timer()
            print ("Iniciou a abertura do arquivo")        
        
            # User has selected something, get the path, set the window's title to the path
            filename = dlg.GetPath()

            arquivo = file(filename, 'r')
            Dados = pickle.load(arquivo)
            arquivo.close()

        dlg.Destroy() # we don't need the dialog any more so we ask it to clean-up
        
        stop = timeit.default_timer()
        print ("Finalizou a abertura do arquivo - Tempo de %s segundos" %(stop - start))
        
        event.Skip()
        
        return Dados, filename

def salvaImagem(event):    
    dlg = wx.FileDialog(event.GetEventObject().GetParent(), "Save project as...", os.getcwd(), "", "*.png", wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
    result = dlg.ShowModal()
    inFile = dlg.GetPath()
    dlg.Destroy()
    if result == wx.ID_OK:  #Botao salvar foi pressionado            
        return inFile

    elif result == wx.ID_CANCEL:    #Qualque um dos botoes cancelar ou fechar janela
        return False
