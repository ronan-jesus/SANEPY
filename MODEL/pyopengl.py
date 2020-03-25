#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import sys

import wx
from wx import glcanvas
from wx.glcanvas import WX_GL_DEPTH_SIZE
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


from camera3d import Camera3d

from formasOpengl import *
from OpenGL.raw.GL.VERSION.GL_1_0 import glNewList, glEndList, glCallList
from OpenGL.raw.GL.VERSION.GL_1_1 import GL_COMPILE

from OpenGL.GL import GLuint
from OpenGL.raw import GL

from OpenGL.arrays import ArrayDatatype as ADT

from AUXILIARES.imagens_do_app import *
from PIL import Image

#attribs=[WX_GL_DEPTH_SIZE,16,0,0]
#_OpenGL.ERROR_CHECKING = False

class MyCanvasBase(glcanvas.GLCanvas,  glcanvas.GLContext):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)#, attribList=None, name='GLCanvas')
        self.init = False
        self.context = glcanvas.GLContext(self)

        self.parent = parent

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        
        # DEFINICAO DOS PARAMETROS DE VIZUALIZACAO
        self.obsx = 20479
        self.obsy = 65271
        self.obsz = 50
        self.alvox = 20479
        self.alvoy = 65271
        self.alvoz = 0
        self.upx = 0
        self.upy = 1
        self.upz = 0

        self.Camera = Camera3d(self)

        self.Camera.SetCamera([self.obsx,self.obsy,self.obsz],
                              [self.alvox,self.alvoy,self.alvoz],
                              [self.upx,self.upy,self.upz])
        # initial mouse position
        self.lastx = 0
        self.lasty = 0
        self.posAnteriorX, self.posAnteriorY = 0, 0

        # Definicao das Variaveis de deslocamentos para a funcao de PAN
        self.deslocamentoX = 0
        self.deslocamentoY = 0
        self.deslocamentoZ = 0

        self.size = None

        

        myCursor= wx.Cursor(wx.CURSOR_CROSS)
        self.SetCursor(myCursor)
        
    def InitEstrutura(self):
        self.ParametrosVizualizacao()

    def OnEraseBackground(self, event):
        pass # Do nothing, to avoid flashing on MSW.

    def OnSize(self, event):
        size = self.size = self.GetClientSize()
        self.SetCurrent(self.context)
        glViewport(0, 0, size.width, size.height)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw(None)


    def OnMouseWheel(self, evt):
        """
        Funcao para a rotina da rodinha do mouse -> ZOOM
        """
        size = self.size = self.GetClientSize()


        if evt.GetWheelRotation() > 0:
            #self.angle += 1
            #self.Camera.angle += 1
            self.Camera.Zoom("+", evt, size)

        elif evt.GetWheelRotation() < 0:
            #self.angle -= 1
            #self.Camera.angle -= 1
            self.Camera.Zoom("-", evt, size)

        self.ParametrosVizualizacao()
        self.Refresh()
        evt.Skip()

    def OnMiddleDown(self, evt):
        pass

    def OnKeyDown(self, evt):
        if evt.GetKeyCode() == 13: #seta para direita
            self.Camera.KeyEvent(evt,"Enter")
        elif evt.GetKeyCode() == 27: #TECLA ESC
            self.parent.LimpaSelecao()            
        elif evt.GetKeyCode() == 127: #TECLA DELETE           
           self.parent.ExcluiElementosSelecionados("TUDO")
        
        self.AtualizaDesenhoTodosElementos()
        self.ParametrosVizualizacao()
        evt.Skip()

    def ZoomAll(self, evt):
        self.Camera.ZoomAll(evt)
        evt.Skip()

    def pickRects(self, x, y, evt, **kwargs):
        try:
            FlagTipoSelecao = 1
            buffer = glSelectBuffer(512)
            projection = glGetDoublev(GL_PROJECTION_MATRIX)
            viewport = glGetIntegerv(GL_VIEWPORT)

            glMatrixMode(GL_PROJECTION)

            glPushMatrix()
            glLoadIdentity()

            #Verifica o tipo de selecao se e pontual o retangulo de selecao
            if (self.parent.RecSelect[2] == None):
                gluPickMatrix(x, viewport[3]-y, 10, 10, viewport)
            else:
                #OTIMIZAR ESTA PARTE DO CODIGO
                FlagTipoSelecao = 2                
                xp1 = kwargs["retangulo"][1][0]
                yp1 = kwargs["retangulo"][1][1]
                xp2 = kwargs["retangulo"][3][0]
                yp2 = kwargs["retangulo"][3][1]
                if (abs(yp1-yp2)==0 or abs(xp1-xp2)==0):
                    gluPickMatrix(x, viewport[3]-y, 5, 5, viewport)
                else:
                    gluPickMatrix((xp1+xp2)/2, (viewport[3]-(yp1+yp2)/2), abs(xp1-xp2), abs(yp1-yp2), viewport)

            self.Camera.GetModeCamera3D()

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

            glRenderMode(GL_SELECT)
            
            self.Camera.CameraLookAt()
            
            #self.AtualizaDesenhoTodosElementos()
            glCallList(self.id_TodosElentos)
            
            glMatrixMode(GL_PROJECTION)
            glPopMatrix()

            glMatrixMode(GL_MODELVIEW)
            glFlush()

            hits = glRenderMode(GL_RENDER)
            
            elementos = self.ProcessaSelecao(hits, len(hits), FlagTipoSelecao)
            print (elementos)
            return elementos
            
        except Exception as e:
            if self.parent.emDesenvolvimento == True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)  
                print (e)
            else:
                pass
        finally:
            self.AtualizaDesenhoPvs()
            self.AtualizaDesenhoTubos()  

    def ProcessaSelecao(self, hits, selecao, flagselecao):
        elementos = []
        if len(hits) != 0:
            for elemento in hits:
                min_depth, max_depth, self.names = elemento
                elementos.append(self.names)
            if flagselecao == 2:
                return elementos
            else:
                if hits[-1][2] !=None:
                    _elem = [len(x) for x in elementos]
                    imax = _elem.index(max(_elem))
                    return [elementos[imax]]
                else:
                    return []
        else:
            return []

    def SetPointsSize(self):
        #SETA O DIAMETRO DO PONTO PRIMITIVA QUE REPRESENTA OS 'NOS'.
        #COM o VALOR DEFINIDO NA CONSTANTE TAMANHO_DOS_NOS em MODEL
        glPointSize(self.parent.TAMANHO_DOS_NOS)

