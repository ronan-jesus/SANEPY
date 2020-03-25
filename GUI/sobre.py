# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 04:20:09 2017

@author: RONAN TEODORO
"""

import wx
import wx.html
import webbrowser
 
class AboutDlg(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title="Sobre o Programa", size=(450,300))
        html = wxHTML(self)
        html.SetPage(
            ''
 
            "<h2>Sobre o UNIBARRAS3D Beta 0.0.1</h2>"
            
            "<h4>Desenvolvedores</h4>"
 
            u"<p>Engº Civil Ronan Teodoro de Jesus</p>"
            u"<p>Profº Dr. Uziel Cavalcanti de Medeiros Quinino</p>"            
 
            '<p><b><a href="http://www.unibarras3d.com.br">http://www.unibarras3d.com.br</a></b></p>'
            )

    def OnClose(self):
        self.Destroy()
        
class wxHTML(wx.html.HtmlWindow):
     def OnLinkClicked(self, link):
         webbrowser.open(link.GetHref(), new=2)
 
 
# Run the program
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = AboutDlg(None)
    app.MainLoop()