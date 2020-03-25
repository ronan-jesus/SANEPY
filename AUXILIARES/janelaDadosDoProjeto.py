# -*- coding: utf-8 -*-

from GUI_DadosDoProjeto import Gui_DadosDoProjeto

class JanelaDadosDoProjeto(Gui_DadosDoProjeto):
    def __ini__(self, parent):
        Gui_DadosDoProjeto.__init__(self, parent)
        
        self.parent = parent
        
        self.Show()