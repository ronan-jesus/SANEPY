# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc
from UI_janelaGerenciaMateriais import UI_janelaGerenciaMateriais
###########################################################################
## Class ChangeDepthDialog
###########################################################################

class ChangeDepthDialog ( UI_janelaGerenciaMateriais ):

    def __init__( self, parent ):
        UI_janelaGerenciaMateriais.__init__ ( self, parent)

        #Bandeira para alterar os modos de salvamento do materia (salvar/modificar)
        self.FLAG = "salvar"
        self.parent = parent
        self.listaMateriais = self.parent.Estrututura.LISTA_MATERIAIS

        self.AtualizaListBoxMateriais()
        self.InicializaJanelaDefineMaterial()


        self.Show()

    def __del__( self ):
        pass

    def InicializaJanelaDefineMaterial(self):
        """INICIALIZA AS INFORMACOES NA JANELA DEFINE MATERIAIS
           ALTERA AS LABELS PARA MOSTRAR AS UNIDADES CORRENTES (m, cm, mm, ...)
        """
        ###REVER ETAPA ABAIXO POIS ESTA COM MUITO CODIGO, TENTAR REDUZIR
        #altera as labels das unidades de medidas
        unidadeComprimento = "m"       
        if self.parent.UnidadeComprimento == "[m] - Metro":
            unidadeComprimento = "m"
        elif self.parent.UnidadeComprimento == "[cm] - Centimetro":
            unidadeComprimento = "cm"
        elif self.parent.UnidadeComprimento == "[mm] - milimetro":
            unidadeComprimento = "mm"
        elif self.parent.UnidadeComprimento == "[ft] - Pes":
            unidadeComprimento = "ft"
        elif self.parent.UnidadeComprimento == "[in] - Polegada":
            unidadeComprimento = "in"        
        
        #altera as labels das unidades de forca
        unidadeForca = "kN"       
        if self.parent.UnidadeForca == "[kN] - Kilo Newton":
            unidadeForca = "kN"
        elif self.parent.UnidadeForca == "[lb] - Libra":
            unidadeForca = "lb"
        elif self.parent.UnidadeForca == "[klb] -Kilo Libra":
            unidadeForca = "klb"
        elif self.parent.UnidadeForca == "[N] - Newton":
            unidadeForca = "N"
        elif self.parent.UnidadeForca == "[kgf] - Kilo Grama Forca":
            unidadeForca = "kgf"
        elif self.parent.UnidadeForca == "[Tonf] - Tonelada Forca":
            unidadeForca = "Tonf"
            
        self.lbl_unid_E.SetLabel(unidadeForca+"/"+unidadeComprimento+u"²")
        self.lbl_unid_G.SetLabel(unidadeForca+"/"+unidadeComprimento+u"²")
        
        
    def NovoMaterial( self, event ):
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
        self.txtCoefPoison.Enable()
        self.txtModElasticidadeTransversal.Enable()
        self.chb_GfuncEv.Enable()
        self.btn_salvar.Enable()
        self.btn_cancela_edicao.Enable()

        #Limpa as textbox
        self.txtNomeMaterial.Clear()
        self.txtModElasticidade.Clear()
        self.txtCoefPoison.Clear()
        self.txtModElasticidadeTransversal.Clear()
        event.Skip()


    def ExcluirMaterial( self, event ):
        try:
            nome_mat = self.listbox.GetString(self.listbox.GetSelection())
            nome_mat = nome_mat.split("(")[0].rstrip() #rstrip remove espacos embranco do final

            for i in range(len(self.listaMateriais)):
                if self.listaMateriais[i][0] == nome_mat:
                    indice_da_listaMateriais = i

            self.listaMateriais.pop(indice_da_listaMateriais)
            self.AtualizaListBoxMateriais()
            self.VerificaListMateriais()
        except:
            print "Nao ha materiais na lista para serem excluidos"

        event.Skip()


    def ModificarMaterial( self, event ):

        try:
            self.FLAG = "modificar"
            nome_mat = self.listbox.GetString(self.listbox.GetSelection()).split("(")[0].rstrip()

            for i in range(len(self.listaMateriais)):
                if self.listaMateriais[i][0] == nome_mat:
                    indice_da_listaMateriais = i

            self.txtNomeMaterial.Enable()
            self.txtModElasticidade.Enable()
            self.txtCoefPoison.Enable()
            self.txtModElasticidadeTransversal.Enable()
            self.chb_GfuncEv.Enable()

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
            self.txtModElasticidade.SetValue(str(self.Convert_E_G(self.listaMateriais[indice_da_listaMateriais][1])))
            self.txtModElasticidadeTransversal.SetValue(str(self.Convert_E_G(self.listaMateriais[indice_da_listaMateriais][2])))
        except:
            print "Nao ha materiais na lista para serem modificados"

        event.Skip()


    def UsarMaterial( self, event ):
        nome_mat = self.listbox.GetString(self.listbox.GetSelection()).split("(")[0].rstrip().lstrip() #rstrip remove espacos embranco do final

        for i in range(len(self.listaMateriais)):
            if self.listaMateriais[i][0] == nome_mat:
                indice_da_listaMateriais = i


        self.parent.materialEmUso = self.listaMateriais[indice_da_listaMateriais]

        self.AtualizaListBoxMateriais()
        self.SelectListBox(event)
        event.Skip()

    def SalvaMaterial( self, event ):
        #Inclui o material na Listbox de materiais
        n_material = self.txtNomeMaterial.GetValue().rstrip().lstrip() #rstrip remove espacos embranco do final
        E_material = self.txtModElasticidade.GetValue()
        v_material = self.txtCoefPoison.GetValue()
        G_material = self.txtModElasticidadeTransversal.GetValue()

        try:
            E_material = self.UN2KN(float(E_material))
            v_material = float(v_material)
            G_material = self.UN2KN(float(G_material))
        except:
            pass

         #Verifica se o nome comeca com letra e os valores de E e G sao numeros
        if n_material[0].isalpha() and isinstance(E_material, float) and (isinstance(G_material, float)) and isinstance(v_material, float):
            if self.VerificaSeMaterialJaExiste(n_material)==False:
                self.IncluiMatrialNaLista(n_material, E_material, v_material, G_material)
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

            #Verifica se o erro ocorreu porque o valor de 'v' do meterial nao e digito
            if v_material.isdigit():
                pass
            else:
                #se nao comeca com letra adiciona alerta do motivo na lista
                alerta.append("Valor de 'v' deve ser apenas numeros e ponto")
                
            #Verifica se o erro ocorreu porque o valor de ModElastTransversale G do meterial nao e digito
            if G_material.isdigit():
                pass
            else:
                #se nao comeca com letra adiciona alerta do motivo na lista
                alerta.append("Valor de 'G' deve ser apenas numeros e ponto")


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
        self.txtCoefPoison.Disable()
        self.txtModElasticidadeTransversal.Disable()
        self.chb_GfuncEv.Disable()
        self.btn_salvar.Disable()
        self.btn_cancela_edicao.Disable()

        self.AtualizaListBoxMateriais()

        event.Skip()


    def IncluiMatrialNaLista(self, Material, ModElast_E, CoefPoison, ModElast_G):
        if self.FLAG == 'salvar':
            self.listaMateriais.append([Material, ModElast_E, CoefPoison, ModElast_G])
            self.listbox.Append(Material)
        elif self.FLAG == 'modificar':
            nome_mat = self.listbox.GetString(self.listbox.GetSelection()).split("(")[0].rstrip() #rstrip remove espacos embranco do final
            for i in range(len(self.listaMateriais)):
                if self.listaMateriais[i][0] == nome_mat:
                    indice_da_listaMateriais = i

            self.listaMateriais[indice_da_listaMateriais] = [Material, ModElast_E, CoefPoison, ModElast_G]
        self.FLAG = 'salvar'



    def VerificaSeMaterialJaExiste(self, nome_material):
        if self.FLAG == 'salvar':
            materiaisexistente = self.listbox.GetItems()

            if nome_material in materiaisexistente:
                wx.MessageBox('ESTE NOME JA EXISTE, ESCOLHA OUTRO NOME', 'Info', wx.OK | wx.ICON_INFORMATION)
                return True
            else:
                return False
        else:
            return False



    def SelectListBox(self, evt):
        index = evt.GetSelection()
        nome_mat = self.listbox.GetString(index).split("(")[0].rstrip().lstrip() #rstrip remove espacos embranco do final

        for i in range(len(self.listaMateriais)):
            if self.listaMateriais[i][0] == nome_mat:
                valores = self.listaMateriais[i]

        try:
            self.txtNomeMaterial.SetValue(valores[0])
            self.txtModElasticidade.SetValue(str(self.Convert_E_G(valores[1])))
            self.txtCoefPoison.SetValue(str(valores[2]))
            self.txtModElasticidadeTransversal.SetValue(str(self.Convert_E_G(valores[3])))
        except:
            pass



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
            self.txtCoefPoison.Disable()
            self.txtModElasticidadeTransversal.Disable()
            self.chb_GfuncEv.Disable()
            self.btn_salvar.Disable()
            self.btn_cancela_edicao.Disable()

    def AtualizaListBoxMateriais(self):
        self.listbox.Clear()

        for item in self.listaMateriais:
            try:
                if item[0] == self.parent.materialEmUso[0]:
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
            self.txtModElasticidade.SetValue(str(self.Convert_E_G(self.listaMateriais[indice_da_listaMateriais][1])))
            self.txtCoefPoison.SetValue(str(self.listaMateriais[indice_da_listaMateriais][2]))
            self.txtModElasticidadeTransversal.SetValue(str(self.Convert_E_G(self.listaMateriais[indice_da_listaMateriais][3])))
        except:
            print "Nao foi possivel selecionar um item na listbox de materiais"

            self.txtNomeMaterial.Clear()
            self.txtModElasticidade.Clear()
            self.txtCoefPoison.Clear()
            self.txtModElasticidadeTransversal.Clear()

    def Convert_E_G(self, valor):
        """
        Retorna o valor do Modulo de Elasticidade Longitudinal E ou G conforme a
        unidade de medida especificada
        """
        fator_forca = 1               
        if self.parent.UnidadeForca == "[kN] - Kilo Newton":
            fator_forca = 1
        elif self.parent.UnidadeForca == "[lb] - Libra":
            fator_forca = 224.8089431
        elif self.parent.UnidadeForca == "[klb] -Kilo Libra":
            fator_forca = 0.2248089431
        elif self.parent.UnidadeForca == "[N] - Newton":
            fator_forca = 1000
        elif self.parent.UnidadeForca == "[kgf] - Kilo Grama Forca":
            fator_forca = 101.9716213
        elif self.parent.UnidadeForca == "[Tonf] - Tonelada Forca":
            fator_forca = 0.1019716213
        
        if  self.parent.UnidadeComprimento == "[m] - Metro":
            return valor*fator_forca            
        elif self.parent.UnidadeComprimento == "[cm] - Centimetro":
            return valor*fator_forca/(100**2)
        elif self.parent.UnidadeComprimento == "[mm] - milimetro":
            return valor*fator_forca/(1000**2)            
        elif self.parent.UnidadeComprimento == "[ft] - Pes":
            return valor*fator_forca*(0.3048**2)            
        elif self.parent.UnidadeComprimento == "[in] - Polegada":
            return valor*fator_forca*(0.0254**2)
    
    def UN2KN(self, valor):
        """
        Retorna o valor do Modulo de Elasticidade Longitudinal E ou G conforme a
        unidade de medida especificada convertida para KN/m2
        """
        fator_forca = 1               
        if self.parent.UnidadeForca == "[kN] - Kilo Newton":
            fator_forca = 1
        elif self.parent.UnidadeForca == "[lb] - Libra":
            fator_forca = 224.8089431
        elif self.parent.UnidadeForca == "[klb] -Kilo Libra":
            fator_forca = 0.2248089431
        elif self.parent.UnidadeForca == "[N] - Newton":
            fator_forca = 1000
        elif self.parent.UnidadeForca == "[kgf] - Kilo Grama Forca":
            fator_forca = 101.9716213
        elif self.parent.UnidadeForca == "[Tonf] - Tonelada Forca":
            fator_forca = 0.1019716213
        
        if  self.parent.UnidadeComprimento == "[m] - Metro":
            return valor/fator_forca            
        elif self.parent.UnidadeComprimento == "[cm] - Centimetro":
            return valor*fator_forca*(100**2)
        elif self.parent.UnidadeComprimento == "[mm] - milimetro":
            return valor*fator_forca*(1000**2)            
        elif self.parent.UnidadeComprimento == "[ft] - Pes":
            return valor*fator_forca/(0.3048**2)            
        elif self.parent.UnidadeComprimento == "[in] - Polegada":
            return valor*fator_forca/(0.0254**2)
            
    def RetirarFoco_TXT_E_or_v(self, event ):
        """Faz o calculo do modulo G por meio da relacao com o modulo E e v
           Antes de fazer o calculo, verifica se a combtext esta ligada
        """
        if self.chb_GfuncEv.GetValue() == True:
            try:
                G = (float(self.txtModElasticidade.GetValue())/
                (2*(1 + float(self.txtCoefPoison.GetValue()))))
                self.txtModElasticidadeTransversal.SetValue(str(G))
            except:
                pass
            
        event.Skip()
  
    def CancelaEdicao( self, event ):
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
        self.txtCoefPoison.Disable()
        self.txtModElasticidadeTransversal.Disable()
        self.chb_GfuncEv.Disable()
        self.btn_salvar.Disable()
        self.btn_cancela_edicao.Disable()
        

        event.Skip()

    def SalvaAlteracoes( self, event ):
        self.OnClose(event)
        event.Skip()

    def OnClose( self, event ):
        self.Destroy()
        event.Skip()



