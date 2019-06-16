# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from gui_janela_cria_perfil import GUI_CriaPerfil
###########################################################################
## Class DlgGerenciaNO
###########################################################################

class JanelaCriaPerfil( GUI_CriaPerfil ):
    def __init__( self, parent):
        GUI_CriaPerfil.__init__ (self, parent)
        self.parent = parent
        
        self.Show() 
    
   
    def OnButtonOK(self, evt):
        nomePerfil = self.txt_nomePerfil.GetValue()
        pvInicial = self.txt_perfilInicial.GetValue()
        pvFinal = self.txt_perfilFinal.GetValue()
        
        self.parent.ON_PERFIL = [True, [nomePerfil, pvInicial, pvFinal]]
        
        self.Destroy()
    
    def OnButtonCancel(self, evt):
        self.OnClose()
        
    def OnClose(self, evt):
        self.Destroy()
        
    