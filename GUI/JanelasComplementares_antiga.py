# -*- coding: utf-8 -*-
import wx
#import wx.xrc
        
class ChangeDepthDialog(wx.Dialog):
    def __init__( self, parent):
        wx.Dialog.__init__ (self, parent,  id = wx.ID_ANY, title = u"Definição de Materiais", pos = wx.DefaultPosition, size = wx.Size( 400,400 ), style = wx.DEFAULT_DIALOG_STYLE )
                
        self.parent = parent
        #Bandeira para alterar os modos de salvamento do materia (salvar/modificar)
        self.FLAG = "salvar"
        
        self.listaMateriais = self.parent.Estrututura.LISTA_MATERIAIS
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        self.materialEmUso = None
        
        
        self.InitUI()
        
        self.SetSize((600, 600))        
        
        self.Show()
        
        
        
    def InitUI(self):
        """
        Cria os componentes da janela de definicao de material
        """
        
        #Painel Principal onde fica os outros componentes
        painel_principal = wx.Panel(self)
        
        #Painel de Botoes, onde ficara os botoes novo, modificar, excluir, e usar
        btnPanel = wx.Panel(painel_principal, -1)
        
        #Botoes
        self.btn_novo = wx.Button(btnPanel, -1, 'Novo', size=(90, 30))
        self.btn_modificar = wx.Button(btnPanel, -1, 'Modificar', size=(60, 30))
        self.btn_excluir = wx.Button(btnPanel, -1, 'Excluir', size=(60, 30))
        self.btn_usar = wx.Button(btnPanel, -1, 'Usar', size=(60, 30))
        self.btn_ok = wx.Button(painel_principal, -1, 'OK', size=(60, 30))
        self.btn_cancela = wx.Button(painel_principal, -1, 'Cancelar', size=(60, 30))
        self.btn_salvar = wx.Button(painel_principal, -1, 'Salvar', size=(80, 30))
        self.btn_cancela_edicao = wx.Button(painel_principal, -1, 'Cancelar', size=(80, 30))
        
        #Labels de descricao dos componentes
        lbl_material = wx.StaticText(painel_principal, -1, "MATERIAL")
        lbl_nome_material = wx.StaticText(painel_principal, -1, "Nome:")
        lbl_E = wx.StaticText(painel_principal, -1, "         E:  ")
        lbl_G = wx.StaticText(painel_principal, -1, "         G: ")
        
        #ListBox e TextBoxs para entrada de dados
        self.listbox = wx.ListBox(painel_principal, -1, size=((200,140)))
        self.txtNomeMaterial = wx.TextCtrl(painel_principal, -1, size=((155,25)))
        self.txtModElasticidade = wx.TextCtrl(painel_principal, -1, size=((155,25)))
        self.txtModElasticidadeTransversal = wx.TextCtrl(painel_principal, -1, size=((155,25)))
        
        
        VBOX = wx.BoxSizer(wx.VERTICAL) #VBOX Principal
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)#Com listBox e Painel de Botoes
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL) #Label Nome Material e TxtMateria
        hbox3 = wx.BoxSizer(wx.HORIZONTAL) #Label ModElasticidade e TxtModElasticidade
        hbox4 = wx.BoxSizer(wx.HORIZONTAL) #Label ModElasticidadeTrans e TxtModElasticidadeTrans

        hbox2.Add(lbl_nome_material, 0,  wx.ALIGN_RIGHT)
        hbox2.Add(self.txtNomeMaterial, wx.ALIGN_RIGHT)
        
        hbox3.Add(lbl_E,0, wx.ALIGN_RIGHT)
        hbox3.Add(self.txtModElasticidade, wx.ALIGN_RIGHT)
        
        hbox4.Add(lbl_G,0, wx.ALIGN_RIGHT)
        hbox4.Add(self.txtModElasticidadeTransversal, wx.ALIGN_RIGHT)
        
        hbox5 = wx.BoxSizer(wx.HORIZONTAL) #Hbox que contera a vbox1 e a vbox2
        vbox1 = wx.BoxSizer(wx.VERTICAL) #Vbox que contera as Hbox dos modulos elasticidades
        
        
        vbox1.Add(hbox2)
        vbox1.Add(hbox3)
        vbox1.Add(hbox4)
        
        vbox2 = wx.BoxSizer(wx.VERTICAL) #Vbox que contera os botoes Salvar e CancelaEdicao
        
        vbox2.Add(self.btn_salvar, 0, wx.LEFT , 10)
        vbox2.Add(self.btn_cancela_edicao, 0, wx.LEFT | wx.TOP, 10)
        
        hbox5.Add(vbox1, 1, wx.EXPAND | wx.LEFT , 10)
        hbox5.Add(vbox2, 1, wx.EXPAND | wx.LEFT , 10)
        
        hbox6 = wx.BoxSizer(wx.HORIZONTAL) #Hbox que contera os botoes OK e Cancela
        
        hbox6.Add(self.btn_ok, 1, wx.ALL, 10 )
        hbox6.Add(self.btn_cancela, 1, wx.ALL, 10)
        
        for item in self.listaMateriais:
            self.listbox.Append(item[0])
        
        hbox1.Add(self.listbox, 1, wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, 10)

        
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add((-1, 10))
        vbox.Add(self.btn_novo, 0, wx.EXPAND | wx.ALL, 0)
        vbox.Add(self.btn_modificar, 0, wx.EXPAND | wx.ALL, 0)
        vbox.Add(self.btn_excluir, 0, wx.EXPAND | wx.ALL, 0)
        vbox.Add(self.btn_usar, 0, wx.EXPAND | wx.ALL, 0)

        #btnPanel.SetSizer(vbox)
        #hbox1.Add(btnPanel, 0, wx.EXPAND | wx.BOTTOM, 10)
        
        
        VBOX.Add((-1,10))
        VBOX.Add(lbl_material,0, wx.EXPAND | wx.ALL, 10 )
        VBOX.Add(hbox1)
        VBOX.Add(hbox5)
        VBOX.Add(hbox6, 1, wx.EXPAND | wx.ALL, 10 )
        
        
        hbox1.Add(painel_principal, 0, wx.EXPAND | wx.BOTTOM, 10)
        
        
        
        #Verifica se a listaBox nao esta vazia
        if len(self.listbox.GetItems())==0:
            #Desabilita os botoes de Modificar, excluir e usar
            self.btn_modificar.Disable()
            self.btn_excluir.Disable()
            self.btn_usar.Disable()
        else:
            #Caso a listbox nao esteja vazia seleciona o 1 item
            self.listbox.SetSelection(0)
        
        #Desabilita as textbox de exibicao do NomeMateria, ModElasticidae e ModElasticiTransve
        #Dabilita os botoes de salvar e cancelar da parte de edicao do material
        self.txtNomeMaterial.Disable()
        self.txtModElasticidade.Disable()
        self.txtModElasticidadeTransversal.Disable()
        self.btn_salvar.Disable()
        self.btn_cancela_edicao.Disable()
        
        
        self.Bind(wx.EVT_BUTTON, self.NovoMaterial, self.btn_novo)
