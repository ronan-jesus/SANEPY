# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc
from gui_WinInsertCoord import Gui_Dialog_InsertCoord

###########################################################################
## Class Dialog_InsertCoord
###########################################################################


class Dialog_InsertCoord ( Gui_Dialog_InsertCoord ):
    def __init__( self, parent ):
        Gui_Dialog_InsertCoord.__init__ (self, parent)
        self.parent = parent
        self.SetPosition((100,100))
        self.Show()

        self.InicializaJanela()
    
    def InicializaJanela(self):
        """INICIALIZA OS ELEMENTOS DA JANELA DE INSERCAO DE COORDENADAS.
           FAZ AS ALTERACOES DOS TIPOS DE UNIDADES        
        """        
        unidade = "(m)"        
        if self.parent.UnidadeComprimento == "[m] - Metro":
            unidade = "(m)"
        elif self.parent.UnidadeComprimento == "[cm] - Centimetro":
            unidade = "(cm)"
        elif self.parent.UnidadeComprimento == "[mm] - milimetro":
            unidade = "(mm)"
        elif self.parent.UnidadeComprimento == "[ft] - Pes":
            unidade = "(ft)"
        elif self.parent.UnidadeComprimento == "[in] - Polegada":
            unidade = "(in)"            
            
        self.lbl_coord_x.SetLabel(unidade)
        self.lbl_coord_y.SetLabel(unidade)
        self.lbl_coord_z.SetLabel(unidade)
        
    def VerificaTextBox(self, event):
        """Verifica Qual CheckBox esta selecionada, se for Global a checkBox
           Local e' deselecionada, o contrario tambem"""
        #Verifica se a checkbox global esta selecionada
        if event.GetEventObject().GetLabel()== self.chb_global.GetLabel():
            if self.chb_global.IsChecked():
                self.chb_relativo.SetValue(False)
                self.parent.TIPO_COORDS = "GLOBAL"
            else:
                self.chb_relativo.SetValue(True)
                self.parent.TIPO_COORDS = "RELATIVO"

        #Verifica se a checkbox relativo esta selecionada
        if event.GetEventObject().GetLabel()== self.chb_relativo.GetLabel():
            if self.chb_relativo.IsChecked():
                self.chb_global.SetValue(False)
                self.parent.TIPO_COORDS = "RELATIVO"
            else:
                self.chb_global.SetValue(True)
                self.parent.TIPO_COORDS = "GLOBAL"

        event.Skip()



    # Virtual event handlers, overide them in your derived class
    def Onchar_txtCoord( self, evt ):
        self.VerificaSeNumero(evt.GetEventObject().GetValue(), evt)
        evt.Skip()

    def VerificaSeNumero(self, valor, evt):
        try:
            self.parent.COORDS_ATUAIS = list([float(self.txt_coordx.GetValue())*100,
                                                       float(self.txt_coordy.GetValue())*100,
                                                        float(self.txt_coordz.GetValue())*100])
            evt.Skip()
        except:
            evt.GetEventObject().SetValue("0")
            evt.Skip()

    def OnClose(self):
        self.Destroy()
        
    def __del__( self ):
        pass
