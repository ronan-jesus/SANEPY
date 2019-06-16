# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Gui_DadosDoProjeto
###########################################################################

class Gui_DadosDoProjeto ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.notebbok_dadosDoProjeto = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.panel_dimensionamento = wx.Panel( self.notebbok_dadosDoProjeto, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText2 = wx.StaticText( self.panel_dimensionamento, wx.ID_ANY, u"Diâmetro minímo (mm):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        gSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

        cbx_diamMinimoChoices = [ u"100", u"150", u"200", u"250", u"300", u"350", u"400", u"450", u"500", u"550", u"600" ]
        self.cbx_diamMinimo = wx.ComboBox( self.panel_dimensionamento, wx.ID_ANY, u"150", wx.DefaultPosition, wx.DefaultSize, cbx_diamMinimoChoices, 0 )
        gSizer2.Add( self.cbx_diamMinimo, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self.panel_dimensionamento, wx.ID_ANY, u"Coef. Manning:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        gSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.txt_coefManning = wx.TextCtrl( self.panel_dimensionamento, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.txt_coefManning, 0, wx.ALL, 5 )

        self.m_staticText4 = wx.StaticText( self.panel_dimensionamento, wx.ID_ANY, u"Distância Máxima\nentre PVs (m):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        gSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.txt_distMaxima = wx.TextCtrl( self.panel_dimensionamento, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.txt_distMaxima, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self.panel_dimensionamento, wx.ID_ANY, u"Cobrimento Mínimo (m):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        gSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.txt_cobrimMinimo = wx.TextCtrl( self.panel_dimensionamento, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.txt_cobrimMinimo, 0, wx.ALL, 5 )

        self.m_staticText6 = wx.StaticText( self.panel_dimensionamento, wx.ID_ANY, u"Profundidade Máxima (m):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        gSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.txt_profundMaxima = wx.TextCtrl( self.panel_dimensionamento, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.txt_profundMaxima, 0, wx.ALL, 5 )


        bSizer3.Add( gSizer2, 0, 0, 5 )

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button( self.panel_dimensionamento, wx.ID_OK )
        m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
        self.m_sdbSizer1Cancel = wx.Button( self.panel_dimensionamento, wx.ID_CANCEL )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
        m_sdbSizer1.Realize();

        bSizer3.Add( m_sdbSizer1, 0, wx.ALIGN_RIGHT, 5 )


        self.panel_dimensionamento.SetSizer( bSizer3 )
        self.panel_dimensionamento.Layout()
        bSizer3.Fit( self.panel_dimensionamento )
        self.notebbok_dadosDoProjeto.AddPage( self.panel_dimensionamento, u"Dimensionamento", False )

        bSizer1.Add( self.notebbok_dadosDoProjeto, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.txt_coefManning.Bind( wx.EVT_KILL_FOCUS, self.verificaTextBoxes )
        self.txt_distMaxima.Bind( wx.EVT_KILL_FOCUS, self.verificaTextBoxes )
        self.txt_cobrimMinimo.Bind( wx.EVT_KILL_FOCUS, self.verificaTextBoxes )
        self.txt_profundMaxima.Bind( wx.EVT_KILL_FOCUS, self.verificaTextBoxes )
        self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.OnCancelOK )
        self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.OnButtonOK )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def verificaTextBoxes( self, event ):
        event.Skip()




    def OnCancelOK( self, event ):
        event.Skip()

    def OnButtonOK( self, event ):
        event.Skip()


