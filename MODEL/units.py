# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 00:53:56 2017

@author: RONAN TEODORO
"""
class Unidade(object):    
    def __init__(self, modulo, tipo):        
        self._valor = modulo
        self._tipo = tipo    
        
    @property
    def valor(self):        
        print "agora o valor foi pegado"
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        self._valor = valor
        print "O valor foi settado"
    
    def ConverteTOmetro(self):
        pass
    
    def MetroTOUnidade(self):
        pass
    
    def __call__(self):
        print "ASASAS"
        return self.__valor
    
Fx = Unidade(10, 'm')

Fx.valor = 30
    
