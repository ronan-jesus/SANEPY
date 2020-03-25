# -*- coding: utf-8 -*-

import wx
from GUI_janelaGerenciaPerfis import JanelaGerenciaPerfis
try:
    import wx.gizmos as gizmos
    
    class TreeListCtrl(gizmos.TreeListCtrl):
        """
        This class implements the functions of the new Phoenix interface
        using the classic TreeListCtrl api, in order to make the transition between 
        them as seamless as possible
        """
            
        def AppendColumn(self, colname, **kwargs):
            # classic style
            if 'align' in kwargs:
                kwargs['flag'] = kwargs.pop('align')
            self.AddColumn(colname, **kwargs)
            
        def AppendItem(self, parent, text, imageClosed=-1, imageOpened=-1):
            # classic style
            child = gizmos.TreeListCtrl.AppendItem(self, parent, text)
            self.SetItemImage(child, imageClosed, which = wx.TreeItemIcon_Normal)
            self.SetItemImage(child, imageOpened, which = wx.TreeItemIcon_Expanded)
            return child
        
        def SetItemText(self, item, col, value):
            child = gizmos.TreeListCtrl.SetItemText(self, item, value, col)
            
        def FillColumn(self, index, value):
            item = self.GetRootItem()
            while item.IsOk():
                self.SetItemText(item,value,index)
                item = self.GetNextItem(item)
        
        def GetNextItem(self, item):
            return self.GetNext(item) # GetNextItem in wxwidgets - why was it called GetNext in wxpython?
                
        def GetFirstChild(self, item):
            item, junk = gizmos.TreeListCtrl.GetFirstChild(self, item)
            return item
            
        def ClearColumns(self):
            while self.GetColumnCount() > 0:
                self.RemoveColumn(0)
except ImportError:
    from wx.dataview import TreeListCtrl    
        
    
