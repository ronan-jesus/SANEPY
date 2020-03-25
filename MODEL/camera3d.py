# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 16:16:16 2014

@author: ronan
"""
from __future__ import division
import math as m
import time
from CALCULOS.vector3 import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Camera3d(object):
    def __init__(self, parent):
        self.Parent = parent

        #Definicao dos Vetores da Camera
        self.CameraPosition = Vector3(20479,65271,500)
        self.CameraView = Vector3(20479,65271,0)
        self.CameraUp = Vector3(0,1,0)
        self.CameraDirection = Vector3()


        #Definicao das variaveis Angulos de Rotacao
        self.theta = 0
        self.phi = 0
        self.angle = 60.0

        self.posAnteriorX = 0.0
        self.posAnteriorY = 0.0

        self.aspect = 1

        #Parametros da camera ORTHOGONAL
        #self.winspect = parent.GetClientSize()
        #print "Aspect %s" %self.winspect

        self.cameraLeft = -40000
        self.cameraRight = 40000
        self.cameraBotton = -40000
        self.cameraTop = 40000

        self.Near = -500
        self.Far = 5000

        self.Fator_do_zoom = 50.0
        self._scl = 1
        self.CameraPosition = Vector3(0,0,1)


    def SetCamera(self, positionCam, cameraLookAt, cameraUp):
        """
        Seta os valores da camera
        """
        self.CameraPosition = Vector3(positionCam)
        self.CameraView = Vector3(cameraLookAt)
        self.CameraUp = Vector3(cameraUp)

        self.CameraDirection = Vector3(self.CameraPosition - self.CameraView)


    def SetCameraTop(self, x_max, x_min, y_max, y_min, z_max, z_min):
        x_meio = (x_max+x_min)/2

        y_meio = (y_max+y_min)/2

        z_meio = (z_max+z_min)/2

        self.CameraPosition = Vector3(x_meio-1, y_meio-1, 5000)

        self.CameraView = Vector3([x_meio, y_meio, z_meio])


        self.Parent.ParametrosVizualizacao()
    

    def GetCamera(self):

        return (self.CameraPosition, self.CameraView, self.CameraUp)

    def GetCameraDirection(self):
        self.CameraDirection = self.CameraPosition - self.CameraView

    def CameraLookAt(self):

        return  gluLookAt(self.CameraPosition[0],self.CameraPosition[1],self.CameraPosition[2],
                          self.CameraView[0],self.CameraView[1],self.CameraView[2],
                          self.CameraUp[0],self.CameraUp[1],self.CameraUp[2])

    def ViewPortAspect(self, width, height, aspc=0):

        self.aspect = width/height
        self.GetModeCamera3D()

    def GetModeCamera3D(self):

        #return gluPerspective(self.angle, self.aspect, 0.1, 10000.)

        if self.aspect<=1:
            return glOrtho(self.cameraLeft,self.cameraRight,self.cameraBotton/self.aspect,self.cameraTop/self.aspect,self.Near,self.Far)
        else:
            return glOrtho(self.cameraLeft*self.aspect,self.cameraRight*self.aspect,self.cameraBotton,self.cameraTop,self.Near,self.Far)

    def GetModeCamera2D(self):
        pass
        #return gluPerspective(self.angle, float(600)/800, 0.1, 1000.)
        #return gluOrtho2D(self.cameraLeft,self.cameraRight,self.cameraBotton,self.cameraTop*self.aspect)


    def GetDirectionX(self):
        self.GetCameraDirection()
        CameraDirection = Vector3(self.CameraDirection[0],self.CameraDirection[1],self.CameraDirection[2])

        directionX = CameraDirection.cross(self.CameraUp)

        return directionX.normalise()

    def GetDirectY(self):
        self.GetCameraDirection()

        CameraDirection = Vector3(self.CameraDirection[0],self.CameraDirection[1],self.CameraDirection[2])

        directionX = self.GetDirectionX()

        directionY = directionX.cross(CameraDirection.normalise())

        return directionY.normalise()

    def MoveLeft(self, deslocamento_x):
        directionX = self.GetDirectionX()
        
        size = self.Parent.GetClientSize()
            
        self.CameraPosition += (directionX*deslocamento_x*(size[0]/size[1]))
        self.CameraView += directionX*deslocamento_x*(size[0]/size[1])
        
    def MoveRight(self, deslocamento_x):
        directionX = self.GetDirectionX()        
        
        size = self.Parent.GetClientSize()
        
        self.CameraPosition -= directionX*deslocamento_x*(size[0]/size[1])
        self.CameraView -= directionX*deslocamento_x*(size[0]/size[1])      
        
    def MoveTop(self, deslocamento_y):
        directionY = self.GetDirectY()

        self.CameraPosition -= directionY*deslocamento_y
        self.CameraView -= directionY*deslocamento_y        
        
    def MoveBotton(self, deslocamento_y):
        directionY = self.GetDirectY()

        self.CameraPosition -= directionY*deslocamento_y
        self.CameraView -= directionY*deslocamento_y
       
    def MouseEvent(self, posAtualX, posAtualY, evt):
        #Pega a posicao atual do Mouse
        #posAtualX, posAtualY

        if evt.Dragging() and evt.MiddleIsDown():
            size = self.Parent.GetClientSize()
            width, height = size[0], size[1]

            correl_x = (abs(self.cameraLeft)+abs(self.cameraRight))/width
            correl_y = (abs(self.cameraTop)+abs(self.cameraBotton))/height

            deslocamento_x = self.posAnteriorX - posAtualX
            deslocamento_y = self.posAnteriorY - posAtualY

            # Movimento de PAN no eixo X
            if deslocamento_x > 0:
                self.MoveLeft(-deslocamento_x*correl_x)
                self.posAnteriorX = posAtualX

            elif deslocamento_x < 0:
                self.MoveRight(deslocamento_x*correl_x)
                self.posAnteriorX = posAtualX

            #Movimento de PAN no eixo Y
            if deslocamento_y > 0:
                self.MoveTop(deslocamento_y*correl_y)
                self.posAnteriorY = posAtualY

            elif deslocamento_y < 0:
                self.MoveBotton(deslocamento_y*correl_y)
                self.posAnteriorY = posAtualY

        else:
            self.Parent.SNAPpickRects(posAtualX, posAtualY)
            

    def KeyEvent(self, evt, Eixo):
        pass        

    def ZoomAll(self, event):
        maximos = self.GetExtremidadesDoModelo()        
        
        meioX = (maximos[0][0]+maximos[0][1])/2
        meioY = (maximos[1][0]+maximos[1][1])/2        
        
       
        bandaX = abs((maximos[0][1]-maximos[0][0])/2)
        bandaY = abs((maximos[1][1]-maximos[1][0])/2)
        
        if bandaX >= bandaY:
            self.cameraLeft = -bandaX
            self.cameraRight = +bandaX
            self.cameraBotton = -bandaX
            self.cameraTop = +bandaX
        else:
            self.cameraLeft = -bandaY
            self.cameraRight = +bandaY
            self.cameraBotton = -bandaY
            self.cameraTop = +bandaY
        
        size = self.Parent.GetClientSize()
        self.ViewPortAspect(size[0], size[1])
        
        self.CameraPosition = Vector3(meioX,meioY,1000)
        self.CameraView = Vector3(meioX,meioY,0)
        
        self.Parent.ParametrosVizualizacao()
        
        event.Skip()


    def Zoom(self, tipoZoom, evt, size):
        mousepos_x, mousepos_y  = evt.GetPosition()

        xj = mousepos_x
        yj = mousepos_y

        xi, yi = size[0], size[1]
        
        s = xi/yi
        
        width_rigth = (xi-xj)/xi
        width_left = 1-width_rigth

        height_bottom = (yi-yj)/yi
        height_top = 1-height_bottom

        if tipoZoom == "+":
#            if self.Fator_do_zoom < 2*self.scl:
#                self.Fator_do_zoom = self.scl
#            else:
           
            self.Fator_do_zoom = self.scl
            
            self.cameraLeft +=(20*self.Fator_do_zoom)#*width_left)
            self.cameraRight -= (20*self.Fator_do_zoom)#*width_rigth)
            self.cameraBotton += 20*self.Fator_do_zoom#*height_bottom
            self.cameraTop -= 20*self.Fator_do_zoom#*height_top
            
#            print "cameraLeft = %s" %self.cameraLeft
#            print "cameraRight = %s" %self.cameraRight
#            print "cameraBotton = %s" %self.cameraBotton
#            print "cameraTop = %s" %self.cameraTop
#            print "Fator_do_zoom = %s" %self.Fator_do_zoom
            
#            if self.Fator_do_zoom <= 0.0:
#                 self.Fator_do_zoom = 2*self.scl
                 

        elif tipoZoom == "-":
             self.cameraLeft -=(20*self.Fator_do_zoom)#*width_left)
             self.cameraRight += (20*self.Fator_do_zoom)#*width_rigth)
             self.cameraBotton -= (20*self.Fator_do_zoom)#*height_bottom)
             self.cameraTop += (20*self.Fator_do_zoom)#*height_top)
             self.Fator_do_zoom = self.scl
             
#             print "cameraLeft = %s" %self.cameraLeft
#             print "cameraRight = %s" %self.cameraRight
#             print "cameraBotton = %s" %self.cameraBotton
#             print "cameraTop = %s" %self.cameraTop
#             print "Fator_do_zoom = %s" %self.Fator_do_zoom
             
        else:
            return       

        evt.Skip()
        
    def GetExtremidadesDoModelo(self):
        model = self.Parent.parent
       
        listaPVs = model.Estrututura.LISTA_PVS
        listaPontosCurvas = model.terreno.pontos
        listaDxfElementos = model.dadosDXF.graficos
        
        
        lintsPontos_X_Modelo = []
        lintsPontos_Y_Modelo = []
        
        for pv in listaPVs:
            lintsPontos_X_Modelo.append(pv.pos[0])
            lintsPontos_Y_Modelo.append(pv.pos[1])
            
        for ponto in listaPontosCurvas:
            lintsPontos_X_Modelo.append(ponto[0]) 
            lintsPontos_Y_Modelo.append(ponto[1])
            
        for linha in listaDxfElementos["LINES"]:
            lintsPontos_X_Modelo.append(linha[0][0]*100) 
            lintsPontos_Y_Modelo.append(linha[0][1]*100)
            lintsPontos_X_Modelo.append(linha[1][0]*100) 
            lintsPontos_Y_Modelo.append(linha[1][1]*100)                
            
        min_x, max_x = min(lintsPontos_X_Modelo), max(lintsPontos_X_Modelo)
        min_y, max_y = min(lintsPontos_Y_Modelo), max(lintsPontos_Y_Modelo)
        
        return ((min_x, max_x), (min_y, max_y))
            
        
    @property
    def scl(self):        
        return abs(self.cameraLeft-self.cameraRight)/100
    
    @scl.setter
    def scl(self, value):
        pass
        
        