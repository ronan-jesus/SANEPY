# -*- coding: utf-8 -*-
""" Arquivo responsavel por chamar os outros do progra"""

import sys
import os
#sys.path.insert(0, "C:\Python27\Lib\site-packages")
sys.path.insert(0, "MODEL/")
sys.path.insert(1, "GUI/")
sys.path.insert(2, "AUXILIARES/")
sys.path.insert(3, "CALCULOS/")
sys.path.insert(4, "IMGs/")
sys.path.insert(5, "DLLs/")
sys.path.insert(6, "GRAFICOS/")


import wx
from AUXILIARES import *
from CALCULOS import *
from GUI.app import * 

def resource_path(relative):
    return os.path.join(os.environ.get("_MEIPASS2",os.path.abspath(".")),relative)

if __name__ == '__main__':
    APP = wx.App(redirect=False)
    App(None)
    APP.MainLoop()