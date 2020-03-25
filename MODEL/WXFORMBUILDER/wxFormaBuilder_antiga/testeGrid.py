# -*- coding: utf-8 -*-

import wx
from painelPropriedadesTrechos import PainelPropTrechos


#----------------------------------------------------------------------
class App(wx.Frame):
    
    DIAMETROS = ["Ø100mm", "Ø150mm", "Ø200mm", "Ø250mm", "Ø300mm", "Ø350mm",
                 "Ø400mm", "Ø450mm", "Ø500mm", "Ø550mm", "Ø600mm"
                 ]
                 
    def __init__(self, parent):
        wx.Frame.__init__ ( self, parent)
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        self.painel = PainelPropTrechos(self)
        
        bSizer1.Add(self.painel)

        self.Show()
  
        
        
if __name__ == '__main__':
    app = wx.App()
    App(None)
    app.MainLoop()
