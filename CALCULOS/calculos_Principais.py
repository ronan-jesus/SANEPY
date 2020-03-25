# -*- coding: utf-8 -*-
from __future__ import division

import sys, os
import math as m
import math
import numpy as np

sys.path.insert(0, "C:\PROGRAMAS PYTHON\SANEPY\Projetos\SANEPY")
    
from AUXILIARES import *
from CALCULOS import *
#from GUI.app import *

#from sympy import Point, Line, Segment
#from sympy.geometry import intersection

from vector3 import *
from AUXILIARES.util import GetAnguloTextosTubos

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from estruturas_PVs import PV_Retangular
from rede_esgoto import TrechoRede

class Tubo(TrechoRede):
    def __init__(self, pvs, nome="Sem Descricao"):
        TrechoRede.__init__(self, pvs, nome)             
        
        self.GetCoordenadas()
        self.visivel = True
    
        self.escala = 20
        self.anguloTextosTubos = 0
        
    def Cria_Matriz_Rotacao(self):
        alpha = np.radians(0)       
        
        self.Cx = ((self.PV2.pos[0]-self.PV1.pos[0])/100)/self.L
        self.Cy = ((self.PV2.pos[1]-self.PV1.pos[1])/100)/self.L
        self.Cz = ((self.PV2.pos[2]-self.PV1.pos[2])/100)/self.L
        Cx = self.Cx
        Cy = self.Cy
        Cz = self.Cz
        #VERIFICA SE A BARRA E VERTICAL
        #SE NAO FOR VERTICAL APLICA A MATRIZ DE ROTACAO NORMAL
        if Cx+Cz!=0:
            Ri = np.array([
                [Cx, Cy, Cz],
                [(-Cx*Cy*m.cos(alpha)-Cz*m.sin(alpha))/(m.sqrt(Cx**2+Cz**2)),  m.sqrt(Cx**2+Cz**2)*m.cos(alpha), (-Cy*Cz*m.cos(alpha)+Cx*m.sin(alpha))/(m.sqrt(Cx**2+Cz**2))],
                [ (Cx*Cy*m.sin(alpha)-Cz*m.cos(alpha))/(m.sqrt(Cx**2+Cz**2)), -m.sqrt(Cx**2+Cz**2)*m.sin(alpha),  (Cy*Cz*m.sin(alpha)+Cx*m.cos(alpha))/(m.sqrt(Cx**2+Cz**2))]
                ])
        #SE FOR VERTICAL, APLICA A MATRIZ DE ROTACAO ALTERADA
        else:
            Cz = Cz+0.0000000000000000000000000000000000000000000000000001
            Ri = np.array([
                [Cx, Cy, Cz],
                [(-Cx*Cy*m.cos(alpha)-Cz*m.sin(alpha))/(m.sqrt(Cx**2+Cz**2)), m.sqrt(Cx**2+Cz**2)*m.cos(alpha), (-Cy*Cz*m.cos(alpha)+Cx*m.sin(alpha))/(m.sqrt(Cx**2+Cz**2))],
                [(Cx*Cy*m.sin(alpha)-Cz*m.cos(alpha))/(m.sqrt(Cx**2+Cz**2)), -m.sqrt(Cx**2+Cz**2)*m.sin(alpha), (Cy*Cz*m.sin(alpha)+Cx*m.cos(alpha))/(m.sqrt(Cx**2+Cz**2))]
                ])
        
        Ri.round(decimals=20, out=None)
        #Cria a Matriz de Rotacao da barra desconexo
        self.R = np.array([
            [Ri[0,0],Ri[0,1],Ri[0,2],0,0,0,0,0,0,0,0,0],
            [Ri[1,0],Ri[1,1],Ri[1,2],0,0,0,0,0,0,0,0,0],
            [Ri[2,0],Ri[2,1],Ri[2,2],0,0,0,0,0,0,0,0,0],

            [0,0,0,Ri[0,0],Ri[0,1],Ri[0,2],0,0,0,0,0,0],
            [0,0,0,Ri[1,0],Ri[1,1],Ri[1,2],0,0,0,0,0,0],
            [0,0,0,Ri[2,0],Ri[2,1],Ri[2,2],0,0,0,0,0,0],

            [0,0,0,0,0,0,Ri[0,0],Ri[0,1],Ri[0,2],0,0,0],
            [0,0,0,0,0,0,Ri[1,0],Ri[1,1],Ri[1,2],0,0,0],
            [0,0,0,0,0,0,Ri[2,0],Ri[2,1],Ri[2,2],0,0,0],

            [0,0,0,0,0,0,0,0,0,Ri[0,0],Ri[0,1],Ri[0,2]],
            [0,0,0,0,0,0,0,0,0,Ri[1,0],Ri[1,1],Ri[1,2]],
            [0,0,0,0,0,0,0,0,0,Ri[2,0],Ri[2,1],Ri[2,2]]
            ])
        self.Ri = Ri
       #Define a Matriz de Rotacao Transposta
        self.RT = np.transpose(self.R)
        
        self.anguloTextosTubos = GetAnguloTextosTubos(Cx, Cy)

    def InverteDirecaoTubo(self):
        """Inverte o sentido da barra, PV1->PV2   e  PV2->PV1
           e cria novamente a matriz de rotacao da barra"""
        self.PV1, self.PV2 = self.PV2, self.PV1        
        self.PVmontante = self.PV1
        self.PVjusante = self.PV2        
        
        self.Cria_Matriz_Rotacao()   
            
    def GetCoordenadas(self):
        self.L = math.sqrt((self.PV2.pos[0]/100-self.PV1.pos[0]/100)**2+(self.PV2.pos[1]/100-self.PV1.pos[1]/100)**2+(self.PV2.pos[2]/100-self.PV1.pos[2]/100)**2)
        try:
                        
            self.Cria_Matriz_Rotacao()
