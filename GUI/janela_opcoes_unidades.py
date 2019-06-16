# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 20:04:27 2017

@author: RONAN TEODORO
"""

from gui_OpcoesDeUnidades import GuiOpcoesUnidades

class JanelaOpcoesUnidades(GuiOpcoesUnidades):
    def __init__(self, parent):
        GuiOpcoesUnidades.__init__(self, parent)
        self.parent = parent
        self.Show()
        
        self.AtualizaUnidades()
       
       
    def AtualizaUnidades(self):
        self.cbx_UnidadeComprimento.SetValue(self.parent.UnidadeComprimento)
        self.cbx_UnidadeForca.SetValue(self.parent.UnidadeForca)
        self.cbx_UnidadeAngulo.SetValue(self.parent.UnidadeAngulo)
        self.cbx_FormatoComprimento.SetValue(self.parent.FormatoComprimento)
        self.cbx_FormatoForca.SetValue(self.parent.FormatoForca)
        self.cbx_FormatoAngulo.SetValue(self.parent.FormatoAngulo)
    
    def SalvaUnidades(self):
        UnidCompr = self.cbx_UnidadeComprimento.GetValue()
        UnidForca = self.cbx_UnidadeForca.GetValue()
        UnidAngulo = self.cbx_UnidadeAngulo.GetValue()
        FormCompr = self.cbx_FormatoComprimento.GetValue()
        FormForca = self.cbx_FormatoForca.GetValue()
        FormAngulo = self.cbx_FormatoAngulo.GetValue()

        

        self.parent.SetUnidades_e_Formatos(UnidCompr,UnidForca,UnidAngulo,
                                          FormCompr,FormForca,FormAngulo)        
        
    def OnClose( self, event ):
        self.Destroy()
        event.Skip()
    	
    def OnButton_OK( self, event ):
        self.SalvaUnidades()                        
        self.OnClose(event)
        event.Skip()
    	
    def OnButton_Cancel( self, event ):
        self.Destroy()
        event.Skip()