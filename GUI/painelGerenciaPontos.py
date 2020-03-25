# -*- coding: utf-8 -*-
"""
Created on Sat Oct 06 23:54:02 2018

@author: RONAN TEODORO
"""
import sys, os
import wx
import wx.grid

from AUXILIARES.ImportDXF_ezdxf import ImportaArquivoDXF

class PainelGerenciaPontos(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,-1 ), 0 )
        self.parent = parent

        # Grid
        self.CreateGrid( 5, 6 )
        self.EnableEditing( True )
        self.EnableGridLines( True )
        self.EnableDragGridSize( False )
        self.SetMargins( 0, 0 )
        
        # Columns
        self.EnableDragColMove( False )
        self.EnableDragColSize( True )
        self.SetColLabelSize( 30 )
        self.SetColLabelValue( 0, u"ID" )
        self.SetColLabelValue( 1, u"Número" )
        self.SetColLabelValue( 2, u"Descrição" )
        self.SetColLabelValue( 3, u"x" )
        self.SetColLabelValue( 4, u"y" )
        self.SetColLabelValue( 5, u"z" )
        self.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
        
        # Rows
        self.EnableDragRowSize( True )
        self.SetRowLabelSize( 0 )
        self.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
        
        # Label Appearance
        
        # Cell Defaults
        self.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        
        self.populaGrid()
        
    def InsertValoresLinha(self, dados):
        pass
    
    def populaGrid(self):
        dadosDXF = ImportaArquivoDXF("E:\\PROGRAMAS_PYTHON\\SANEPY\\ARQUIVOS\\ficticia_esgoto.dxf")
        pontos = dadosDXF.graficos["POINTS"]
        try:
            self.ClearGrid()
            self.GetTable().InsertRows(pos = 0, numRows = len(pontos))
            for index, ponto in enumerate(pontos):
                self.SetCellValue(index,0, str(index))
                self.SetCellValue(index,1, str(index+100))
                self.SetCellValue(index,2, str("ponto "+str(index)))
                self.SetCellValue(index,3, str(ponto[0]))
                self.SetCellValue(index,4, str(ponto[1]))
                self.SetCellValue(index,5, str(ponto[2]))
        except Exception as e:
            if True:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print (e)
        
    def OnChangePanel(self, event):
        self.SetSizeGridPontos()
    
    def SetSizeGridPontos(self):
        self.Size = (self.Size[0], self.Size[1]-20)    
    