#            tamanho_eixos = 20
#            vec_y = Vector3(0, 1, 0)         
#            vetor_y_global = np.dot(vec_y, self.Ri)
#                       
#            pt1 = Point(-vetor_y_global[0]*tamanho_eixos+self.PV1.pos[0],
#                          -vetor_y_global[1]*tamanho_eixos+self.PV1.pos[1])
#                                 
#            pt2 = Point(-vetor_y_global[0]*tamanho_eixos+self.PV2.pos[0],
#                          -vetor_y_global[1]*tamanho_eixos+self.PV2.pos[1])           
#            
#            pt3 = Point(vetor_y_global[0]*tamanho_eixos+self.PV1.pos[0],
#                          vetor_y_global[1]*tamanho_eixos+self.PV1.pos[1])
#                                 
#            pt4 = Point(vetor_y_global[0]*tamanho_eixos+self.PV2.pos[0],
#                          vetor_y_global[1]*tamanho_eixos+self.PV2.pos[1])           
#     
#            linha_teste = Segment(pt1, pt2)
#            linha_teste2 = Segment(pt3, pt4)
#            
#                  
#            aa = None
#            a = linha_teste.intersection(self.PV1.l1)
#            b = linha_teste.intersection(self.PV1.l2)
#            c = linha_teste.intersection(self.PV1.l3)
#            d = linha_teste.intersection(self.PV1.l4)
#            
#            
#            bb = None
#            e = linha_teste.intersection(self.PV2.l1)
#            f = linha_teste.intersection(self.PV2.l2)
#            g = linha_teste.intersection(self.PV2.l3)
#            h = linha_teste.intersection(self.PV2.l4)
#            
#            
#            if a != []:
#                aa = a
#            elif b != []:
#                aa = b
#            elif c != []:
#                aa = c
#            elif d != []:
#                aa = d
#            else:
#                aa = [pt1]
#            
#           
#            if e != []:
#                bb = e
#            elif f != []:
#                bb = f
#            elif g != []:
#                bb = g
#            elif h != []:
#                bb = h
#            else:
#                bb = [pt2]
#            
#            
#            cc = None
#            i = linha_teste2.intersection(self.PV1.l1)
#            j = linha_teste2.intersection(self.PV1.l2)
#            k = linha_teste2.intersection(self.PV1.l3)
#            l = linha_teste2.intersection(self.PV1.l4)
#            
#            
#            dd = None
#            m = linha_teste2.intersection(self.PV2.l1)
#            n = linha_teste2.intersection(self.PV2.l2)
#            o = linha_teste2.intersection(self.PV2.l3)
#            p = linha_teste2.intersection(self.PV2.l4)
#            
#            if i != []:
#                cc = i
#            elif j != []:
#                cc = j
#            elif k != []:
#                cc = k
#            elif l != []:
#                cc = l
#            else:
#                cc = [pt3]            
#            
#            if m != []:
#                dd = m
#            elif n != []:
#                dd = n
#            elif o != []:
#                dd = o
#            elif p != []:
#                dd = p
#            else:
#                dd = [pt4]
#            
#            
#            self.aa = aa                     
#            self.bb = bb
#            self.cc = cc                     
#            self.dd = dd 
            
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print (e)
        
        
    def Desenha(self):
        escala = self.escala
        try:          
            glPushMatrix()
            glLineWidth(1)
            glBegin(GL_LINES)                        
            glVertex3f(self.PV1.pos[0], self.PV1.pos[1], self.PV1.pos[2])
            glVertex3f(self.PV2.pos[0], self.PV2.pos[1], self.PV2.pos[2])
            #glVertex3f(self.aa[0].x, self.aa[0].y, 0)
            #glVertex3f(self.bb[0].x, self.bb[0].y, 0)
            #glVertex3f(self.cc[0].x, self.cc[0].y, 0)
            #glVertex3f(self.dd[0].x, self.dd[0].y, 0)
            glEnd()
            glPopMatrix()
            
            #Desenha Seta Direcao Escoamento
            tamSeta = [25, 26]
            p1 = np.dot([tamSeta[0]/2, 0.0, 0.0], self.Ri)
            p2 = np.dot([(-tamSeta[0]/2)*escala, (tamSeta[0]/2)*escala, 0.0], self.Ri)
            p3 = np.dot([(-tamSeta[0]/2)*escala, (-tamSeta[0]/2)*escala, 0.0], self.Ri)

            x_medio = (self.PV2.pos[0] - self.PV1.pos[0])/2
            y_medio = (self.PV2.pos[1] - self.PV1.pos[1])/2
            z_medio = (self.PV2.pos[2] - self.PV1.pos[2])/2


            glPushMatrix()
            glTranslatef(self.PV1.pos[0]+x_medio, self.PV1.pos[1]+y_medio, self.PV1.pos[2]+z_medio)

            glColor3f(0.0,0.0,1.0)
            glLineWidth(1)
            glBegin(GL_TRIANGLES)
            glVertex3f(* p1)
            glVertex3f(* p2)
            glVertex3f(* p3)
            glEnd()
            glPopMatrix()
            
            self.DesenhaLabel()
            
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
    
    def DesenhaLabel(self):
        anguloTextos = GetAnguloTextosTubos(self.Cx, self.Cy)
        escala = self.escala        
        escalaText = 2
        
        try:          
            textoLabel = ["i = %sm/m" %(round(self.Iadotada,4))]            
            largura = (self.GetWidth(textoLabel[0]))*escalaText
            
            x_medio = ((self.PV2.pos[0] - self.PV1.pos[0])/2)#-(largura/2)
            y_medio = (self.PV2.pos[1] - self.PV1.pos[1])/2
            z_medio = (self.PV2.pos[2] - self.PV1.pos[2])/2

            glPushMatrix()
            glTranslatef(self.PV1.pos[0]+x_medio, self.PV1.pos[1]+y_medio, self.PV1.pos[2]+z_medio )
            glRotatef(anguloTextos, 0, 0, 1)
            glTranslatef(-(largura/2), 15*escala, 0 )
            for texto in textoLabel:            
                glPushMatrix()
                glScalef(escalaText, escalaText, escalaText )                       
                self.DesenhaStrokText(texto)
                glPopMatrix()
            glPopMatrix()
            
            textoComprimento = ["L = %sm" %round(self.L,2)]
            largura = (self.GetWidth(textoComprimento[0]))*escalaText
            altura = (self.GetHeght())*escalaText
            glPushMatrix()
            glTranslatef(self.PV1.pos[0]+x_medio, self.PV1.pos[1]+y_medio, self.PV1.pos[2]+z_medio )
            glRotatef(anguloTextos, 0, 0, 1)
            glTranslatef(-(largura/2), (-10*escala)-altura, 0 )
            for texto in textoComprimento:            
                glPushMatrix()
                glScalef(escalaText, escalaText, escalaText )                       
                self.DesenhaStrokText(texto)
                glPopMatrix()
            glPopMatrix()
            
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print (e)    
    
    def DesenhaStrokText(self, palavra):
        glPointSize(1)
        glLineWidth(1)
        #glScalef(0.2, 0.2, 0.2)
        for letra in palavra:
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(letra))
        
    def  GetWidth(self, palavra):
        largura = 0
        for letra in palavra:
            largura += glutStrokeWidth(GLUT_STROKE_ROMAN, ord(letra) )
        return largura
    
    def GetHeght(self):
            return glutStrokeHeight(GLUT_STROKE_ROMAN)
        
              
