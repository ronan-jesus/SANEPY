# -*- coding: utf-8 -*-
"""
Created on Domingo Setembro 02 23:12:00 2018

@author: RONAN TEODORO
"""
from __future__ import division
import math as m
import numpy as np

import sys, os
from graficosPerfilLongitudinal import CorePerfilLongitudinal

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from AUXILIARES.util import truncaNumero
    
class PerfilLongitudinal(CorePerfilLongitudinal):
    
    PERFIL_MOV = False
    
    @classmethod
    def __new__(cls, *args, **kwargs):        
        instance = super(PerfilLongitudinal, cls).__new__(cls)
        return instance
    
    @classmethod
    def StatusModificar(cls, *args, **kwargs):
        """ Retorna uma lista com os STATUS das variaveis de controle de
            modificacao dos PERFIS, para verificar se algum PERFIL esta sendo
            modificado por meio de MOVER
        """        
        return [cls.PERFIL_MOV]
                
    def __init__(self, parent, pos, nomePerfil="None", trechos=[], num=1):
        CorePerfilLongitudinal.__init__(self, parent, pos)
        self.parent = parent
        self.numero = num
        self.descricao = ""
        
        
        #Variaveis do Titlo
        self.tittleLabel = nomePerfil
        self.XoffsetTittle = 5
        self.YoffsetTittle = 5
        self.XoffsetMajorCotaVertical = -13
        self.YoffsetMajorCotaVertical = -2        
        self.XoffsetMajorTickVertical = -5
        self.YoffsetMajorTickVertical = 0
        self.tamanhoTickVertical = 5
        self.tamanhoTickHorizontal = 5
        
        #Variaveis do Quadro de Bands
        self.XoffsetGapQuadValuesBands = 0
        self.YoffsetGapQuadValuesBands = 5
        self.XoffsetGapQuadTittleBands = 0
        self.YoffsetGapQuadTittleBands = 5
        self.heightQuadValuesBands = 20
        self.heightQuadTittleBands = 20
        self.withQuadTittleBands = 85
        self.XoffsetTextTittleBands = 5
        self.YoffsetTextTittleBands = 11
        self.XoffsetTextValuesBands = 0
        self.YoffsetTextValuesBands = 2
        
        
        self.escalaVertical = 10
        self.escalaHorizontal = 1
        
        self.espVertLinhas = 2 # Cada quantos metros
        self.espHorizLinhas = 10 # Cada quantos metros
        
        
    
        self.Comprimento = 200
        self.AlturaPerfil = (self.cotaMaxima-self.cotaMinima)
        
        self.posx = 0
        self._posx = 50
        
        self.PVs = []
        self.Trechos = trechos
        #self.Trechos = parent.Estrututura.LISTA_TUBULACOES
        
        self.coordsPV = {}
        self.coordsPVReal = {}
        self.InicializaDados()
        
        band1 = EstruturaBand(self, ["N do Poco de Visita"])
        band1.SetScaleTitleText(0.07)
        band1.SetHeighBand(10)
        band1.tipoDadosBand = "NUM_PV"
        band1.anchorPosBands = "MIDLE"
        
        band2 = EstruturaBand(self, ["Cota da Tampa"])
        band2.SetScaleTitleText(0.07)
        band2.SetHeighBand(10)
        band2.tipoDadosBand = "COTA_TAMPA"
        band2.anchorPosBands = "MIDLE"
        
        band3 = EstruturaBand(self, ["Cota do Fundo"])
        band3.SetScaleTitleText(0.07)
        band3.SetHeighBand(10)
        band3.tipoDadosBand = "COTA_FUNDO"
        band3.anchorPosBands = "MIDLE"
        
        band4 = EstruturaBand(self, ["Profundidade"])
        band4.SetScaleTitleText(0.07)
        band4.SetHeighBand(10)
        band4.tipoDadosBand = "PROFUNDIDADE"
        band4.anchorPosBands = "MIDLE"
        
        band5 = EstruturaBand(self, ["Degrau"])
        band5.SetScaleTitleText(0.07)
        band5.SetHeighBand(10)
        band5.tipoDadosBand = "DEGRAU"
        band5.anchorPosBands = "MIDLE"
        
        band6 = TrechoBand(self, ["Extensao"])
        band6.SetScaleTitleText(0.07)
        band6.SetHeighBand(10)
        band6.tipoDadosBand = "COMPRIMENTO"
        band6.anchorPosBands = "MIDLE_MIDLE"
        
        band7 = TrechoBand(self, ["Diametro"])
        band7.SetScaleTitleText(0.07)
        band7.SetHeighBand(10)
        band7.tipoDadosBand = "DIAMETRO"
        band7.anchorPosBands = "MIDLE_MIDLE"
        
        band8 = TrechoBand(self, ["Declividade"])
        band8.SetScaleTitleText(0.07)
        band8.SetHeighBand(10)
        band8.tipoDadosBand = "DECLIVIDADE"
        band8.anchorPosBands = "MIDLE_MIDLE"
        
        self.Bands = DataBands(self)
        self.Bands.AddBand(band1)
        self.Bands.AddBand(band2)        
        self.Bands.AddBand(band3)        
        self.Bands.AddBand(band4)        
        self.Bands.AddBand(band5)        
        self.Bands.AddBand(band6)        
        self.Bands.AddBand(band7)        
        self.Bands.AddBand(band8)        
    
    def InicializaDados(self):
        ########### COMPRIMENTO ###################
        self.GetListCoordsRealPVs()
        self.GetListCoordsTRECHOS()
        
        comprimento = 0
        cotasTampas = []
        cotasFundo = []
        for trec in self.Trechos:
            comprimento += trec.L
            cotasTampas.append(trec.PV1.CotaTampa)
            cotasTampas.append(trec.PV2.CotaTampa)
            cotasFundo.append(trec.PV1.CotaFundo)
            cotasFundo.append(trec.PV2.CotaFundo)

        self.Comprimento = comprimento+(2*self._posx) #Comprimento do Perfil (pegar do modelo depois)
        self.cotaMaxima = int(self.cotaMaxima)+3
        self.cotaMinima = int(self.cotaMinima)-3        
        self.AlturaPerfil = (self.cotaMaxima-self.cotaMinima)
        
        self.cotaMinima = self.GetCotaMinMaxAutomatico()[0]
        self.cotaMaxima = self.GetCotaMinMaxAutomatico()[1]
    
    def DesenhaPerfil(self, pos=False):
        """ Desenha apenas a janela de Visualizacao do Perfil, sem os elementos
            como PVs, Trechos, Labels. Apenas quadro, linhas horizontais,
            linhas verticais, titulos, numeracao das alturas entre outros.
        """
        try:
            glPushMatrix()
            #glEnable(GL_LINE_SMOOTH)
            if pos != False:                
                glTranslatef(* pos)
            else:
                glTranslatef(* self.pos)
                
            glScalef(100, 100, 100)
            
            self.DesenhaTitulosPefil()
            self.DesenhaCotasVerticaisPerfil()
            
            #Desenha Marges do Perfil        
            glPushMatrix() 
            glLineWidth(1)
            glColor3ub(0, 0, 205)
            glBegin(GL_LINE_LOOP)        
            glVertex2d(0.0, 0.0)
            glVertex2d(self.Comprimento, 0.0*self.escalaVertical)
            glVertex2d(self.Comprimento, self.AlturaPerfil*self.escalaVertical)
            glVertex2d(0.0, self.AlturaPerfil*self.escalaVertical)
            glEnd()
            glPopMatrix()
            
            #Desenha Linhas Verticais do Perfil        
            glPushMatrix()
            glTranslatef(0,0,-1)
            glLineWidth(1)
            glColor3ub(105, 105, 105)
            glBegin(GL_LINES)
            for i in range(1, int(self.Comprimento/self.espHorizLinhas)+1):
                glVertex2d(self.espHorizLinhas*i, 0.0*self.escalaVertical)
                glVertex2d(self.espHorizLinhas*i, self.AlturaPerfil*self.escalaVertical)
            glEnd()
            glPopMatrix()
            
            #Desenha Linhas Horizontais do Perfil
            glPushMatrix()
            glTranslatef(0,0,-1)
            glLineWidth(1)
            glColor3ub(105, 105, 105)
            glBegin(GL_LINES)
            for i in range(1, int(self.AlturaPerfil/self.espVertLinhas)+1):
                glVertex2d(0.0, self.espVertLinhas*i*self.escalaVertical)
                glVertex2d(self.Comprimento, self.espVertLinhas*i*self.escalaVertical)
            glEnd()
            glPopMatrix() 
            
            self.DesenhaBands()
            glPopMatrix()
            
            
            
        except Exception as e:
            if True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
        

    def DesenhaTitulosPefil(self):
        xpos = 0
        ypos = self.AlturaPerfil*self.escalaVertical + self.YoffsetTittle
        
        glPushMatrix()
        glLineWidth(2)
        glPointSize(2)
        glTranslatef(xpos, ypos, 0 )
        glColor3f(0.0, 0.0, 1.0)
        self.DesenhaStrokText(self.tittleLabel)
        glPopMatrix()
    
    def DesenhaCotasVerticaisPerfil(self):             
        def DesenhaTickVertical():
            glPushMatrix()
            glColor3f(0.0, 1.0, 0.0)
            glTranslatef(self.XoffsetMajorTickVertical, 0, 0)
            glBegin(GL_LINES)
            glVertex2f(0, 0)
            glVertex2f(-self.XoffsetMajorTickVertical, 0)
            glEnd()
            glPopMatrix()
        
        glPushMatrix()
        glLineWidth(2)
        glColor3ub(0, 0, 205)        
        for cota in range(int(self.cotaMinima), int(self.cotaMaxima), self.espVertLinhas):
            DesenhaTickVertical()
            glTranslatef(0, self.espVertLinhas*self.escalaVertical, 0)
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(self.XoffsetMajorCotaVertical, self.YoffsetMajorCotaVertical, 0)
        glLineWidth(2)
        glPointSize(2)
        glColor3ub(0, 0, 205)        
        for cota in range(int(self.cotaMinima), int(self.cotaMaxima), self.espVertLinhas):
            self.DesenhaStrokText(str(cota), escala=0.5)
            glTranslatef(0, self.espVertLinhas*self.escalaVertical, 0)
        glPopMatrix()
    
    def DesenhaBands(self):
        #try:
            self.Bands.DesenhaBands()
