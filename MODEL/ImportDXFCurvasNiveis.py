# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 08:49:34 2018

@author: RONAN TEODORO
"""
from __future__ import division
import ezdxf
import matplotlib.pyplot as plt
import matplotlib.tri as Tri
from matplotlib.tri import TriAnalyzer, UniformTriRefiner
import numpy as np
import scipy.ndimage
import matplotlib.cm as cm
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Terreno(object):
    def __init__(self):
        self.pontos = []
        self.borda = []
        self.triangulos = []
        self.relacao_circulo_minimo = 0.03
        
        self.visivel = True
        
        self.ImportaPontos()
        #self.DesenhaTriangulacao()
        
    def ImportaPontos(self):
        LISTA_PONTOS = []
        dwg = ezdxf.readfile("C:\PROGRAMAS PYTHON\SANEPY\Projetos\SANEPY\ARQUIVOS/ficticea_esgoto.dxf")
        
        X = []
        Y = []
        Z = []
        
        modelspace = dwg.modelspace()
        for e in modelspace:
            if e.dxftype() == 'POINT':
                LISTA_PONTOS.append([e.dxf.location[0],e.dxf.location[1],e.dxf.location[2]])
                X.append(e.dxf.location[0]*100) #Multiplicado por 100 apenas
                Y.append(e.dxf.location[1]*100) #por questao de desenho no
                Z.append(e.dxf.location[2])     #Opengl, 1m = 100points
        
        
        X = np.array(X)
        Y = np.array(Y)
        Z = np.array(Z)
        
        self.triangulacao = Tri.Triangulation(X,Y)
            
        
        #mask = TriAnalyzer(self.triangulacao).get_flat_tri_mask(self.relacao_circulo_minimo)
        
        #self.triangulacao.set_mask(mask)
        
        ###Bordas do terreno
        boundaries = []
        for i in range(len(self.triangulacao.triangles)):
          if all(self.triangulacao.neighbors[i] == -1):
              pass
          else:
              for j in range(3):
                if self.triangulacao.neighbors[i,j] < 0:
                  # Triangle edge (i,j) has no neighbor so is a boundary edge.
                  boundaries.append((self.triangulacao.triangles[i,j],
                                     self.triangulacao.triangles[i,(j+1)%3]))
        
        
        self.pontos = [X, Y, Z]
        self.borda = np.asarray(boundaries)
        self.triangulos = self.triangulacao.triangles
        
        # refining the data
        refiner = UniformTriRefiner(self.triangulacao)
        tri_refi, z_test_refi = refiner.refine_field(Z, subdiv=3)

        self.Curvas = plt.tricontour(tri_refi, z_test_refi, levels=[89, 90, 91, 92, 93, 94, 95, 96, 97])

        self.Curvas = self.Curvas.collections

    def Get_Z(self, x, y):
        interpolacao = Tri.LinearTriInterpolator(self.triangulacao, self.pontos[2])
        z = interpolacao.__call__(x, y) # Pega A interpolacao x,y retorna o Z
        
        return z
    
    def DesenhaTriangulacao(self):
        for triang in self.triangulos:
            glPushMatrix()
            glColor3f(1.0, 0.0, 0.0)
            glBegin(GL_LINE_LOOP)
            glVertex2f(self.pontos[0][triang[0]],self.pontos[1][triang[0]])
            glVertex2f(self.pontos[0][triang[1]],self.pontos[1][triang[1]])
            glVertex2f(self.pontos[0][triang[2]],self.pontos[1][triang[2]])
            glEnd()
            glPopMatrix()
    
    def DesenhaBordaTerreno(self):        
        """ self.borda e uma lista de listas, cada lista dentra da lista,
            possuem os numeros do primeiro ponto e do segundo ponto que
            compoem cada linha que foram a poligonal da borda do terreno
            
            self.borda = [
                           [p1, p2] -> Linha 1
                           [p1, p2] -> Linha 2
                           [p1, p2] -> Linha n
                           [p1, p2] -> Linha n+1
                                                   ]            
            usar self.borda[0][i] e self.borda[1][i] para compor
        """
        glPushMatrix()
        glColor3f(0.0, 1.0, 1.0)
        glBegin(GL_LINES)
        for b in self.borda:            
            glVertex2f(self.pontos[0][b[0]],self.pontos[1][b[0]])          
            glVertex2f(self.pontos[0][b[1]],self.pontos[1][b[1]])          
        glEnd()
        glPopMatrix()        
    
    def DesenhaCurvasDeNiveis(self):
        """self.curvas contem uma colecao de curvas, ou seja um objeto do tipo
           lista e cada item e do tipo 'matplotlib.collections.LineCollection'
           que contem os segmentos que compoem cada curva de nivel.
           
           o metodo curva.get_paths() returna uma lista com um objeto do tipo
           'Path' que nada mais e do que um array([[coordx1, coordy1],
                                                   [coordx2, coordy2],
                                                   [coordxN, coordyN],
                                                   [coordxN+1, coordyN+1]])
          ou seja [coordx1, coordy1] e [coordx2, coordy2] representa os 
          respectivamente o primeiro e segundo ponto primeira reta que forma
          a curva de nivel, a segunda reta se da pelos pontos
          [coordx2, coordy2] e [coordx3, coordy3] e assim por diante com
          os outros pontos.
          
          o Poligono que representa a curva de nivel pode ser aberto ou fechado.
          
          
        """
        
        
        glPushMatrix()
        glColor3f(0.8, 0.8, 0.0)
        for curva in self.Curvas:          
            data = curva.get_paths()            
            for i in data:
                glBegin(GL_LINE_STRIP)
                a = i.vertices
                for j in a:
                    glVertex2f(j[0],j[1])            
                glEnd()
        glPopMatrix()



        
 
        

