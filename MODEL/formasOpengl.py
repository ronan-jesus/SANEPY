# -*- coding: utf-8 -*-
from __future__ import division
import sys
from ctypes import *
import math as m
import numpy as np
from numpy.polynomial import Polynomial as P
from CALCULOS.vector3 import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
#import OpenGL.GL as ogl

from GRAFICOS.perfilLongitudinal import PerfilLongitudinal

def CriaDesenhoDXF(model, id_Dxf, mode=None):    
    glNewList(id_Dxf, GL_COMPILE)
    try:               
        # Verifica se a variavel LISTA_PVS ja estiver sido atribuida
        if hasattr(model, "dadosDXF"):
            glPushMatrix()
            glTranslatef(0.0, 0.0, -100)
            glScale(100, 100, 100)
            
            for ponto in model.dadosDXF.graficos["POINTS"]:
                pass                    
#                glPushMatrix()
#                glColor3f(0.0,0.0,1.0)
#                glPointSize(10)
#                glLineWidth(1)                
#                glBegin(GL_POINT)
#                glVertex3f(ponto[0],ponto[1],ponto[2])                
#                glEnd()
#                glPopMatrix()

            for linha in model.dadosDXF.graficos["LINES"]:
                glColor3f(1.0,1.0,1.0)
                glLineWidth(1)
                glPushMatrix()
                glBegin(GL_LINES)
                glVertex3f(linha[0][0],linha[0][1],linha[0][2])
                glVertex3f(linha[1][0],linha[1][1],linha[1][2])
                glEnd()
                glPopMatrix()
                
            for circulo in model.dadosDXF.graficos["CIRCLES"]:                    
                sides = 32    
                radius = circulo[1]
                glPushMatrix()
                glColor3f(1.0, 1.0, 1.0)
                glTranslate(circulo[0][0], circulo[0][1], circulo[0][2])            
                glBegin(GL_LINE_LOOP)    
                for i in range(sides):    
                    cosine= radius * cos(i*2*pi/sides)    
                    sine  = radius * sin(i*2*pi/sides)   
                    glVertex2f(cosine,sine)
                glEnd()
                glPopMatrix()
                
            for arc in model.dadosDXF.graficos["ARCS"]:
                sides = 20  
                
                radius = arc[1]
                theta_ini = arc[2]
                theta_fin = arc[3]
                theta1 = m.radians(theta_ini)                
                
                glPushMatrix()
                glColor3f(1.0, 1.0, 1.0)
                glTranslate(arc[0][0], arc[0][1], arc[0][2])            
                glBegin(GL_LINE_STRIP)    
                for i in range(sides+1):
                    if (theta_ini < theta_fin):                        
                        theta =  theta1 + m.radians((theta_fin-theta_ini)* (i/sides))                    
                    elif (theta_ini > theta_fin):
                        theta = (360 - (theta_ini - theta_fin))
                        theta =  theta1 + m.radians((theta)* (i/sides))                    
                    glVertex2f(radius * cos(theta),radius * sin(theta))
                glEnd()
                glPopMatrix()            
            
            for lwpolylinha in model.dadosDXF.graficos["LWPOLYLINES"]:                    
                glPushMatrix()
                glColor3f(1.0,1.0,1.0)
                glLineWidth(1)               
                if lwpolylinha[0] == 0:                    
                    glBegin(GL_LINE_STRIP)
                    for p in lwpolylinha[1]:
                       glVertex3f(p[0],p[1],p[2])                
                    glEnd()
                elif lwpolylinha[0] == 1:                    
                    glBegin(GL_LINE_LOOP)
                    for p in lwpolylinha[1]:
                       glVertex3f(p[0],p[1],p[2])                
                    glEnd()
                glPopMatrix()            
                
            for polylinha in model.dadosDXF.graficos["POLYLINES"]:                    
                glPushMatrix()
                glColor3f(1.0,1.0,1.0)
                glLineWidth(1)                
                glBegin(GL_LINE_STRIP)
                for p in polylinha:
                    if round((p[0]+p[1]+p[2]),0)== 0:
                        pass
                    else:
                        glVertex3f(p[0],p[1],p[2])                
                glEnd()
                glPopMatrix()
                
            for texto in model.dadosDXF.graficos["TEXTS"]:                
                glPushMatrix()
                glColor3f(1.0,1.0,1.0)
                glTranslatef(* texto[0][1])
                DesenhaStrokText(texto[1])
                glPopMatrix()   
                
            for texto in model.dadosDXF.graficos["MTEXTS"]:
                """
                MTEXT_TOP_LEFT	  =  1
                MTEXT_TOP_CENTER	  =  2
                MTEXT_TOP_RIGHT	  =  3
                MTEXT_MIDDLE_LEFT	  =  4
                MTEXT_MIDDLE_CENTER =  5
                MTEXT_MIDDLE_RIGHT	  =  6
                MTEXT_BOTTOM_LEFT   =  7
                MTEXT_BOTTOM_CENTER =  8
                MTEXT_BOTTOM_RIGHT	  =  9
                """
                    
                glPushMatrix()
                glColor3f(1.0,1.0,1.0)
                glTranslatef(* texto[0])
                glRotatef(texto[8], 0, 0, 1)
                try:
                    t = texto[1].split(";")[1]
                    t = t.replace("}", " ")
                    DesenhaStrokText(t,texto[10])
                except:
                    pass
                glPopMatrix()                
                
            for insert in model.dadosDXF.graficos["INSERTS"]:
                glPushMatrix()
                glTranslate(* insert[0])
                glScale(* insert[1])
                glRotatef(insert[2], 0, 0, 1)
                
                for entidade in insert[3]:
                    if entidade[0] == "LINE":                    
                        glColor3f(1.0,1.0,1.0)
                        glLineWidth(1)
                        glPushMatrix()
                        glBegin(GL_LINES)
                        glVertex3f(* entidade[1][0])
                        glVertex3f(* entidade[1][1])
                        glEnd()
                        glPopMatrix()
                    
                    if entidade[0] == "CIRCLE":                    
                        sides = 32    
                        radius = entidade[1][1]
                        glPushMatrix()
                        glColor3f(1.0, 1.0, 1.0)
                        glTranslate(* entidade[1][0])            
                        glBegin(GL_LINE_LOOP)    
                        for i in range(sides):    
                            cosine= radius * cos(i*2*pi/sides)    
                            sine  = radius * sin(i*2*pi/sides)   
                            glVertex2f(cosine,sine)
                        glEnd()
                        glPopMatrix()
                        
                    if entidade[0] == "ARC":
                        sides = 20  
                        
                        radius = entidade[1][1]
                        theta_ini = entidade[1][2]
                        theta_fin = entidade[1][3]
                        theta1 = m.radians(theta_ini)                
                        
                        glPushMatrix()
                        glColor3f(1.0, 1.0, 1.0)
                        glTranslate(* entidade[1][0])            
                        glBegin(GL_LINE_STRIP)    
                        for i in range(sides+1):
                            if (theta_ini < theta_fin):                        
                                theta =  theta1 + m.radians((theta_fin-theta_ini)* (i/sides))                    
                            elif (theta_ini > theta_fin):
                                theta = (360 - (theta_ini - theta_fin))
                                theta =  theta1 + m.radians((theta)* (i/sides))                    
                            glVertex2f(radius * cos(theta),radius * sin(theta))
                        glEnd()
                        glPopMatrix()                  
                    
                    if entidade[0] == "LWPOLYLINE":                    
                        glPushMatrix()
                        glColor3f(1.0,1.0,1.0)
                        glLineWidth(1)               
                        if entidade[1][0] == 0:
                            glBegin(GL_LINE_STRIP)
                            for p in entidade[1][1]:                                
                                glVertex3f(p[0],p[1],p[2])                
                            glEnd()
                        elif entidade[1][0] == 1:
                            glBegin(GL_LINE_LOOP)
                            for pp in entidade[1][1]:                                
                                glVertex3f(p[0],p[1],p[2])                
                            glEnd()
                        glPopMatrix()
                        
                    for polylinha in model.dadosDXF.graficos["POLYLINES"]:                    
                        glPushMatrix()
                        glColor3f(1.0,1.0,1.0)
                        glLineWidth(1)                
                        glBegin(GL_LINE_STRIP)
                        for p in polylinha:
                            if round((p[0]+p[1]+p[2]),0)== 0:
                                pass
                            else:
                                glVertex3f(p[0],p[1],p[2])                
                        glEnd()
                        glPopMatrix()
                    
                glPopMatrix()
            glPopMatrix()
                
            
                
            
        else:    #Se a variavel LISTA_PVS ainda nao estiver sido
            pass #atribuida, nao faz nada            
        
    except Exception as e:
        if True:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print (e)
    finally:
        glEndList()
        
        
