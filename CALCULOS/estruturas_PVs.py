# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 22:53:53 2018

@author: RONAN TEODORO
"""

from __future__ import division
import numpy as np
import math as m

from CALCULOS.vector3 import *
from sympy import Point, Line, Segment
from sympy.geometry import intersection

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from atributosPVs import *


class PV_Padrao(object):
    """ Classe que define os atributos padroes de um Poco de Visita, classe
    base para criacao de outras classes de PVs.
    """
    
    ESTRUTURAS = ["PV - Poço de Visita", "TIL - Terminal de Inspeção eLimpeza",
                  "TL - Terminal de Limpeza", "CP - Caixa de Passagem"]                 
    
    PVMover = False
    PVRotacionar = False
    PVLabelArrastar = False
    PVTick_top = False
    PVTick_bottom = False
    
    @classmethod
    def StatusModificar(cls, *args, **kwargs):
        """ Retorna uma lista com os STATUS das variaveis de controle de
            modificacao dos PVs, para verificar se algum PV esta sendo
            modificado por meio de MOVER, ROTACIONAR, LABEL_ARRASTAS, TICK_TOP
        """
        
        return [cls.PVMover, cls.PVRotacionar, cls.PVLabelArrastar,
                cls.PVTick_top, cls.PVTick_bottom]
                
    @classmethod
    def LimpaStatus(cls, *args, **kwargs):
        """ Seta como False todos os Ticks
        """
        cls.PVMover = False
        cls.PVRotacionar = False
        cls.PVLabelArrastar = False
        cls.PVTick_top = False
        cls.PVTick_bottom = False
        
        
    def __init__(self, pos, CT=0.0, Altura=2.0):
        self._numero = None        
        self.nomePV = "PV"
        self.descricaoPV = "Caixa Retangular"
        
        self.pos = pos        
        self._x = pos[0]
        self.y = pos[1]
        
        self.AngloRotacao = 0
        
        self.AjusteAutomDaSuperficie = True
        
        
        self.AlturaQueda = 0.0
        
        self.CotaTerreno = CT
        self.CotaTampa = CT
        self.AlturaPv = Altura
        self.CotaFundo = CT-self.AlturaPv
        
        self.Rotulo = None
        
        self.Tipo = None
       
        self.Label = LabelPV(self)
        
        self.id_pontoArraste = None
        self.id_pontoRotacao = None
        
        self.color = [0.0, 1.0, 0.0]        
        
        self.escala = 5
        self.AtualizaMatrizRotacao()
        
        self.visivel = True  
        
        self.pontoRotacao = [25*self.escala, 0, 0]
    
    def CalculaAngMousePV(self, mouseX, mouseY):
        """Calcula o angulo entre o vetor [origemPV-PontoRotacao] e o vetor
           [origemPV-PosicaoMouse]
        """
        v = self.pontoRotacao
        v0 = np.array([v[0], v[1]])
        v1 = np.array([mouseX-self.pos[0], mouseY-self.pos[1]])        
        
        angulo = m.degrees(np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1)))
    
        return angulo        
            
    def AtualizaMatrizRotacao(self):        
        alpha = np.radians(self.AngloRotacao)
        
        self.Ri = np.array([[m.cos(alpha), m.sin(alpha), 0],
                            [-m.sin(alpha),  m.cos(alpha), 0],
                            [     0,              0,      1]])
        
        self.pontoRotacao = np.dot(np.array([25*self.escala, 0, 0]), self.Ri)    
        
    @property
    def numero(self):
        return self._numero
        
    @numero.setter
    def numero(self, value):
        if value != None:
            self.AlteraPontoArraste(value)        
        self._numero =  value
        
    def SetNomeEstrutura(self, nomeEstrutura):
        """Seta o nome da Estrutura"""
        self.nomePV = nomeEstrutura
        
    def SetCoordenadaX(self, coord_x):
        """Seta o valor da Coordenada X da Estrutura"""
        self.pos[0] = coord_x
        
    def SetCoordenadaY(self, coord_y):
        """Seta o valor da Coordenada Y da Estrutura"""
        self.pos[1] = coord_y
        
    def SetAnguloRotacao(self, angulo):
        """Seta o valor do angulo de rotacao da Estrutura"""
        self.AngloRotacao = angulo
        
    def SetCotaTerreno(self, cotaTerreno):
        """Seta a cota do Terreno e faz os ajustes nas variaveis
           que interferem na Cota do Terreno"""
        self.CotaTerreno = round(cotaTerreno, 3)        
            
    def SetCotaTampa(self, cotaTampa):
        """Seta a cota da Tampa da Estrutura e faz os ajustes nas variaveis
           que interferem na Cota da Tampa"""
        self.CotaTampa = round(cotaTampa, 3)
        
        if (self.CotaTampa - self.CotaFundo) >= 0.4:
            self.AlturaPv = round(self.CotaTampa - self.CotaFundo, 3)
        else:
            self.AlturaPv = round(0.4, 3)
            self.CotaFundo = round(self.CotaTampa - self.AlturaPv, 3)
            
    def SetCotaFundo(self, cotaFundo):
        """Seta a cota do Fundo da Estrutura e faz os ajustes nas variaveis
           que interferem na Cota do Fundo"""
        self.CotaFundo = round(cotaFundo, 3)
        
        if (self.CotaTampa - self.CotaFundo) >= 0.4:
            self.AlturaPv = round(self.CotaTampa - self.CotaFundo, 3)
        else:
            self.AlturaPv = round(0.4, 3)
            self.CotaTampa = round(self.CotaFundo + self.AlturaPv, 3)
            
    def SetAlturaEstrutura(self, altura):
        """Seta a Altura da Estrutura e faz os ajustes nas variaveis
           que interferem na Altura da Estrutura"""
        self.AlturaPv = round(abs(altura), 3)
        
        if (self.AlturaPv) >= 0.4:
            self.CotaFundo = round(self.CotaTampa - self.AlturaPv, 3)
        else:
            self.AlturaPv = round(0.4, 3)
            self.CotaFundo = round(self.CotaTampa - self.AlturaPv, 3)
                        
            
class PV_Retangular(PV_Padrao):
    """Classe que define um Poco de Visita do tipo Retangular
       
       Classe Base (PV_Padrao)
    """
    def __init__(self, pos, CT=None, Altura=2.0):
        PV_Padrao.__init__(self, pos, CT=CT, Altura=Altura)
        self.ComprimentoInterno = 1.0
        self.LarguraInterno = 1.0
        
        self.pontosPV = []
        
        self.CriaGeometria()        
                
    
    def CriaGeometria(self):
        compr = self.ComprimentoInterno*self.escala
        largu = self.LarguraInterno*self.escala
        self.pontosPV.append([-compr/2, +largu/2, 0.0])
        self.pontosPV.append([+compr/2, +largu/2, 0.0])
        self.pontosPV.append([+compr/2, -largu/2, 0.0])
        self.pontosPV.append([-compr/2, -largu/2, 0.0])    
    
        self.CalculaArestas()
        
    def AlteraAnguloRotacao(self, mouseX, mouseY, geometria=False):
        v = self.pontoRotacao
        v0 = np.array([v[0], v[1]])
        v1 = np.array([mouseX-self.pos[0], mouseY-self.pos[1]])        
        
        self.AngloRotacao += m.degrees(np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1)))
        
        self.AtualizaMatrizRotacao()
        self.AtualizaGeometria()
        
    def AtualizaGeometria(self):
        compr = self.ComprimentoInterno*self.escala
        largu = self.LarguraInterno*self.escala        
        self.pontosPV[0] = np.dot(np.array([-compr/2, +largu/2, 0.0]), self.Ri)
        self.pontosPV[1] = np.dot(np.array([+compr/2, +largu/2, 0.0]), self.Ri)
        self.pontosPV[2] = np.dot(np.array([+compr/2, -largu/2, 0.0]), self.Ri)
        self.pontosPV[3] = np.dot(np.array([-compr/2, -largu/2, 0.0]), self.Ri)
    
    def CalculaArestas(self):
        self.AtualizaGeometria()
        
        #P1 = Point(self.pontosPV[0][0]+self.pos[0], self.pontosPV[0][1]+self.pos[1])
        #P2 = Point(self.pontosPV[1][0]+self.pos[0], self.pontosPV[1][1]+self.pos[1])
        #P3 = Point(self.pontosPV[2][0]+self.pos[0], self.pontosPV[2][1]+self.pos[1])
        #P4 = Point(self.pontosPV[3][0]+self.pos[0], self.pontosPV[3][1]+self.pos[1])   
       
        #self.l1 = Segment(P1, P2)
        #self.l2 = Segment(P2, P3)
        #self.l3 = Segment(P3, P4)
        #self.l4 = Segment(P4, P1)
        
    
    def DesenhaOutrosElementos(self):
        try:
            glPushMatrix()
            glColor3ub(100, 166, 200)
            glTranslate(self.pos[0],self.pos[1],self.pos[2])
            #glRotatef(self.AngloRotacao, 0, 0, 1)
            glBegin(GL_LINES)
            glVertex3f(0.0, 0.0, 0.0)
            glVertex3f(* self.pontoRotacao)                     
            glEnd()
            glPopMatrix()
        except Exception:
            pass
    
    def DesenhaPV(self, emMov = False):   
#        compr = self.ComprimentoInterno*100*self.escala
#        largu = self.LarguraInterno*100*self.escala
#        
#        #Se o pv nao estiver sendo arrastado ou rotacionado
#        #desenha o pv em modo normal
#        glPushMatrix()
#        if emMov == False: # Se o PV nao estiver sendo desenhado em movimento
#            glTranslate(self.pos[0],self.pos[1],self.pos[2])
#        else:
#            pass
#        glRotatef(self.AngloRotacao, 0, 0, 1)
#        glBegin(GL_LINES)
#        glVertex3f(-compr/2, +largu/2, 0)
#        glVertex3f(+compr/2, +largu/2, 0)
#        
#        glVertex3f(+compr/2, +largu/2, 0)
#        glVertex3f(+compr/2, -largu/2, 0)
#        
#        glVertex3f(+compr/2, -largu/2, 0)
#        glVertex3f(-compr/2, -largu/2, 0)
#        
#        glVertex3f(-compr/2, -largu/2, 0)
#        glVertex3f(-compr/2, +largu/2, 0)
#        glEnd()
#        
#        glPopMatrix()
        
        #################################
        posx, posy = 0,0    
        sides = 16   
        radius = 50
        glPushMatrix()
        glTranslate(self.pos[0],self.pos[1],self.pos[2])
        glBegin(GL_LINE_LOOP)    
        for i in range(16):    
            cosine= radius * cos(i*2*pi/sides) + posx    
            sine  = radius * sin(i*2*pi/sides) + posy    
            glVertex2f(cosine*self.escala,sine*self.escala)
        glEnd()
        glPopMatrix()
        ################################
        
        self.Label.DesenhaLabel(emMov=emMov)
        
        
        
    def DesenhaPVemMovimento(self):
        glColor3f(1.0, 0.0, 0.0)
        self.DesenhaPV(emMov=True)
        
            
    def DesenhaPvRotacionado(self, x=None, y=None):
        compr = self.ComprimentoInterno*100*self.escala
        largu = self.LarguraInterno*100*self.escala
        ang = self.CalculaAngMousePV(x, y)
        ang += self.AngloRotacao
        if (x != None and y != None):
            glPushMatrix()
            glTranslatef(self.pos[0], self.pos[1], self.pos[2])
            glRotatef(ang, 0, 0, 1)           
            glBegin(GL_LINES)
            glColor(1.0, 0.0, 0.0)
            glVertex3f(-compr/2, +largu/2, 0)
            glVertex3f(+compr/2, +largu/2, 0)
            
            glColor(0.0, 1.0, 0.0)
            glVertex3f(+compr/2, +largu/2, 0)
            glVertex3f(+compr/2, -largu/2, 0)
            
            glColor(0.0, 0.0, 1.0)
            glVertex3f(+compr/2, -largu/2, 0)
            glVertex3f(-compr/2, -largu/2, 0)
            
            glColor(1.0, 0.0, 1.0)
            glVertex3f(-compr/2, -largu/2, 0)
            glVertex3f(-compr/2, +largu/2, 0)
            glEnd()
            
            glPopMatrix()
    
    def DesenhaPontosArrasto(self):
        try:
            glPushMatrix()
            glTranslate(self.pos[0],self.pos[1],self.pos[2])            
            glRotatef(self.AngloRotacao, 0, 0, 1)
            glBegin(GL_TRIANGLES)
            glVertex3f(-5*self.escala, +5*self.escala, 0.0)
            glVertex3f(-5*self.escala, -5*self.escala, 0.0)
            glVertex3f(+5*self.escala, -5*self.escala, 0.0)
            
            glVertex3f(+5*self.escala, +5*self.escala, 0.0)
            glVertex3f(+5*self.escala, -5*self.escala, 0.0)
            glVertex3f(-5*self.escala, +5*self.escala, 0.0)                       
            glEnd()
            glPopMatrix()
        except Exception:
            pass
        
    def DesenhaPontoRotacao(self):
        try:
            posx, posy = 0,0    
            sides = 32    
            radius = 5
            glPushMatrix()
            glColor3ub(100, 164, 200)
            glTranslate(self.pos[0],self.pos[1],self.pos[2])            
            glTranslate(* self.pontoRotacao)
            glBegin(GL_POLYGON)    
            for i in range(100):    
                cosine= radius * cos(i*2*pi/sides) + posx    
                sine  = radius * sin(i*2*pi/sides) + posy    
                glVertex2f(cosine*self.escala,sine*self.escala)
            glEnd()
            glPopMatrix()
        except Exception:
            pass
        
    def DesenhaPontoSnapRotacao(self, dadosVisual):
        try:
            coordenadas = gluProject(self.pos[0]+self.pontoRotacao[0],
                                     self.pos[1]+self.pontoRotacao[1],
                                     self.pos[2]+self.pontoRotacao[2],
                            dadosVisual[0], dadosVisual[1], dadosVisual[2])
    
            x, y = coordenadas[0], dadosVisual[3][1]-coordenadas[1]
                    
            glPushMatrix()
            glLineWidth (1.0)
            glColor3f(0.0, 1.0, 0.0)
            glBegin(GL_POLYGON)
            glVertex3f(x-5,y+5, 0)
            glVertex3f(x+5,y+5, 0)
            glVertex3f(x+5,y-5, 0)
            glVertex3f(x-5,y-5, 0)
            glEnd()
            glPopMatrix()                    
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print ("*"*30)
            print(exc_type, fname, exc_tb.tb_lineno)
            print (e)
            print ("*"*30)
        
    @property
    def x(self):
        return self._x
        
    @x.setter
    def x(self, value):
        self._x =  value        
        
        
    def AlteraPontoArraste(self, value):        
        if value != None:
            self.id_pontoArraste = value + 10000
            self.id_pontoRotacao = value + 20000
            self.id_pontoArrasteLabel = value + 30000

    
    