#        self.Bind(wx.EVT_BUTTON, self.OnRename, -1)
#        self.Bind(wx.EVT_BUTTON, self.OnDelete, -1)
#        self.Bind(wx.EVT_BUTTON, self.OnClear, -1)
        self.Bind(wx.EVT_BUTTON, self.CancelaEdicao, self.btn_cancela_edicao)
        self.Bind(wx.EVT_BUTTON, self.SalvaMaterial, self.btn_salvar)
        self.Bind(wx.EVT_BUTTON, self.ModificarMaterial, self.btn_modificar)
        self.Bind(wx.EVT_BUTTON, self.ExcluirMaterial, self.btn_excluir)
        self.Bind(wx.EVT_BUTTON, self.UsarMaterial, self.btn_usar)
        self.Bind(wx.EVT_BUTTON, self.SalvaAlteracoes, self.btn_ok)
        self.Bind(wx.EVT_BUTTON, self.OnClose, self.btn_cancela)
        
        self.Bind(wx.EVT_LISTBOX, self.SelectListBox)
        
        
    
    def NovoMaterial(self, evt):
        #Desabilita a lisBox e os botoes novo, editar, excluir e usar
        self.listbox.Disable()
        self.btn_novo.Disable()
        self.btn_modificar.Disable()
        self.btn_excluir.Disable()
        self.btn_usar.Disable()
        self.btn_ok.Disable()
        self.btn_cancela.Disable()
        
        #Abilita os botoes de salvar e cancelarModificacao
        self.txtNomeMaterial.Enable()
        self.txtModElasticidade.Enable()
        self.txtModElasticidadeTransversal.Enable()
        self.btn_salvar.Enable()
        self.btn_cancela_edicao.Enable()
        
        #Limpa as textbox
        self.txtNomeMaterial.Clear()
        self.txtModElasticidade.Clear()
        self.txtModElasticidadeTransversal.Clear()
        
    def CancelaEdicao(self, evt):
        #Abilita a lisBox e os botoes novo, editar, excluir e usar
        self.listbox.Enable()
        self.btn_novo.Enable()
        self.btn_modificar.Enable()
        self.btn_excluir.Enable()
        self.btn_usar.Enable()
        self.btn_ok.Enable()
        self.btn_cancela.Enable()
        
        #Desabilita os botoes de salvar e cancelarModificacao
        self.txtNomeMaterial.Disable()
        self.txtModElasticidade.Disable()
        self.txtModElasticidadeTransversal.Disable()
        self.btn_salvar.Disable()
        self.btn_cancela_edicao.Disable()
        
    def SalvaMaterial(self, evt, FLAG="salvar"):
    
        
        #Inclui o material na Listbox de materiais
        n_material = self.txtNomeMaterial.GetValue().rstrip().lstrip() #rstrip remove espacos embranco do final
        E_material = self.txtModElasticidade.GetValue()
        G_material = self.txtModElasticidadeTransversal.GetValue()
        
        try:
            E_material = float(E_material)
            G_material = float(G_material)
        except:
            pass
        
         #Verifica se o nome comeca com letra e os valores de E e G sao numeros
        if n_material[0].isalpha() and isinstance(E_material, float) and (isinstance(G_material, float)):
            if self.VerificaSeMaterialJaExiste(n_material)==False:                
                self.IncluiMatrialNaLista(n_material, E_material, G_material)
            else:
                return
        else:
            alerta = []
            
            #Verifica se o erro ocorreu porque o nome do meterial nao comecao com letra
            if n_material[0].isalpha():
                pass
            else:
                #se nao comeca com letra adiciona alerta do motivo na lista
                alerta.append("Nome do Matrial deve comecar com letra")
                
            #Verifica se o erro ocorreu porque o valor de ModElasticidade E do meterial nao e digito
            if E_material.isdigit():
                pass
            else:
                #se nao comeca com letra adiciona alerta do motivo na lista
                alerta.append("Valor de 'E' deve ser apenas numeros e ponto")
            
            #Verifica se o erro ocorreu porque o valor de ModElastTransversale G do meterial nao e digito
            if G_material.isdigit():
                pass
            else:
                #se nao comeca com letra adiciona alerta do motivo na lista
                alerta.append("Valor de 'G' deve ser apenas numeros e ponto")
                
            for menssagem in alerta:
                print menssagem
            
            return
         
        #Abilita a lisBox e os botoes novo, editar, excluir e usar
        self.listbox.Enable()
        self.btn_novo.Enable()
        self.btn_modificar.Enable()
        self.btn_excluir.Enable()
        self.btn_usar.Enable()
        self.btn_ok.Enable()
        self.btn_cancela.Enable()
        
        #Desabilita os botoes de salvar e cancelarModificacao
        self.txtNomeMaterial.Disable()
        self.txtModElasticidade.Disable()
        self.txtModElasticidadeTransversal.Disable()
        self.btn_salvar.Disable()
        self.btn_cancela_edicao.Disable()
    
        self.AtualizaListBoxMateriais()
        
    def IncluiMatrialNaLista(self, Material, ModElast_E, ModElast_G):
            if self.FLAG == 'salvar':
                self.listaMateriais.append([Material, ModElast_E, ModElast_G])
                self.listbox.Append(Material)
            elif self.FLAG == 'modificar':
                nome_mat = self.listbox.GetString(self.listbox.GetSelection()).split("(")[0].rstrip() #rstrip remove espacos embranco do final
                print "NOMME %s" %nome_mat
                for i in range(len(self.listaMateriais)):
                    if self.listaMateriais[i][0] == nome_mat:
                        indice_da_listaMateriais = i
                
                self.listaMateriais[indice_da_listaMateriais] = [Material, ModElast_E, ModElast_G]
            self.FLAG = 'salvar'
             
    def VerificaSeMaterialJaExiste(self, nome_material):
        if self.FLAG == 'salvar':        
            materiaisexistente = self.listbox.GetItems()
            
            if nome_material in materiaisexistente:
                print "ESTE NOME JA EXISTE, ESCOLHA OUTRO NOME"
                
                wx.MessageBox('ESTE NOME JA EXISTE, ESCOLHA OUTRO NOME', 'Info', wx.OK | wx.ICON_INFORMATION)
                return True
            else:
                print "False"
                return False
        else:
            return False
         
    def SelectListBox(self, evt):
        index = evt.GetSelection()
        nome_mat = self.listbox.GetString(index).split("(")[0].rstrip().lstrip() #rstrip remove espacos embranco do final
        
       # print self.listaMateriais
        
        for i in range(len(self.listaMateriais)):
            if self.listaMateriais[i][0] == nome_mat:
                valores = self.listaMateriais[i]    
        
        try:
            self.txtNomeMaterial.SetValue(valores[0])
            self.txtModElasticidade.SetValue(str(valores[1]))
            self.txtModElasticidadeTransversal.SetValue(str(valores[2]))
        except:
            pass
        
    def ModificarMaterial(self, evt):
        try:
            self.FLAG = "modificar"
            nome_mat = self.listbox.GetString(self.listbox.GetSelection()).split("(")[0].rstrip()
            
            for i in range(len(self.listaMateriais)):
                if self.listaMateriais[i][0] == nome_mat:
                    indice_da_listaMateriais = i
                    
            self.txtNomeMaterial.Enable()
            self.txtModElasticidade.Enable()
            self.txtModElasticidadeTransversal.Enable()
            
            self.btn_salvar.Enable()
            self.btn_cancela_edicao.Enable()
            
            self.listbox.Disable()
            self.btn_novo.Disable()
            self.btn_modificar.Disable()
            self.btn_excluir.Disable()
            self.btn_usar.Disable()
            self.btn_ok.Disable()
            self.btn_cancela.Disable()
            
            self.txtNomeMaterial.SetValue(str(self.listaMateriais[indice_da_listaMateriais][0]))
            self.txtModElasticidade.SetValue(str(self.listaMateriais[indice_da_listaMateriais][1]))
            self.txtModElasticidadeTransversal.SetValue(str(self.listaMateriais[indice_da_listaMateriais][2]))
        except:
            print "Nao ha materiais na lista para serem modificados"
    
            
        
    def VerificaListMateriais(self):
        if len(self.listbox.GetItems())==0:
            self.listbox.Disable()
            self.btn_novo.Enable()
            self.btn_modificar.Disable()
            self.btn_excluir.Disable()
            self.btn_usar.Disable()
            self.btn_ok.Disable()
            self.btn_cancela.Disable()
        
            #Desabilita os botoes de salvar e cancelarModificacao
            self.txtNomeMaterial.Disable()
            self.txtModElasticidade.Disable()
            self.txtModElasticidadeTransversal.Disable()
            self.btn_salvar.Disable()
            self.btn_cancela_edicao.Disable()
            
    def AtualizaListBoxMateriais(self):
        self.listbox.Clear()
        
        for item in self.listaMateriais:
            try:
                if item[0] == self.materialEmUso[0]:                    
                    item = item[0] + "   (Em Uso)"                    
                    self.listbox.Append(item)
                    
                else:
                    self.listbox.Append(item[0])  
            except:                
                self.listbox.Append(item[0])
            
         
        try:
            self.listbox.SetSelection(0)
            
            nome_mat = self.listbox.GetString(self.listbox.GetSelection())
            
            for i in range(len(self.listaMateriais)):
                if self.listaMateriais[i][0] == nome_mat:
                    indice_da_listaMateriais = i
            
            self.txtNomeMaterial.SetValue(str(self.listaMateriais[indice_da_listaMateriais][0]))
            self.txtModElasticidade.SetValue(str(self.listaMateriais[indice_da_listaMateriais][1]))
            self.txtModElasticidadeTransversal.SetValue(str(self.listaMateriais[indice_da_listaMateriais][2]))
        except:
            print "Nao foi possivel selecionar um item na listbox de materiais"
    
            self.txtNomeMaterial.Clear()
            self.txtModElasticidade.Clear()
            self.txtModElasticidadeTransversal.Clear()
            
            
            
    def ExcluirMaterial(self, evt):
        try:
            nome_mat = self.listbox.GetString(self.listbox.GetSelection())
            nome_mat = nome_mat.split("(")[0].rstrip() #rstrip remove espacos embranco do final
            print nome_mat
            print self.listaMateriais
            for i in range(len(self.listaMateriais)):
                if self.listaMateriais[i][0] == nome_mat:
                    indice_da_listaMateriais = i
        
            self.listaMateriais.pop(indice_da_listaMateriais)
            self.AtualizaListBoxMateriais()
            self.VerificaListMateriais()            
        except:
            print "Nao ha materiais na lista para serem excluidos"
            
    def UsarMaterial(self, evt):
        nome_mat = self.listbox.GetString(self.listbox.GetSelection()).split("(")[0].rstrip().lstrip() #rstrip remove espacos embranco do final
        
        for i in range(len(self.listaMateriais)):
            if self.listaMateriais[i][0] == nome_mat:
                indice_da_listaMateriais = i
                    
                    
        self.materialEmUso = self.listaMateriais[indice_da_listaMateriais]
        
        self.AtualizaListBoxMateriais()
        
    def SalvaAlteracoes(self, evt):
        print "Material em uso = %s" %self.materialEmUso
        
        self.OnClose(evt)
        
    def OnClose(self, e):
        print "Dentro" 
        
        print self.parent.Estrututura.LISTA_MATERIAIS
        self.Destroy()       
        
if __name__ == '__main__':
    app = wx.App()
    ChangeDepthDialog([], None, title='TCC_3D')
    app.MainLoop()