class ConeCanvas(MyCanvasBase):
    def InitGL( self ):
        self.numPVMover = None
        self.numPVRotacionar = None
        self.numPVLabelArrastar = None
        self.pvEmMovimento = False
        self.pvEmRotacao = False
        self.labelEmMovimento = False
       
        
        self.FLAG_ROTATION = "Rotation_off"
        self.id_EixosGlobais = 1
        self.id_Pvs = 2
        self.id_Tubos = 3
        self.id_EixosBarras = 4       
        
        self.id_Terreno = 5
        self.id_Dxf = 6      
        self.id_TodosElentos = 7      
        self.id_Perfis = 8     
        

        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouse_LeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouse_LeftUp)

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnMouse_RightDown)
        self.Bind(wx.EVT_RIGHT_UP, self.OnMouse_RightUp)

        self.Bind(wx.EVT_MIDDLE_DOWN, self.OnMidleMouseDown)
        self.Bind(wx.EVT_MIDDLE_UP, self.OnMidleMouseUp)

        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseWheel)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        
        # Initialize
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        #DEFINE A COR DE UTILIZACAO CORRENTE
        glColor3f(1.0, 1.0, 0.0)       

        #SETA A ESPESSURA DA LINHA PRIMITIVA
        glLineWidth(1.0)

        #SETA O DIAMETRO DO PONTO PRIMITIVA QUE REPRESENTA OS 'NOS'.
        glPointSize(self.parent.TAMANHO_DOS_NOS)
        glEnable(GL_POINT_SMOOTH)#NECESSARIO PARA APRESENTAR PONTOS CIRCULARES
        glEnable(GL_BLEND)#NECESSARIO PONTOS CIRCULARES
        glEnable(GL_COLOR_MATERIAL)#NECESSARIO PONTOS CIRCULARES
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)#NECESSARIO PONTOS CIRCULARES        
        
        self.ParametrosVizualizacao()

        glutInit(sys.argv)
        glutInitDisplayMode (GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGB)        
        glEnable(GL_DEPTH_TEST)
        
        self.AtualizaTodasAsGlList()

    def AtualizaTodasAsGlList(self):
        """Atualiza todas as glList, para atualizar os desenhos que sao
        chamados por glCallList()"""
        self.AtualizaDesenhoEixosBarras()
        self.AtualizaDesenhoEixosGlobais()
        self.AtualizaDesenhoTubos()
        self.AtualizaDesenhoPvs()
        self.AtualizaDesenhoDXF()        
        self.AtualizaDesenhoTerreno()
        self.AtualizaDesenhoTodosElementos()
        self.AtualizaDesenhoPerfis()
        self.ParametrosVizualizacao()



    def AtualizaDesenhoEixosBarras(self):
        """Metodo para atualizar o desenho dos eixos das barras, sempre sera
        chamado depois de alguma mudanca nas barras, podendo ser uma mudanca
        da inclinacao da secao, inversao do sentido da barra ou mesmo inserindo
        ou apagando uma barra.

        Altera a glList(id_EixosBarras)
        """
        CriaEixosDasBarra(self.parent, self.id_EixosBarras)

    def AtualizaDesenhoEixosGlobais(self):
        """Metodo para atualizar o desenho dos Eixos Globais, devera ser
        chamada sempre que os Eixos Globais sofrerem alteracao, seja no
        tamanho dos Eixos ou mesmo posicao dos Eixos.

        Altera a glList(id_EixosGlobais)
        """
        CriaDesenhoEixosGlobais(self.parent, self.id_EixosGlobais)

        
    def AtualizaDesenhoTubos(self):
        """Metodo para atualizar o desenho das barras,

        Altera a glList(id_Tubos)
        """
        CriaDesenhoTubos(self.parent, self.id_Tubos)
        CriaDesenhoTerreno(self.parent, self.id_Terreno, GL_RENDER)
        
    def AtualizaDesenhoPvs(self):
        """Metodo para atualizar o desenho das barras,

        Altera a glList(id_Pvs)
        """
        CriaDesenhoPVs(self.parent, self.id_Pvs, GL_RENDER)
        
    def AtualizaDesenhoDXF(self):
        """Metodo para atualizar o desenho das barras,

        Altera a glList(id_Pvs)
        """
        CriaDesenhoDXF(self.parent, self.id_Dxf, GL_RENDER)
        
    def AtualizaDesenhoTerreno(self):
        """Metodo para atualizar o desenho dos Terreno,

        Altera a glList(id_Pvs)
        """
        CriaDesenhoTerreno(self.parent, self.id_Terreno, GL_RENDER)
        
    def AtualizaDesenhoPerfis(self):
        """Metodo para atualizar o desenho dos Perfis,

        Altera a glList(id_Perfis)
        """
        CriaDesenhoPerfis(self.parent, self.id_Perfis, GL_RENDER)
        
    def AtualizaDesenhoTodosElementos(self):        
        DesenhaTodosElementos(self.parent, self.id_TodosElentos)
        

    def OnMouseMotion(self, evt):
        self.x, self.y = evt.GetPosition()
        if (self.parent.FLAG_DESENHO == "SELECT" and evt.LeftIsDown()):
            if evt.Dragging():
                self.parent.RecSelect[2] = self.x
                self.parent.RecSelect[3] = self.y
        else:
            self.Camera.MouseEvent(self.x, self.y, evt)        
        
        self.ParametrosVizualizacao()
        evt.Skip()
    
    
    def OnMouse_LeftDown(self, evt):
        self.x, self.y = evt.GetPosition()
        
        self.parent.RecSelect[0], self.parent.RecSelect[1] = self.x, self.y
        
        selecao = self.pickRects(self.x, self.y, evt, retangulo=[])        
        self.parent.CliqueBtnEsquerdoDown(selecao, self.x, self.y)
        
        evt.Skip()
        
    def OnMouse_LeftUp(self, evt):
        selected = self.parent.selected  
        
        #Para Caso a Selecao for Retangular
        if self.parent.FLAG_DESENHO == "SELECT":
            if None in self.parent.RecSelect:
                if self.parent.ON_PERFIL[0] == True:
                    x, y = self.GetCoordMundo(self.x, self.y)
                    self.parent.CriaPerfil(x, y)
                else:
                    elem = self.pickRects(self.x, self.y, evt)    
                    self.parent.AdicionaElementosListaSelecao(elem, evt)
            elif None not in self.parent.RecSelect:
                retangulo = self.parent.VerificaSelecao()    
                elem = self.pickRects(self.x, self.y, evt, retangulo=retangulo)    
                self.parent.AdicionaElementosListaSelecao(elem, evt)
                self.parent.RecSelect = [None, None, None, None]
                
        elif self.parent.FLAG_DESENHO == "BARRA":
            elem = self.pickRects(self.x, self.y, evt)
            self.parent.CriaBarra(elem)

        elif self.parent.FLAG_DESENHO == "NO":
            _x, _y = self.GetCoordMundo(self.x, self.y)        
            self.parent.InserePV(_x, _y)            
            self.AtualizaDesenhoPvs()        
                
        self.AtualizaDesenhoTodosElementos()        
        
        self.ParametrosVizualizacao()
        evt.Skip()

    def OnMouse_RightDown(self, evt):
        self.x, self.y = evt.GetPosition()        
        try:
            selecao = self.pickRects(self.x, self.y, evt)
            
            self.parent.VerificaClickButtonRightDown(selecao, self.x, self.y, evt)
        
        except Exception as e:
            if self.parent.emDesenvolvimento == True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
            else:
                pass

        evt.Skip()

    def OnMouse_RightUp(self, evt):
        self.FLAG_ROTATION = "Rotation_off"

        if self.parent.FLAG_DESENHO == "SELECT":
            if  None not in self.parent.RecSelect:
                retangulo = self.parent.VerificaSelecao()    
                self.pickRects(self.x, self.y, evt, retangulo=retangulo)    
                self.parent.RecSelect = [None, None, None, None]
                
        elif self.parent.FLAG_DESENHO == "BARRA":
            pass
        elif self.parent.FLAG_DESENHO == "NO":
            pass

        self.ParametrosVizualizacao()
        evt.Skip()
        
    def OnMidleMouseDown(self, evt):
        self.Camera.posAnteriorX = evt.GetPosition()[0]
        self.Camera.posAnteriorY = evt.GetPosition()[1]

        image = img_pan_fechada.GetImage()
        image.SetOption(wx.IMAGE_OPTION_CUR_HOTSPOT_X, 0)
        image.SetOption(wx.IMAGE_OPTION_CUR_HOTSPOT_Y, 0)
        self.SetCursor(wx.Cursor(image))

    def OnMidleMouseUp(self, evt):
        if self.parent.FLAG_DESENHO == "PAN":
            image = img_pan_aberta.GetImage()
            image.SetOption(wx.IMAGE_OPTION_CUR_HOTSPOT_X, 0)
            image.SetOption(wx.IMAGE_OPTION_CUR_HOTSPOT_Y, 0)
            self.SetCursor(wx.CursorFromImage(image))
        else:
            self.SetCursor(wx.Cursor(wx.CURSOR_DEFAULT))

    def ParametrosVizualizacao(self):
        #COLOCA A MATRIZ DO MODELO NA MATRIZ DE UTILIZACAO
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        #Seta o Aspecto da Viewport para nao distorcer as imagens
        size = self.GetClientSize()
        self.Camera.ViewPortAspect(size[0], size[1])
        #POSICIONA O OBSERVADOR
        self.Camera.CameraLookAt()

        self.Refresh()

    def DrawEstrutura(self, mode):
        """Desenha todos os elementos da estrutura, NOS, BARRAS,
        CARGAS DISTRIBUIDAS, CARGAS CONCENTRADAS e os Diagramas de Solicitacoes.
        """
        if self.parent.MOSTRAR_NOS == True:
            #DESENHA OS NOS DA ESTRUTURA, devera ser desenhado separado dos outros
            #elementos, uma vez que usa o 'mode' para fazer o picking de selecao
            try:
                glCallList(self.id_TodosElentos)
            except Exception as e:
                if self.parent.emDesenvolvimento == True:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                    print (e)
                else:
                    pass
                
        if self.parent.MOSTRAR_BARRAS == True:
            #DESENHA OS NOS DA ESTRUTURA, devera ser desenhado separado dos outros
            #elementos, uma vez que usa o 'mode' para fazer o picking de selecao
            try:
                #glCallList(self.id_Tubos)
                glCallList(self.id_Dxf)
                glCallList(self.id_Terreno)
                #glCallList(self.id_Perfis)
            except Exception as e:
                if self.parent.emDesenvolvimento == True:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                    print (e)
                else:
                    pass

        try:
            #Caso Esteja desenhando a estrutura no modo RENDER,
            #nao desenha as outras esruturas, pois senao dara problema
            #na funcao de picking(select) dos NOS e BARRAS
            if mode == GL_RENDER:
                pass
            else: #Caso nao esteja desenhando no modo RENDER, desenha o Resto
                if self.parent.MOSTRAR_EIXOS_GLOBAIS == True:
                        glCallList(self.id_EixosGlobais)#Chama a glList(id_EixosGlobais)
                else:
                    pass                    
                        
        except Exception as e:            
            if self.parent.emDesenvolvimento == True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
            else:
                pass
        
        try:
            self.DesenhaPVMover(self.parent.Estrututura.PV.PVMover, self.x, self.y)
        except Exception as e:
            if self.parent.emDesenvolvimento == True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
            else:
                pass
            
        try: 
            self.DesenhaPVRotacionar(self.parent.Estrututura.PV.PVRotacionar, self.x, self.y)
        except Exception as e:
            if self.parent.emDesenvolvimento == True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)                
            else:
                pass
            
        try: 
            self.DesenhaPVLabelMover(self.parent.Estrututura.PV.PVLabelArrastar, self.x, self.y)
        except Exception as e:
            if self.parent.emDesenvolvimento == True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)                
            else:
                pass
        try:    
            if hasattr(self.parent, "LISTA_PERFIS"):
                for perfil in self.parent.LISTA_PERFIS:                    
                    if perfil == self.parent.OBJETO_SELECIONADO:
                        perfil.DesenhaPerfilMovimento(self.x, self.y)
        except Exception as e:
            if self.parent.emDesenvolvimento == True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)                
            else:
                pass

    def OnDraw(self, mode=None):
        # LIMPA OS BUFFERS DE COR E PROFUNDIDADE
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        #DESENHA ESTRUTURA
        self.DrawEstrutura(mode)        
        self.Desenha2D()
        try:
            self.DesenhaTela2D()
        except Exception as e:
            if self.parent.emDesenvolvimento == True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
            else:
                pass      
        
        
        self.SwapBuffers()

    def BarraDesenhada(self, modelview, projection, viewport, size):
        if (self.parent.STATUS_BARRA == 2 and self.parent.ON_BARRA[0]>-1):        
            try:             
                NO1 = self.parent.Estrututura.Dic_Lista_Pvs[self.parent.ON_BARRA[0]]
                coordenadas = gluProject(NO1.pos[0], NO1.pos[1], NO1.pos[2], modelview, projection, viewport)
                x, y = coordenadas[0], size[1]-coordenadas[1]
            
                glEnable (GL_LINE_STIPPLE)
                glLineStipple(1, 0xFFF)
                glColor3ub(50,205,50)
                glLineWidth (3.0)
                
                glBegin(GL_LINES)
                glVertex3f(x,y, 0)
                glVertex3f(self.x, self.y, 0)
                glEnd()
                glDisable(GL_LINE_STIPPLE)
                glLineWidth (1.0)
                
    
            except Exception as e:
                if self.parent.emDesenvolvimento == True:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                    print (e)
                else:
                    pass
            finally:
                glLineWidth (1.0)
                
    def DesenhaTela2D(self):
        glPushMatrix()
        projection = glGetDoublev(GL_PROJECTION_MATRIX)
        viewport = glGetIntegerv(GL_VIEWPORT)
        modelview = glGetDoublev(GL_MODELVIEW_MATRIX)    
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
    
        glOrtho(viewport[0], viewport[2], viewport[3], viewport[1], 0, 1)
        
        size = self.GetClientSize()

        self.VerificaSnap(modelview, projection, viewport, size)
        self.BarraDesenhada(modelview, projection, viewport, size)
        if hasattr(self.parent, "LISTA_PERFIS"):
            for perfil in self.parent.LISTA_PERFIS:
                perfil.DesenhaSnapPerfil([modelview, projection, viewport, size])
                perfil.DesenhaSnapsPVs(modelview, projection, viewport, size)
                perfil.DesenhaTickMouse(self.x, self.y, self.parent, modelview, projection, viewport, size)
        glPopMatrix()
        
        
    def Desenha2D(self):
        if None in self.parent.RecSelect:
            pass
        else:
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            viewport = glGetIntegerv(GL_VIEWPORT)
            glOrtho(viewport[0], viewport[2], viewport[3], viewport[1], 0, 1)

            glEnable (GL_LINE_STIPPLE)
            glLineStipple(1, 0xFFF)
            glColor3f(0.0, 0.0, 1.0)
            glLineWidth (1.0)

            x1 = self.parent.RecSelect[0]
            y1 = self.parent.RecSelect[1]
            x2 = self.parent.RecSelect[2]
            y2 = self.parent.RecSelect[3]

            pontos = self.parent.DrawRetangulo(x1,y1,x2,y2)

            glBegin(GL_LINES)
            glVertex3f(pontos[1][0],pontos[1][1], 0)
            glVertex3f(pontos[2][0],pontos[2][1], 0)

            glVertex3f(pontos[2][0],pontos[2][1], 0)
            glVertex3f(pontos[3][0],pontos[3][1], 0)

            glVertex3f(pontos[3][0],pontos[3][1], 0)
            glVertex3f(pontos[4][0],pontos[4][1], 0)

            glVertex3f(pontos[4][0],pontos[4][1], 0)
            glVertex3f(pontos[1][0],pontos[1][1], 0)

            glEnd()

            glDisable (GL_LINE_STIPPLE)

    def VerificaSnap(self, modelview, projection, viewport, size):
        try:            
            SELECT_SNAP = self.parent.selectedSnap
            
            if len(SELECT_SNAP) != 0:
                if len(SELECT_SNAP[0])== 5:
                    xpos, ypos = self.parent.GetPositionElemSelect(SELECT_SNAP[0])
                    
                    coordenadas = gluProject(xpos, ypos, 0, modelview, projection, viewport)
                    x, y = coordenadas[0], size[1]-coordenadas[1]
                    
                    glPushMatrix()
                    glColor3ub(50,205,50)
                    glLineWidth (3.0)
    
                    glBegin(GL_LINES)
                    glVertex3f(x-5,y-5, 0)
                    glVertex3f(x-5,y+5, 0)
    
                    glVertex3f(x-5,y+5, 0)
                    glVertex3f(x+5,y+5, 0)
    
                    glVertex3f(x+5,y+5, 0)
                    glVertex3f(x+5,y-5, 0)
    
                    glVertex3f(x+5,y-5, 0)
                    glVertex3f(x-5,y-5, 0)
                    glEnd()
                    glPopMatrix() 
                    