class App(object):
    PV = PV_Retangular
    TRECHO = Tubo
    def __init__(self):
        self.UnidadeComprimento = None
        self.UnidadeForca = None
        self.LISTA_TUBULACOES = []
        self.LISTA_PVS = []
        self.LISTA_COORD_PVS = []
        self.LISTA_MATERIAIS = [[u"CONCRETO C30", 30000000.0, 0.25, 12000000.0]]
        self.LISTA_SECOES = [[u"VIGA 30x60", u"Retangular", 0.6, 0.3, 0.18, 0.003707859375, 0.00135, 0.0054]]
        self.Dic_Lista_Pvs = {} # Dicionario de nos por numero
        self.Dic_Lista_Tubulacoes = {} # Dicionario de Barras por numero
    
        self.ListaRamos = None
    
        
        pv1 = PV_Retangular([83057.0, 31463.9, 0], 29.45, 1.07)
        pv2 = PV_Retangular([75536.9, 33126.8, 0], 28.89, 1.147)
        pv3 = PV_Retangular([77633.5, 41029.1, 0], 26.26, 1.147)
        pv4 = PV_Retangular([83986, 33810.4, 0], 28.95, 1.07)
        pv5 = PV_Retangular([85634.7, 40367.1, 0], 27.62, 1.07)
        pv6 = PV_Retangular([87282.5, 46918.3, 0], 26.29, 1.07)
        pv7 = PV_Retangular([79729.9, 48932.1, 0], 23.63, 1.147)
        pv8 = PV_Retangular([73806, 33437.5, 0], 28.81, 1.07 )
        pv9 = PV_Retangular([68154.9, 34694.4, 0], 28.55, 1.276)
        pv10 = PV_Retangular([70427.1, 42748.6, 0], 25.72, 1.276)
        pv11 = PV_Retangular([72699.4, 50802.8, 0], 22.89, 1.156)
        pv12 = PV_Retangular([52144.2, 38125.1, 0], 29.43, 2.151)
        pv13 = PV_Retangular([66907.7, 34972, 0], 28.66, 1.151)
        pv14 = PV_Retangular([60571.4, 36322.9, 0], 29.22, 2.151)
        pv15 = PV_Retangular([62746.7, 44598.9, 0], 25.525, 1.124)
        pv16 = PV_Retangular([64922.4, 52876.3, 0], 21.83, 1.291)
        pv17 = PV_Retangular([50016.7, 38624.4, 0], 30.28, 1.070)
        pv18 = PV_Retangular([53635.8, 46770.4, 0], 25.725, 1.070)
        pv19 = PV_Retangular([43162, 41278.6, 0], 26.55, 1.070)
        pv20 = PV_Retangular([46687.9, 48957.7, 0], 25.415, 1.070)
        pv21 = PV_Retangular([50214, 56636.8, 0], 24.28, 1.070)
        pv22 = PV_Retangular([57255, 54916.8, 0], 21.17, 1.070)
        pv23 = PV_Retangular([88532.6, 54968.2, 0], 24.26, 1.070)
        pv24 = PV_Retangular([81787.7, 56691.7, 0], 22.86, 1.070)
        pv25 = PV_Retangular([73233, 52435.4, 0], 22.58, 1.070)
        pv26 = PV_Retangular([75042.7, 58415.2, 0], 21.46, 1.070)
        pv27 = PV_Retangular([67863.2, 60386.2, 0], 19.83, 1.077)
        pv28 = PV_Retangular([60679.4, 62343.2, 0], 18.20, 1.077)
        pv29 = PV_Retangular([74197, 68104, 0], 19.83, 1.07)
        pv30 = PV_Retangular([64549.7, 70736.6, 0], 17.63, 1.07)
        pv31 = PV_Retangular([87575.5, 48024.9, 0], 26.03, 1.07)
        pv32 = PV_Retangular([89952.1, 57740, 0], 22.67, 1.07)
        pv33 = PV_Retangular([93496.8, 65709.3, 0], 19.5, 1.076)
        pv34 = PV_Retangular([85784.8, 70508.7, 0], 18.22, 1.076)
        pv35 = PV_Retangular([88029.5, 59798.8, 0], 22.29, 1.07)
        pv36 = PV_Retangular([82122.2, 63618.9, 0], 21.295, 1.07)
        pv37 = PV_Retangular([75249.3, 59453.2, 0], 21.33, 1.07)
        pv38 = PV_Retangular([76215, 67439.1, 0], 20.3, 1.07)
        pv39 = PV_Retangular([78072.8, 75308.1, 0], 16.94, 1.07)
        pv40 = PV_Retangular([68463.3, 79227.8, 0], 15.99, 1.085)
        pv41 = PV_Retangular([62943.6, 81390.7, 0], 18.09, 1.769)
        pv42 = PV_Retangular([59518, 62560.6, 0], 18.56, 1.07)
        pv43 = PV_Retangular([53211.7, 64205.7, 0], 20.57, 3.585)
        pv44 = PV_Retangular([55308.4, 72031.3, 0], 19.33, 2.977)
        pv45 = PV_Retangular([57110.2, 78755.9, 0], 18.09, 3.835)
        pv46 = PV_Retangular([49041.3, 38936.9, 0], 28.86, 1.07)
        pv47 = PV_Retangular([42520.1, 40983.4, 0], 26.4, 1.07)
        pv48 = PV_Retangular([35998.8, 43028.5, 0], 23.94, 1.075)
        pv49 = PV_Retangular([39473.4, 50839.8, 0], 22.64, 1.075)
        pv50 = PV_Retangular([49552.6, 56901.1, 0], 24.00, 1.07)
        pv51 = PV_Retangular([42948, 58651, 0], 21.34, 1.079)
        pv52 = PV_Retangular([52442.8, 64406.3, 0], 20.56, 1.07)
        pv53 = PV_Retangular([45889.7, 66115.8, 0], 20.5, 1.555)
        pv54 = PV_Retangular([47463.8, 72117.6, 0], 16.82, 1.556)
        pv55 = PV_Retangular([49037.9, 78119.4, 0], 13.14, 3.912)
        pv56 = PV_Retangular([44866.6, 66368, 0], 20.33, 1.07)
        pv57 = PV_Retangular([38573.2, 68135, 0], 19.29, 1.07)
        pv58 = PV_Retangular([40137.9, 73956.9, 0], 15.345, 1.07)
        pv59 = PV_Retangular([41686.2, 79784.2, 0], 11.4, 3.953)
        pv60 = PV_Retangular([34346.1, 81446.3, 0], 10.83, 3.953)
#
        self.AdicionaPV(pv1)
        self.AdicionaPV(pv2)
        self.AdicionaPV(pv3)
        self.AdicionaPV(pv4)
        self.AdicionaPV(pv5)
        self.AdicionaPV(pv6)
        self.AdicionaPV(pv7)
        self.AdicionaPV(pv8)
        self.AdicionaPV(pv9)
        self.AdicionaPV(pv10)
        self.AdicionaPV(pv11)
        self.AdicionaPV(pv12)
        self.AdicionaPV(pv13)
        self.AdicionaPV(pv14)
        self.AdicionaPV(pv15)
        self.AdicionaPV(pv16)
        self.AdicionaPV(pv17)
        self.AdicionaPV(pv18)
        self.AdicionaPV(pv19)
        self.AdicionaPV(pv20)
        self.AdicionaPV(pv21)
        self.AdicionaPV(pv22)
        self.AdicionaPV(pv23)
        self.AdicionaPV(pv24)
        self.AdicionaPV(pv25)
        self.AdicionaPV(pv26)
        self.AdicionaPV(pv27)
        self.AdicionaPV(pv28)
        self.AdicionaPV(pv29)
        self.AdicionaPV(pv30)
        self.AdicionaPV(pv31)
        self.AdicionaPV(pv32)
        self.AdicionaPV(pv33)
        self.AdicionaPV(pv34)
        self.AdicionaPV(pv35)
        self.AdicionaPV(pv36)
        self.AdicionaPV(pv37)
        self.AdicionaPV(pv38)
        self.AdicionaPV(pv39)
        self.AdicionaPV(pv40)
        self.AdicionaPV(pv41)
        self.AdicionaPV(pv42)
        self.AdicionaPV(pv43)
        self.AdicionaPV(pv44)
        self.AdicionaPV(pv45)
        self.AdicionaPV(pv46)
        self.AdicionaPV(pv47)
        self.AdicionaPV(pv48)
        self.AdicionaPV(pv49)
        self.AdicionaPV(pv50)
        self.AdicionaPV(pv51)
        self.AdicionaPV(pv52)
        self.AdicionaPV(pv53)
        self.AdicionaPV(pv54)
        self.AdicionaPV(pv55)
        self.AdicionaPV(pv56)
        self.AdicionaPV(pv57)
        self.AdicionaPV(pv58)
        self.AdicionaPV(pv59)
        self.AdicionaPV(pv60)