class TreeListCtrlPerfil(JanelaGerenciaPerfis):
    def __init__(self, parent, perfil):
        JanelaGerenciaPerfis.__init__(self, parent)        
        self.parent = parent
        self.perfil = perfil
        
        self.sbSizer4.SetMinSize(self.sbSizer1.Size)
        
        self.tree = TreeListCtrl(self.m_panel3)   
        
        self.tree.AddColumn("None")
        self.tree.AddColumn("Descrição") 
        
        self.tree.SetColumnEditable(1, True) #Faz com que a coluna seja editavel
        
        self.tree.SetMainColumn(0)
        self.root = self.tree.InsertItem(self.tree.GetRootItem(), gizmos.TR_AUTO_CHECK_CHILD, "ELEMENTOS")
        self.rootPvs = self.tree.InsertItem(self.root, gizmos.TR_AUTO_CHECK_CHILD, "PVs")
        self.rootTrechos = self.tree.InsertItem(self.root, gizmos.TR_AUTO_CHECK_CHILD, "TRECHOS")
        self.tree.Expand(self.root)
        
        self.InicializaDados()
        
        self.boxSizerElementos.Add( self.tree, 1, wx.ALIGN_RIGHT|wx.EXPAND, 5 )
        self.Fit()
       
        self.Show()
        
    def InicializaDados(self):
        perfil = self.perfil
        ##################### TAB INFORMACOES #####################
        self.txt_NomePerfil.SetValue(str(self.perfil.tittleLabel))
        self.txt_DescricaoPerfil.SetValue(str(self.perfil.descricao))
        
        ##################### TAB ELEVACOES e ESCALAS #####################        
        
        self.btrad_Automatico.SetValue(self.perfil.elevAutomatico)
        cotaMin, cotaMax = self.perfil.GetCotaMinMaxAutomatico()
        self.txt_ElevInicioAuto.SetValue(str(cotaMin))
        self.txt_ElevFinalAuto.SetValue(str(cotaMax))
        
        self.btrad_Definido.SetValue(not self.perfil.elevAutomatico)
        self.txt_ElevInicioDefinido.SetValue(str(self.perfil.ElevMinDefinida))
        self.txt_ElevFinalDefinido.SetValue(str(self.perfil.ElevMaxDefinida))
        
        if self.perfil.elevAutomatico == True:
            self.txt_ElevInicioAuto.Enable()
            self.txt_ElevFinalAuto.Enable()
            self.txt_ElevInicioDefinido.Disable()
            self.txt_ElevFinalDefinido.Disable()            
        else:
            self.txt_ElevInicioAuto.Disable()
            self.txt_ElevFinalAuto.Disable()
            self.txt_ElevInicioDefinido.Enable()
            self.txt_ElevFinalDefinido.Enable()
        
        self.txt_escalaHorizontal.SetValue(str(perfil.escalaHorizontal))
        self.txt_escalaVertical.SetValue(str(perfil.escalaVertical))
        
        ##################### TAB TRECHOS E ESTRUTURAS #####################
        for pv in self.perfil.GetListaPVsdoPerfil():
            txtPv = "PV - %d" % pv.numero
            child = self.tree.AppendItem(self.rootPvs, txtPv)
            self.tree.SetItemText(child, 1, "Retangular 1,00mx1,0,80mx1,50m")
            
        for trecho in self.perfil.GetListaTrechosdoPerfil():
            txtTrecho = "Trecho - %d" % trecho.numero
            child = self.tree.AppendItem(self.rootTrechos, txtTrecho)
            self.tree.SetItemText(child, 1, "PVC-OCRE 150mm")        
        
        self.tree.Expand(self.rootPvs)
        self.tree.Expand(self.rootTrechos)
    
    def OnRadioButtomElevacoes(self, event):
        rb = event.EventObject.GetLabel()
        
        if rb == u"Automático":            
            self.txt_ElevInicioAuto.Enable()
            self.txt_ElevFinalAuto.Enable()
            self.txt_ElevInicioDefinido.Disable()
            self.txt_ElevFinalDefinido.Disable()
            
            cotaMin, cotaMax = self.perfil.GetCotaMinMaxAutomatico()
            
            self.txt_ElevInicioAuto.SetValue(str(cotaMin))
            self.txt_ElevFinalAuto.SetValue(str(cotaMax))
            
        elif rb == u"Definido Pelo Usuário":
            self.txt_ElevInicioDefinido.Enable()
            self.txt_ElevFinalDefinido.Enable()
            self.txt_ElevInicioAuto.Disable()
            self.txt_ElevFinalAuto.Disable()           
            
        

    def OnOkButton(self, event):
        perfil = self.perfil
        
        ############# INFORMACOES #########################
        nome = self.txt_NomePerfil.GetValue()
        perfil.tittleLabel = nome       
        
        desc = self.txt_DescricaoPerfil.GetValue()
        perfil.descricao = desc 
        
        ############# ELEVACOES E ESCALAS #########################
        #Elevacoes
        if self.btrad_Automatico.GetValue() == True:
            perfil.cotaMinima = float(self.txt_ElevInicioAuto.GetValue())
            perfil.cotaMaxima = float(self.txt_ElevFinalAuto.GetValue())
            self.perfil.elevAutomatico = True
            
        elif self.btrad_Definido.GetValue() == True:
            perfil.ElevMinDefinida = float(self.txt_ElevInicioDefinido.GetValue())
            perfil.ElevMaxDefinida = float(self.txt_ElevFinalDefinido.GetValue())
            
            perfil.cotaMinima = perfil.ElevMinDefinida
            perfil.cotaMaxima = perfil.ElevMaxDefinida            
            
            self.perfil.elevAutomatico = False
         
        #Escalas
        perfil.escalaHorizontal = int(self.txt_escalaHorizontal.GetValue())
        perfil.escalaVertical = int(self.txt_escalaVertical.GetValue())
        
        
        self.parent.ConeCanvas.AtualizaDesenhoPerfis()
        
        self.OnClose()
    
    def OnCancelButton(self, event):
        self.OnClose()
        
    def OnClose(self):
        self.Destroy()
       

if __name__ == "__main__":        
    app = wx.App()
    frame = TreeListCtrlPerfil(None)
    app.MainLoop()
