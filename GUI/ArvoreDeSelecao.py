# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc
import wx.lib.agw.customtreectrl


class ArvoreSelecaoElementos( wx.Panel ):
    def __init__(self, parent):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
        
        self.parent = parent
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        		
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        		
        self.tctrl_ArvoreSelecaoElementos = self.CriaTreeCtrl()
        bSizer1.Add( self.tctrl_ArvoreSelecaoElementos, 1, wx.ALL|wx.EXPAND, 5 )	
        
        self.SetSizer( bSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )

        # Connect Events
        self.tctrl_ArvoreSelecaoElementos.Bind( wx.lib.agw.customtreectrl.EVT_TREE_ITEM_CHECKED , self.ItemCheckTreeCtrl )
        self.Bind(wx.EVT_CONTEXT_MENU, self.onContext)
        
        self.Show()        
    	  
        
        
    def CriaTreeCtrl(self):
        myModule = wx.lib.agw.customtreectrl
        myStyle = (myModule.TR_DEFAULT_STYLE|myModule.TR_MULTIPLE
           |myModule.TR_FULL_ROW_HIGHLIGHT|myModule.TR_AUTO_CHECK_CHILD
           |myModule.TR_AUTO_CHECK_PARENT|myModule.TR_AUTO_TOGGLE_CHILD)

        tree = myModule.CustomTreeCtrl(self, agwStyle=myStyle)
        self.treeRoot = tree.AddRoot("Grupos")
        self.rootNOS =  tree.AppendItem(self.treeRoot, "PVs", ct_type=1)
        self.rootBARRAS =  tree.AppendItem(self.treeRoot, "TRECHOS", ct_type=1)
        tree.Expand(self.treeRoot)
        #treeNodes =['Node A','Node C']
        #treeItems = ['1', '2', '3']
        #for i, _ in enumerate(treeNodes):
        #    iNode = tree.AppendItem(treeRoot, treeNodes[i], ct_type=1)
        #    for ii in treeItems:
        #        tree.AppendItem(iNode, "%s %s"%(treeNodes[i].replace('Node ',''), ii), ct_type=1)
        #tree.Expand(treeRoot)
        
        return tree
    # Virtual event handlers, overide them in your derived class
    def ClickButton( self, event ):
        if self.m_panel1.IsShown():
            self.m_panel1.Hide()
        else:
            self.m_panel1.Show()
        
        # redo the layout
        self.m_panel2.Fit()        
        self.Layout()
        
        event.Skip()
    
    def RightClickTree(self, evt):
        itemSelecionado =  self.tctrl_ArvoreSelecaoElementos.GetSelection()
        item = itemSelecionado.GetText()
        
        if item.split(" ")[0] in [u"PVs" or u"TRECHOS"]:
            return item.split(" ")[0]
            #self.onContext(evt)        
        elif item.split(" ")[0] == u"PV":
            pass
            #print itemSelecionado.GetChildren()
        
         
    def ItemCheckTreeCtrl(self, evt):
        item =  self.tctrl_ArvoreSelecaoElementos.GetSelection()
        
        if item.GetText().split(" ")[0] == u"PVs":
            visivelStatus = item.GetValue()
            for no in self.parent.Estrututura.LISTA_PVS:
                no.visivel = visivelStatus
                
        elif item.GetText().split(" ")[0] == u"TRECHOS":
            visivelStatus = item.GetValue()
            for barra in self.parent.Estrututura.LISTA_TUBULACOES:
                barra.visivel = visivelStatus
                
        elif item.GetText().split(" ")[0] == u"PV":
            no = self.parent.Estrututura.Dic_Lista_Pvs[int(item.GetText().split(" ")[1])]
            no.visivel = item.GetValue()
        elif item.GetText().split(" ")[0] == u"Barra":
            barra = self.parent.Estrututura.Dic_Lista_Tubulacoes[int(item.GetText().split(" ")[1])]
            barra.visivel = item.GetValue()            
        
        self.parent.Regeneration()
    
    #----------------------------------------------------------------------
    def onContext(self, event):
        """
        Create and show a Context Menu
        """
        # only do this part the first time so the events are only bound once 
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()
            self.Bind(wx.EVT_MENU, self.Selecionar, id=self.popupID1)
            self.Bind(wx.EVT_MENU, self.Desenselecionar, id=self.popupID2)
 
        # build the menu
        menu = wx.Menu()
        menu.Append(self.popupID1, "Selecionar")
        menu.Append(self.popupID2, "Deselecionar")
 
        # show the popup menu
        self.PopupMenu(menu)
        menu.Destroy()
        
    #----------------------------------------------------------------------
    def Selecionar(self, event):
        """
        Print the label of the menu item selected
        """
        EstruturasSelecionadas = {}
        EstruturasSelecionadas["PVs"] = []
        EstruturasSelecionadas["TRECHOS"] = []
        
        itensSelecionados =  [x.GetText() for x in self.tctrl_ArvoreSelecaoElementos.GetSelections()]
        if "Grupos" in itensSelecionados:
            pass
        elif any((item == "PVs" or item == "TRECHOS") for item in itensSelecionados):
            #Adiciona todo os Nos
            if any(item == "PVs" for item in itensSelecionados):
                EstruturasSelecionadas["PVs"] = self.parent.Estrututura.Dic_Lista_Pvs.keys()                
            #Adiciona todas as barras
            if any(item == "TRECHOS" for item in itensSelecionados):
                EstruturasSelecionadas["TRECHOS"] = self.parent.Estrututura.Dic_Lista_Tubulacoes.keys()
                EstruturasSelecionadas["TRECHOS"] = map(lambda x:x, EstruturasSelecionadas["TRECHOS"])
        elif any((item.split(" ")[0] ==u"PV" or item.split(" ")[0] ==u"Barra") for item in itensSelecionados):
            #Adiciona os Nos selecionados
            nos = [int(x.split(" ")[1]) for x in itensSelecionados if x.split(" ")[0] == u"PV"]
            #Adiciona as barras selecionadas
            barras = [int(x.split(" ")[1]) for x in itensSelecionados if x.split(" ")[0] == u"Barra"]
            barras = map(lambda x:x, barras)
            
            EstruturasSelecionadas["PVs"] = nos
            EstruturasSelecionadas["TRECHOS"] = barras            
        
        #Chama a Funcao SelecionaelementosNaTreeCtrl no "model" para fazer a
        #selecao do elementos selecionados na TreeCtrl
        self.parent.SelecionaelementosNaTreeCtrl(EstruturasSelecionadas)        
        
    def Desenselecionar(self, evt):
        """Faz a deselecao dos elementos que estao selecionados no painel
           Lateral Direito, Grupos->Grupo->Elemento
        """
        
        EstruturasSelecionadas = {}
        EstruturasSelecionadas["PVs"] = []
        EstruturasSelecionadas["TRECHOS"] = []
        
        itensSelecionados =  [x.GetText() for x in self.tctrl_ArvoreSelecaoElementos.GetSelections()]
        if "Grupos" in itensSelecionados:
            pass
        elif any((item == "PVs" or item == "TRECHOS") for item in itensSelecionados):
            #Adiciona todo os Nos
            if any(item == "PVs" for item in itensSelecionados):
                EstruturasSelecionadas["PVs"] = self.parent.Estrututura.Dic_Lista_Pvs.keys()
            #Adiciona todas as barras
            if any(item == "TRECHOS" for item in itensSelecionados):
                EstruturasSelecionadas["TRECHOS"] = self.parent.Estrututura.Dic_Lista_Tubulacoes.keys()
                EstruturasSelecionadas["TRECHOS"] = map(lambda x:x, EstruturasSelecionadas["TRECHOS"])
        elif any((item.split(" ")[0] ==u"PV" or item.split(" ")[0] ==u"Barra") for item in itensSelecionados):
            #Adiciona os Nos selecionados
            nos = [int(x.split(" ")[1]) for x in itensSelecionados if x.split(" ")[0] == u"PV"]
            #Adiciona as barras selecionadas
            barras = [int(x.split(" ")[1]) for x in itensSelecionados if x.split(" ")[0] == u"Barra"]
            barras = map(lambda x:x, barras)
            
            EstruturasSelecionadas["PVs"] = nos
            EstruturasSelecionadas["TRECHOS"] = barras
            
        self.parent.DeselecionarElementosNaTreeCtrl(EstruturasSelecionadas)
    
    def CriaTreeCrlt(self, LISTA_PVS, LISTA_TUBULACOES):
        for no in LISTA_PVS:
            item = self.tctrl_ArvoreSelecaoElementos.AppendItem(self.rootNOS, u"PV "+str(no.numero), ct_type=1)
            item.Check()
        for barra in LISTA_TUBULACOES:
            item = self.tctrl_ArvoreSelecaoElementos.AppendItem(self.rootBARRAS, u"Trecho "+str(barra.numero), ct_type=1)
            item.Check()
        
        self.rootNOS.Expand()
        self.rootBARRAS.Expand()        
        self.treeRoot.Expand()
                
    def AdicionaNOTreeCtrl(self, No):      
        item = self.tctrl_ArvoreSelecaoElementos.AppendItem(self.rootNOS, u"PV "+str(No.numero), ct_type=1)
        if No.visivel == True:
            item.Check()            
        else:
            pass
        
    def AdicionaBarraTreeCtrl(self, Barra):      
        item = self.tctrl_ArvoreSelecaoElementos.AppendItem(self.rootBARRAS, u"Trecho "+str(Barra.numero), ct_type=1)
        if Barra.visivel == True:
            item.Check()
        else:
            pass
        
    def DeleteNoTreeCtrl(self, LISTA_PVS):
        self.tctrl_ArvoreSelecaoElementos.DeleteChildren(self.rootNOS)
        for no in LISTA_PVS:
            item = self.tctrl_ArvoreSelecaoElementos.AppendItem(self.rootNOS, u"PV "+str(no.numero), ct_type=1)
            if no.visivel == True:
                item.Check()
            else:
                pass
            
    def DeleteBarraTreeCtrl(self, LISTA_TUBULACOES):
        self.tctrl_ArvoreSelecaoElementos.DeleteChildren(self.rootBARRAS)
        for barra in LISTA_TUBULACOES:
            item = self.tctrl_ArvoreSelecaoElementos.AppendItem(self.rootBARRAS, u"Trecho "+str(barra.numero), ct_type=1)
            if barra.visivel == True:
                item.Check()
            else:
                pass
            
    def ClearTreeCtrl(self):
        self.tctrl_ArvoreSelecaoElementos.DeleteChildren(self.rootNOS)
        self.tctrl_ArvoreSelecaoElementos.DeleteChildren(self.rootBARRAS)
        
    def __del__( self ):
        pass



class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.PainelLaretal = ArvoreSelecaoElementos(self)
        
        self.Show()
    
    
    
    
if __name__ == "__main__":   
    app = wx.App(redirect=False)
    MyFrame(None)
    app.MainLoop()