#        
        self.Dic_Lista_Pvs[pv1.numero] = pv1
        self.Dic_Lista_Pvs[pv2.numero] = pv2
        self.Dic_Lista_Pvs[pv3.numero] = pv3
        self.Dic_Lista_Pvs[pv4.numero] = pv4
        self.Dic_Lista_Pvs[pv5.numero] = pv5
        self.Dic_Lista_Pvs[pv6.numero] = pv6
        self.Dic_Lista_Pvs[pv7.numero] = pv7
        self.Dic_Lista_Pvs[pv8.numero] = pv8
        self.Dic_Lista_Pvs[pv9.numero] = pv9
        self.Dic_Lista_Pvs[pv10.numero] = pv10
        self.Dic_Lista_Pvs[pv11.numero] = pv11
        self.Dic_Lista_Pvs[pv12.numero] = pv12
        self.Dic_Lista_Pvs[pv13.numero] = pv13
        self.Dic_Lista_Pvs[pv14.numero] = pv14
        self.Dic_Lista_Pvs[pv15.numero] = pv15
        self.Dic_Lista_Pvs[pv16.numero] = pv16
        self.Dic_Lista_Pvs[pv17.numero] = pv17
        self.Dic_Lista_Pvs[pv18.numero] = pv18
        self.Dic_Lista_Pvs[pv19.numero] = pv19
        self.Dic_Lista_Pvs[pv20.numero] = pv20
        self.Dic_Lista_Pvs[pv21.numero] = pv21
        self.Dic_Lista_Pvs[pv22.numero] = pv22
        self.Dic_Lista_Pvs[pv23.numero] = pv23
        self.Dic_Lista_Pvs[pv24.numero] = pv24
        self.Dic_Lista_Pvs[pv25.numero] = pv25
        self.Dic_Lista_Pvs[pv26.numero] = pv26
        self.Dic_Lista_Pvs[pv27.numero] = pv27
        self.Dic_Lista_Pvs[pv28.numero] = pv28
        self.Dic_Lista_Pvs[pv29.numero] = pv29
        self.Dic_Lista_Pvs[pv30.numero] = pv30
        self.Dic_Lista_Pvs[pv31.numero] = pv31
        self.Dic_Lista_Pvs[pv32.numero] = pv32
        self.Dic_Lista_Pvs[pv33.numero] = pv33
        self.Dic_Lista_Pvs[pv34.numero] = pv34
        self.Dic_Lista_Pvs[pv35.numero] = pv35
        self.Dic_Lista_Pvs[pv36.numero] = pv36
        self.Dic_Lista_Pvs[pv37.numero] = pv37
        self.Dic_Lista_Pvs[pv38.numero] = pv38
        self.Dic_Lista_Pvs[pv39.numero] = pv39
        self.Dic_Lista_Pvs[pv40.numero] = pv40
        self.Dic_Lista_Pvs[pv41.numero] = pv41
        self.Dic_Lista_Pvs[pv42.numero] = pv42
        self.Dic_Lista_Pvs[pv43.numero] = pv43
        self.Dic_Lista_Pvs[pv44.numero] = pv44
        self.Dic_Lista_Pvs[pv45.numero] = pv45
        self.Dic_Lista_Pvs[pv46.numero] = pv46
        self.Dic_Lista_Pvs[pv47.numero] = pv47
        self.Dic_Lista_Pvs[pv48.numero] = pv48
        self.Dic_Lista_Pvs[pv49.numero] = pv49
        self.Dic_Lista_Pvs[pv50.numero] = pv50
        self.Dic_Lista_Pvs[pv51.numero] = pv51
        self.Dic_Lista_Pvs[pv52.numero] = pv52
        self.Dic_Lista_Pvs[pv53.numero] = pv53
        self.Dic_Lista_Pvs[pv54.numero] = pv54
        self.Dic_Lista_Pvs[pv55.numero] = pv55
        self.Dic_Lista_Pvs[pv56.numero] = pv56
        self.Dic_Lista_Pvs[pv57.numero] = pv57
        self.Dic_Lista_Pvs[pv58.numero] = pv58
        self.Dic_Lista_Pvs[pv59.numero] = pv59
        self.Dic_Lista_Pvs[pv60.numero] = pv60
#         
#         
        trecho1 = Tubo([pv1,pv2], nome="C-1")
        trecho2 = Tubo([pv2,pv3], nome="C-1")
        trecho3 = Tubo([pv3,pv7], nome="C-1")
        trecho4 = Tubo([pv4,pv5], nome="1-1")
        trecho4.TaxaInicial = 0.0009587635423781
        trecho4.TaxaFinal = 0.00228077752333507/2
        trecho5 = Tubo([pv5,pv6], nome="1-1")
        trecho5.TaxaInicial =  0.0009587635423781
        trecho5.TaxaFinal =  0.00228077752333507/2
        trecho6 = Tubo([pv6,pv7], nome="1-1")
        trecho6.SetCGIF(22.56)
        trecho7 = Tubo([pv7,pv11], nome="C-1")
        trecho7.Iadotada = 0.0101718
        trecho8 = Tubo([pv8,pv9], nome="1-2")
        trecho9 = Tubo([pv9,pv10], nome="1-2")
        trecho10 = Tubo([pv10,pv11], nome="1-2")
        trecho11 = Tubo([pv11,pv16], nome="C-1")
        trecho12 = Tubo([pv12,pv14], nome="1-3")
        trecho13 = Tubo([pv13,pv14], nome="1-3-1")
        trecho14 = Tubo([pv14,pv15], nome="1-3")
        trecho15 = Tubo([pv15,pv16], nome="1-3")
        trecho16 = Tubo([pv16,pv22], nome="C-1")
        trecho17 = Tubo([pv17,pv18], nome="1-4")
        trecho18 = Tubo([pv18,pv22], nome="1-4")
        trecho19 = Tubo([pv19,pv20], nome="1-5")
        trecho20 = Tubo([pv20,pv21], nome="1-5")
        trecho21 = Tubo([pv21,pv22], nome="1-5")
        trecho22 = Tubo([pv22,pv28], nome="C-1")
        trecho23 = Tubo([pv23,pv24], nome="1-6")
        trecho24 = Tubo([pv24,pv26], nome="1-6")
        trecho25 = Tubo([pv25,pv26], nome="1-6-1")
        trecho26 = Tubo([pv26,pv27], nome="1-6")
        trecho27 = Tubo([pv27,pv28], nome="1-6")
        trecho28 = Tubo([pv28,pv30], nome="C-1")
        trecho29 = Tubo([pv29,pv30], nome="1-7")
        trecho30 = Tubo([pv30,pv40], nome="C-1")
        trecho31 = Tubo([pv31,pv32], nome="1-8")
        trecho32 = Tubo([pv32,pv33], nome="1-8")
        trecho33 = Tubo([pv33,pv34], nome="1-8")
        trecho34 = Tubo([pv34,pv39], nome="1-8")
        trecho35 = Tubo([pv35,pv36], nome="1-8-1")
        trecho36 = Tubo([pv36,pv38], nome="1-8-1")
        trecho37 = Tubo([pv37,pv38], nome="1-8-1-1")
        trecho38 = Tubo([pv38,pv39], nome="1-8-1")
        trecho39 = Tubo([pv39,pv40], nome="1-8")
        trecho40 = Tubo([pv40,pv41], nome="C-1")
        trecho41 = Tubo([pv41,pv45], nome="C-1")
        trecho42 = Tubo([pv42,pv43], nome="1-9")
        trecho43 = Tubo([pv43,pv44], nome="1-9")
        trecho44 = Tubo([pv44,pv45], nome="1-9")
        trecho45 = Tubo([pv45,pv55], nome="C-1")
        trecho46 = Tubo([pv46,pv47], nome="1-10")
        trecho47 = Tubo([pv47,pv48], nome="1-10")
        trecho48 = Tubo([pv48,pv49], nome="1-10")
        trecho49 = Tubo([pv49,pv51], nome="1-10")
        trecho50 = Tubo([pv50,pv51], nome="1-10-1")
        trecho51 = Tubo([pv51,pv53], nome="C-1")
        trecho52 = Tubo([pv52,pv53], nome="1-10-2")
        trecho53 = Tubo([pv53,pv54], nome="1-10")
        trecho54 = Tubo([pv54,pv55], nome="1-10")
        trecho55 = Tubo([pv55,pv59], nome="C-1")
        trecho56 = Tubo([pv56,pv57], nome="1-11")
        trecho57 = Tubo([pv57,pv58], nome="1-11")
        trecho58 = Tubo([pv58,pv59], nome="1-11")
        trecho59 = Tubo([pv59,pv60], nome="C-1")
       
        