def CriaDesenhoTerreno(model, id_Terreno, mode=None):
    '''
    Descrição:
      Funcao que cria o desenhos do terreno, bem como os triangulos da
      triangulacao e a borda do terreno.
      Apenas cria e armazena na glList(num->id_Terreno), para que possa ser
      chamada para o desenho na area de trabalho do programa

    Utilização:
      CriaDesenhoTerreno(model, id_Terreno, mode)

    Parâmetros:
      model
        tipo(classe->Model) que contem os dados do programa bem como as o
        objeto terreno que quarda od dados do Terreno.
      id_Terreno        
        tipo(int) -> numero que sera utilizado para chamar a glList quando
        for necessario desenhar os elementos na area de trabalho.
      mode        
        tipo(mode -> GL_RENDER) -> Variavel da API Opengl, utilizada para
        função de selecao pelo metodo picking.
        
    Return:
        Nao tem valor de retorno, as acoes sao feitas na API do Opengl que esta
        ATIVA no momento da chamada da funcao
    '''    
    glNewList(id_Terreno, GL_COMPILE)
    try:
        # Verifica se a variavel LISTA_PVS ja estiver sido atribuida
        if hasattr(model, "terreno"):
            if model.terreno.visivel == True:                        
                glColor3f(0.8, 0.2, 0.5)
    
                if mode == GL_RENDER:
                    glPushMatrix()
                    glTranslatef(0.0, 0.0, -100)
                    #model.terreno.DesenhaTriangulacao()
                    model.terreno.DesenhaCurvasDeNiveis()
                    model.terreno.DesenhaBordaTerreno()
