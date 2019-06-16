# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:00:27 2017

@author: RONAN TEODORO
"""
import os
import wx
import ezdxf

#print ("*"*30)
#print (entidade.dxftype())
#print (entidade.valid_dxf_attrib_names())
#print ("*"*30)
 
"""
The BLOCK definitions are stored in Drawing.blocks property:

# iterate over all existing block definitions
for block in dwg.blocks:
    for e in block:
        analyseElement(e)
"""
"""
The INSERT entity is stored in the model space or in another block definition:

for insert in modelspace.query('INSERT'):
    block = dwg.blocks[insert.dxf.name]
    for e in block:
         analyseElement(e)
"""
"""
To search for specific INSERT entities:

for insert in modelspace.query('INSERT[name=="MyBlock"]'):
    ...
"""
           
def AbrirArquivo(event, tipo_arq):
        """
        Funcao para abrir dialogo de selecao de arquivo para abertura, carrega um arquivo
        gravado com cPickle
        """
        dlg = wx.FileDialog(event.GetEventObject().GetParent(), message="Abrir Arquivo...", defaultDir=os.getcwd(),
                            defaultFile="", style=wx.FD_OPEN)

        # Call the dialog as a model-dialog so we're required to choose Ok or Cancel
        if dlg.ShowModal() == wx.ID_OK:
            # User has selected something, get the path, set the window's title to the path
            filename = dlg.GetPath()

        dlg.Destroy() # we don't need the dialog any more so we ask it to clean-up

        return filename
            
def ImportaArquivoDXF(path):
    dxf = ezdxf.readfile(path)
    
    return DXFImport(dxf)

class DXFImport(object):
    def __init__(self, dxf):
        self.dxf = dxf
        self.mdspace = dxf.modelspace()
        
        self.graficos = {}
        
        #self.ExtractBlocks()
        
        self.InicializaNomesEntidades()
        
        self.ExtractAll(self.mdspace)
        
        
    def InicializaNomesEntidades(self):
        self.graficos['POINTS'] = []
        self.graficos['LINES'] = []
        self.graficos['CIRCLES'] = []
        self.graficos['ARCS'] = []
        self.graficos['POLYLINES'] = []
        self.graficos['LWPOLYLINES'] = []
        self.graficos['TEXTS'] = []
        self.graficos['MTEXTS'] = []        
        self.graficos['HATCHS'] = []
        self.graficos['DIMENSIONS'] = []
        self.graficos['SOLIDS'] = []
        self.graficos['INSERTS'] = []        
        self.graficos['3DFACES'] = []
        self.graficos['OLE2FRAMES'] = []
        self.graficos['INSERTS'] = []
    
#    def ExtractBlocks(self):
#        for block in self.dxf.blocks:
#            print ("*"*30)
#            print (block.name)
#            for e in block:
#                print (e.dxftype())
#            print ("*"*30)
        
    def ExtractAll(self, entidades):
        for entidade in entidades:
            if entidade.dxftype() == 'POINT':                
                e = self.ExtractPoints(entidade)
                self.graficos['POINTS'].append(e)
            elif entidade.dxftype() == 'LINE':
                e = self.ExtractLines(entidade)
                self.graficos['LINES'].append(e)
            elif entidade.dxftype() == 'CIRCLE': 
                e = self.ExtractCircles(entidade) 
                self.graficos['CIRCLES'].append(e)
            elif entidade.dxftype() == 'ARC': 
                e = self.ExtractArcs(entidade)
                self.graficos['ARCS'].append(e)                
            elif entidade.dxftype() == 'LWPOLYLINE':                
                e = self.ExtractLWPolylines(entidade)
                self.graficos['LWPOLYLINES'].append(e)                
            elif entidade.dxftype() == 'TEXT':                
                e = self.ExtractTexts(entidade)
                self.graficos['TEXTS'].append(e)                
            elif entidade.dxftype() == 'MTEXT':                
                e = self.ExtractMTexts(entidade)
                self.graficos['MTEXTS'].append(e)                
            elif entidade.dxftype() == 'INSERT':
                e = self.ExtractInserts(entidade)
                self.graficos['INSERTS'].append(e)
            elif entidade.dxftype() == 'DIMENSION':
                e = self.ExtractDimensions(entidade)
                self.graficos['DIMENSIONS'].append(e)
        

    def ExtractPoints(self, entidade):
        e = entidade
        if hasattr(e, 'dxftype'):
            if e.dxftype() != 'POINT':
                raise "A entidade passada como parametro para a funcao 'ExtractPoints' nao e do tipo 'POINT'"
            else:
                return e.dxf.location
        else:
            raise "O parametro passado na funcao 'ExtractPoints' nao possui o atributo 'dxftype'"
    
    def ExtractLines(self, entidade):
        e = entidade
        if hasattr(e, 'dxftype'):
            if e.dxftype() != 'LINE':
                raise "A entidade passada como parametro para a funcao 'ExtractLines' nao e do tipo 'LINE'"
            else:
                return [e.dxf.start, e.dxf.end]                
        else:
            raise "O parametro passado na funcao 'ExtractLines' nao possui o atributo 'dxftype'"
            
    def ExtractCircles(self, entidade):
        e = entidade
        if hasattr(e, 'dxftype'):
            if e.dxftype() != 'CIRCLE':
                raise "A entidade passada como parametro para a funcao 'ExtractCircles' nao e do tipo 'CIRCLE'"
            else:
                return [e.dxf.center, e.dxf.radius]                
        else:
            raise "O parametro passado na funcao 'ExtractCircles' nao possui o atributo 'dxftype'"
            
    def ExtractArcs(self, entidade):
        e = entidade
        if hasattr(e, 'dxftype'):
            if e.dxftype() != 'ARC':
                raise "A entidade passada como parametro para a funcao 'ExtractArcs' nao e do tipo 'ARCS'"
            else:
                return [e.dxf.center, e.dxf.radius, e.dxf.start_angle, e.dxf.end_angle]                
        else:
            raise "O parametro passado na funcao 'ExtractArcs' nao possui o atributo 'dxftype'"
            
    def ExtractLWPolylines(self, entidade):
        e = entidade        
        if hasattr(e, 'dxftype'):
            if e.dxftype() != 'LWPOLYLINE':
                raise "A entidade passada como parametro para a funcao 'ExtractLWPolylines' nao e do tipo 'LWPOLYLINE'"
            else:
                lwpolyline = e.get_points()
                return [e.dxf.flags, list(lwpolyline)]                              
        else:
            raise "O parametro passado na funcao 'ExtractPolylines' nao possui o atributo 'dxftype'"
    
    def ExtractInserts(self, entidade):
        block = self.dxf.blocks[entidade.dxf.name]        
        entityes = []
        entityes.append([entidade.dxf.insert,
                         [entidade.dxf.yscale,
                          entidade.dxf.yscale,
                          entidade.dxf.zscale],
                          entidade.dxf.rotation,[]])        
        for e in block:
            if e.dxftype() == 'POINT':                
                entidade = self.ExtractPoints(e)
                entityes[0][3].append(["POINT",entidade])
            elif e.dxftype() == 'LINE':
                entidade = self.ExtractLines(e)
                entityes[0][3].append(["LINE",entidade])
            elif e.dxftype() == 'CIRCLE': 
                entidade = self.ExtractCircles(e) 
                entityes[0][3].append(["CIRCLE",entidade])
            elif e.dxftype() == 'ARC': 
                entidade = self.ExtractArcs(e)
                entityes[0][3].append(["ARC",entidade])                
            elif e.dxftype() == 'LWPOLYLINE':                
                entidade = self.ExtractLWPolylines(e)
                entityes[0][3].append(["LWPOLYLINE",entidade])
                
        return entityes[0]
        
    def ExtractDimensions(self, entidade):
#        print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#        print (entidade.valid_dxf_attrib_names())
                
        return 
        
    def ExtractTexts(self, entidade):
        #print (entidade.valid_dxf_attrib_names())
        #[u'layer', u'color', u'text', u'oblique', u'height', u'owner',
        #u'paperspace', u'shadow_mode', u'style', u'align_point',
        #u'thickness', u'width', u'valign', u'handle', u'ltscale',
        #u'linetype', u'invisible', u'rotation', u'lineweight', u'insert',
        #u'true_color', u'extrusion', u'halign', u'color_name',
        #u'transparency', u'text_generation_flag']               
        
        pos = entidade.get_pos()
        text = entidade.dxf.text
        oblique = entidade.dxf.oblique
        height = entidade.dxf.height
        width = entidade.dxf.width
        estilo = entidade.dxf.style
        valign = entidade.dxf.valign
        ltscale = entidade.dxf.ltscale
        halign = entidade.dxf.halign
        rotation = entidade.dxf.rotation
        text_generation_flag = entidade.dxf.text_generation_flag
        
        texto = [pos,text, oblique, height, width, estilo,valign,ltscale,
                 halign,rotation, text_generation_flag]
                 
        return texto
    
    def ExtractMTexts(self, entidade):
        print (entidade.valid_dxf_attrib_names())
        #[u'layer', u'color', u'owner', u'line_spacing_style', u'paperspace',
        # u'shadow_mode', u'style', u'text_direction', u'width', u'handle',
        # u'insert', u'attachment_point', u'ltscale', u'line_spacing_factor',
        # u'linetype', u'invisible', u'rotation', u'lineweight', u'rect_width',
        # u'flow_direction', u'char_height', u'true_color', u'extrusion',
        # u'color_name', u'transparency', u'rect_height']

        pos = entidade.dxf.insert
        text = entidade.get_text()
        #print ("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        #print (text)
        #print (entidade.dxf.char_height)
        #print (entidade.dxf.width)
        #print (entidade.get_rotation())        
        #print (entidade.dxf.flow_direction)
        #print (entidade.dxf.attachment_point)
        #print ("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        line_spacing_style = entidade.dxf.line_spacing_style
        style = entidade.dxf.style
        width = entidade.dxf.width        
        attachment_point = entidade.dxf.attachment_point
        ltscale = entidade.dxf.ltscale
        line_spacing_factor = entidade.dxf.line_spacing_factor
        rotation = entidade.get_rotation()        
        flow_direction = entidade.dxf.flow_direction
        char_height = entidade.dxf.char_height
        
        texto = [pos, text, line_spacing_style, style, width, attachment_point,
                 ltscale, line_spacing_factor, rotation, flow_direction,
                 char_height]
                 
#        print ("*"*30)        
#        print (e.get_text())
#        print (e.dxf.insert)
#        print (e.dxf.char_height)
#        print (e.dxf.width)
#        print (e.dxf.rotation)
#        print ("*"*30)
        
#        if hasattr(e, 'dxftype'):
#            if e.dxftype() != 'MTEXT':
#                raise "A entidade passada como parametro para a funcao 'ExtractMTexts' nao e do tipo 'MTEXT'"
#            else:
#                polyline = []
#                for num, line in enumerate(e.points(), start=0):
#                    polyline.append(line)                
#                
#                self.graficos['MTEXTS'].append(polyline)
#                
#        else:
#            raise "O parametro passado na funcao 'ExtractMTexts' nao possui o atributo 'dxftype'"
 
        return texto
        
    def ExtractHatchs(self, entidade):
        return
        e = entidade
        with e.edit_pattern() as pater:
               return
               #print (pater.lines[0].angle)
               #print (pater.lines[0].base_point)
               #print (pater.lines[0].offset)
               #print (pater.lines[0].dash_length_items)
               
#        with e.edit_boundary() as boundary:
#            
#            print (help(e))
#            print ("PolylinePath")
#            for b in boundary.paths:
#                print ("*"*30)
#                print (b.edges)
#                #print (b.is_closed)
#                #print (b.vertices)
#                print (b.source_boundary_objects)
#        print (e.valid_dxf_attrib_names())
#        print ("*"*30)
#        print ("pattern_type = %s" %e.dxf.pattern_type)
#        print ("*"*30)
#        print ("layer = %s" %e.dxf.layer)
#        print ("*"*30)
#        print ("color = %s" %e.dxf.color)
#        print ("*"*30)
#        print ("n_seed_points = %s" %e.dxf.n_seed_points)
#        print (e.get_seed_points())
#        print ("*"*30)
#        print ("owner = %s" %e.dxf.owner)
#        print ("*"*30)
#        print ("elevation = (%s, %s, %s)" %(e.dxf.elevation))
#        print ("*"*30)
#        print ("paperspace = %s" %e.dxf.paperspace)
##        print ("*"*30)
##        print (e.shadow_mode)
#        print ("*"*30)
#        print ("pattern_scale = %s" %e.dxf.pattern_scale)
#        print ("*"*30)
#        print ("handle = %s" %e.dxf.handle)
#        print ("*"*30)
#        print ("ltscale = %s" %e.dxf.ltscale)
#        print ("*"*30)
#        print ("linetype = %s" %e.dxf.linetype)
#        print ("*"*30)
#        print ("invisible = %s" %e.dxf.invisible)
##        print ("*"*30)
##        print (e.dxf.lineweight)
#        print ("*"*30)
#        print ("hatch_style = %s" %e.dxf.hatch_style)
##        print ("*"*30)
##        print (e.dxf.true_color)
#        print ("*"*30)
#        print ("extrusion = (%s, %s, %s)" %(e.dxf.extrusion))
#        print ("*"*30)
#        print ("pattern_double = %s" %e.dxf.pattern_double)
#        print ("*"*30)
#        print ("solid_fill = %s" %e.dxf.solid_fill)
##        print ("*"*30)
##        print (e.dxf.color_name)
##        print ("*"*30)
##        print (e.dxf.transparency)
#        print ("*"*30)
#        print ("pattern_name = %s" %e.dxf.pattern_name)
#        print ("*"*30)
#        print ("associative = %s" %e.dxf.associative)
#        print ("*"*30)
#        print ("pattern_angle = %s" %e.dxf.pattern_angle)
#        print ("*"*30)
        
        return
        
        if hasattr(e, 'dxftype'):
            if e.dxftype() != 'HATCH':
                raise "A entidade passada como parametro para a funcao 'ExtractHatchs' nao e do tipo 'HATCH'"
            else:
                polyline = []
                for num, line in enumerate(e.points(), start=0):
                    polyline.append(line)                
                
                self.graficos['HATCH'].append(polyline)
                
        else:
            raise "O parametro passado na funcao 'ExtractHatchs' nao possui o atributo 'dxftype'"