#            try:
#                dadosVizualizacao = [modelview, projection, viewport, size]
#                if self.parent.selectedSnap[0] > 30000:
#                    #Se o ponto for o ponto de arraste da label
#                    num = self.parent.selectedSnap[0]-30000
#                    PV = self.parent.Estrututura.Dic_Lista_Pvs[num]
#                    PV.Label.DesenhaPontoSnapLabel(dadosVizualizacao)
#                    
#                elif self.parent.selectedSnap[0] > 20000:
#                    #Se o ponto for o ponto de rotacao
#                    num = self.parent.selectedSnap[0]-20000
#                    PV = self.parent.Estrututura.Dic_Lista_Pvs[num]
#                    PV.DesenhaPontoSnapRotacao(dadosVizualizacao)
#                    
#                elif self.parent.selectedSnap[0] > 10000:
#                    #Se o ponto for o ponto de arraste
#                    num = self.parent.selectedSnap[0]-10000                    
#                    PV = self.parent.Estrututura.Dic_Lista_Pvs[num]
#                    coordenadas = gluProject(PV.pos[0], PV.pos[1], PV.pos[2], modelview, projection, viewport)
#    
#                    x, y = coordenadas[0], size[1]-coordenadas[1]
#                    
#                    glPushMatrix()
#                    glColor3ub(50,205,50)
#                    glLineWidth (3.0)
#    
#                    glBegin(GL_LINES)
#                    glVertex3f(x-5,y-5, 0)
#                    glVertex3f(x-5,y+5, 0)
#    
#                    glVertex3f(x-5,y+5, 0)
#                    glVertex3f(x+5,y+5, 0)
#    
#                    glVertex3f(x+5,y+5, 0)
#                    glVertex3f(x+5,y-5, 0)
#    
#                    glVertex3f(x+5,y-5, 0)
#                    glVertex3f(x-5,y-5, 0)
#                    glEnd()
#                    glPopMatrix()                

        except Exception as e:                
            if self.parent.emDesenvolvimento == True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
            else:
                pass
        finally:
            glLineWidth (1.0)


    def EscreveDeslocamentos2D(self):
        if self.parent.MOSTRAR_TEXTOS_DESLOCAMENTOS == True:
            try:
                NO = self.parent.selectedSnap = [hits[-1][2][0]]
                MostraTextoDeslocamentos()
    
            except Exception as e:
                if self.parent.emDesenvolvimento == True:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                    print (e)
                else:
                    pass
            finally:
                glLineWidth (1.0)
                
    
    def SNAPpickRects(self, x, y):
        pass
