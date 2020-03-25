# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:00:27 2017

@author: RONAN TEODORO
"""
import os
import wx
import ezdxf
#from ezdxf.algebra import UCS
from ezdxf.math import UCS
import numpy as np

class DXFExport(object):
    def __init__(self, parent):
        self.parent = parent
        self.rede = parent.Estrututura
        self.dxf = ezdxf.new('R2010')
        self.mdspace = self.dxf.modelspace()
        
        self.CreateDrawing()
        
    def CreateDrawing(self):
        for trecho in self.rede.LISTA_TUBULACOES:
            matrixRotation = trecho.GetMatrixRotation()
            xi, yi, zi = trecho.PV1.pos
            xj, yj, zj = trecho.PV2.pos
            self.mdspace.add_line((xi/100, yi/100, zi/100),
                                                      (xj/100, yj/100, zj/100))
            
            
            anguloTexto = self.GetRealAngleText(trecho)
            posTextoDescricao = trecho.Get_1_4_Position()
            posTextoDiametro = trecho.Get_1_4_Position()
            posTextoComprimento = trecho.Get_3_4_Position()
            posTextoDeclividade = trecho.Get_3_4_Position()
            self.mdspace.add_text(trecho.nomeTrecho, dxfattribs={'rotation': anguloTexto, 'height': 3.0}).set_pos((posTextoDescricao[0], posTextoDescricao[1]), align='BOTTOM_CENTER')
            self.mdspace.add_text(trecho.GetTextoDiamentro("NUM"), dxfattribs={'rotation': anguloTexto, 'height': 3.0}).set_pos((posTextoDiametro[0], posTextoDiametro[1]), align='TOP_CENTER')
            self.mdspace.add_text(trecho.GetTextoComprimento(), dxfattribs={'rotation': anguloTexto, 'height': 3.0}).set_pos((posTextoComprimento[0], posTextoComprimento[1]), align='BOTTOM_CENTER')
            self.mdspace.add_text(trecho.GetTextoDeclividade(), dxfattribs={'rotation': anguloTexto, 'height': 3.0}).set_pos((posTextoDeclividade[0], posTextoDeclividade[1]), align='TOP_CENTER')
            
            
            matriz = [[+5, 0], [-2.5, +2.5], [-2.5, -2.5]]            
            coords = np.dot(matriz, matrixRotation) 
            x,y,z = trecho.GetMiddliPosition()
            ucs = UCS(origin=(x, y, z))
            
            hatch = self.mdspace.add_hatch(color=2)
            with hatch.edit_boundary() as boundary:
                ucs.to_ocs((coords[0,0],coords[0,1]))
                boundary.add_polyline_path([ucs.to_ocs((coords[0,0],coords[0,1])), ucs.to_ocs((coords[1,0],coords[1,1])), ucs.to_ocs((coords[2,0],coords[2,1]))], is_closed=1)
            
            
        for pv in self.rede.LISTA_PVS:
            xi, yi, zi = pv.pos
            self.mdspace.add_circle((xi/100, yi/100, zi/100), 2.5)
            
            self.DesenhaLablsPVs(pv)
            
        self.DrenhaPerfils()
        
        self.dxf.saveas('line.dxf')
    
    def GetRealAngleText(self, trecho):
        anguloTexto = trecho.GetAngleDirection()
        if anguloTexto > 90 and anguloTexto <= 270:
            anguloTexto +=180       
        elif anguloTexto < -90 and anguloTexto > -180:
            anguloTexto +=180       
        
        #print ("Trecho %s = %s" %(trecho.numero, anguloTexto))
        return anguloTexto
    
    def DesenhaLablsPVs(self, PV):
        x,y,z = (PV.pos[0]/100,PV.pos[1]/100,PV.pos[2]/100)
        ucs = UCS(origin=(x, y))       

        anchorX, anchorY, anchorZ = PV.Label.posAnchorPv
        self.mdspace.add_line(ucs.to_ocs((0, 0)),ucs.to_ocs((anchorX/100, anchorY/100)))
        
        labelBlock = self.dxf.blocks.new(name=str(PV.numero))
        labelBlock.add_line((0, 0), (21, 0))
        texto = PV.Label.GetTextLabel()
        y = 0
        x = 0
        for text in texto:
            labelBlock.add_text(text, dxfattribs={'height': 3.0}).set_pos((x, y), align='BOTTOM_LEFT')
            y -= 4.5
        self.mdspace.add_blockref(str(PV.numero), ucs.to_ocs((anchorX/100, anchorY/100)))
        
        
        
#        if (PV.Label.posAnchorPv[0]/100 > -13.5): # Se a posicao da label estiver
#            
#            self.mdspace.add_line(ucs.to_ocs((0.0, 0.0, 0.0)),
#                                  ucs.to_ocs(((PV.Label.posAnchorPv[0]/100)-2.25,
#                                              PV.Label.posAnchorPv[1]/100,
#                                              PV.Label.posAnchorPv[2]/100)))
#            
#        else: # Se a posicao da label estiver antes do meio do PV
#            self.mdspace.add_line(ucs.to_ocs((0.0, 0.0, 0.0)),
#                                  ucs.to_ocs(((PV.Label.posAnchorPv[0]/100)+31.5,
#                                              PV.Label.posAnchorPv[1]/100,
#                                              PV.Label.posAnchorPv[2]/100)))
#        
#        self.mdspace.add_line(ucs.to_ocs(((PV.Label.posAnchorPv[0]/100)-2.25, #da label
#                               PV.Label.posAnchorPv[1]/100,
#                               PV.Label.posAnchorPv[2]/100)),
#                              ucs.to_ocs(((PV.Label.posAnchorPv[0]/100)+31.5,
#                               PV.Label.posAnchorPv[1]/100,
#                               PV.Label.posAnchorPv[2]/100)))
#    
#        ucs = UCS(origin=(0, 0, 0))
        
    def DrenhaPerfils(self):
        for perfil in self.parent.LISTA_PERFIS:
            nomePerfil = "perfil-" + str(perfil.numero)
            perfilBlock = self.dxf.blocks.new(name=nomePerfil)
            escVert = perfil.escalaVertical
            
            x0,y0,z0 = 0, 0, 0
            ucs = UCS(origin=(x0, y0))
            
            #Desenha retangulo do Perfil
            p1 = (ucs.to_ocs((0, 0)))
            p2 = (ucs.to_ocs((perfil.Comprimento, 0)))
            p3 = (ucs.to_ocs((perfil.Comprimento, perfil.AlturaPerfil*escVert)))
            p4 = (ucs.to_ocs((0, perfil.AlturaPerfil*escVert)))
            perfilBlock.add_polyline2d((p1, p2, p3, p4, p1),  dxfattribs={'color': 5})
            
            #Desenha Linhas Verticais do Perfil        
            for i in range(1, int(perfil.Comprimento/perfil.espHorizLinhas)+1):
                perfilBlock.add_line(ucs.to_ocs((perfil.espHorizLinhas*i, 0.0*escVert)),ucs.to_ocs((perfil.espHorizLinhas*i, perfil.AlturaPerfil*escVert)), dxfattribs={'color': 251})
            
            for i in range(1, int(perfil.AlturaPerfil/perfil.espVertLinhas)+1):
                perfilBlock.add_line(ucs.to_ocs((0.0, perfil.espVertLinhas*i*escVert)),ucs.to_ocs((perfil.Comprimento, perfil.espVertLinhas*i*escVert)), dxfattribs={'color': 251})

            #Desenha Titulo do Perfil
            xpos = 0
            ypos = perfil.AlturaPerfil*escVert + perfil.YoffsetTittle
            perfilBlock.add_text(perfil.tittleLabel, dxfattribs={'height': 9.5}).set_pos(ucs.to_ocs((xpos, ypos)), align='BOTTOM_LEFT')
            
        
            #Desenha texto das Cotas Verticais
            i = 0       
            for cota in range(int(perfil.cotaMinima), int(perfil.cotaMaxima), perfil.espVertLinhas):
                x = x0+perfil.XoffsetMajorTickVertical
                y = y0+(i*perfil.espVertLinhas*escVert)
                ucs = UCS(origin=(x, y))
                perfilBlock.add_text(cota, dxfattribs={'height': 7.5, 'color': 5}).set_pos(ucs.to_ocs((0, 0)), align='MIDDLE_RIGHT')
                perfilBlock.add_line(ucs.to_ocs((0, 0)),ucs.to_ocs((-perfil.XoffsetMajorTickVertical, 0)))
                ucs = UCS(origin=(x0, y0))
                i += 1
            
            posx = perfil.posx/100
            for i in range(len(perfil.Trechos)):            
                pv1 = perfil.Trechos[i].PV1
                pv2 = perfil.Trechos[i].PV2
                
                L = perfil.Trechos[i].L
                D = perfil.Trechos[i].D
                
                ucs = UCS(origin=(x0+posx, y0))
                
                if i != (len(perfil.Trechos)-1):
                    
                    #PV 1                    
                    #(ucs.to_ocs((0, 0)),ucs.to_ocs((-perfil.XoffsetMajorTickVertical, 0)))
                    p1 = (ucs.to_ocs((-1, (pv1.CotaTampa-perfil.cotaMinima)*escVert)))
                    p2 = (ucs.to_ocs((+1, (pv1.CotaTampa-perfil.cotaMinima)*escVert)))
                    p3 = (ucs.to_ocs((+1, (pv1.CotaTampa-(pv1.AlturaPv)-perfil.cotaMinima)*escVert)))
                    p4 = (ucs.to_ocs((-1, (pv1.CotaTampa-(pv1.AlturaPv)-perfil.cotaMinima)*escVert)))
                    perfilBlock.add_polyline2d((p1, p2, p3, p4, p1),  dxfattribs={'color': 10})
                    
                    #Desenha Tubulacoes
                    x1 = 0
                    x2 = L
                    y1 = ((perfil.Trechos[i].CGII-perfil.cotaMinima)*escVert)
                    y2 = ((perfil.Trechos[i].CGIF-perfil.cotaMinima)*escVert)

                    p1 = ucs.to_ocs((x1, y1))
                    p2 = ucs.to_ocs((x2, y2))
                    p3 = ucs.to_ocs((x1, y1+D*escVert))
                    p4 = ucs.to_ocs((x2, y2+D*escVert))
                    perfilBlock.add_polyline2d((p1, p2, p4, p3, p1),  dxfattribs={'color': 2})
                    
                    #Desenha Linha do TERRENO            
                    x1 = 0
                    x2 = L
                    y1 = ((pv1.CotaTerreno-perfil.cotaMinima)*escVert)
                    y2 = ((pv2.CotaTerreno-perfil.cotaMinima)*escVert)
                    
                    p1 = ucs.to_ocs((x1, y1))
                    p2 = ucs.to_ocs((x2, y2))
                    perfilBlock.add_line(p1, p2,  dxfattribs={'color': 3})
                
                    posx += L
                    
                else:
                    #PV 1
                    p1 = (ucs.to_ocs((-1, (pv1.CotaTampa-perfil.cotaMinima)*escVert)))
                    p2 = (ucs.to_ocs((+1, (pv1.CotaTampa-perfil.cotaMinima)*escVert)))
                    p3 = (ucs.to_ocs((+1, (pv1.CotaTampa-(pv1.AlturaPv)-perfil.cotaMinima)*escVert)))
                    p4 = (ucs.to_ocs((-1, (pv1.CotaTampa-(pv1.AlturaPv)-perfil.cotaMinima)*escVert)))
                    perfilBlock.add_polyline2d((p1, p2, p3, p4, p1),  dxfattribs={'color': 10})
                    
                    #Desenha Tubulacoes
                    x1 = 0
                    x2 = L
                    y1 = ((perfil.Trechos[i].CGII-perfil.cotaMinima)*escVert)
                    y2 = ((perfil.Trechos[i].CGIF-perfil.cotaMinima)*escVert)

                    p1 = ucs.to_ocs((x1, y1))
                    p2 = ucs.to_ocs((x2, y2))
                    p3 = ucs.to_ocs((x1, y1+D*escVert))
                    p4 = ucs.to_ocs((x2, y2+D*escVert))
                    perfilBlock.add_polyline2d((p1, p2, p4, p3, p1),  dxfattribs={'color': 2})
                    
                    #Desenha Linha do TERRENO            
                    x1 = 0
                    x2 = L
                    y1 = ((pv1.CotaTerreno-perfil.cotaMinima)*escVert)
                    y2 = ((pv2.CotaTerreno-perfil.cotaMinima)*escVert)
                    
                    p1 = ucs.to_ocs((x1, y1))
                    p2 = ucs.to_ocs((x2, y2))
                    perfilBlock.add_line(p1, p2,  dxfattribs={'color': 3})
                    
                    #PV 2
                    posx += L
                    ucs = UCS(origin=(x0+posx, y0))
                    
                    p1 = (ucs.to_ocs((-1, (pv2.CotaTampa-perfil.cotaMinima)*escVert)))
                    p2 = (ucs.to_ocs((+1, (pv2.CotaTampa-perfil.cotaMinima)*escVert)))
                    p3 = (ucs.to_ocs((+1, (pv2.CotaTampa-(pv2.AlturaPv)-perfil.cotaMinima)*escVert)))
                    p4 = (ucs.to_ocs((-1, (pv2.CotaTampa-(pv2.AlturaPv)-perfil.cotaMinima)*escVert)))
                    perfilBlock.add_polyline2d((p1, p2, p3, p4, p1),  dxfattribs={'color': 10})
            
            #ucs = UCS(origin=(x0, y0))
            #Desenha Bands
            _x = x0+0
            _y = y0+0
            for band in perfil.Bands.listBands:
                _y -=band.height
                ucs = UCS(origin=(_x, _y))
                
                ###########################################################
                #Desenha Retangulo dos valores da Band
                p1 = ucs.to_ocs((0, 0))
                p2 = ucs.to_ocs((perfil.Comprimento, 0))
                p3 = ucs.to_ocs((perfil.Comprimento, band.height))
                p4 = ucs.to_ocs((0, band.height))
                perfilBlock.add_polyline2d((p1, p2, p3, p4, p1),  dxfattribs={'color': 251})
                
                anchors = band.GetAnchorPosBands()              
                for num, valor in enumerate(band.GetDadosBand()):
                    perfilBlock.add_text(valor[0], dxfattribs={'height': 5.0, 'color': 5}).set_pos(ucs.to_ocs((anchors[num][0], anchors[num][1])), align='MIDDLE_CENTER')
                ###########################################################
                
                #Desenha retangulo do titulo da band
                p1 = ucs.to_ocs((0, 0))
                p2 = ucs.to_ocs((-band.width_title, 0))
                p3 = ucs.to_ocs((-band.width_title, band.height))
                p4 = ucs.to_ocs((0, band.height))
                perfilBlock.add_polyline2d((p1, p2, p3, p4, p1),  dxfattribs={'color': 251})
                
                perfilBlock.add_text(band.titulo_band[0], dxfattribs={'height': 5.0, 'color': 5}).set_pos(ucs.to_ocs(band.GetAnchorTitleBand()), align='MIDDLE_CENTER')
            
            self.mdspace.add_blockref(nomePerfil, (perfil.pos[0]/100, perfil.pos[1]/100))
