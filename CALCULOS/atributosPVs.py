# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 12:50:53 2018

@author: RONAN TEODORO
"""
from __future__ import division
import sys
from ctypes import *
import numpy as np
import math as m

from CALCULOS.vector3 import *
from AUXILIARES.util import truncaNumero

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
 
class LabelPV(object):
    def __init__(self, parent):
        self.parent = parent
        self._posAnchorPv = [210, 210, 0]
        self.textoLabel = ["PV-1","CT = 2,49","CF = 3,67", "h = 1,20"]      
    
        self.id_pontoArrasteLabel = None
        
        
        
    def AlteraTextoLabel(self):
        self.textoLabel = []
        self.textoLabel.append("PV-"+str(self.parent.numero))
        self.textoLabel.append("CT = "+str(round(self.parent.CotaTampa, 3)))
        self.textoLabel.append("CF = "+str(round((self.parent.CotaFundo), 3)))
        self.textoLabel.append("h = "+truncaNumero(self.parent.AlturaPv, 3))
        
        
    def GetTextLabel(self):
        self.AlteraTextoLabel()
        return self.textoLabel
        
    def DesenhaLabel(self, x=None, y=None, emMov=False):
        escala = self.parent.escala*3
        self.AlteraTextoLabel()        
        PV = self.parent
        if (x != None and y != None): #Se A label estiver sendo arrastada
            glPushMatrix()
            glColor3f(1.0, 0.0, 0.0)            
            if (x > PV.pos[0]-90*escala): # Se a posicao da label estiver
                glBegin(GL_LINES)         # mais do meio do PV
                glVertex3f(PV.pos[0],PV.pos[1],PV.pos[2])
                glVertex3f(x-15*escala, y, 0)        
                glEnd()
            else: # Se a posicao da label estiver antes do meio do PV
                glBegin(GL_LINES)
                glVertex3f(PV.pos[0],PV.pos[1],PV.pos[2])
                glVertex3f(x+210*escala, y, 0)        
                glEnd()
            
            glBegin(GL_LINES) # desenha a linha reta abaixo dos texto
            glVertex3f(x-15*escala, y, 0)        
            glVertex3f(x+210*escala, y, 0)        
            glEnd()
            glPopMatrix()
            
            glPushMatrix()
            glTranslate(x,y,0)
           
            for texto in self.textoLabel:            
                glPushMatrix()
                glScalef(escala, escala, escala )                       
                self.DesenhaStrokText(texto)
                glPopMatrix()
                glTranslate(0.0, -25*escala, 0.0)                
            glPopMatrix()
            
        else: # Se a label nao estiver sendo arrastada, desenho normal
            glPushMatrix()
            glColor3f(0.0, 0.5, 0.5)
            if emMov == False: #Pra quando o PV nao estiver em movimento
                glTranslate(PV.pos[0],PV.pos[1],PV.pos[2])
            else:
                pass
            if (self.posAnchorPv[0] > -90*escala): # Se a posicao da label estiver
                glBegin(GL_LINES)                  # mais do meio do PV
                glVertex3f(0.0, 0.0, 0.0)
                glVertex3f(self.posAnchorPv[0]-15*escala,
                           self.posAnchorPv[1]+0*escala,
                           self.posAnchorPv[2]+0*escala)
                glEnd()
            else: # Se a posicao da label estiver antes do meio do PV
                glBegin(GL_LINES)
                glVertex3f(0.0, 0.0, 0.0)
                glVertex3f(self.posAnchorPv[0]+210*escala,
                       self.posAnchorPv[1]+0*escala,
                       self.posAnchorPv[2]+0*escala)                           
                glEnd()
            
            glBegin(GL_LINES) # Desenha linha do PV ate o ponto de acoragem                 
            glVertex3f(self.posAnchorPv[0]-15*escala, #da label
                       self.posAnchorPv[1]+0*escala,
                       self.posAnchorPv[2]+0*escala)        
            glVertex3f(self.posAnchorPv[0]+210*escala, #desenha linha do ponto
                       self.posAnchorPv[1]+0*escala,   #de ancoragem da label
                       self.posAnchorPv[2]+0*escala)   #ate o final da linha      
            glEnd()                                    #reta abaixo dos textos 
            glPopMatrix()
            
            self.DesenhaTextosLabel(emMov=emMov)
            
            
    def DesenhaTextosLabel(self, emMov=False):
        PV = self.parent
        escala = self.parent.escala*3
        
        glPushMatrix()
        if emMov == False: # Se o PV nao estiver em movimento
            glTranslate(PV.pos[0],PV.pos[1],PV.pos[2])
        else: # Se o PV estiver em movimento
            pass
        glTranslate(* self.posAnchorPv) #Trasfere para inicio da ancoragem      
       
        for texto in self.textoLabel: #Desenha os textos da label           
            glPushMatrix()
            glScalef(escala, escala, escala )                       
            self.DesenhaStrokText(texto)
            glPopMatrix()
            glTranslate(0.0, -25*escala, 0.0)                
        glPopMatrix()
            
    def DesenhaPontoArrastoLabel(self):
        escala = self.parent.escala
        PV = self.parent
        try:
            glPushMatrix()
            glTranslate(PV.pos[0],PV.pos[1],PV.pos[2])            
            glTranslate(* self.posAnchorPv)            
            
            glBegin(GL_TRIANGLES)
            glVertex3f(-5*escala, +5*escala, 0.0)
            glVertex3f(-5*escala, -5*escala, 0.0)
            glVertex3f(+5*escala, -5*escala, 0.0)
            
            glVertex3f(+5*escala, +5*escala, 0.0)
            glVertex3f(+5*escala, -5*escala, 0.0)
            glVertex3f(-5*escala, +5*escala, 0.0)                       
            glEnd()
            glPopMatrix()
        except Exception:
            pass
    
    def AlteraPosicaoLabel(self, x, y):
        PV = self.parent
        self.posAnchorPv = [x-PV.pos[0],y-PV.pos[1],PV.pos[2]]
    
    def DesenhaPontoSnapLabel(self, dadosVisual):
        PV = self.parent
        try:
            coordenadas = gluProject(PV.pos[0]+self.posAnchorPv[0],
                                     PV.pos[1]+self.posAnchorPv[1],
                                     PV.pos[2]+self.posAnchorPv[2],
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
    def posAnchorPv (self):
        escala = self.parent.escala
        return [self._posAnchorPv[0]*escala,
                self._posAnchorPv[1]*escala,
                self._posAnchorPv[2]*escala] 
    
    @posAnchorPv.setter
    def posAnchorPv(self, value):
        escala = self.parent.escala
        self._posAnchorPv = [value[0]/escala, value[1]/escala, value[2]/escala]
        
    def DesenhaStrokText(self, palavra):
        glPointSize(1)
        glScalef(0.2, 0.2, 0.2)
        for letra in palavra:
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(letra))
                    
    def DesenhaTexto(self, FONT, Texto):
        for letra in Texto:
            glutBitmapCharacter(FONT, ord(letra))