#        
        self.AdicionaTubo(trecho1)
        self.AdicionaTubo(trecho2)
        self.AdicionaTubo(trecho3)
        self.AdicionaTubo(trecho4)
        self.AdicionaTubo(trecho5)
        self.AdicionaTubo(trecho6)
        self.AdicionaTubo(trecho7)
        self.AdicionaTubo(trecho8)
        self.AdicionaTubo(trecho9)
        self.AdicionaTubo(trecho10)
        self.AdicionaTubo(trecho11)
        self.AdicionaTubo(trecho12)
        self.AdicionaTubo(trecho13)
        self.AdicionaTubo(trecho14)
        self.AdicionaTubo(trecho15)
        self.AdicionaTubo(trecho16)
        self.AdicionaTubo(trecho17)
        self.AdicionaTubo(trecho18)
        self.AdicionaTubo(trecho19)
        self.AdicionaTubo(trecho20)
        self.AdicionaTubo(trecho21)
        self.AdicionaTubo(trecho22)
        self.AdicionaTubo(trecho23)
        self.AdicionaTubo(trecho24)
        self.AdicionaTubo(trecho25)
        self.AdicionaTubo(trecho26)
        self.AdicionaTubo(trecho27)
        self.AdicionaTubo(trecho28)
        self.AdicionaTubo(trecho29)
        self.AdicionaTubo(trecho30)
        self.AdicionaTubo(trecho31)
        self.AdicionaTubo(trecho32)
        self.AdicionaTubo(trecho33)
        self.AdicionaTubo(trecho34)
        self.AdicionaTubo(trecho35)
        self.AdicionaTubo(trecho36)
        self.AdicionaTubo(trecho37)
        self.AdicionaTubo(trecho38)
        self.AdicionaTubo(trecho39)
        self.AdicionaTubo(trecho40)
        self.AdicionaTubo(trecho41)
        self.AdicionaTubo(trecho42)
        self.AdicionaTubo(trecho43)
        self.AdicionaTubo(trecho44)
        self.AdicionaTubo(trecho45)
        self.AdicionaTubo(trecho46)
        self.AdicionaTubo(trecho47)
        self.AdicionaTubo(trecho48)
        self.AdicionaTubo(trecho49)
        self.AdicionaTubo(trecho50)
        self.AdicionaTubo(trecho51)
        self.AdicionaTubo(trecho52)
        self.AdicionaTubo(trecho53)
        self.AdicionaTubo(trecho54)
        self.AdicionaTubo(trecho55)
        self.AdicionaTubo(trecho56)
        self.AdicionaTubo(trecho57)
        self.AdicionaTubo(trecho58)
        self.AdicionaTubo(trecho59)
