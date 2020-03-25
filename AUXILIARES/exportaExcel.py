# -*- coding: utf-8 -*-
import os, sys
import xlwt
import wx

def resource_path(relative):
    return os.path.join(os.environ.get("_MEIPASS2",os.path.abspath(".")),relative)
    
def resource_path2(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
        
class ExportaEstruturaExcel(object):
    """docstring for ExportaEstruturaExcel"""
    def __init__(self, model, estrutura, event):
        super(ExportaEstruturaExcel, self).__init__()
        self.model = model
        self.Estrutura = estrutura
        self.event = event
        self.workbook = xlwt.Workbook()
        self.caminho = None
        self.SalvaEstrutura()
        #self.EscreveDadosEstrutura()
    
    
    
    def EscreveDadosBarras(self):
        # add new colour to palette and set RGB colour value
        xlwt.add_palette_colour("azul_claro", 0x21)
        xlwt.add_palette_colour("rosa_salmao", 0x22)
        xlwt.add_palette_colour("azul_escuro", 0x23)
        xlwt.add_palette_colour("verde_cinza", 0x24)
        self.workbook.set_colour_RGB(0x21, 228, 223, 236)
        self.workbook.set_colour_RGB(0x22, 253, 233, 217)
        self.workbook.set_colour_RGB(0x23, 218, 238, 243)
        self.workbook.set_colour_RGB(0x24, 235, 241, 222)
                   
        ws = self.workbook.add_sheet(u'DIMENSIONAMENTO')

        ws.set_panes_frozen(True)
        ws.set_horz_split_pos(4) 
        ws.set_vert_split_pos(4)
    
        ws.write_merge(0,0,0,3, u'', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: top_color black, bottom_color black,\
                                right_color black, left_color black, left medium,\
                                right medium, top medium, bottom medium;\
                                pattern: pattern solid, fore_colour azul_claro;'))
                                
        ws.write_merge(0,0,4,45, u'DIMENSIONAMENTO DA REDE DE ESGOTO - SANEPY', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: top_color black, bottom_color black,\
                                right_color black, left_color black, left medium,\
                                right medium, top medium, bottom medium;\
                                pattern: pattern solid, fore_color azul_claro;'))
                                
        ws.write_merge(1,3,0,0, u'COLETOR', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: top_color black, bottom_color black,\
                                top medium, bottom medium,  left dotted, right dotted; pattern: pattern solid,\
                                fore_color rosa_salmao;'))
                                
        ws.write_merge(1,2,1,2, u'PV nº', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: top_color black, top medium, bottom dotted; pattern: pattern solid, fore_color rosa_salmao;'))
        
        ws.write(3,1, u'M', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color rosa_salmao'))
                                
        ws.write(3,2, u'J', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color rosa_salmao'))
        
        ws.write_merge(1,3,3,3, u'COMP. TRECHO (m)', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: top_color black, bottom_color black, right_color black,\
                                left_color black,  top medium, bottom medium, right medium, left dotted; pattern: pattern solid,\
                                fore_color rosa_salmao;'))
                                
        ws.write_merge(1,1,4,5, u'VAZÕES (L/s)', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: top_color black, top medium, right_color black, left_color black, bottom dotted, left medium,\
                                right medium; pattern: pattern solid, fore_color azul_escuro;'))
                                
        ws.write_merge(2,2,4,5, u'ADOTADAS', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, top dotted, bottom dotted, left medium, right medium;pattern: pattern solid, fore_color azul_escuro'))
                                
        ws.write(3,4, u'Inicial', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: bottom_color black, top dotted, bottom medium, left medium, right dotted;pattern: pattern solid, fore_color azul_escuro'))
                                
        ws.write(3,5, u'Final', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right medium;pattern: pattern solid, fore_color azul_escuro'))
        
        ws.write_merge(1,2,6,7, u'COTA DO TERRENO', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: top_color black, top medium, bottom dotted, left medium, right medium, right_color black, left_color black, left medium,\
                                right medium; pattern: pattern solid, fore_color rosa_salmao;'))

        ws.write(3,6, u'M', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: bottom_color black, top dotted, bottom medium, left medium, right dotted, left_color black;pattern: pattern solid, fore_color rosa_salmao'))
                                
        ws.write(3,7, u'J', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right medium;pattern: pattern solid, fore_color rosa_salmao'))

        ws.write_merge(1,1,8,12, u'DECLIVIDADES', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: top_color black, top medium, right_color black, left_color black, top medium, bottom dotted, left medium,\
                                right medium; pattern: pattern solid, fore_color verde_cinza;'))
        
        ws.write_merge(2,3,8,8, u'MÍNIMA', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom medium, left medium,\
                                right dotted; pattern: pattern solid, fore_color verde_cinza;'))
                                
        ws.write_merge(2,3,9,9, u'RUA', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: bottom_color black, top dotted, bottom medium, left dotted,\
                                right dotted; pattern: pattern solid, fore_color verde_cinza;'))
                                
        ws.write_merge(2,3,10,10, u'ADOTADA', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: bottom_color black, top dotted, bottom medium, left dotted,\
                                right dotted; pattern: pattern solid, fore_color verde_cinza;'))
                                
        ws.write_merge(2,3,11,11, u'AJUSTE DECLIV.', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, top dotted, bottom medium, left dotted,\
                                right dotted; pattern: pattern solid, fore_color verde_cinza;'))
        
        ws.write_merge(2,3,12,12, u'DESNÍVEL', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right medium, ;pattern: pattern solid, fore_color verde_cinza'))
        
        ws.write_merge(1,1,13,15, u'DIÂMETROS', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: top_color black, right_color black, left_color black,top medium, bottom dotted, left medium,\
                                right medium; pattern: pattern solid, fore_color rosa_salmao;'))
        
        ws.write_merge(2,3,13,13, u'DIÂMETRO (mm)', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom medium, left medium,\
                                right dotted; pattern: pattern solid, fore_color rosa_salmao;'))
                                
        ws.write_merge(2,3,14,14, u'ESPESSURA', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: bottom_color black, top dotted, bottom medium, left dotted,\
                                right dotted; pattern: pattern solid, fore_color rosa_salmao;'))
         
        ws.write_merge(2,3,15,15, u'CONF. DIÂM.', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, right dotted, right medium;pattern: pattern solid, fore_color rosa_salmao'))
                                
        ws.write_merge(1,1,16,23, u'CÁLCULO DA VELOCIDADE', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: top_color black, top medium, right_color black, left_color black, top medium, bottom dotted, left medium,\
                                right medium; pattern: pattern solid, fore_color verde_cinza;'))
        
        ws.write_merge(2,3,16,16, u'Vo', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom medium, left medium,\
                                right dotted; pattern: pattern solid, fore_color verde_cinza;'))
                                
        ws.write_merge(2,3,17,17, u'Qo', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom medium, left dotted,\
                                right dotted; pattern: pattern solid, fore_color verde_cinza;'))
                                
        ws.write_merge(2,2,18,19, u'Q/Qo', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom dotted, left dotted,\
                                right dotted; pattern: pattern solid, fore_color verde_cinza;'))
        
        ws.write(3,18, u'Inicial', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                
        ws.write(3,19, u'Final', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted,;pattern: pattern solid, fore_color verde_cinza'))
                                
        ws.write_merge(2,2,20,21, u'V/Vo', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom dotted, left dotted,\
                                right dotted; pattern: pattern solid, fore_color verde_cinza;'))
                                
        ws.write(3,20, u'Inicial', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))   
                                
        ws.write(3,21, u'Final', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))  
        
        ws.write_merge(2,2,22,23, u'VELOCIDADE', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom dotted, left dotted,\
                                right medium; pattern: pattern solid, fore_color verde_cinza;'))
                                
        ws.write(3,22, u'Inicial', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))   
                                
        ws.write(3,23, u'Final', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right medium;pattern: pattern solid, fore_color verde_cinza'))                       
        
        ws.write_merge(1,1,24,31, u'CÁLCULO DA VELOCIDADE CRÍTICA (CASO h/D>0,50)', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: top_color black, right_color black, left_color black, top medium, bottom dotted, left medium,\
                                right medium; pattern: pattern solid, fore_color verde_cinza;'))
                                
        ws.write_merge(2,2,24,25, u'Rh/D', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom dotted, left dotted,\
                                right dotted; pattern: pattern solid, fore_color verde_cinza;'))
                                
        ws.write(3,24, u'Inicial', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left medium, right dotted;pattern: pattern solid, fore_color verde_cinza'))   
                                
        ws.write(3,25, u'Final', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))                                 
                                
        ws.write_merge(2,2,26,27, u'RAIO HIDRÁULICO', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom dotted, left dotted,\
                                right dotted; pattern: pattern solid, fore_color verde_cinza;'))
                                
        ws.write(3,26, u'Inicial', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))   
                                
        ws.write(3,27, u'Final', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))      
        
        ws.write_merge(2,2,28,29, u'VELOCIDADE CRÍTICA', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom dotted, left dotted,\
                                right dotted; pattern: pattern solid, fore_color verde_cinza;'))
                                
        ws.write(3,28, u'Inicial', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))   
                                
        ws.write(3,29, u'Final', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))      
         
        ws.write_merge(2,2,30,31, u'Vf>Vc', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom dotted, left dotted,\
                                right dotted; pattern: pattern solid, fore_color verde_cinza;'))
                                
        ws.write(3,30, u'Inicial', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))   
                                
        ws.write(3,31, u'Final', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right medium;pattern: pattern solid, fore_color verde_cinza'))                             
        
        ws.write_merge(1,2,32,33, u'COTA DE FUNDO DO COLETOR', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top medium, bottom dotted, left medium,\
                                right dotted; pattern: pattern solid, fore_color rosa_salmao;'))
                                
        ws.write(3,32, u'M', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left medium, right dotted;pattern: pattern solid, fore_color rosa_salmao'))   
                                
        ws.write(3,33, u'J', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color rosa_salmao'))
                                
        ws.write_merge(1,2,34,38, u'PROFUNDIDADE', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top medium, bottom dotted, left dotted,\
                                right medium; pattern: pattern solid, fore_color rosa_salmao;'))
                                
        ws.write(3,34, u'M', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color rosa_salmao'))   
                                
        ws.write(3,35, u'J', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color rosa_salmao'))
                                
        ws.write(3,36, u'Δh JUS.', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color rosa_salmao'))                   
        
        ws.write(3,37, u'RECOB.', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color rosa_salmao'))
                                
        ws.write(3,38, u'AJUSTE', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right medium;pattern: pattern solid, fore_color rosa_salmao'))      
        
        ws.write_merge(1,1,39,45, u'ALTURA DA LÂMINA D"ÁGUA', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: top_color black, bottom_color black, right_color black, left_color black, top medium, bottom dotted, left medium,\
                                right medium; pattern: pattern solid, fore_color azul_escuro;'))
        
        ws.write_merge(2,2,39,40, u'h/D', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom dotted, left medium,\
                                right dotted; pattern: pattern solid, fore_color azul_escuro;'))
                                
        ws.write(3,39, u'Inicial', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left medium, right dotted;pattern: pattern solid, fore_color azul_escuro'))   
                                
        ws.write(3,40, u'Final', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted; pattern: pattern solid, fore_color azul_escuro'))      
        
        ws.write_merge(2,2,41,42, u'ALTURA DA LÂMINA', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black,top dotted, bottom dotted, left dotted, right dotted; pattern: pattern solid, fore_color azul_escuro;'))
                                
        ws.write(3,41, u'Inicial', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color azul_escuro'))   
                                
        ws.write(3,42, u'Final', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted;pattern: pattern solid, fore_color azul_escuro'))  
                                
        ws.write_merge(2,2,43,44, u'COTA', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom dotted, left dotted, right dotted; pattern: pattern solid, fore_color azul_escuro;'))
                                
        ws.write(3,43, u'M', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted; pattern: pattern solid, fore_color azul_escuro'))   
                                
        ws.write(3,44, u'J', xlwt.easyxf('align: horiz center,  vert centre; font: bold on, color black;\
                                borders: right_color black, bottom_color black, top dotted, bottom medium, left dotted, right dotted; pattern: pattern solid, fore_color azul_escuro'))             
        
        ws.write_merge(2,3,45,45, u'CONF. REMANSO', xlwt.easyxf('align: horiz center,  vert centre, wrap on; font: bold on, color black;\
                                borders: bottom_color black, left_color black, top dotted, bottom medium, left dotted,\
                                right medium; pattern: pattern solid, fore_color azul_escuro;'))
        
        
        #ws.col(0).width = int(10*256)
        ####### FIM DESCRICAO DAS FORCAS DE ENGASTAMENTO PERFEITO GLOBAL DA BARRA #################
        BARRAS = self.Estrutura.LISTA_TUBULACOES
        for i in range(4, len(self.Estrutura.LISTA_TUBULACOES)+4):
            ws.write(i,0, str(BARRAS[i-4].nomeTrecho), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color rosa_salmao'))
             
            ws.write(i,1, str(BARRAS[i-4].PV1.nomePV+str(BARRAS[i-4].PV1.numero)), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color rosa_salmao'))
                                             
            ws.write(i,2, str(BARRAS[i-4].PV2.nomePV+str(BARRAS[i-4].PV2.numero)), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color rosa_salmao'))
                                             
            ws.write(i,3, str(round(BARRAS[i-4].L, 2)).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right medium;pattern: pattern solid, fore_color rosa_salmao'))
    
            ws.write(i,4, str(round(BARRAS[i-4].QsaidaInicial, 2)).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left medium, right dotted;pattern: pattern solid, fore_color azul_escuro'))
                                             
            ws.write(i,5, str(round(BARRAS[i-4].QsaidaFinal, 2)).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right medium;pattern: pattern solid, fore_color azul_escuro'))
                                             
            ws.write(i,6, str(round(BARRAS[i-4].PV1.CotaTerreno, 3)).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left medium, right dotted;pattern: pattern solid, fore_color rosa_salmao'))
                                             
            ws.write(i,7, str(round(BARRAS[i-4].PV2.CotaTerreno, 3)).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right medium;pattern: pattern solid, fore_color rosa_salmao'))
                                             
            ws.write(i,8, str(round(BARRAS[i-4].Iminima/100, 7)).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left medium, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,9, str(round(BARRAS[i-4].Iterreno/100, 7)).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,10, str(round(BARRAS[i-4].Iadotada, 7)).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,11, round((BARRAS[i-4].Iadotada - max(BARRAS[i-4].Iminima/100, BARRAS[i-4].Iterreno/100)),4), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
            
            ws.write(i,12, str(round(BARRAS[i-4].Desnivel, 2)).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right medium;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,13, str(int(BARRAS[i-4].D*1000)), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left medium, right dotted;pattern: pattern solid, fore_color rosa_salmao'))
                                             
            ws.write(i,14, str(BARRAS[i-4].EspessuraTubo).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color rosa_salmao'))
                                             
            ws.write(i,15, "OK", xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right medium;pattern: pattern solid, fore_color rosa_salmao'))
                                             
            ws.write(i,16, str(BARRAS[i-4].V0).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left medium, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,17, str(BARRAS[i-4].Q0).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,18, str(BARRAS[i-4].Q_Q0_inicial).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,19, str(BARRAS[i-4].Q_Q0_final).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,20, str(BARRAS[i-4].V_V0_inicial).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,21, str(BARRAS[i-4].V_V0_final).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,22, str(BARRAS[i-4].Vinicial).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,23, str(BARRAS[i-4].Vfinal).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right medium;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,24, str(BARRAS[i-4].Rh_D_inicial).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left medium, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,25, str(BARRAS[i-4].Rh_D_final).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,26, str(BARRAS[i-4].Rhidraulico_inicial).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
            
            ws.write(i,27, str(BARRAS[i-4].Rhidraulico_final).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,28, str(BARRAS[i-4].Vcritica_inicial).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,29, str(BARRAS[i-4].Vcritica_final).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,30, str(BARRAS[i-4].StatusVcritica_inicial), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,31, str(BARRAS[i-4].StatusVcritica_final), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right medium;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,32, str(BARRAS[i-4].CGII).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left medium, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,33, str(BARRAS[i-4].CGIF).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,34, str(BARRAS[i-4].PV1.CotaTerreno - BARRAS[i-4].CGII).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,35, str(BARRAS[i-4].PV2.CotaTerreno - BARRAS[i-4].CGIF).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,36, str(BARRAS[i-4].alturaFinalTrecho).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,37, str(BARRAS[i-4].coberturaInicioTrecho).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,38, "-", xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right medium;pattern: pattern solid, fore_color verde_cinza'))
                                             
            ws.write(i,39, str(BARRAS[i-4].h_D_inicial).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left medium, right dotted;pattern: pattern solid, fore_color azul_escuro'))
                                             
            ws.write(i,40, str(BARRAS[i-4].h_D_final).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color azul_escuro'))
                                             
            ws.write(i,41, str(BARRAS[i-4].Lamina_inicial).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color azul_escuro'))
                                             
            ws.write(i,42, str(BARRAS[i-4].Lamina_final).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color azul_escuro'))
                                             
            ws.write(i,43, str(BARRAS[i-4].CotaLaminaMontante).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color azul_escuro'))
                                             
            ws.write(i,44, str(BARRAS[i-4].CotaLaminaJusante).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right dotted;pattern: pattern solid, fore_color azul_escuro'))
    
            ws.write(i,45, str(BARRAS[i-4].Remanso).replace(".",","), xlwt.easyxf('align: horiz center,  vert centre; font: bold off, color black;\
                                             borders: right_color black, bottom_color black, top dotted, bottom dotted, left dotted, right medium;pattern: pattern solid, fore_color azul_escuro'))
                                             
    
    def SalvaEstrutura(self):    
        """
        Funcao responsavel por abrir a janela de salvamento, escolhe o nome e local
        do arquivo, apos faz o salvamento.
        """
        dlg = wx.FileDialog(self.event.GetEventObject().GetParent(), "Save project as...", os.getcwd(), "", "*.xls", wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        result = dlg.ShowModal()
        inFile = dlg.GetPath()
        dlg.Destroy()

        if result == wx.ID_OK:  #Botao salvar foi pressionado            
            # Abra o arquivo (leitura)
            try:
                self.EscreveDadosBarras()
                self.workbook.save(inFile)                
                #self.SalvaMatrizGlobal(inFile)
            except Exception as e:                
                print (e)                
            finally:
                pass
            return True

        elif result == wx.ID_CANCEL:    #Qualque um dos botoes cancelar ou fechar janela
            return False
        