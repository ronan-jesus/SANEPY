# -*- coding: utf-8 -*-
"""
Created on Tue Oct 09 02:13:30 2018

@author: RONAN TEODORO
"""

import ctypes
sane = ctypes.cdll.LoadLibrary("C:/PROGRAMAS PYTHON/SANEPY/App/AUXILIARES/sanepyCore.dll")


def Declividade(compr, desnivel):
    sane.Inclinacao.argtypes = [ctypes.c_float, ctypes.c_float]
    sane.Inclinacao.restype = ctypes.c_float
    
    res = sane.Inclinacao(compr, desnivel)
    
    return res