#        
        self.Dic_Lista_Tubulacoes[trecho1.numero] = trecho1
        self.Dic_Lista_Tubulacoes[trecho2.numero] = trecho2
        self.Dic_Lista_Tubulacoes[trecho3.numero] = trecho3
        self.Dic_Lista_Tubulacoes[trecho4.numero] = trecho4
        self.Dic_Lista_Tubulacoes[trecho5.numero] = trecho5
        self.Dic_Lista_Tubulacoes[trecho6.numero] = trecho6
        self.Dic_Lista_Tubulacoes[trecho7.numero] = trecho7
        self.Dic_Lista_Tubulacoes[trecho8.numero] = trecho8
        self.Dic_Lista_Tubulacoes[trecho9.numero] = trecho9
        self.Dic_Lista_Tubulacoes[trecho10.numero] = trecho10
        self.Dic_Lista_Tubulacoes[trecho11.numero] = trecho11
        self.Dic_Lista_Tubulacoes[trecho12.numero] = trecho12
        self.Dic_Lista_Tubulacoes[trecho13.numero] = trecho13
        self.Dic_Lista_Tubulacoes[trecho14.numero] = trecho14
        self.Dic_Lista_Tubulacoes[trecho15.numero] = trecho15
        self.Dic_Lista_Tubulacoes[trecho16.numero] = trecho16
        self.Dic_Lista_Tubulacoes[trecho17.numero] = trecho17
        self.Dic_Lista_Tubulacoes[trecho18.numero] = trecho18
        self.Dic_Lista_Tubulacoes[trecho19.numero] = trecho19
        self.Dic_Lista_Tubulacoes[trecho20.numero] = trecho20
        self.Dic_Lista_Tubulacoes[trecho21.numero] = trecho21
        self.Dic_Lista_Tubulacoes[trecho22.numero] = trecho22
        self.Dic_Lista_Tubulacoes[trecho23.numero] = trecho23
        self.Dic_Lista_Tubulacoes[trecho24.numero] = trecho24
        self.Dic_Lista_Tubulacoes[trecho25.numero] = trecho25
        self.Dic_Lista_Tubulacoes[trecho26.numero] = trecho26
        self.Dic_Lista_Tubulacoes[trecho27.numero] = trecho27
        self.Dic_Lista_Tubulacoes[trecho28.numero] = trecho28
        self.Dic_Lista_Tubulacoes[trecho29.numero] = trecho29
        self.Dic_Lista_Tubulacoes[trecho30.numero] = trecho30
        self.Dic_Lista_Tubulacoes[trecho31.numero] = trecho31
        self.Dic_Lista_Tubulacoes[trecho32.numero] = trecho32
        self.Dic_Lista_Tubulacoes[trecho33.numero] = trecho33
        self.Dic_Lista_Tubulacoes[trecho34.numero] = trecho34
        self.Dic_Lista_Tubulacoes[trecho35.numero] = trecho35
        self.Dic_Lista_Tubulacoes[trecho36.numero] = trecho36
        self.Dic_Lista_Tubulacoes[trecho37.numero] = trecho37
        self.Dic_Lista_Tubulacoes[trecho38.numero] = trecho38
        self.Dic_Lista_Tubulacoes[trecho39.numero] = trecho39
        self.Dic_Lista_Tubulacoes[trecho40.numero] = trecho40
        self.Dic_Lista_Tubulacoes[trecho41.numero] = trecho41
        self.Dic_Lista_Tubulacoes[trecho42.numero] = trecho42
        self.Dic_Lista_Tubulacoes[trecho43.numero] = trecho43
        self.Dic_Lista_Tubulacoes[trecho44.numero] = trecho44
        self.Dic_Lista_Tubulacoes[trecho45.numero] = trecho45
        self.Dic_Lista_Tubulacoes[trecho46.numero] = trecho46
        self.Dic_Lista_Tubulacoes[trecho47.numero] = trecho47
        self.Dic_Lista_Tubulacoes[trecho48.numero] = trecho48
        self.Dic_Lista_Tubulacoes[trecho49.numero] = trecho49
        self.Dic_Lista_Tubulacoes[trecho50.numero] = trecho50
        self.Dic_Lista_Tubulacoes[trecho51.numero] = trecho51
        self.Dic_Lista_Tubulacoes[trecho52.numero] = trecho52
        self.Dic_Lista_Tubulacoes[trecho53.numero] = trecho53
        self.Dic_Lista_Tubulacoes[trecho54.numero] = trecho54
        self.Dic_Lista_Tubulacoes[trecho55.numero] = trecho55
        self.Dic_Lista_Tubulacoes[trecho56.numero] = trecho56
        self.Dic_Lista_Tubulacoes[trecho57.numero] = trecho57
        self.Dic_Lista_Tubulacoes[trecho58.numero] = trecho58
        self.Dic_Lista_Tubulacoes[trecho59.numero] = trecho59    
            
    def AdicionaPV(self, pv, arquivo=None):
        num_aux = pv.numero

        FLAG = self.VerificaDistancias(pv)
        
        
        if arquivo !=None:            
            pv.numero = len(self.LISTA_PVS)+1            
            self.LISTA_PVS.append(pv)                
                
        elif FLAG == True:
            # Verifica se a lista de NOS esta fazia
            # Se estiver vazia, e o primeiro no, tera numero 1
            if len(self.LISTA_PVS) == 0:
                pv.numero = 1
                self.LISTA_PVS.append(pv)
            #Caso a lista nao esteje vazia, procura o NO de numero maior
            # e acrescenta uma unidade ao numero e coloca o no dentro da
            # da lista de NOS
            elif len(self.LISTA_PVS) != 0:
                num_aux = 0
                for pv_aux in self.LISTA_PVS:
                    num_pv = pv_aux.numero

                    if num_pv > num_aux:
                        num_aux = num_pv

                num_aux += 1
                pv.numero = num_aux
                self.LISTA_PVS.append(pv)

        else:
            pass

    def VerificaDistancias(self, pv):
        # Se a lista de nos estiver vazia retorna true para adicionar o primeiro no
        if len(self.LISTA_PVS) == 0:
            return True

        x = pv.pos[0]
        y = pv.pos[1]
        z = pv.pos[2]

        i = 0
        for ponto in self.LISTA_PVS:
            xi = ponto.pos[0]
            yi = ponto.pos[1]
            zi = ponto.pos[2]
            xf = x
            yf = y
            zf = z

            dist = m.sqrt((xi-xf)**2 + (yi-yf)**2 + (zi-zf)**2)

            # Se for menor que 0.1 m, nao vai inserir o NO
            if dist < 0.05:
                return False

            # Se a distancia do ultimo PV for MAIOR que 0.1 m, inserir o PV
            elif (dist > 0.05 and i == len(self.LISTA_PVS)-1):
                return True
            i += 1

    def VerificaSeTubulacaoJaExiste(self, tubo):
        for t in self.LISTA_TUBULACOES:
            if (t.PV1 == tubo.PV1 and t.PV2 == tubo.PV2) or (t.PV1 == tubo.PV2 and t.PV2 == tubo.PV1):
                return True
            else:
                pass
        return False
        
    def AdicionaTubo(self, tubo):
        # Verifica se a lista de tubos esta fazia
        # Se estiver vazia, o primeiro tubo, tera numero 1
        if len(self.LISTA_TUBULACOES) == 0:
            num_aux = 1
            tubo.numero = num_aux
            self.LISTA_TUBULACOES.append(tubo)
        #Caso a lista nao esteje vazia, procura o TUBO de numero maior
        # e acrescenta uma unidade ao numero e coloca o tubo dentro da
        # da lista de TUBULACOES
        elif (len(self.LISTA_TUBULACOES) != 0 and self.VerificaSeTubulacaoJaExiste(tubo)==False):
            num_aux = 0
            for tubo_aux in self.LISTA_TUBULACOES:
                num_tubo = tubo_aux.numero
                if num_tubo > num_aux:
                    num_aux = num_tubo
            num_aux += 1
            tubo.numero = num_aux

            self.LISTA_TUBULACOES.append(tubo)

    def ExcluirPv(self, Pvs):
        lista_pvs_tubulacoes = []

        for tubo in self.LISTA_TUBULACOES:
            pv1 = tubo.PV1.numero
            pv2 = tubo.PV2.numero

            lista_pvs_tubulacoes.append(pv1)
            lista_pvs_tubulacoes.append(pv2)

        for pv in Pvs:
            if pv.numero in lista_pvs_tubulacoes:
                #NAO EXCLUI O NO POIS ELE FAZ PARTE DE ALGUMA BARRA
                pass
            else:
                #EXCLUI O NO POIS ELE NAO FAZ PARTE DE NENHUMA BARRA
                self.LISTA_PVS.remove(pv)

        self.ReorganizaPvsProjeto()


    def ExcluirTubo(self, tubo):
        """Retira da Lista de Tubulacoes os tubos da lista passada como
           prametro da funcao.
           
           Os elementos da lista deve ser as referencias das instancias de
           cada tubo, nao os numeros.
        """
        #Remove barra da lista de barras da estrutura
        for tub in tubo:            
            self.Dic_Lista_Tubulacoes.pop(tub.numero)
            self.LISTA_TUBULACOES.remove(tub)           
            
        self.ReorganizaTubosProjeto()
        

    def ReorganizaPvsProjeto(self):
        for i in range(0,len(self.LISTA_PVS)):
            self.LISTA_PVS[i].numero = i+1

        #Reorganiza o Dicionario de Nos
        self.Dic_Lista_Pvs = {}
        for pv in self.LISTA_PVS:
            self.Dic_Lista_Pvs[pv.numero] = pv
            
    def ReorganizaTubosProjeto(self):
        for i in range(0,len(self.LISTA_TUBULACOES)):
            self.LISTA_TUBULACOES[i].numero = i+1

        #Reorganiza o Dicionario de Barras
        self.Dic_Lista_Tubulacoes = {}
        for tubo in self.LISTA_TUBULACOES:
            self.Dic_Lista_Tubulacoes[tubo.numero] = tubo    

    def VerificaMovimentoPv(self, numPv):
        for tubo in self.LISTA_TUBULACOES:
            numPv1 = tubo.PV1.numero
            numPv2 = tubo.PV2.numero
            
            if numPv in [numPv1, numPv2]:
                try:
                    #tubo.PV1.CalculaArestas()
                    #tubo.PV2.CalculaArestas()
                    tubo.GetCoordenadas()
                except Exception as e:                   
                    print (e)
                    
    def VerificaRamificacoes(self, trecho, pv_jusante, listaTrechos):
            nPV1 = trecho.PV1.numero       
            
            if nPV1 == pv_jusante:
                return listaTrechos
                #pv_montante = trecho.PV2
            else:
                pv_montante = trecho.PV1
             
            
            #print ("%s - %s" %(pv_jusante,pv_montante.numero))
            listaTrechos = listaTrechos+[trecho.numero]
            
            if len(self.ListaRamos[pv_montante.numero]) == 1:
                return listaTrechos
            
            elif len(self.ListaRamos[pv_montante.numero]) == 2:            
                if self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][0]] == trecho:
                    return self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][1]],pv_montante.numero, listaTrechos)
                else:
                    return self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][0]],pv_montante.numero, listaTrechos)
            
            elif len(self.ListaRamos[pv_montante.numero]) == 3:
                if self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][0]] == trecho:
                    return self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][1]],pv_montante.numero, listaTrechos)+self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][2]],pv_montante.numero, listaTrechos)
                elif self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][1]] == trecho:
                    return self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][0]],pv_montante.numero, listaTrechos)+self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][2]],pv_montante.numero, listaTrechos)
                elif self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][2]] == trecho:
                    return self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][0]],pv_montante.numero, listaTrechos)+self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][1]],pv_montante.numero, listaTrechos)
            
            elif len(self.ListaRamos[pv_montante.numero]) == 4:
                if self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][0]] == trecho:
                    return self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][1]],pv_montante.numero, listaTrechos)+self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][2]],pv_montante.numero, listaTrechos)+self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][3]],pv_montante.numero, listaTrechos)
                elif self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][1]] == trecho:
                    return self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][0]],pv_montante.numero, listaTrechos)+self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][2]],pv_montante.numero, listaTrechos)+self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][3]],pv_montante.numero, listaTrechos)
                elif self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][2]] == trecho:
                    return self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][0]],pv_montante.numero, listaTrechos)+self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][1]],pv_montante.numero, listaTrechos)+self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][3]],pv_montante.numero, listaTrechos)
                elif self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][3]] == trecho:
                    return self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][0]],pv_montante.numero, listaTrechos)+self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][1]],pv_montante.numero, listaTrechos)+self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[self.ListaRamos[pv_montante.numero][2]],pv_montante.numero, listaTrechos)
                    
    
    def CriaListaDeLigacoes(self):
        """Cria a lista de ligacoes de cada PV trechos que entram e que saem"""
        listaLigacoes = {}
        for pv in self.LISTA_PVS:
            listaLigacoes[pv.numero] = []
        
        for trecho in self.LISTA_TUBULACOES:
            listaLigacoes[trecho.PV1.numero].append(trecho.numero)
            listaLigacoes[trecho.PV2.numero].append(trecho.numero)            
        
        self.ListaRamos = listaLigacoes
            
    def VerificaSaidasPVs(self):
        """Verifica se todos os PVs tem apenas um trecho de saida, ou seja
           se todos os PVs sao apenas pvs de montante de apenas um trecho,
           caso tenha mais de um trecho que tenha o mesmo PV como sendo pv
           de montante, indica que o PV tem mais de uma tubulacao de saida
           o que nao pode ocorrer.
           
           Verifica todos os PVs, se encontrar mais de um trecho saindo do
           mesmo PV, retorna uma lista de listas tendo o numero do PV e
           dentro da lista os trechos que saem do PV.
           
           return [[numPV, [Trecho1, Trecho2]]] --> [[3,[2, 3]]]
        """
        lista_trechosDeSaida = {}
        for pv in self.LISTA_PVS:
            for trecho in self.LISTA_TUBULACOES:
                if pv == trecho.PVmontante:
                    if pv.numero not in lista_trechosDeSaida:
                        lista_trechosDeSaida[pv.numero] = [trecho.numero]
                    else:
                        lista_trechosDeSaida[pv.numero].append(trecho.numero)
                    
        
        pvs_Verificar = [] #lista dos PVs com inconsistencias
        
        for pv in lista_trechosDeSaida:
            if len(lista_trechosDeSaida[pv]) > 1:
                pvs_Verificar.append([pv, lista_trechosDeSaida[pv]])
        
        return []
    
    def VerificaPvsInicioRede(self):
        """Verifica quais PVs sao pvs de inicio de rede. Faz a verificacao
           dos PVs que sao apenas pvs de Montante e nao sao pvs de Jusante,
           ou seja, caso um PV seja pv de montante de um trecho e o mesmo
           nao seja tambem pv de Jusante em qualquer outro trecho, este sera
           um PV de inicio de rede, retornando uma lista com os numeros dos
           PVs que sao de inicio de rede.
           
           return [int->numPv1, int->numPv2, ..., int->numPvn]
        """
        listaPvsMontante = []
        listaPvsJusante = []
        for trecho in self.LISTA_TUBULACOES:
            listaPvsMontante.append(trecho.PVmontante.numero)
            listaPvsJusante.append(trecho.PVjusante.numero)        
        
        return [x for x in set(listaPvsJusante) if x not in set(listaPvsMontante)]
    
    def VerificaPvsFinalRede(self):
        """Verifica quais PVs sao pvs de final de rede. Faz a verificacao
           dos PVs que sao apenas pvs de Jusante e nao sao pvs de Montante,
           ou seja, caso um PV seja pv de jusante de um trecho e o mesmo
           nao seja tambem pv de montante em qualquer outro trecho, este sera
           um PV de final de rede, retornando uma lista com os numeros dos
           PVs que sao de final de rede.
           
           return [int->numPv1, int->numPv2, ..., int->numPvn]
        """
        listaPvsMontante = []
        listaPvsJusante = []
        for trecho in self.LISTA_TUBULACOES:
            listaPvsMontante.append(trecho.PVmontante.numero)
            listaPvsJusante.append(trecho.PVjusante.numero)
        
        return [x for x in set(listaPvsJusante) if x not in set(listaPvsMontante)]
   
    def RetornaSaidasPvs(self):
        """Retorna dicionario, sendo as chaves os numeros dos PVs os valores
           e- o numero do trecho que sai do PV. 
        """
        lista_trechosDeSaida = {}
        for pv in self.LISTA_PVS:
            for trecho in self.LISTA_TUBULACOES:
                if pv == trecho.PVmontante:
                    if pv.numero not in lista_trechosDeSaida:
                        lista_trechosDeSaida[pv.numero] = [trecho.numero]
                    else:
                        lista_trechosDeSaida[pv.numero].append(trecho.numero)                   
        
        return lista_trechosDeSaida
        
    def VerificaCaminho(self, pv, saidasPvs = None, pvsChegada = None, caminho=[], flag = True):
        """Retorna o caminho do PV informado ate o PV de final de trecho mais
           proximo. Retorna lista com os objetos tipo Tubo em ordem do caminho
           do PV de informado ate o PV de fim.
           
           return [Obj->Tubo1, Obj->Tubo2, ..., Obj->TuboN]
           
           Rede.RetornaSaidasPvs(), Rede.
        """
        if flag == True:
            caminho = []
            flag = False
            
        if saidasPvs == None:
            saidasPvs = self.RetornaSaidasPvs()
        else:
            pass
        
        if pvsChegada == None:
            pvsChegada = self.VerificaPvsFinalRede()
        else:
            pass        
        
        if pv in pvsChegada:
            return caminho
        else:
            caminho.append(self.Dic_Lista_Tubulacoes[saidasPvs[pv][0]])
            jusante = self.Dic_Lista_Tubulacoes[saidasPvs[pv][0]].PVjusante.numero
            return self.VerificaCaminho(jusante, saidasPvs, pvsChegada, caminho, flag=flag)
        
    def CalculaContribuicoesPV(self, pv):
        """Verifica quais trechos contribuem com vazoes para o pv indicado
        """
        _a = [] #lista de trechos que contribuem com vazao para o pv indicado
        for trecho in self.ListaRamos[pv]: #ListaRamos deve ter sido calculada
            if pv == self.Dic_Lista_Tubulacoes[trecho].PVjusante.numero:
                _a += set(self.VerificaRamificacoes(self.Dic_Lista_Tubulacoes[trecho], pv, []))                
            else:
                pass        
        return _a
    
    def CalculaVazoesEntradas(self):        
        self.CriaListaDeLigacoes()
        for trecho in self.LISTA_TUBULACOES:
            PVMontante = trecho.PVmontante.numero
            trechosContribuem = self.CalculaContribuicoesPV(PVMontante)
            vazaoEntradaInicio = [] #lista com as vazoes de entrada cada trecho Inicio
            vazaoEntradaFinal = [] #lista com as vazoes de entrada cada trecho Final
            for t in trechosContribuem:
                vazaoEntradaInicio.append(self.Dic_Lista_Tubulacoes[t].ContribTotalInicio)
                vazaoEntradaFinal.append(self.Dic_Lista_Tubulacoes[t].ContribTotalFinal)
            trecho.QentradaInicial = sum(vazaoEntradaInicio)            
            trecho.QentradaFinal = sum(vazaoEntradaFinal)            
    
    def CalculaVazaoEntrada(self, trecho):        
        self.CriaListaDeLigacoes()        
        PVMontante = trecho.PVmontante.numero
        trechosContribuem = self.CalculaContribuicoesPV(PVMontante)
        vazaoEntradaInicio = [] #lista com as vazoes de entrada cada trecho Inicio
        vazaoEntradaFinal = [] #lista com as vazoes de entrada cada trecho Final
        for t in trechosContribuem:
            vazaoEntradaInicio.append(self.Dic_Lista_Tubulacoes[t].ContribTotalInicio)
            vazaoEntradaFinal.append(self.Dic_Lista_Tubulacoes[t].ContribTotalFinal)
        trecho.QentradaInicial = sum(vazaoEntradaInicio)            
        trecho.QentradaFinal = sum(vazaoEntradaFinal)            
    
    
    def CalculaRemansoTrechos(self):
        self.CriaListaDeLigacoes()
        for trecho in self.LISTA_TUBULACOES:
            PVMontante = trecho.PVmontante.numero
            trechosContribuem = self.CalculaContribuicoesPV(PVMontante)
            
            cotasLaminaMontante = [] #lista com as cotas das laminas na entrada cada trecho Montante
            cotasLaminaJusante = [] #lista com as cotas das laminas na entrada cada trecho Jusante
            for t in trechosContribuem:
                cotasLaminaMontante.append(self.Dic_Lista_Tubulacoes[t].CotaLaminaMontante)
                cotasLaminaJusante.append(self.Dic_Lista_Tubulacoes[t].CotaLaminaJusante)
                
            if len(cotasLaminaJusante) !=0:
                trecho.cotaMinLaminaJusante = min(cotasLaminaJusante)   
            else:
                trecho.cotaMinLaminaJusante = trecho.CotaLaminaJusante+trecho.Desnivel
    
    def CalculaRemansoTrecho(self, trecho):        
        PVMontante = trecho.PVmontante.numero
        trechosContribuem = self.CalculaContribuicoesPV(PVMontante)        
        cotasLaminaMontante = [] #lista com as cotas das laminas na entrada cada trecho Montante
        cotasLaminaJusante = [] #lista com as cotas das laminas na entrada cada trecho Jusante
        for t in trechosContribuem:
            cotasLaminaMontante.append(self.Dic_Lista_Tubulacoes[t].CotaLaminaMontante)
            cotasLaminaJusante.append(self.Dic_Lista_Tubulacoes[t].CotaLaminaJusante)
            
        if len(cotasLaminaJusante) !=0:
            trecho.cotaMinLaminaJusante = min(cotasLaminaJusante)   
        else:
            trecho.cotaMinLaminaJusante = trecho.CotaLaminaJusante+trecho.Desnivel
    
    def CalculaDistanciaPVs(self, pvMontante, PvJusante):
        """Retorna o comprimento total dos trechos entre dois PVs (Montante- Jusante)
        """
        
        trechos =  self.VerificaCaminho(pvMontante, pvsChegada = [PvJusante])
        comprimentos = []
        for trecho in trechos:
            comprimentos.append(trecho.L)
        
        return sum(comprimentos)
        
    def CalculaRedePrincipal(self):
        """ Retorna uma lista com os trechos que compoem o trecho principal,
            a verificação e realizada verificando qual o pv e- o PV de final
            de rede, e verificando qual o pv mais distante dele.
            
            a lista contem os objetos do tipo tubo de montante para jusante
        """
        
        PVsFinal = self.VerificaPvsFinalRede()[0]       
        
        distancias = {}
        
        for pv in self.LISTA_PVS:
            if pv.numero == PVsFinal:
                pass
            else:
                dist = self.CalculaDistanciaPVs(pv.numero, PVsFinal)
                distancias[pv.numero] = round(dist, 2)
                
        maiorCaminho = max(distancias, key=distancias.get)
        
        return self.VerificaCaminho(maiorCaminho, pvsChegada = [PVsFinal])
    
    def OrdenaTrechos(self):
        redePrincipal = self.CalculaRedePrincipal()
        trechosEmOrdem = []
        trechosContabilizados = []
        
        for trecho in redePrincipal:
            contrib = self.CalculaContribuicoesPV(trecho.PVjusante.numero)
            
            if len(contrib) == 1:
                trechosEmOrdem.append(contrib[0])
                trechosContabilizados.append(contrib[0])
            
            elif len(contrib) > 1:
                contrib = [item for item in contrib if item not in trechosContabilizados]
        
    def CalculaRedes(self):               
        return False
            