#                try:
#                    if hasattr(model, "Perfis"):
#                        model.Perfis.DesenhaPerfil()
#                        model.Perfis.DesenhaPVs()
#                        model.Perfis.DesenhaTrechos()
#                except Exception as e:
#                    if model.emDesenvolvimento == True:
#                        exc_type, exc_obj, exc_tb = sys.exc_info()
#                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#                        print(exc_type, fname, exc_tb.tb_lineno)
#                        print (e)
                
                if mode == GL_RENDER:
                    glPopMatrix()
                        
        else:    #Se a variavel LISTA_PVS ainda nao estiver sido
            pass #atribuida, nao faz nada            
        
    except Exception as e:
        if model.emDesenvolvimento == True:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print (e)
    finally:
        glEndList()
        
def CriaDesenhoPVs(model, id_PVs, mode=GL_RENDER):
    '''
    Descrição:
      Funcao que cria os denhos das singularidades do tipo Poco de Visita (PV).
      Apenas cria e armazena na glList(num->id_PVs), para que possa ser
      chamada para o desenho na area de trabalho do programa

    Utilização:
      CriaDesenhoPV(model, id_PVs, mode)

    Parâmetros:
      model
        tipo(classe->Model) que contem os dados do programa bem como as listas com
        os PVs que serao desenhados
      id_PVs        
        tipo(int) -> numero que sera utilizado para chamar a glList quando
        for necessario desenhar os elementos na area de trabalho.
      mode        
        tipo(mode -> GL_RENDER) -> Variavel da API Opengl, utilizada para
        função de selecao pelo metodo picking.
        
    Return:
        Nao tem valor de retorno, as acoes sao feitas na API do Opengl que esta
        ATIVA pv momento da chamada da funcao
    '''
    if mode == GL_RENDER:
        glNewList(id_PVs, GL_COMPILE)
    try:              
        # Verifica se a variavel LISTA_PVS ja estiver sido atribuida
        if hasattr(model.Estrututura, "LISTA_PVS"):
            for pv in model.Estrututura.LISTA_PVS:
                if pv.visivel == True:                        
                    if (model.selected == -1 or model.selected == None):
                        glColor3f(* pv.color)
                    elif pv.numero not in  model.GetNosSelecionados():                        
                        glColor3f(* pv.color)                        
                    elif pv.numero in model.GetNosSelecionados():
                        #Desenha o quadradinho de mover o elemento
                        #Altera a cor para a cor de selecao
                        glColor3f(1.0, 0.0, 0.0)
        
                    glPushName(pv.numero)
                    pv.DesenhaPV()                    
                    
                    if type(model.selected)==list:
                        if pv.numero in model.GetNosSelecionados():
                            pv.DesenhaOutrosElementos()
                            
                            glPushName(1)
                            pv.DesenhaPontosArrasto()
                            glPopName()
                            
                            glPushName(2)
                            pv.DesenhaPontoRotacao()
                            glPopName()

                            glPushName(3)
                            pv.Label.DesenhaPontoArrastoLabel()
                            glPopName()
                            
                    glPopName()
                            
        else:    #Se a variavel LISTA_PVS ainda nao estiver sido
            pass #atribuida, nao faz nada            
        
    except Exception as e:
        if model.emDesenvolvimento == True:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print (e)
    finally:
        if mode == GL_RENDER:            
            glEndList()
            
    