#        except Exception as e:
#            if True:
#                exc_type, exc_obj, exc_tb = sys.exc_info()
#                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#                print(exc_type, fname, exc_tb.tb_lineno)
#                print (e)
            
#        #Desenha os Ticks Verticais Dentro do retangulo dos valores das BandData
#        try:            
#            #Desenha Retangulo dos Valores
#            glPushMatrix()
#            glColor3f(0.0, 0.5, 0.5)
#            glLineWidth(1)
#            glTranslatef(0, -(self.heightQuadValuesBands+self.YoffsetGapQuadValuesBands), 0)
#            glBegin(GL_LINE_LOOP)
#            glVertex2f(0, 0)
#            glVertex2f(self.Comprimento, 0)
#            glVertex2f(self.Comprimento, self.heightQuadValuesBands)
#            glVertex2f(0, self.heightQuadValuesBands)
#            glEnd()
#            glPopMatrix()
#            
#            #Desenha Retangulo dos Titulos a esquerda do retangulo dos valores
#            glPushMatrix()
#            glColor3f(0.0, 0.5, 0.5)
#            glLineWidth(1)
#            glTranslatef(-self.withQuadTittleBands, -(self.heightQuadTittleBands+self.YoffsetGapQuadTittleBands), 0)
#            glBegin(GL_LINE_LOOP)
#            glVertex2f(0, 0)
#            glVertex2f(self.withQuadTittleBands, 0)
#            glVertex2f(self.withQuadTittleBands, self.heightQuadTittleBands)
#            glVertex2f(0, self.heightQuadTittleBands)
#            glEnd()
#            glPopMatrix()
#            
#            #Desenha o Titulo da BandData
#            glPushMatrix()
#            glColor3f(0.0, 0.5, 0.5)
#            glLineWidth(1)
#            glTranslatef(-self.withQuadTittleBands, -(self.heightQuadTittleBands+self.YoffsetGapQuadTittleBands), 0)
#            glTranslatef(self.XoffsetTextTittleBands, self.YoffsetTextTittleBands, 0)
#            textoCotas = "Cota da Tampa/Cota do Fundo"
#            for texto in textoCotas.split("/"):
#                self.DesenhaStrokText(texto, escala=0.75)
#                glTranslate(0.0, -9, 0.0)
#            glPopMatrix()
#        
#            #TICK vertical dentro do retangulo de valores da BandaData
#            glPushMatrix()
#            glTranslatef(0, -(self.heightQuadValuesBands+self.YoffsetGapQuadValuesBands), 0)
#            for num, coord in self.coordsPVReal.items():            
#                glPushMatrix()
#                glTranslatef(coord[0], 0, 0)
#                glBegin(GL_LINES)
#                glVertex2f(0, 0)
#                glVertex2f(0, self.heightQuadValuesBands)
#                glEnd()
#                glPopMatrix()
#            
#            for num, coord in self.coordsPVReal.items():
#                #Cota da Tampa
#                glPushMatrix()
#                glTranslatef(coord[0]-1, self.YoffsetTextValuesBands, 0)
#                glRotatef(90, 0, 0, 1)
#                glPointSize(1)
#                glScalef(0.1, 0.1, 0.1)
#                glScalef(0.50, 0.50, 0.50)                
#                for letra in truncaNumero(coord[1], 2):
#                    glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(letra))
#                glPopMatrix()
#                
#                #Cota do Fundo
#                glPushMatrix()
#                glTranslatef(coord[0]+6, self.YoffsetTextValuesBands, 0)
#                glRotatef(90, 0, 0, 1)
#                glPointSize(1)
#                glScalef(0.1, 0.1, 0.1)
#                glScalef(0.50, 0.50, 0.50)                
#                for letra in truncaNumero(coord[2], 2):
#                    glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(letra))
#                glPopMatrix()
#                
#            glPopMatrix()
#        except Exception as e:
#            if True:
#                exc_type, exc_obj, exc_tb = sys.exc_info()
#                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#                print(exc_type, fname, exc_tb.tb_lineno)
#                print (e)
        
        
        
    def DesenhaPVs(self):
        """Desenha os PVs dentro do Perfil Longitudinal, apenas os PVS
        """
        try:
            self.coordsPV = {}
            
            glPushMatrix()
            glEnable(GL_LINE_SMOOTH)
            glTranslatef(* self.pos)      
            glScalef(100, 100, 100)       
            
            #Desenha POcos de Visitas no Perfil        
            glLineWidth(1)
            glColor3ub(255, 0, 0)        
            
            self.posx = self._posx        
            glPushName(1)
            for i in range(len(self.Trechos)):            
                pv1 = self.Trechos[i].PV1
                pv2 = self.Trechos[i].PV2
                
                L = self.Trechos[i].L
                
                glPushMatrix()
                glTranslatef(self.posx, 0, 0)
                
                if i != (len(self.Trechos)-1):
                    #PV 1
                    glColor3ub(255, 0, 0)
                    glPushName(pv1.numero)
                    glBegin(GL_LINE_LOOP)
                    glVertex2f(-1, (pv1.CotaTampa-self.cotaMinima)*self.escalaVertical)
                    glVertex2f(+1, (pv1.CotaTampa-self.cotaMinima)*self.escalaVertical)
                    glVertex2f(+1, (pv1.CotaTampa-(pv1.AlturaPv)-self.cotaMinima)*self.escalaVertical)
                    glVertex2f(-1, (pv1.CotaTampa-(pv1.AlturaPv)-self.cotaMinima)*self.escalaVertical)
                    glEnd()                    
                    glPopName()
                    
                    XSnapTop = (self.pos[0]+self.posx*100)
                    YSnapTop = (self.pos[1]+(pv1.CotaTampa-self.cotaMinima)*self.escalaVertical*100)
                    YSnapBottom = (self.pos[1]+(pv1.CotaFundo-self.cotaMinima)*self.escalaVertical*100)
                    self.coordsPV[pv1.numero] = [XSnapTop, YSnapTop, YSnapBottom]
                    self.coordsPVReal[pv1.numero] = [self.posx, pv1.CotaTampa, pv1.CotaFundo]
                    self.posx += L
                    
                    
                else:
                    #PV 1
                    glColor3ub(255, 0, 0)
                    glPushName(pv1.numero)
                    glBegin(GL_LINE_LOOP)
                    glVertex2f(-1, (pv1.CotaTampa-self.cotaMinima)*self.escalaVertical)
                    glVertex2f(+1, (pv1.CotaTampa-self.cotaMinima)*self.escalaVertical)
                    glVertex2f(+1, (pv1.CotaTampa-(pv1.AlturaPv)-self.cotaMinima)*self.escalaVertical)
                    glVertex2f(-1, (pv1.CotaTampa-(pv1.AlturaPv)-self.cotaMinima)*self.escalaVertical)
                    glEnd()
                    glPopName()
                    
                    XSnapTop = (self.pos[0]+self.posx*100)
                    YSnapTop = (self.pos[1]+(pv1.CotaTampa-self.cotaMinima)*self.escalaVertical*100)
                    YSnapBottom = (self.pos[1]+(pv1.CotaFundo-self.cotaMinima)*self.escalaVertical*100)
                    self.coordsPV[pv1.numero] = [XSnapTop, YSnapTop, YSnapBottom]
                    self.coordsPVReal[pv1.numero] = [self.posx, pv1.CotaTampa, pv1.CotaFundo]
                    
                    #PV 2
                    glTranslatef(L, 0, 0)
                    glColor3ub(255, 0, 0)
                    glPushName(pv2.numero)
                    glBegin(GL_LINE_LOOP)
                    glVertex2f(-1, (pv2.CotaTampa-self.cotaMinima)*self.escalaVertical)
                    glVertex2f(+1, (pv2.CotaTampa-self.cotaMinima)*self.escalaVertical)
                    glVertex2f(+1, (pv2.CotaTampa-(pv2.AlturaPv)-self.cotaMinima)*self.escalaVertical)
                    glVertex2f(-1, (pv2.CotaTampa-(pv2.AlturaPv)-self.cotaMinima)*self.escalaVertical)
                    glEnd()
                    glPopName()
                    
                    XSnapTop = (self.pos[0]+(self.posx+L)*100)
                    YSnapTop = (self.pos[1]+(pv1.CotaTampa-self.cotaMinima)*self.escalaVertical*100)
                    YSnapBottom = (self.pos[1]+(pv1.CotaFundo-self.cotaMinima)*self.escalaVertical*100)
                    self.coordsPV[pv2.numero] = [XSnapTop, YSnapTop, YSnapBottom]
                    self.coordsPVReal[pv2.numero] = [self.posx+L, pv2.CotaTampa, pv2.CotaFundo]
                
                glPopMatrix()
    
            glPopName()            
            glDisable(GL_LINE_SMOOTH)
            glPopMatrix()            
        except Exception as e:
            if True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
                
    def DesenhaTrechos(self):
        """Desenha as Tubulacoes no Perfil Longitudial, apenas os Tubos
        """
        try:
            self.coordsTRECHOS = {}
            
            glPushMatrix()
            glEnable(GL_LINE_SMOOTH)
            glTranslatef(* self.pos)      
            glScalef(100, 100, 100)
            
            #Desenha POcos de Visitas no Perfil
            
            glLineWidth(1)        
            glPushName(2)
            self.posx = self._posx
            for trecho in self.Trechos:
                pv1 = trecho.PV1
                pv2 = trecho.PV2
                
                L = trecho.L
                D = trecho.D
                
                glPushMatrix()
                glTranslatef(self.posx, 0, 0)            
                
                #TUBULACAO            
                glPushName(trecho.numero)
                x1 = 0
                x2 = L
                y1 = ((trecho.CGII-self.cotaMinima)*self.escalaVertical)
                y2 = ((trecho.CGIF-self.cotaMinima)*self.escalaVertical)
                glColor3ub(255, 255, 0)
                glBegin(GL_LINES)
                glVertex2f(x1, y1)
                glVertex2f(x2, y2)
                glVertex2f(x1, y1+D*self.escalaVertical)
                glVertex2f(x2, y2+D*self.escalaVertical)
                glEnd()
                glPopName()
                
                #TERRENO            
                x1 = 0
                x2 = L
                y1 = ((pv1.CotaTerreno-self.cotaMinima)*self.escalaVertical)
                y2 = ((pv2.CotaTerreno-self.cotaMinima)*self.escalaVertical)
                glColor3ub(0, 255, 0)            
                
                glBegin(GL_LINES)
                glVertex2f(x1, y1)
                glVertex2f(x2, y2)            
                glEnd()
                
                glPopMatrix()
                
                #Necessario para Buscar os Trechos Por coordenadas
                x1 = self.pos[0]+self.posx*100 #Inicio do Trecho
                x2 = self.pos[0]+self.posx*100 #Inicio do Trecho
                x3 = (x1+(L*100)/2) #Meio do Trecho
                x4 = (x1+(L*100)) #Meio do Trecho
                x5 = (x1+(L*100)) #Meio do Trecho
                
                y1 = (self.pos[1]+(trecho.CGSI-self.cotaMinima)*self.escalaVertical*100)
                y2 = (self.pos[1]+(trecho.CGII-self.cotaMinima)*self.escalaVertical*100)
                y3 = (self.pos[1]+(((((trecho.CGII+trecho.CGIF)/2)+(trecho.D/2)-self.cotaMinima)*100)*self.escalaVertical))
                y4 = (self.pos[1]+(trecho.CGSF-self.cotaMinima)*self.escalaVertical*100)
                y5 = (self.pos[1]+(trecho.CGIF-self.cotaMinima)*self.escalaVertical*100)                
                
                self.coordsTRECHOS[trecho.numero] = [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]
                    
                self.posx += L
            
            glPopName()
            
            glDisable(GL_LINE_SMOOTH)
            glPopMatrix()
        except Exception as e:
            if True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
    
    def DesenhaSnapsPVs(self, modelview=None, projection=None, viewport=None, size=None, mode=GL_RENDER):
        """Desenha os Ticks de snaps dos pvs, apenas para visualizacao
           nao para selecao, os para selecao e desenhado em outra funcao"""
        self.posx = self._posx*100         
        
        selecionados_Trechos = self.parent.GetBarrasSelecionadas()
        listaPVdoPerfil = []
        for i in range(len(self.Trechos)):            
            pv1 = self.Trechos[i].PV1
            pv2 = self.Trechos[i].PV2
            if pv1 not in listaPVdoPerfil:
                listaPVdoPerfil.append(pv1)
            if pv2 not in listaPVdoPerfil:
                listaPVdoPerfil.append(pv2)
            
            L = self.Trechos[i].L       
            
     ##########################################################################
     #DESENHA OS TICKS DAS EXTREMIDADES DOS TUBOS QUANDO ESTES ESTIVEREM      #
     #SELECIONADOS.                                                           #
     ##########################################################################            
            if self.Trechos[i].numero in selecionados_Trechos:
                #Tick TOP Tubo INICIO
                XSnapTopInicio = self.pos[0]+(self.posx)
                YSnapTopInicio = self.pos[1]+(((self.Trechos[i].CGSI-self.cotaMinima)*100)*self.escalaVertical)
                
                #Tick BOTTOM Tubo INICIO
                XSnapBottomInicio = self.pos[0]+(self.posx)
                YSnapBottomInicio = self.pos[1]+(((self.Trechos[i].CGII-self.cotaMinima)*100)*self.escalaVertical)
            
                coordenadas = gluProject(XSnapTopInicio, YSnapTopInicio, 0, modelview, projection, viewport)
                xTopInicio, yTopInicio = coordenadas[0], size[1]-coordenadas[1]
                
                coordenadas = gluProject(XSnapBottomInicio, YSnapBottomInicio, 0, modelview, projection, viewport)
                xBottomInicio, yBottomInicio = coordenadas[0], size[1]-coordenadas[1]                
                
                #Desenha Tick TOP INICIO
                glColor3ub(0, 255, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(xTopInicio-5, yTopInicio+8)
                glVertex2f(xTopInicio+5, yTopInicio+8)
                glVertex2f(xTopInicio+0, yTopInicio-15)
                glEnd()
                    
                #Desenha Tick BOTTOM INICIO
                glColor3ub(0, 255, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(xBottomInicio-5, yBottomInicio-8)
                glVertex2f(xBottomInicio+5, yBottomInicio-8)
                glVertex2f(xBottomInicio+0, yBottomInicio+15)
                glEnd()                
                
                #Tick TOP Tubo FINAL
                XSnapTopFinal = self.pos[0]+(self.posx)+(L*100)
                YSnapTopFinal = self.pos[1]+(((self.Trechos[i].CGSF-self.cotaMinima)*100)*self.escalaVertical)
                
                #Tick BOTTOM Tubo INICIO
                XSnapBottomFinal = self.pos[0]+(self.posx)+(L*100)
                YSnapBottomFinal = self.pos[1]+(((self.Trechos[i].CGIF-self.cotaMinima)*100)*self.escalaVertical)
                
                coordenadas = gluProject(XSnapTopFinal, YSnapTopFinal, 0, modelview, projection, viewport)
                xTopFinal, yTopFinal = coordenadas[0], size[1]-coordenadas[1]
                
                coordenadas = gluProject(XSnapBottomFinal, YSnapBottomFinal, 0, modelview, projection, viewport)
                xBottomFinal, yBottomFinal = coordenadas[0], size[1]-coordenadas[1]
                                
                #Desenha Tick TOP FINAL
                glColor3ub(0, 255, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(xTopFinal-5, yTopFinal+8)
                glVertex2f(xTopFinal+5, yTopFinal+8)
                glVertex2f(xTopFinal+0, yTopFinal-15)
                glEnd()
                
                #Desenha Tick BOTTOM FINAL
                glColor3ub(0, 255, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(xBottomFinal-5, yBottomFinal-8)
                glVertex2f(xBottomFinal+5, yBottomFinal-8)
                glVertex2f(xBottomFinal+0, yBottomFinal+15)
                glEnd()                
                
                #Tick MIDDLE Tubo MEIO
                XSnapMiddleMeio = self.pos[0]+(self.posx)+((L/2)*100)
                YSnapMiddleMeio = self.pos[1]+(((((self.Trechos[i].CGII+self.Trechos[i].CGIF)/2)+(self.Trechos[i].D/2)-self.cotaMinima)*100)*self.escalaVertical)
                
                coordenadas = gluProject(XSnapMiddleMeio, YSnapMiddleMeio, 0, modelview, projection, viewport)
                xMiddleMeio, yMiddleMeio = coordenadas[0], size[1]-coordenadas[1]
                
                #Desenha Tick BOTTOM FINAL
                glColor3ub(0, 255, 0)
                glBegin(GL_QUADS)
                glVertex2f(xMiddleMeio-5, yMiddleMeio-5)
                glVertex2f(xMiddleMeio+5, yMiddleMeio-5)
                glVertex2f(xMiddleMeio+5, yMiddleMeio+5)
                glVertex2f(xMiddleMeio-5, yMiddleMeio+5)
                glEnd()                
            
            else:
                pass
            self.posx += L*100
            
     ##########################################################################
     #DESENHA OS TICKS DAS EXTREMIDADES DOS PVS QUANDO ESTES ESTIVEREM        #
     #SELECIONADOS.                                                           #
     ##########################################################################            
        selecionados_PV = self.parent.GetNosSelecionados()
        for pv, posx in self.GetListaPVsDoPerfil():
                                
            if pv.numero in selecionados_PV:
                #Tick TOP
                XSnapTop = self.pos[0]+posx
                YSnapTop = self.pos[1]+(((pv.CotaTampa-self.cotaMinima)*100)*self.escalaVertical)
                
                #Tick BOTTON
                XSnapBottom = self.pos[0]+posx
                YSnapBottom = self.pos[1]+(((pv.CotaFundo-self.cotaMinima)*100)*self.escalaVertical)
                
                coordenadas = gluProject(XSnapTop, YSnapTop, 0, modelview, projection, viewport)
                xTop, yTop = coordenadas[0], size[1]-coordenadas[1]
                
                coordenadas = gluProject(XSnapBottom, YSnapBottom, 0, modelview, projection, viewport)
                xBottom, yBottom = coordenadas[0], size[1]-coordenadas[1]
                
                
                #Desenha Tick TOP
                glColor3ub(0, 255, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(xTop-5, yTop+8)
                glVertex2f(xTop+5, yTop+8)
                glVertex2f(xTop+0, yTop-15)
                glEnd()
                
                #Desenha Tick BOTTOM
                glColor3ub(0, 255, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(xBottom-5, yBottom-8)
                glVertex2f(xBottom+5, yBottom-8)
                glVertex2f(xBottom+0, yBottom+15)
                glEnd()            
                
            
    def DesenhaSnapsSelect(self):
        """Desenhas os Ticks no modo de selecao, para o processo de picking
        """
        try:
            projection = glGetDoublev(GL_PROJECTION_MATRIX)
            viewport = glGetIntegerv(GL_VIEWPORT)
            modelview = glGetDoublev(GL_MODELVIEW_MATRIX)             
            size = [viewport[2], viewport[3]]
            self.posx = self._posx*100            
            
            self.DesenhaSnapPerfilSelect([modelview,projection,viewport, size])
            
            selecionados_PV = self.parent.GetNosSelecionados()
            for pv, posx in self.GetListaPVsDoPerfil():
               if pv.numero in selecionados_PV:
                   glPushMatrix()
                   #Tick TOP
                   XSnapTop = self.pos[0]+posx
                   YSnapTop = self.pos[1]+(((pv.CotaTampa-self.cotaMinima)*100)*self.escalaVertical)
               
                   #Tick BOTTON
                   XSnapBottom = self.pos[0]+posx
                   YSnapBottom = self.pos[1]+(((pv.CotaFundo-self.cotaMinima)*100)*self.escalaVertical)
               
                   coordenadas = gluProject(XSnapTop, YSnapTop, 0, modelview, projection, viewport)
                   xTop, yTop = coordenadas[0], size[1]-coordenadas[1]
               
                   coordenadas = gluProject(XSnapBottom, YSnapBottom, 0, modelview, projection, viewport)
                   xBottom, yBottom = coordenadas[0], size[1]-coordenadas[1]
                   
                   x1Top, y1Top = self.GetCoordMundo(xTop-5, yTop+8)
                   x2Top, y2Top = self.GetCoordMundo(xTop+5, yTop+8)
                   x3Top, y3Top = self.GetCoordMundo(xTop, yTop-15)
                   
                   x1Bottom, y1Bottom = self.GetCoordMundo(xBottom-5, yBottom+8)
                   x2Bottom, y2Bottom = self.GetCoordMundo(xBottom+5, yBottom+8)
                   x3Bottom, y3Bottom = self.GetCoordMundo(xBottom, yBottom-15)
                   
                   #Tick_select TOP
                   glPushName(1)
                   glPushName(pv.numero)
                   glPushName(4)
                   glColor3ub(0, 0, 255)
                   glBegin(GL_TRIANGLES)
                   glVertex2f(x1Top, y1Top)
                   glVertex2f(x2Top, y2Top)
                   glVertex2f(x3Top, y3Top)
                   glEnd()
                   glPopName()
                   glPopName()
                   glPopName()
               
                   #Tick_select BOTTOM
                   glPushName(1)
                   glPushName(pv.numero)
                   glPushName(5)
                   glColor3ub(0, 0, 255)
                   glBegin(GL_TRIANGLES)
                   glVertex2f(x1Bottom, y1Bottom)
                   glVertex2f(x2Bottom, y2Bottom)
                   glVertex2f(x3Bottom, y3Bottom)
                   glEnd()
                   glPopName()
                   glPopName()
                   glPopName()
               
                   glPopMatrix()
               else:
                   pass
            
            selecionados_TUBOS = self.parent.GetBarrasSelecionadas()
            for trecho, pos in self.GetListaTRECHOSDoPerfil():
                 if trecho.numero in selecionados_TUBOS:
                      #Tick TOP
                   XTopInicio = pos[0]
                   YTopInicio = pos[3]
                   XBottomInicio = pos[0]
                   YBottomInicio = pos[4]
                   XMiddleMeio = pos[2]
                   YMiddleMeio = pos[5]
                   XTopFinal = pos[1]
                   YTopFinal = pos[6]
                   XBottomFinal = pos[1]
                   YBottomFinal = pos[7]
              
                   coordenadas = gluProject(XTopInicio, YTopInicio, 0, modelview, projection, viewport)
                   xTopInicio, yTopInicio = coordenadas[0], size[1]-coordenadas[1]
                   
                   coordenadas = gluProject(XBottomInicio, YBottomInicio, 0, modelview, projection, viewport)
                   xBottomInicio, yBottomInicio = coordenadas[0], size[1]-coordenadas[1]
                   
                   coordenadas = gluProject(XMiddleMeio, YMiddleMeio, 0, modelview, projection, viewport)
                   xMiddleMeio, yMiddleMeio = coordenadas[0], size[1]-coordenadas[1]
                   
                   coordenadas = gluProject(XTopFinal, YTopFinal, 0, modelview, projection, viewport)
                   xTopFinal, yTopFinal = coordenadas[0], size[1]-coordenadas[1]
                   
                   coordenadas = gluProject(XBottomFinal, YBottomFinal, 0, modelview, projection, viewport)
                   xBottomFinal, yBottomFinal = coordenadas[0], size[1]-coordenadas[1]
                   
                   x1TopInicio, y1TopInicio = self.GetCoordMundo(xTopInicio-5, yTopInicio-8)
                   x2TopInicio, y2TopInicio = self.GetCoordMundo(xTopInicio+5, yTopInicio-8)
                   x3TopInicio, y3TopInicio = self.GetCoordMundo(xTopInicio, yTopInicio+15)
                   
                   x1BottomInicio, y1BottomInicio = self.GetCoordMundo(xBottomInicio-5, yBottomInicio+8)
                   x2BottomInicio, y2BottomInicio = self.GetCoordMundo(xBottomInicio+5, yBottomInicio+8)
                   x3BottomInicio, y3BottomInicio = self.GetCoordMundo(xBottomInicio, yBottomInicio-15)
                   
                   x1MiddleMeio, y1MiddleMeio = self.GetCoordMundo(xMiddleMeio-5, yMiddleMeio+8)
                   x2MiddleMeio, y2MiddleMeio = self.GetCoordMundo(xMiddleMeio+5, yMiddleMeio+8)
                   x3MiddleMeio, y3MiddleMeio = self.GetCoordMundo(xMiddleMeio, yMiddleMeio-15)
                   
                   x1TopFinal, y1TopFinal = self.GetCoordMundo(xTopFinal-5, yTopFinal+8)
                   x2TopFinal, y2TopFinal = self.GetCoordMundo(xTopFinal+5, yTopFinal+8)
                   x3TopFinal, y3TopFinal = self.GetCoordMundo(xTopFinal, yTopFinal-15)
                   
                   x1BottomFinal, y1BottomFinal = self.GetCoordMundo(xBottomFinal-5, yBottomFinal+8)
                   x2BottomFinal, y2BottomFinal = self.GetCoordMundo(xBottomFinal+5, yBottomFinal+8)
                   x3BottomFinal, y3BottomFinal = self.GetCoordMundo(xBottomFinal, yBottomFinal-15)
                   
                   #Tick_select TOP_INICIO
                   glPushName(2)
                   glPushName(trecho.numero)
                   glPushName(4)
                   glColor3ub(0, 0, 255)
                   glBegin(GL_TRIANGLES)
                   glVertex2f(x1TopInicio, y1TopInicio)
                   glVertex2f(x2TopInicio, y2TopInicio)
                   glVertex2f(x3TopInicio, y3TopInicio)
                   glEnd()
                   glPopName()
                   glPopName()
                   glPopName()
                   
                   #Tick_select BOTTOM_INICIO
                   glPushName(2)
                   glPushName(trecho.numero)
                   glPushName(5)
                   glColor3ub(0, 0, 255)
                   glBegin(GL_TRIANGLES)
                   glVertex2f(x1BottomInicio, y1BottomInicio)
                   glVertex2f(x2BottomInicio, y2BottomInicio)
                   glVertex2f(x3BottomInicio, y3BottomInicio)
                   glEnd()
                   glPopName()
                   glPopName()
                   glPopName()
                   
                   #Tick_select MIDDLE_MEIO
                   glPushName(2)
                   glPushName(trecho.numero)
                   glPushName(6)
                   glColor3ub(0, 0, 255)
                   glBegin(GL_TRIANGLES)
                   glVertex2f(x1MiddleMeio, y1MiddleMeio)
                   glVertex2f(x2MiddleMeio, y2MiddleMeio)
                   glVertex2f(x3MiddleMeio, y3MiddleMeio)
                   glEnd()
                   glPopName()
                   glPopName()
                   glPopName()
                   
                   #Tick_select TOP_FINAL
                   glPushName(2)
                   glPushName(trecho.numero)
                   glPushName(7)
                   glColor3ub(0, 0, 255)
                   glBegin(GL_TRIANGLES)
                   glVertex2f(x1TopFinal, y1TopFinal)
                   glVertex2f(x2TopFinal, y2TopFinal)
                   glVertex2f(x3TopFinal, y3TopFinal)
                   glEnd()
                   glPopName()
                   glPopName()
                   glPopName()
                   
                   #Tick_select BOTTOM_FINAL
                   glPushName(2)
                   glPushName(trecho.numero)
                   glPushName(8)
                   glColor3ub(0, 0, 255)
                   glBegin(GL_TRIANGLES)
                   glVertex2f(x1BottomFinal, y1BottomFinal)
                   glVertex2f(x2BottomFinal, y2BottomFinal)
                   glVertex2f(x3BottomFinal, y3BottomFinal)
                   glEnd()
                   glPopName()
                   glPopName()
                   glPopName()
                   
                
                   
        except Exception as e:            
            if True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
    
    def TickAlteraCotaTampa(self, pv, x_tela, y_tela):
        """Altera a COTA DA TAMPA quando o tick for arrastado
        
            pv = objeto (tipo pv)
            x = coordenada x da (tela)
            y = coordenada y da (tela)
        
        """
        glPushMatrix()
        glLoadIdentity()
        x, y = self.GetCoordMundo(x_tela, y_tela)
        glPopMatrix()
        
        altura = self.GetAlturaNoPerfil(y)        
        pv.SetCotaTampa(altura)
        
    def TickAlteraCotaFundo(self, pv, x_tela, y_tela):
        """Altera a COTA DO FUNDO quando o tick for arrastado
        
            pv = objeto (tipo pv)
            x = coordenada x da (tela)
            y = coordenada y da (tela)
        
        """
        glPushMatrix()
        glLoadIdentity()
        x, y = self.GetCoordMundo(x_tela, y_tela)
        glPopMatrix()
        
        altura = self.GetAlturaNoPerfil(y)        
        pv.SetCotaFundo(altura)
        
    def TickAlteraCGSI(self, trecho, x_tela, y_tela):
        """Altera a COTA DA GERATRIZ SUPERIOR DO INICIO do trecho quando o tick
           for arrastado.
        
            trecho = objeto (TrechoRede)
            x = coordenada x da (tela)
            y = coordenada y da (tela)
        
        """
        glPushMatrix()
        glLoadIdentity()
        x, y = self.GetCoordMundo(x_tela, y_tela)
        glPopMatrix()
        
        altura = self.GetAlturaNoPerfil(y)        
        trecho.SetCGSI(altura)
        
    def TickAlteraCGSF(self, trecho, x_tela, y_tela):
        """Altera a COTA DA GERATRIZ SUPERIOR DO FINAL do trecho quando o tick
           for arrastado.
        
            trecho = objeto (TrechoRede)
            x = coordenada x da (tela)
            y = coordenada y da (tela)
        
        """
        glPushMatrix()
        glLoadIdentity()
        x, y = self.GetCoordMundo(x_tela, y_tela)
        glPopMatrix()
        
        altura = self.GetAlturaNoPerfil(y)        
        trecho.SetCGSF(altura)
        
    def TickAlteraCGIF(self, trecho, x_tela, y_tela):
        """Altera a COTA DA GERATRIZ INFERIOR DO FINAL do trecho quando o tick
           for arrastado.
        
            trecho = objeto (TrechoRede)
            x = coordenada x da (tela)
            y = coordenada y da (tela)
        
        """
        glPushMatrix()
        glLoadIdentity()
        x, y = self.GetCoordMundo(x_tela, y_tela)
        glPopMatrix()
        
        altura = self.GetAlturaNoPerfil(y)        
        trecho.SetCGIF(altura)
        
    def TickAlteraCGII(self, trecho, x_tela, y_tela):
        """Altera a COTA DA GERATRIZ INFERIOR DO INICIO do trecho quando o tick
           for arrastado.
        
            trecho = objeto (TrechoRede)
            x = coordenada x da (tela)
            y = coordenada y da (tela)
        
        """
        glPushMatrix()
        glLoadIdentity()
        x, y = self.GetCoordMundo(x_tela, y_tela)
        glPopMatrix()
        
        altura = self.GetAlturaNoPerfil(y)        
        trecho.SetCGII(altura)
        
    def TickAlteraCMIDDLE(self, trecho, x_tela, y_tela):
        """Altera a COTA GERAL DO TUBO  do trecho quando o tick
           for arrastado.
        
            trecho = objeto (TrechoRede)
            x = coordenada x da (tela)
            y = coordenada y da (tela)
        
        """
        glPushMatrix()
        glLoadIdentity()
        x, y = self.GetCoordMundo(x_tela, y_tela)
        glPopMatrix()
        
        altura = self.GetAlturaNoPerfil(y)
        trecho.SetCMEIO(altura)
    
    def GetAlturaNoPerfil(self, y):
        if y < self.pos[1]: # Ponto fora do Perfil - abaixo do Perfil
            return None
        elif y > (self.pos[1] + (self.AlturaPerfil*self.escalaVertical))*100:
            return None
        else:
            return ((y - self.pos[1])/(self.escalaVertical*100))+self.cotaMinima
            
    def DesenhaTickMouse(self, mouseX, MouseY, model,  modelview=None, projection=None, viewport=None, size=None, mode=GL_RENDER):
        """Desenha o Tick na tela quando este estiver sendo arrastado pelo
           movimento do mouse na tela. 
        """
        try:            
            if model.Estrututura.PV.PVTick_top != False:
    
                numPV = model.Estrututura.PV.PVTick_top
                _x = self.coordsPV[numPV][0]
                _y = self.coordsPV[numPV][1]
    
                coordenadas = gluProject(_x, _y, 0, modelview, projection, viewport)
                x, y = coordenadas[0], size[1]-coordenadas[1]
    
                glColor3ub(200, 150, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(x-5, MouseY+8)
                glVertex2f(x+5, MouseY+8)
                glVertex2f(x, MouseY-15)
                glEnd()
                
            elif model.Estrututura.PV.PVTick_bottom != False:
    
                numPV = model.Estrututura.PV.PVTick_bottom
                _x = self.coordsPV[numPV][0]
                _y = self.coordsPV[numPV][1]
    
                coordenadas = gluProject(_x, _y, 0, modelview, projection, viewport)
                x, y = coordenadas[0], size[1]-coordenadas[1]
    
                glColor3ub(200, 150, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(x-5, MouseY-8)
                glVertex2f(x+5, MouseY-8)
                glVertex2f(x, MouseY+15)
                glEnd()
                
            elif model.Estrututura.TRECHO.TUBOTick_inicio_top != False:
                numTRECHO = model.Estrututura.TRECHO.TUBOTick_inicio_top
                _x = self.coordsTRECHOS[numTRECHO][0]
                _y = self.coordsTRECHOS[numTRECHO][1]
    
                coordenadas = gluProject(_x, _y, 0, modelview, projection, viewport)
                x, y = coordenadas[0], size[1]-coordenadas[1]
    
                glColor3ub(200, 150, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(x-5, MouseY+8)
                glVertex2f(x+5, MouseY+8)
                glVertex2f(x, MouseY-15)
                glEnd()
                
            elif model.Estrututura.TRECHO.TUBOTick_inicio_bottom != False:
                numTRECHO = model.Estrututura.TRECHO.TUBOTick_inicio_bottom

                _x = self.coordsTRECHOS[numTRECHO][2]
                _y = self.coordsTRECHOS[numTRECHO][3]
                
                coordenadas = gluProject(_x, _y, 0, modelview, projection, viewport)
                x, y = coordenadas[0], size[1]-coordenadas[1]
    
                glColor3ub(200, 150, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(x-5, MouseY-8)
                glVertex2f(x+5, MouseY-8)
                glVertex2f(x, MouseY+15)
                glEnd()
                
            elif model.Estrututura.TRECHO.TUBOTick_middle != False:
                numTRECHO = model.Estrututura.TRECHO.TUBOTick_middle

                _x = self.coordsTRECHOS[numTRECHO][4]
                _y = self.coordsTRECHOS[numTRECHO][5]
                
                coordenadas = gluProject(_x, _y, 0, modelview, projection, viewport)
                x, y = coordenadas[0], size[1]-coordenadas[1]
    
                glColor3ub(200, 150, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(x-5, MouseY-8)
                glVertex2f(x+5, MouseY-8)
                glVertex2f(x, MouseY+15)
                glEnd()
                
            elif model.Estrututura.TRECHO.TUBOTick_final_top != False:
                numTRECHO = model.Estrututura.TRECHO.TUBOTick_final_top

                _x = self.coordsTRECHOS[numTRECHO][6]
                _y = self.coordsTRECHOS[numTRECHO][7]
                
                coordenadas = gluProject(_x, _y, 0, modelview, projection, viewport)
                x, y = coordenadas[0], size[1]-coordenadas[1]
    
                glColor3ub(200, 150, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(x-5, MouseY+8)
                glVertex2f(x+5, MouseY+8)
                glVertex2f(x, MouseY-15)
                glEnd()
                
            elif model.Estrututura.TRECHO.TUBOTick_final_bottom != False:
                numTRECHO = model.Estrututura.TRECHO.TUBOTick_final_bottom

                _x = self.coordsTRECHOS[numTRECHO][8]
                _y = self.coordsTRECHOS[numTRECHO][9]
                
                coordenadas = gluProject(_x, _y, 0, modelview, projection, viewport)
                x, y = coordenadas[0], size[1]-coordenadas[1]
    
                glColor3ub(200, 150, 0)
                glBegin(GL_TRIANGLES)
                glVertex2f(x-5, MouseY-8)
                glVertex2f(x+5, MouseY-8)
                glVertex2f(x, MouseY+15)
                glEnd()
                
        except Exception as e:
             if True:
                 exc_type, exc_obj, exc_tb = sys.exc_info()
                 fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                 print(exc_type, fname, exc_tb.tb_lineno)
                 print (e)                

    def GetListCoordsRealPVs(self):
        try:
            self.coordsPV = {}
            
            self.posx = self._posx        

            for i in range(len(self.Trechos)):            
                pv1 = self.Trechos[i].PV1
                pv2 = self.Trechos[i].PV2
                
                L = self.Trechos[i].L
                
                
                if i != (len(self.Trechos)-1):
                    #PV 1
                    XSnapTop = (self.pos[0]+self.posx*100)
                    YSnapTop = (self.pos[1]+(pv1.CotaTampa-self.cotaMinima)*self.escalaVertical*100)
                    YSnapBottom = (self.pos[1]+(pv1.CotaFundo-self.cotaMinima)*self.escalaVertical*100)
                    self.coordsPV[pv1.numero] = [XSnapTop, YSnapTop, YSnapBottom]
                    self.coordsPVReal[pv1.numero] = [self.posx, pv1.CotaTampa, pv1.CotaFundo]
                    self.posx += L 
                else:
                    #PV 1
                    XSnapTop = (self.pos[0]+self.posx*100)
                    YSnapTop = (self.pos[1]+(pv1.CotaTampa-self.cotaMinima)*self.escalaVertical*100)
                    YSnapBottom = (self.pos[1]+(pv1.CotaFundo-self.cotaMinima)*self.escalaVertical*100)
                    self.coordsPV[pv1.numero] = [XSnapTop, YSnapTop, YSnapBottom]
                    self.coordsPVReal[pv1.numero] = [self.posx, pv1.CotaTampa, pv1.CotaFundo]
                    
                    #PV 2
                    XSnapTop = (self.pos[0]+(self.posx+L)*100)
                    YSnapTop = (self.pos[1]+(pv1.CotaTampa-self.cotaMinima)*self.escalaVertical*100)
                    YSnapBottom = (self.pos[1]+(pv1.CotaFundo-self.cotaMinima)*self.escalaVertical*100)
                    self.coordsPV[pv2.numero] = [XSnapTop, YSnapTop, YSnapBottom]
                    self.coordsPVReal[pv2.numero] = [self.posx+L, pv2.CotaTampa, pv2.CotaFundo]
        except Exception as e:
            if True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
                
    def GetListCoordsTRECHOS(self):
        try:
            self.coordsTRECHOS = {}
            self.posx = self._posx
            for trecho in self.Trechos:
                pv1 = trecho.PV1
                pv2 = trecho.PV2
                
                L = trecho.L
                D = trecho.D
                
                #TUBULACAO            
                x1 = 0
                x2 = L
                y1 = ((trecho.CGII-self.cotaMinima)*self.escalaVertical)
                y2 = ((trecho.CGIF-self.cotaMinima)*self.escalaVertical)
                
                #TERRENO            
                x1 = 0
                x2 = L
                y1 = ((pv1.CotaTerreno-self.cotaMinima)*self.escalaVertical)
                y2 = ((pv2.CotaTerreno-self.cotaMinima)*self.escalaVertical)
                
                #Necessario para Buscar os Trechos Por coordenadas
                x1 = self.pos[0]+self.posx*100 #Inicio do Trecho
                x2 = self.pos[0]+self.posx*100 #Inicio do Trecho
                x3 = (x1+(L*100)/2) #Meio do Trecho
                x4 = (x1+(L*100)) #Meio do Trecho
                x5 = (x1+(L*100)) #Meio do Trecho
                
                y1 = (self.pos[1]+(trecho.CGSI-self.cotaMinima)*self.escalaVertical*100)
                y2 = (self.pos[1]+(trecho.CGII-self.cotaMinima)*self.escalaVertical*100)
                y3 = (self.pos[1]+(((((trecho.CGII+trecho.CGIF)/2)+(trecho.D/2)-self.cotaMinima)*100)*self.escalaVertical))
                y4 = (self.pos[1]+(trecho.CGSF-self.cotaMinima)*self.escalaVertical*100)
                y5 = (self.pos[1]+(trecho.CGIF-self.cotaMinima)*self.escalaVertical*100)                
                
                self.coordsTRECHOS[trecho.numero] = [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]
                    
                self.posx += L
            
        except Exception as e:
            if True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
    
    def GetListaPVsDoPerfil(self):
        """Retorna lista de lista com pares [PV, posX]
        
           PV -> Objeto tipo PV
           posX -> Posicao x do PV no perfil longitudinal, ja como as escalas
                   do perfil aplicada.
        """
        self.posx = self._posx*100
        _posx = self.posx 
        listaPVdoPerfil = []
        listaNumPvs = []
        
        for i in range(len(self.Trechos)):
            
            pv1 = self.Trechos[i].PV1
            
            pv2 = self.Trechos[i].PV2
            
            if pv1.numero not in listaNumPvs:
                listaNumPvs.append(pv1.numero)
                listaPVdoPerfil.append([pv1, _posx])
                
            if pv2.numero not in listaNumPvs:
                listaNumPvs.append(pv2.numero)
                listaPVdoPerfil.append([pv2, (_posx+self.Trechos[i].L*100)])
            
            _posx += (self.Trechos[i].L*100)
        
        return listaPVdoPerfil
        
    def GetListaTRECHOSDoPerfil(self):
        """Retorna lista de lista com pares [TRECHO, posX]
        
           TRECHO -> Objeto tipo TrechoRede
           posX -> Posicao x do TRECHO no perfil longitudinal, ja como as
                   escalas do perfil aplicada.
        """
        self.posx = self._posx*100
        _posx = self.posx 
        listaTRECHOSdoPerfil = []
        listaPosTrechos = []
        
        for trecho in self.Trechos:            
            if trecho not in listaTRECHOSdoPerfil:                
                xInicio = self.pos[0]+(_posx)
                xFinal = self.pos[0]+(_posx)+(trecho.L*100)
                xMeio = self.pos[0]+(_posx)+((trecho.L/2)*100)
                yTopInicio = self.pos[1]+(((trecho.CGSI-self.cotaMinima)*100)*self.escalaVertical)
                yBottomInicio = self.pos[1]+(((trecho.CGII-self.cotaMinima)*100)*self.escalaVertical)
                yMiddle = self.pos[1]+(((((trecho.CGII+trecho.CGIF)/2)+(trecho.D/2)-self.cotaMinima)*100)*self.escalaVertical)
                yTopFinal = self.pos[1]+(((trecho.CGSF-self.cotaMinima)*100)*self.escalaVertical)
                yBottomFinal = self.pos[1]+(((trecho.CGIF-self.cotaMinima)*100)*self.escalaVertical)
                
                listaTRECHOSdoPerfil.append(trecho)
                listaPosTrechos.append([xInicio, xFinal, xMeio, yTopInicio, yBottomInicio,yMiddle, yTopFinal, yBottomFinal])
                
            _posx += (trecho.L*100)
        
        return zip(listaTRECHOSdoPerfil, listaPosTrechos)
        
        
        
    def GetPosElemTick(self, ELEMTO):
        """Retorna a posicao [x, y] do tick do elemento passado para a funcao
           
           ELEMENT -> int (numPV)
           TICK -> int (tipoTick (opcoes-> 4 TOP, 5 BOTTOM))
        """
        #PV
        if ELEMTO[2] == 1: #Trata-se de PV
            if ELEMTO[4] == 4:
                return [self.coordsPV[ELEMTO[3]][0], self.coordsPV[ELEMTO[3]][1]]
            elif ELEMTO[4] == 5:
                return [self.coordsPV[ELEMTO[3]][0], self.coordsPV[ELEMTO[3]][2]]
        #TRECHOS
        elif ELEMTO[2] == 2: #Trata-se de TRECHO
            if ELEMTO[4] == 4:# TICK_TOP_INICIO
                return [self.coordsTRECHOS[ELEMTO[3]][0], self.coordsTRECHOS[ELEMTO[3]][1]]
            elif ELEMTO[4] == 5:# TICK_TOP_INICIO
                return [self.coordsTRECHOS[ELEMTO[3]][2], self.coordsTRECHOS[ELEMTO[3]][3]]
            elif ELEMTO[4] == 6:# TICK_TOP_INICIO
                return [self.coordsTRECHOS[ELEMTO[3]][4], self.coordsTRECHOS[ELEMTO[3]][5]]
            elif ELEMTO[4] == 7:# TICK_TOP_INICIO
                return [self.coordsTRECHOS[ELEMTO[3]][6], self.coordsTRECHOS[ELEMTO[3]][7]]
            elif ELEMTO[4] == 8:# TICK_TOP_INICIO
                return [self.coordsTRECHOS[ELEMTO[3]][8], self.coordsTRECHOS[ELEMTO[3]][9]]
    
    def DesenhaStrokText(self, palavra, escala=1):
        glPushMatrix()
        glPointSize(1)
        glScalef(0.1, 0.1, 0.1)
        glScalef(escala, escala, escala)
        for letra in palavra:
            #print ("letra = %s  --> Tipo = %s" %(letra, type(letra)))
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(letra))
        glPopMatrix()

class EstruturaBand:
    def __init__(self, perfil, titulo=[]):
        self.tipo = "ESTRUTURA"
        self.POS_ANCHORS = ["LEFT_TOP","LEFT_MIDLE","LEFT_BOTTOM",
                            "MIDLE_TOP", "MIDLE_MIDLE", "MIDLE_BOTTOM",
                            "RIGHT_TOP", "RIGHT_MIDLE", "RIGHT_BOTTOM"]
        self.perfil = perfil
        self.titulo_band = titulo
        self.height = 20
        self.width_title = 100
        self.scale_title = 1.0
        self.anchorPosBands = "BOTTOM"
        self.anchorPosTitleBand = "MIDLE_MIDLE"
        self.titleColor = [1.0, 0.5, 0.5]
        self.tipoDadosBand = "OTHER"
    
    def GetDadosBand(self):                
        if self.tipoDadosBand == "NUM_PV":
            labels = [(x[0].nomePV+"-"+str(x[0].numero)) for x in self.perfil.GetListaPVsDoPerfil()]        
        elif self.tipoDadosBand == "COTA_TERRENO":
            labels = [truncaNumero(x[0].CotaTerreno, 2).replace(".",",") for x in self.perfil.GetListaPVsDoPerfil()]
        elif self.tipoDadosBand == "COTA_TAMPA":
            labels = [truncaNumero(x[0].CotaTampa, 2).replace(".",",") for x in self.perfil.GetListaPVsDoPerfil()]
        elif self.tipoDadosBand == "COTA_FUNDO":
            labels = [truncaNumero(x[0].CotaFundo, 2).replace(".",",") for x in self.perfil.GetListaPVsDoPerfil()]
        elif self.tipoDadosBand == "PROFUNDIDADE":
            labels = [truncaNumero(x[0].AlturaPv, 2).replace(".",",") for x in self.perfil.GetListaPVsDoPerfil()]
        elif self.tipoDadosBand == "DEGRAU":            
            trechos = [x[0] for x in self.perfil.GetListaTRECHOSDoPerfil()]
            LabelsAux = trechos[0].GetListaDregraus(trechos)
            labels = [truncaNumero(x, 2).replace(".",",") if x != 0.00 else "-" for x in LabelsAux]       
        elif self.tipoDadosBand == "OTHER":
            labels = [str(x) for x in range(len(self.perfil.GetListaPVsDoPerfil()))]
        
        coords = [x[0] for x in self.perfil.coordsPVReal.values()]
        return zip(labels, coords)
        
    def Desenha(self, perfil):
        #Desenha retangulo dos valores da band        
        try:
            self.DesenhaRetanguloValores(perfil)
            self.DesenhaRetanguloTitulo(perfil)
            self.DesenhaTextoPerfil()
            self.DesenhaValoresBand(perfil)
            self.DesenhaTextosValoresBand()
        except Exception as e:
             if True:
                 exc_type, exc_obj, exc_tb = sys.exc_info()
                 fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                 print(exc_type, fname, exc_tb.tb_lineno)
                 print (e)
    
        
    
    def DesenhaRetanguloValores(self, perfil):
        """Desenha o retangulo dos valores da Band abaixo do Perfil
        """
        glBegin(GL_LINE_LOOP)
        glVertex2f(0, 0)
        glVertex2f(perfil.Comprimento, 0)
        glVertex2f(perfil.Comprimento, self.height)
        glVertex2f(0, self.height)
        glEnd()
    
    def DesenhaRetanguloTitulo(self, perfil):
        """Desenha o retangulo do titulo abaixo do Perfil
        """
        glBegin(GL_LINE_LOOP)
        glVertex2f(0, 0)
        glVertex2f(-self.width_title, 0)
        glVertex2f(-self.width_title, self.height)
        glVertex2f(0, self.height)
        glEnd()
    
    def DesenhaValoresBand(self, perfil):        
        #TICK vertical dentro do retangulo de valores da BandaData        
        pass
#        for num, coord in perfil.coordsPVReal.items():            
#            glPushMatrix()
#            glTranslatef(coord[0], 0, 0)
#            glBegin(GL_LINES)
#            glVertex2f(0, 0)
#            glVertex2f(0, self.height)
#            glEnd()
#            glPopMatrix()
    
    def DesenhaTextoPerfil(self):
        try:
            glPushMatrix()            
            glTranslatef(self.GetAnchorTitleBand()[0], self.GetAnchorTitleBand()[1], 0)
            texto = TextOpenGL(self.titulo_band, 0.05, "MIDLE_MIDLE")
            texto.SetTitleColor(*self.titleColor)
            #texto.SetTextAngle(45)
            texto.Desenha()    
            glPopMatrix()
            
        except Exception as e:
             if True:
                 exc_type, exc_obj, exc_tb = sys.exc_info()
                 fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                 print(exc_type, fname, exc_tb.tb_lineno)
                 print (e)
    
    def DesenhaTextosValoresBand(self):
#            #for num, coord in perfil.coordsPVReal.items():
#            for num, coord in self.GetDadosBand():
#                #Cota da Tampa
#                glPushMatrix()
#                glTranslatef(coord, 0, 0)
#                #glRotatef(90, 0, 0, 1)
#                glPointSize(1)
#                glScalef(0.1, 0.1, 0.1)
#                glScalef(0.50, 0.50, 0.50)                
#                for letra in num:
#                    glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(letra))
#                glPopMatrix()
                
#                #Cota do Fundo
#                glPushMatrix()
#                glTranslatef(coord[0]+6, 0, 0)
#                glRotatef(90, 0, 0, 1)
#                glPointSize(1)
#                glScalef(0.1, 0.1, 0.1)
#                glScalef(0.50, 0.50, 0.50)                
#                for letra in truncaNumero(coord[2], 2):
#                    glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(letra))
#                glPopMatrix()
            glPushMatrix()
            anchors = self.GetAnchorPosBands()              
            for num, valor in enumerate(self.GetDadosBand()):
                glPushMatrix()
                glTranslatef(0, anchors[0][1], 0)
                glTranslatef(anchors[num][0], 0 , 0)
                texto = TextOpenGL(valor[0], 0.05, "MIDLE_MIDLE")
                texto.Desenha()
                glPopMatrix()
            glPopMatrix()
            
    
    def SetHeighBand(self, newHeight):
        self.height = newHeight
               
    def SetScaleTitleText(self, newScale):
        self.scale_title = newScale
    
    def GetAnchorTitleBand(self):
        if self.anchorPosTitleBand == "LEFT_TOP":
            x0 = -(self.width_title)
            y0 =  (self.height)
        elif self.anchorPosTitleBand == "LEFT_MIDLE":
            x0 = -(self.width_title)
            y0 =  (self.height/2)
            
        elif self.anchorPosTitleBand == "LEFT_BOTTOM":
            x0 = -(self.width_title)
            y0 = 0.0
            
        elif self.anchorPosTitleBand == "MIDLE_TOP":
            x0 = -(self.width_title/2)
            y0 = (self.height)
            
        elif self.anchorPosTitleBand == "MIDLE_MIDLE":
            x0 = -(self.width_title/2)
            y0 = (self.height/2)
            
        elif self.anchorPosTitleBand == "MIDLE_BOTTOM":
            x0 = -(self.width_title/2)
            y0 = 0.0
            
        elif self.anchorPosTitleBand == "RIGHT_TOP":
            x0 = 0.0
            y0 = (self.height)
            
        elif self.anchorPosTitleBand == "RIGHT_MIDLE":
            x0 = 0.0
            y0 = (self.height/2)
            
        elif self.anchorPosTitleBand == "RIGHT_BOTTOM":
            x0 = 0.0
            y0 = 0.0
        
        else:
            raise Exception

        return (x0, y0)
    
    def GetAnchorPosBands(self):
        """Retorna Lista com as posicoes das bands dos PVS dentro do
           perfil longitudinal.
        """
        posicoes = [x[0] for x in self.perfil.coordsPVReal.values()]
        
        
        posTop = self.height      
        posMidle = (self.height/2)    
        posBottom = 0
        
        if self.anchorPosBands == "TOP":
            return [[x, posTop] for x in posicoes]
        elif self.anchorPosBands == "MIDLE":
            return [[x, posMidle] for x in posicoes]  
        elif self.anchorPosBands == "BOTTOM":
            return [[x, posBottom] for x in posicoes]        
    
    def DesenhaStrokText(self, palavra):        
        for letra in palavra:
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(letra))
        
class TrechoBand:
    def __init__(self, perfil, titulo=[]):
        self.tipo = "TRECHO"
        self.POS_ANCHORS = ["LEFT_TOP","LEFT_MIDLE","LEFT_BOTTOM",
                            "MIDLE_TOP", "MIDLE_MIDLE", "MIDLE_BOTTOM",
                            "RIGHT_TOP", "RIGHT_MIDLE", "RIGHT_BOTTOM"]
        
        self.perfil = perfil
        self.titulo_band = titulo
        self.height = 20
        self.width_title = 100
        self.scale_title = 1.0
        self.anchorPosBands = "MIDLE_MIDLE"
        self.anchorPosTitleBand = "MIDLE_MIDLE"
        self.titleColor = [1.0, 0.5, 0.5]
        self.tipoDadosBand = "OTHER"
    
    def GetDadosBand(self): 
        try:
            if self.tipoDadosBand == "NUM_TRECHO":
                labels = [(x[0].nomePV+"-"+str(x[0].numero)) for x in self.perfil.GetListaTRECHOSDoPerfil()]        
            elif self.tipoDadosBand == "COMPRIMENTO":
                labels = [truncaNumero(x[0].L, 2).replace(".",",") for x in self.perfil.GetListaTRECHOSDoPerfil()]
            elif self.tipoDadosBand == "DIAMETRO":
                labels = [x[0].GetTextoDiamentro() for x in self.perfil.GetListaTRECHOSDoPerfil()]
            elif self.tipoDadosBand == "DECLIVIDADE":
                labels = [truncaNumero(x[0].Iadotada, 6)+"m/m" for x in self.perfil.GetListaTRECHOSDoPerfil()]                      
            elif self.tipoDadosBand == "OTHER":
                labels = [str(x) for x in range(len(list(self.perfil.GetListaTRECHOSDoPerfil())))]
                        
            coords = [x[0] for x in self.perfil.coordsTRECHOS.values()]
            return zip(labels, coords)
        except Exception as e:
             if True:
                 exc_type, exc_obj, exc_tb = sys.exc_info()
                 fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                 print(exc_type, fname, exc_tb.tb_lineno)
                 print (e)
    
    def Desenha(self, perfil):
        #Desenha retangulo dos valores da band        
        try:
            self.DesenhaRetanguloValores(perfil)
            self.DesenhaRetanguloTitulo(perfil)
            self.DesenhaTextoPerfil()
            self.DesenhaValoresBand(perfil)
            self.DesenhaTextosValoresBand()
        except Exception as e:
             if True:
                 exc_type, exc_obj, exc_tb = sys.exc_info()
                 fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                 print(exc_type, fname, exc_tb.tb_lineno)
                 print (e)
    
        
    
    def DesenhaRetanguloValores(self, perfil):
        """Desenha o retangulo dos valores da Band abaixo do Perfil
        """
        glBegin(GL_LINE_LOOP)
        glVertex2f(0, 0)
        glVertex2f(perfil.Comprimento, 0)
        glVertex2f(perfil.Comprimento, self.height)
        glVertex2f(0, self.height)
        glEnd()
    
    def DesenhaRetanguloTitulo(self, perfil):
        """Desenha o retangulo do titulo abaixo do Perfil
        """
        glBegin(GL_LINE_LOOP)
        glVertex2f(0, 0)
        glVertex2f(-self.width_title, 0)
        glVertex2f(-self.width_title, self.height)
        glVertex2f(0, self.height)
        glEnd()
    
    def DesenhaValoresBand(self, perfil):        
        #TICK vertical dentro do retangulo de valores da BandaData        
        for num, coord in perfil.coordsPVReal.items():            
            glPushMatrix()
            glTranslatef(coord[0], 0, 0)
            glBegin(GL_LINES)
            glVertex2f(0, 0)
            glVertex2f(0, self.height)
            glEnd()
            glPopMatrix()
    
    def DesenhaTextoPerfil(self):
        try:
#            textoTitulo = self.titulo_band
#            glPushMatrix()
#            for texto in textoTitulo:            
#                glPushMatrix()
#                glTranslatef(-self.width_title, 0, 0)
#                glScalef(self.scale_title, self.scale_title, self.scale_title)
#                self.DesenhaStrokText(texto)
#                glPopMatrix()                
#                glTranslate(0.0, -10, 0.0)
#            glPopMatrix()
            
            
            glPushMatrix()            
            glTranslatef(self.GetAnchorTitleBand()[0], self.GetAnchorTitleBand()[1], 0)
            texto = TextOpenGL(self.titulo_band, 0.05, "MIDLE_MIDLE")
            texto.SetTitleColor(*self.titleColor)
            #texto.SetTextAngle(45)
            texto.Desenha()    
            glPopMatrix()
        except Exception as e:
             if True:
                 exc_type, exc_obj, exc_tb = sys.exc_info()
                 fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                 print(exc_type, fname, exc_tb.tb_lineno)
                 print (e)
    
    def DesenhaTextosValoresBand(self):
        try:
            glPushMatrix()
            anchors = self.GetAnchorPosBands()
            glTranslatef(0, anchors[0][1], 0)
            for num, valor in enumerate(self.GetDadosBand()):            
                glPushMatrix()
                glTranslatef(anchors[num][0], 0, 0)            
                texto = TextOpenGL(valor[0], 0.05, "MIDLE_MIDLE")
                #texto.SetTextAngle(45.0)
                texto.Desenha()
                glPopMatrix()
            glPopMatrix()
        except Exception as e:
             if True:
                 exc_type, exc_obj, exc_tb = sys.exc_info()
                 fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                 print(exc_type, fname, exc_tb.tb_lineno)
                 print (e)
    
    def SetHeighBand(self, newHeight):
        self.height = newHeight
        
    def SetScaleTitleText(self, newScale):
        self.scale_title = newScale
        
    def SetAnchorPos(self, flag_anchorPos):
        if (type(flag_anchorPos) == str and flag_anchorPos.upper() in \
                                                            self.POS_ANCHORS):
            self.anchorPosBands = flag_anchorPos.upper()
        else:
            raise Exception
    
    def GetAnchorPos(self):
        if self.anchorPosBands == "LEFT_TOP":
            return self.GetLeftTopPos()
        elif self.anchorPosBands == "LEFT_MIDLE":
            return self.GetLeftMidlePos()
        elif self.anchorPosBands == "LEFT_BOTTOM":
            return self.GetLeftBottomPos()
        elif self.anchorPosBands == "MIDLE_TOP":
            return self.GetMidleTopPos()
        elif self.anchorPosBands == "MIDLE_MIDLE":
            return self.GetMidleMidlePos()
        elif self.anchorPosBands == "MIDLE_BOTTOM":
            return self.GetMidleBottomPos()
        elif self.anchorPosBands == "RIGHT_TOP":
            return self.GetRightTopPos()
        elif self.anchorPosBands == "RIGHT_MIDLE":
            return self.GetRightMidlePos()
        elif self.anchorPosBands == "RIGHT_BOTTOM":
            return self.GetRightBottomPos()
        else:
            raise Exception
            
    def GetAnchorPosBands(self):
        """Retorna Lista com as posicoes das bands dos trechos dentro do
           perfil longitudinal.
        """
        posInicio = []
        posMeio = []
        posFinal = []        
        
        posInicio.append(self.perfil._posx)        
        posMeio.append((posInicio[0]+self.perfil.Trechos[0].L/2))     
        posFinal.append((posInicio[0]+self.perfil.Trechos[0].L))     
        
        posTop = self.height      
        posMidle = (self.height/2)    
        posBottom = 0
        
        for num, trecho in enumerate(self.perfil.Trechos[:-1]):
            #Posicao Inicio
            posIni = posInicio[-1]+trecho.L
            posInicio.append(posIni)
            
            #Posicao Meio
            posMei = posIni+(self.perfil.Trechos[num+1].L/2)
            posMeio.append(posMei)
            
            #Posicao Final
            posFin = posIni+(self.perfil.Trechos[num+1].L)
            posFinal.append(posFin)
        
        if self.anchorPosBands == "LEFT_TOP":
            return [[x, posTop] for x in posInicio]
        elif self.anchorPosBands == "LEFT_MIDLE":
            return [[x, posMidle] for x in posInicio]  
        elif self.anchorPosBands == "LEFT_BOTTOM":
            return [[x, posBottom] for x in posInicio]
        elif self.anchorPosBands == "MIDLE_TOP":
            return [[x, posTop] for x in posMeio]   
        elif self.anchorPosBands == "MIDLE_MIDLE":
            return [[x, posMidle] for x in posMeio]
        elif self.anchorPosBands == "MIDLE_BOTTOM":
            return [[x, posBottom] for x in posMeio]
        elif self.anchorPosBands == "RIGHT_TOP":
            return [[x, posTop] for x in posFinal]    
        elif self.anchorPosBands == "RIGHT_MIDLE":
            return [[x, posMidle] for x in posFinal]
        elif self.anchorPosBands == "RIGHT_BOTTOM":
            return [[x, posBottom] for x in posFinal]  
    
    def GetAnchorTitleBand(self):
        if self.anchorPosTitleBand == "LEFT_TOP":
            x0 = -(self.width_title)
            y0 =  (self.height)
        elif self.anchorPosTitleBand == "LEFT_MIDLE":
            x0 = -(self.width_title)
            y0 =  (self.height/2)
            
        elif self.anchorPosTitleBand == "LEFT_BOTTOM":
            x0 = -(self.width_title)
            y0 = 0.0
            
        elif self.anchorPosTitleBand == "MIDLE_TOP":
            x0 = -(self.width_title/2)
            y0 = (self.height)
            
        elif self.anchorPosTitleBand == "MIDLE_MIDLE":
            x0 = -(self.width_title/2)
            y0 = (self.height/2)
            
        elif self.anchorPosTitleBand == "MIDLE_BOTTOM":
            x0 = -(self.width_title/2)
            y0 = 0.0
            
        elif self.anchorPosTitleBand == "RIGHT_TOP":
            x0 = 0.0
            y0 = (self.height)
            
        elif self.anchorPosTitleBand == "RIGHT_MIDLE":
            x0 = 0.0
            y0 = (self.height/2)
            
        elif self.anchorPosTitleBand == "RIGHT_BOTTOM":
            x0 = 0.0
            y0 = 0.0
        
        else:
            raise Exception

        return (x0, y0)
    
    def DesenhaStrokText(self, palavra):        
        for letra in palavra:
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(letra))
        
class DataBands:
    def __init__(self, perfil_parent):
        self.perfil = perfil_parent
        self.listBands = []
    
    def AddBand(self, band):
        self.listBands.append(band)
        
    def DesenhaBands(self):
        """Desenha o quadro de Bands abaixo do grafico"""
        try:
            for band in self.listBands:
                glTranslatef(0, -band.height, 0)
                band.Desenha(self.perfil)
        except Exception as e:
             if True:
                 exc_type, exc_obj, exc_tb = sys.exc_info()
                 fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                 print(exc_type, fname, exc_tb.tb_lineno)
                 print (e) 
            
              
class TextOpenGL:
    def __init__(self, texto, scale=1.0, anchorPos="LEFT_BOTTOM"):
        self.texto = texto
        self.scale = scale
        self.angle = 0.0
        self.color = [0.5, 0.5, 0.5]
        
        self.POS_ANCHORS = ["LEFT_TOP","LEFT_MIDLE","LEFT_BOTTOM",
                   "MIDLE_TOP", "MIDLE_MIDLE", "MIDLE_BOTTOM",
                   "RIGHT_TOP", "RIGHT_MIDLE", "RIGHT_BOTTOM"]
        
        #Verifica se a FLAG_POSANCHOR esta correta
        if anchorPos not in self.POS_ANCHORS:
            raise Exception
        else:
            self.AnchorPos = anchorPos
    
    def SetTitleColor(self, r, g, b):
        self.color = [r, g, b]
        
    def VerificaTexto(self):
        """Verifica o texto para saber se nao tem caracteres que nao podem
           ser desenhados pela Opengl, como por exemplo cecedilha, acentos
           entre outros caracteres.
        """
        pass
    def SetTextAngle(self, angle):
        if (type(angle) in (float, int)):
            self.angle = angle
        else:
            raise Exception
            
    def  GetWidth(self, palavra=None):        
        if palavra == None:
            if isinstance(self.texto, str):
                largura = 0
                for letra in self.texto:
                    largura += glutStrokeWidth(GLUT_STROKE_ROMAN, ord(letra) )
                return largura
            elif isinstance(self.texto, list):
                larguras = []
                for palavra in self.texto:
                    largura = 0
                    for letra in palavra:
                        largura += glutStrokeWidth(GLUT_STROKE_ROMAN, ord(letra) )
                    larguras.append(largura)
                return max(larguras)
        else:
            largura = 0
            for letra in palavra:
                largura += glutStrokeWidth(GLUT_STROKE_ROMAN, ord(letra) )
            return largura
    
    def GetHeght(self):
        return glutStrokeHeight(GLUT_STROKE_ROMAN)
    
    def GetLeftTopPos(self):
        x0 = 0.0
        y0 = -(self.GetHeght() * self.scale)
        
        if isinstance(self.texto, str):
            return self.GetPosReal([x0, y0])
        elif isinstance(self.texto, list):
            return self.GetPosReal([x0, y0*len(self.texto)])
        
    def GetLeftMidlePos(self):
        x0 = 0.0
        y0 = -((self.GetHeght()/2) * self.scale)
        
        if isinstance(self.texto, str):
            return self.GetPosReal([x0, y0])
        elif isinstance(self.texto, list):
            return self.GetPosReal([x0, y0*len(self.texto)])
    
    def GetLeftBottomPos(self):
        x0 = 0.0
        y0 = 0.0
        
        if isinstance(self.texto, str):
            return self.GetPosReal([x0, y0])
        elif isinstance(self.texto, list):
            return self.GetPosReal([x0, y0])
    
    def GetMidleTopPos(self):
        x0 = -((self.GetWidth()/2) * self.scale)
        y0 = -(self.GetHeght() * self.scale)
        
        if isinstance(self.texto, str):
            return self.GetPosReal([x0, y0])
        elif isinstance(self.texto, list):
            return self.GetPosReal([x0, y0*len(self.texto)])
    
    def GetMidleMidlePos(self):
        x0 = -((self.GetWidth()/2) * self.scale)
        y0 = -((self.GetHeght()/2) * self.scale)
        
        if isinstance(self.texto, str):
            return self.GetPosReal([x0, y0])
        elif isinstance(self.texto, list):
            return self.GetPosReal([x0, (-0.5+(len(self.texto)-1)*0.5)*self.GetHeght()*self.scale])
    
    def GetMidleBottomPos(self):
        x0 = -((self.GetWidth()/2) * self.scale)
        y0 = 0.0
        
        if isinstance(self.texto, str):
            return self.GetPosReal([x0, y0])
        elif isinstance(self.texto, list):
            return self.GetPosReal([x0, y0*len(self.texto)])
    
    def GetRightTopPos(self):
        x0 = -(self.GetWidth() * self.scale)
        y0 = -(self.GetHeght() * self.scale)
        
        if isinstance(self.texto, str):
            return self.GetPosReal([x0, y0])
        elif isinstance(self.texto, list):
            return self.GetPosReal([x0, y0*len(self.texto)])
    
    def GetRightMidlePos(self):
        x0 = -(self.GetWidth() * self.scale)
        y0 = -((self.GetHeght()/2) * self.scale)
        
        if isinstance(self.texto, str):
            return self.GetPosReal([x0, y0])
        elif isinstance(self.texto, list):
            return self.GetPosReal([x0, y0*len(self.texto)])
    
    def GetRightBottomPos(self):
        x0 = -(self.GetWidth() * self.scale)
        y0 = 0.0
        
        if isinstance(self.texto, str):
            return self.GetPosReal([x0, y0])
        elif isinstance(self.texto, list):
            return self.GetPosReal([x0, y0*len(self.texto)])
    
    def SetAnchorPos(self, flag_anchorPos):
        if (type(flag_anchorPos) == str and flag_anchorPos.upper() in \
                                                            self.POS_ANCHORS):
            self.AnchorPos = flag_anchorPos.upper()
        else:
            raise Exception
    
    def GetAnchorPos(self):
        if self.AnchorPos == "LEFT_TOP":
            return self.GetLeftTopPos()
        elif self.AnchorPos == "LEFT_MIDLE":
            return self.GetLeftMidlePos()
        elif self.AnchorPos == "LEFT_BOTTOM":
            return self.GetLeftBottomPos()
        elif self.AnchorPos == "MIDLE_TOP":
            return self.GetMidleTopPos()
        elif self.AnchorPos == "MIDLE_MIDLE":
            return self.GetMidleMidlePos()
        elif self.AnchorPos == "MIDLE_BOTTOM":
            return self.GetMidleBottomPos()
        elif self.AnchorPos == "RIGHT_TOP":
            return self.GetRightTopPos()
        elif self.AnchorPos == "RIGHT_MIDLE":
            return self.GetRightMidlePos()
        elif self.AnchorPos == "RIGHT_BOTTOM":
            return self.GetRightBottomPos()
        else:
            raise Exception
    
    def GetPosReal(self, XY):
        Ri = np.array([[m.cos(m.radians(self.angle)), m.sin(m.radians(self.angle))],
                            [-m.sin(m.radians(self.angle)),  m.cos(m.radians(self.angle))]])
        
        return np.dot(XY, Ri)
        #return XY
            
    def Desenha(self): 
        glPushAttrib(GL_CURRENT_BIT)
        glLineWidth(2.0)        
        glColor3f(*self.color)
        x0, y0 = self.GetAnchorPos()        
        glTranslatef(x0, y0, 0)
        glRotatef(self.angle, 0, 0, 1)
        glScalef(self.scale, self.scale, self.scale)         
        if isinstance(self.texto, str):
            for letra in self.texto:
                glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(letra))
        elif isinstance(self.texto, list):
            for palavra in self.texto:            
                for letra in palavra:
                    glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(letra))
                glTranslatef(-self.GetWidth(palavra), -self.GetHeght(), 0)            
        else:
            raise Exception
        glLineWidth(1.0)
        glPopAttrib()
        
            
            
        
    