if __name__ == "__main__":

    Rede = App()
    
    
    Rede.CriaListaDeLigacoes()
    Rede.VerificaSaidasPVs()
    PvsFinal = Rede.VerificaPvsFinalRede()
    trecho = Rede.VerificaCaminho(1, pvsChegada = [7])
    
    redePrincipal = Rede.OrdenaTrechos()
    
    #Trechos = Rede.VerificaRamificacoes(Rede.Dic_Lista_Tubulacoes[trecho], pv_jusante, listaTrechos)
    
    print (Rede.ListaRamos)
    
    #trecho = Rede.VerificaCaminho(3, pvsChegada = [4])
    
    #for trecho in Rede.VerificaCaminho(8):
        #print (trecho.numero)
    
    #print (Rede.CalculaContribuicoesPV(60))
    #Rede.CalculaVazoesEntradas()
    
#    for i in range(1, len(Rede.Dic_Lista_Tubulacoes)+1):
#        print ("Vazao no tubo %s = %s" %(Rede.Dic_Lista_Tubulacoes[i].numero, Rede.Dic_Lista_Tubulacoes[i].QentradaInicial))


#    for pv in Rede.ListaRamos:
#        print ("Lista de contribuicao PV %s" %pv)
#        _a = []
#        for trecho in Rede.ListaRamos[pv]:
#            if pv == Rede.Dic_Lista_Tubulacoes[trecho].PVjusante.numero:
#                _a += set(Rede.VerificaRamificacoes(Rede.Dic_Lista_Tubulacoes[trecho], pv, []))
#        print (_a)
    
    

    

    