def CriaDesenhoTubos(model, id_Barras, mode=GL_RENDER):
        """Desenha as Barras na instancia de PyOpengl ativa

         model-> Classe Model-> Encontra-se as variaveis das regras de negocio
         do programa.
        """
        if (mode == None or mode == GL_RENDER):
            glNewList(id_Barras, GL_COMPILE)
        try:
            # Se a variavel LISTA_TUBULACOES ja estiver sido atribuida
            if hasattr(model.Estrututura, "LISTA_TUBULACOES"):
                tubos_selecionados = model.GetBarrasSelecionadas()
                for tubo in model.Estrututura.LISTA_TUBULACOES:
                    if tubo.visivel == True:
                        if (type(model.selected) is list and tubo.numero in \
                                                           tubos_selecionados):
                            #SE TUBO ESTIVER SELECIONADA FICARA NA COR VERMELHA
                            glColor3f(1.0, 0.0, 0.0)
                        else:
                            #CASO NAO ESTEJA SELECIONADA FICARA NA COR AZUL
                            glColor3f(0.0, 0.0, 1.0)                           
                    
                        glPushName(tubo.numero)                    
                        tubo.Desenha()
                        glPopName()
                    
            else:    #Se a variavel LISTA_TUBULACOES ainda nao estiver sido
                pass #atribuida, nao faz nada
            
        except Exception as e:
            if model.emDesenvolvimento == True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
        finally:
            if (mode == None or mode == GL_RENDER):
                glEndList()
                


def CriaDesenhoPerfis(model, id_Perfis, mode=GL_RENDER):
    """Desenha os Perfis Longitudinais na instancia de PyOpengl ativa

     model-> Classe Model-> Encontra-se as variaveis das regras de negocio
     do programa.
    """
    if (mode == None or mode == GL_RENDER):
        glNewList(id_Perfis, GL_COMPILE)
    try:
        # Se a variavel 'Perfis' ja estiver sido atribuida
        if hasattr(model, "LISTA_PERFIS"):
            for perfil in model.LISTA_PERFIS:                    
                glPushName(perfil.numero)
                perfil.DesenhaPerfil()
                perfil.DesenhaPVs()
                perfil.DesenhaTrechos()                                        
                if mode == GL_SELECT:
                    perfil.DesenhaSnapsSelect()
                glPopName()
                
        else:    #Se a variavel LISTA_TUBULACOES ainda nao estiver sido
            pass #atribuida, nao faz nada
        
    except Exception as e:
        if model.emDesenvolvimento == True:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print (e)
    finally:
        if (mode == None or mode == GL_RENDER):
            glEndList()