#        try:
#            buffer = glSelectBuffer(512)
#            viewport = glGetIntegerv(GL_VIEWPORT)
#
#            glMatrixMode(GL_PROJECTION)
#
#            glPushMatrix()
#            glLoadIdentity()
#
#            gluPickMatrix(x, viewport[3]-y, 10, 10, viewport)
#
#            self.Camera.GetModeCamera3D()
#
#            glMatrixMode(GL_MODELVIEW)
#            glLoadIdentity()
#
#            glRenderMode(GL_SELECT)
#            
#            self.Camera.CameraLookAt()
#            
#            glCallList(self.id_TodosElentos)
#            
#            glMatrixMode(GL_PROJECTION)
#            glPopMatrix()
#
#            glMatrixMode(GL_MODELVIEW)
#            glFlush()
#            
#            hits = glRenderMode(GL_RENDER)
#
#            self.parent.selectedSnap = self.ProcessaSelecao(hits, len(hits), 1)
#
#        except Exception as e:
#            self.parent.selectedSnap = []
#            if self.parent.emDesenvolvimento == True:
#                exc_type, exc_obj, exc_tb = sys.exc_info()
#                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#                print(exc_type, fname, exc_tb.tb_lineno)
#                print (e)
#            else:
#                pass
    
    
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
        
        glPushMatrix()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        viewport = glGetIntegerv(GL_VIEWPORT)
        projection = glGetDoublev(GL_PROJECTION_MATRIX)        
        modelview = glGetDoublev(GL_MODELVIEW_MATRIX)    

        mouse_y = viewport[3]-mouse_y
        
        
        x, y, z = gluUnProject(mouse_x, mouse_y, 0, modelview, projection, viewport)
        
        glPopMatrix()
        
        glLoadIdentity()
        
        return x, y
        
    def GetCoordTela(self, pos_x, pos_y):         
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
        
        glPushMatrix()
        glLoadIdentity()
        projection = glGetDoublev(GL_PROJECTION_MATRIX)
        viewport = glGetIntegerv(GL_VIEWPORT)
        modelview = glGetDoublev(GL_MODELVIEW_MATRIX)    
        size = [viewport[2], viewport[3]]
        
        coordenadas = gluProject(pos_x, pos_y, 0, modelview, projection, viewport)
        x, y = coordenadas[0], size[1]-coordenadas[1]
        
        glPopMatrix()
        return x, y
    
    
    def DesenhaPVRotacionar(self, numPv, x, y):
        PV = self.parent.Estrututura.Dic_Lista_Pvs[numPv]
        x, y = self.GetCoordMundo(x, y)      
        
        glPushMatrix()
        PV.DesenhaPvRotacionado(x, y)
        glPopMatrix()
        
        
    def DesenhaPVMover(self, numPv, x, y):
        PV = self.parent.Estrututura.Dic_Lista_Pvs[numPv]     
        x, y = self.GetCoordMundo(x, y)      
        glPushMatrix()
        glTranslate(x, y, 0)
        PV.DesenhaPVemMovimento()
        glPopMatrix()
        
    def DesenhaPVLabelMover(self, numPv, x, y):        
        PV = self.parent.Estrututura.Dic_Lista_Pvs[numPv]
        x, y = self.GetCoordMundo(x, y)        
        PV.Label.DesenhaLabel(x, y)        
        
    
    def Pyopengl2PNG(self, path):
        glPixelStorei(GL_PACK_ALIGNMENT, 1)
        data = glReadPixels(0, 0, self.size[0], self.size[1], GL_RGBA, GL_UNSIGNED_BYTE)
        image = Image.fromstring("RGBA", (self.size[0], self.size[1]), data)
        image_transposta = image.transpose(Image.FLIP_LEFT_RIGHT)
        image_rotacionada = image_transposta.rotate(180)
        image_rotacionada.save(path, 'PNG')
        
        
##CLASSE DO VERTEX BUFFER, UTILIZADA PARA ACELERAR OS DESENHOS DO PYOPENGL
#class VertexBuffer(object):
#
#    def __init__(self, data, usage):
#        self.buffer = GLuint(0)
#        glGenBuffers(1, self.buffer)
#        glBindBuffer(GL_ARRAY_BUFFER, self.buffer)
#        glBufferData(GL_ARRAY_BUFFER, ADT.arrayByteCount(data),
#                     ADT.voidDataPointer(data), usage)
#
#    def __del__(self):
#        glDeleteBuffers(1, GLuint(self.buffer))
#
#    def bind(self):
#        glBindBuffer(GL_ARRAY_BUFFER, self.buffer)
#
#    def bind_vertexes(self, size, type, stride=0):
#        self.bind()
#        glVertexPointer(size, type, stride, None)