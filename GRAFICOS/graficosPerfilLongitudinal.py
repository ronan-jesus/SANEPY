# -*- coding: utf-8 -*-
"""
Created on Domingo Setembro 02 23:12:00 2018

@author: RONAN TEODORO
"""
from __future__ import division

import sys, os

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class CorePerfilLongitudinal:
    
    def __init__(self, parent, pos):
        self.parent = parent
        self.pos = [pos[0], pos[1], 0]       
        
        self._elevAutomatico = True
        
        self.ElevMinDefinida = 0
        self.ElevMaxDefinida = 0
        
        self._cotaMaxima = 95
        self._cotaMinima = 85
        
    def DesenhaSnapPerfil(self, dados):
        """ Desenha o Snap do Perfil longitudinal, o quadrado e desenhado na
            posicao (0,0) do perfil
        """
        
        if (self == self.parent.OBJETO_SELECIONADO):
            x, y = self.GetCoordTela(self.pos[0], self.pos[1], dados)
            
            glPushMatrix()
            #Desenha Tick INICIO PErFIL
            glColor3ub(0, 255, 0)
            glBegin(GL_QUADS)
            glVertex2f(x-5, y+5)
            glVertex2f(x+5, y+5)
            glVertex2f(x+5, y-5)
            glVertex2f(x-5, y-5)
            glEnd()
            glPopMatrix()
        
    def DesenhaSnapPerfilSelect(self, dados):
        """ 
        """
        if (self == self.parent.OBJETO_SELECIONADO):
            x, y = self.GetCoordTela(self.pos[0], self.pos[1], dados)
            
            x1, y1 = self.GetCoordMundo(x-5, y+5)
            x2, y2 = self.GetCoordMundo(x+5, y+5)
            x3, y3 = self.GetCoordMundo(x+5, y-5)
            x4, y4 = self.GetCoordMundo(x-5, y-5)
                       
            glPushName(1)        
            glPushMatrix()
            #Desenha Tick INICIO PErFIL
            glColor3ub(0, 255, 0)
            glBegin(GL_QUADS)
            glVertex2f(x1, y1)
            glVertex2f(x2, y2)
            glVertex2f(x3, y3)
            glVertex2f(x4, y4)
            glEnd()
            glPopMatrix()
            glPopName()
    
    
    def GetCoordTela(self, pos_x, pos_y, dados):         
        '''
        Descrição:
          Funcao que entra com a posicao x, y do clique no Mundo e retorna a
          posicao X, Y da Tela, ou seja, entra com as Coordenadas do Mundo
          e retorna as Coordenadas do Tela.
    
        Utilização:
          GetCoordTela(pos_x, pos_y)
    
        Parâmetros:
          pos_x
            tipo(int) posicao x do Mundo.
          mouse_y
            tipo(int) posicao y do Mundo.
            
        Return:
            tupla (float x, float y)Tupla contendo as Coordenadas calculadas
            da Tela.
        '''         
        
        coordenadas = gluProject(pos_x, pos_y, 0, dados[0], dados[1], dados[2])
        x, y = coordenadas[0], dados[3][1]-coordenadas[1]
        
        return x, y
        
    def GetCoordMundo(self, mouse_x, mouse_y):         
        '''
        Descrição:
          Funcao que entra com a posicao x, y do clique na ViewPort e retorna a
          posicao X, Y do Desenho, ou seja, entra com as Coordenadas da Tela
          e retorna as Coordenadas do Mundo.
    
        Utilização:
          GetCoordMundo(mouse_x, mouse_y, viewport, camera)
    
        Parâmetros:
          mouse_x
            tipo(int) posicao x da tela.
          mouse_y
            tipo(int) posicao y da tela.
            
        Return:
            tupla (float x, float y)Tupla contendo as Coordenadas calculadas do Mundo.
        '''         
                
        projection = glGetDoublev(GL_PROJECTION_MATRIX)
        viewport = glGetIntegerv(GL_VIEWPORT)
        modelview = glGetDoublev(GL_MODELVIEW_MATRIX)    
        
        mouse_y = viewport[3]-mouse_y
            
        x, y, z = gluUnProject(mouse_x, mouse_y, 0, modelview, projection, viewport)
        
        return x, y
        
    def SetPosPerfil(self, posx, posy):
        """Altera a posicao da origem do grafico.
        
           posx -> flot(coord_x_Tela, coord_y_Tela)
        """        
        glPushMatrix()
        glLoadIdentity()

        x, y = self.GetCoordMundo(posx, posy)

        glPopMatrix()
        
        self.pos = [x, y, 0]
        
    def DesenhaPerfilMovimento(self, xTela, yTela):       
        if self.numero == self.parent.PERFIL.PERFIL_MOV:
            x, y = self.GetCoordMundo(xTela, yTela)
        
        self.DesenhaPerfil(pos=[x, y, 0])
        
    def GetListaPVsdoPerfil(self):
        """Retorna lista com os OBJETOS do tipo PV que fazem parte dos TRECHOS
           contidos no PERFIL
        """
        listaPVs = []
        
        for trecho in self.Trechos:            
            if trecho.PV1 not in listaPVs:
                listaPVs.append(trecho.PV1)
            if trecho.PV2 not in listaPVs:
                listaPVs.append(trecho.PV2)
            
        return listaPVs
        
    def GetListaTrechosdoPerfil(self):
        """Retorna lista com os OBJETOS do tipo TRECHOS contidos no PERFIL
        """        
            
        return self.Trechos
    
    def CalculaCotaMinMaxAlturaAutomatico(self):
        cotasTampas = []
        cotasFundo = []
        for trec in self.Trechos:
            cotasTampas.append(trec.PV1.CotaTampa)
            cotasTampas.append(trec.PV2.CotaTampa)
            cotasFundo.append(trec.PV1.CotaFundo)
            cotasFundo.append(trec.PV2.CotaFundo)

        self.cotaMaxima = int(max(cotasTampas))+3
        self.cotaMinima = int(min(cotasFundo))-3        
        self.AlturaPerfil = (self.cotaMaxima-self.cotaMinima)    
    
    def GetCotaMinMaxAutomatico(self):
        cotasTampas = []
        cotasFundo = []
        for trec in self.Trechos:
            cotasTampas.append(trec.PV1.CotaTampa)
            cotasTampas.append(trec.PV2.CotaTampa)
            cotasFundo.append(trec.PV1.CotaFundo)
            cotasFundo.append(trec.PV2.CotaFundo)

        cotaMaxima = int(max(cotasTampas))+3
        cotaMinima = int(min(cotasFundo))-3        
        
        return [cotaMinima, cotaMaxima]
        
    def CalculaCotaMinMaxAlturaDefinido(self):
        self.cotaMaxima = int(self.ElevMaxDefinida)+3
        self.cotaMinima = int(self.ElevMinDefinida)-3        
        self.AlturaPerfil = (self.cotaMaxima-self.cotaMinima)
    
    @property
    def cotaMaxima(self):
        return self._cotaMaxima
    
    @cotaMaxima.setter
    def cotaMaxima(self, value):   
        self._cotaMaxima = value
        self.AlturaPerfil = (self.cotaMaxima-self.cotaMinima)
        
    @property
    def cotaMinima(self):
        return self._cotaMinima
    
    @cotaMinima.setter
    def cotaMinima(self, value):   
        self._cotaMinima = value
        self.AlturaPerfil = (self.cotaMaxima-self.cotaMinima)
        
    @property
    def elevAutomatico(self):
        return self._elevAutomatico
        
    @elevAutomatico.setter
    def elevAutomatico(self, value):        
        self._elevAutomatico = value
        
#        if self.elevAutomatico == True:
#            self.CalculaCotaMinMaxAlturaAutomatico()
#        else:
#            self.CalculaCotaMinMaxAlturaDefinido()
            
        
        