def CriaDesenhoEixosGlobais(model, id_EixosGlobais):
    """Cria o Desenho dos Eixos GLOBAIS, cria
    e armazena na glList(id_EixosGlobais)
    """
    glNewList(id_EixosGlobais, GL_COMPILE)
    tamanho = model.TAMANHO_EIXOS_GLOBAIS*100
    x,y,z = model.POSICAO_EIXOS_GLOBAIS
    x,y,z = x*100,y*100,z*100
    
    b = int(tamanho/6.66) #base da seta e tamanho da seta
    e = int(tamanho/20) #Diametro do Eixo
    d = e+10 #Distancia das LETRAS XYZ da ponta da seta

    glPushMatrix()
    glTranslate(x,y,z)
    
    glDisable(GL_BLEND)
    c = gluNewQuadric()

    #Eixo x
    glColor4f(0.0, 0.0, 1.0, 0.0) #Azul
    glPushMatrix()
    #glTranslate(100,100,0)
    glRotate(90, 0, 1, 0)
    gluCylinder(c, e, e, tamanho, 5, 5)
    glTranslate(0,0,tamanho)
    gluCylinder(c, b, 0, b, 5, 5)

    glRasterPos3f(0.0,0.0,d)
    glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord("X"))

    glPopMatrix()

    #Eixo y
    glColor4f(0.0, 1.0, 0.0, 0.0) #Verde
    glPushMatrix()
    #glTranslate(100,100,0)
    glRotate(-90, 1, 0, 0)
    gluCylinder(c, e, e, tamanho, 5, 5)
    glTranslate(0,0,tamanho)
    gluCylinder(c, b, 0, b, 5, 5)

    glRasterPos3f(0.0,0.0,d)
    glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord("Y"))


    glPopMatrix()
    glEnable(GL_BLEND)
    
    glPopMatrix()
    glEndList()
        
        
def CriaEixosDasBarra(model, id_glListEixosBarras):
    """
        Cria o desenho dos eixos locais XYZ das barras e armazena em uma glList
    """
    try:
        glNewList(id_glListEixosBarras, GL_COMPILE)
        tamanho_eixos = model.TAMANHO_EIXOS_BARRAS*100
        #Se a variavel LISTA_TUBULACOES ja estiver sido atribuida
        if hasattr(model.Estrututura, "LISTA_TUBULACOES"):
            for barra in model.Estrututura.LISTA_TUBULACOES:
                if barra.visivel == True:
                    vetor_barra_x_global = [barra.PV2.pos[0] - barra.PV1.pos[0], barra.PV2.pos[1] - barra.PV1.pos[1], barra.PV2.pos[2] - barra.PV1.pos[2]]
        
                    vetor_barra_x_normalizado = Vector3(vetor_barra_x_global[0], vetor_barra_x_global[1], vetor_barra_x_global[2]).normalise()
        
                    vetor_barra_x_normalizado = np.array(vetor_barra_x_normalizado[:])
        
                    vetor_barra_z_normalizado = np.array([0,0,1])
        
        
                    vetor_barra_x_normalizado_local = [1, 0, 0]
        
                    vetor_barra_x_normalizado_local = Vector3(vetor_barra_x_normalizado_local[0], vetor_barra_x_normalizado_local[1],vetor_barra_x_normalizado_local[2])
                    vetor_barra_z_normalizado = Vector3(vetor_barra_z_normalizado[0], vetor_barra_z_normalizado[1], vetor_barra_z_normalizado[2])
        
        
                    vec_x = Vector3(vetor_barra_x_normalizado_local[0], vetor_barra_x_normalizado_local[1], vetor_barra_x_normalizado_local[2]).normalise()
                    vec_z = Vector3(vetor_barra_z_normalizado[0], vetor_barra_z_normalizado[1], vetor_barra_z_normalizado[2]).normalise()
        
        
                    vetor_barra_y_normalizado = vec_x.cross(vec_z)
        
        
        
                    vetor_y_global = np.dot(vetor_barra_y_normalizado, barra.Ri)
                    vetor_z_global = np.dot(vec_z, barra.Ri)
        
        
                    x_medio = (barra.PV2.pos[0] - barra.PV1.pos[0])/2
                    y_medio = (barra.PV2.pos[1] - barra.PV1.pos[1])/2
                    z_medio = (barra.PV2.pos[2] - barra.PV1.pos[2])/2
        
        
                    glPushMatrix()
                    glTranslatef(barra.PV1.pos[0]+x_medio, barra.PV1.pos[1]+y_medio, barra.PV1.pos[2]+z_medio )
        
                    glColor3f(0.0,0.0,1.0)
                    glLineWidth(4)
                    glBegin(GL_LINES)
                    glVertex3f(0,0,0)
                    glVertex3f(vetor_barra_x_normalizado[0]*tamanho_eixos,vetor_barra_x_normalizado[1]*tamanho_eixos,vetor_barra_x_normalizado[2]*tamanho_eixos)
                    glEnd()
        
        
                    glLineWidth(4)
                    glColor3f(0.0,1.0,0.0)
                    glBegin(GL_LINES)
                    glVertex3f(0,0,0)
                    glVertex3f(-vetor_y_global[0]*tamanho_eixos,-vetor_y_global[1]*tamanho_eixos,-vetor_y_global[2]*tamanho_eixos)
                    glEnd()
        
                    glLineWidth(4)
                    glColor3f(1.0,0.0,0.0)
                    glBegin(GL_LINES)
                    glVertex3f(0,0,0)
                    glVertex3f(vetor_z_global[0]*tamanho_eixos,vetor_z_global[1]*tamanho_eixos,vetor_z_global[2]*tamanho_eixos)
                    glEnd()
        
                    glPopMatrix()
                else:
                    pass
        else:    #Se a variavel LISTA_TUBULACOES nao estiver atribuida ainda, 
            pass #nao faz nada
    except Exception as e:
        if model.emDesenvolvimento == True:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print (e)
        else:
            pass
    finally:
        glLineWidth(2)
        glEndList()
        



