# -*- coding: utf-8 -*-

class Linha(object):
    def __init__(self, p1, p2):
        self.coods = [p1, p2]
        
class commandLine(object):
    def __init__(self, parent):
        self.parent = parent
        self.p1 = None
        self.p2 = None
        
    def InicializaLinha(self, p):
        if (self.p1 == None and self.p2 == None):
            self.p1 = p
            
        elif (self.p1 != None and self.p2 == None):
            self.p2 = p
            
            
            self.parent.dadosDXF.graficos["LINES"].append([self.p1, self.p2])
            
            #self.parent.LINHAS.append(Linha(self.p1, self.p2))            
            self.reinicializaValores()              
            
            self.parent.ConeCanvas.AtualizaTodasAsGlList()
                
    def reinicializaValores(self):
        self.p1 = None
        self.p2 = None
            