def MostraEscalaDeCores(xi, yi):
    xi = xi
    yi = yi

    dados = Cargas2Colors(-1000, 1000)

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    viewport = glGetIntegerv(GL_VIEWPORT)
    glOrtho(viewport[0], viewport[2], viewport[3], viewport[1], 0, 1)
    glLineWidth (1.0)

    for i in range(len(dados)):
        glBegin(GL_TRIANGLE_STRIP)
        glColor3ub(dados[i][1][0], dados[i][1][1], dados[i][1][2])
        glVertex3f(xi,(i*30)+yi, 0)
        glVertex3f(xi+25,(i*30)+yi, 0)
        glVertex3f(xi,(i*30)+yi+30, 0)
        glVertex3f(xi+25,(i*30)+yi+30, 0)
        glEnd()

        if i == 0:
            pass
        else:
            glColor3ub(0, 0, 0)
            glRasterPos3f(xi+40,(i*30)+yi+5, 0)
            DesenhaTexto(GLUT_BITMAP_HELVETICA_12, (str(dados[i][0])))

    glPopMatrix()


def Cargas2Colors(c_min, c_max):
    carga_maxima = c_max
    carga_minima = c_min

    cores= [[102, 153, 255,1],
            [153, 153, 255,2],
            [153, 204, 255,3],
            [153, 255, 255,4],
            [102, 255, 204,5],
            [153, 255, 153,6],
            [204, 255, 153,7],
            [255, 255, 000,8],
            [255, 208, 134,10],
            [255, 192, 127,11],
            [255, 161, 127,12],
            [255, 124, 119,13],
            [235, 131, 185,14],
            [237, 000, 220,15]]

    incremento = (abs(carga_minima)+abs(carga_maxima))/14

    cargas = [round(carga_minima+(incremento*i),0) for i in range(15)]

    cargas.sort(reverse=True)

    return zip(cargas, cores)

def DesenhaTexto(FONT, Texto):
    """FUNCAO PARA DESENHAR CARACTERES BITMAP
     
       UTILIZAR A FORMA ABAIXO PARA DESENHAR
       #glRasterPos3f(pv.pos[0]-50,pv.pos[1]-20, pv.pos[2]+20)
       #DesenhaTexto(GLUT_BITMAP_HELVETICA_12, texto)
    """
    for letra in Texto:
        glutBitmapCharacter(FONT, ord(letra))


def DesenhaStrokText(palavra, scale=1.0):
        glPointSize(1)
        glLineWidth(1)
        glScalef(scale/100, scale/100, scale/100)
        
        largura = 0
        for letra in palavra:
            largura += glutStrokeWidth(GLUT_STROKE_ROMAN, ord(letra) )
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(letra))
            

def DesenhaTodosElementos(model, id_TodosElentos):
    glNewList(id_TodosElentos, GL_COMPILE)
    
    glInitNames()
    
    glPushName(2) # 2 - Para desenho das Tubulacoes
    CriaDesenhoTubos(model, 2, GL_SELECT)
    glPopName()
    
    glPushName(1) # 1 - Para desenho dos PVs
    CriaDesenhoPVs(model, 1, GL_SELECT)    
    glPopName()
    
    glPushName(3) # 3 - Para desenho dos Perfis
    CriaDesenhoPerfis(model, 3, GL_SELECT)    
    glPopName()
    
    glEndList()