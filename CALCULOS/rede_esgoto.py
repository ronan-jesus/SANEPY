# -*- coding: utf-8 -*-
from __future__ import division

import sys, os

from math import sqrt, sin, cos, pi, asin, degrees, atan2

#from AUXILIARES.SanepyCore import Declividade   
from estruturas_PVs import PV_Retangular
from tabelaIndicesGeometricos import CriaTabelaIndices
import bisect
import numpy as np            

from AUXILIARES.util import truncaNumero         
            
def try_Except(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    print (e)
    
class RedeEsgoto(object):
    def __init__(self):
        
        self.LISTA_TRECHOS = []
        self.ramificacoes = []
    
    
    def VerificaRamificacoes(self):
        pass
        

class TrechoRede(object):    
    TABELA_INDICES = CriaTabelaIndices()#[h/D, Ø, A/D², R/D,Pm/D, Qh/QD, Vh/VD]
    TABELA_Qh_QD = [float(x[5]) for x in TABELA_INDICES]
    
    GamaEsgoto = 10000
    MODELO_CALCULO = "TABELA"
    
    
    TUBOTick_inicio_top = False
    TUBOTick_inicio_bottom = False
    TUBOTick_middle = False
    TUBOTick_final_top = False
    TUBOTick_final_bottom = False
    
    __instancias = []
    __ListaRamos = []
    __LISTA_PVS = []
    
    DIAMETROS = ["Ø100mm", "Ø150mm", "Ø200mm", "Ø250mm", "Ø300mm", "Ø350mm",
                 "Ø400mm", "Ø450mm", "Ø500mm", "Ø550mm", "Ø600mm"
                 ]
                 
    DIC_DIAMETROS = {u"Ø100mm":0.100, u"Ø150mm":0.150, u"Ø200mm":0.200,
                     u"Ø250mm":0.250, u"Ø300mm":0.300, u"Ø350mm":0.350,
                     u"Ø400mm":0.400, u"Ø450mm":0.450, u"Ø500mm":0.500,
                     u"Ø550mm":0.550, u"Ø600mm":0.600
                 }
                 
    
    
    @classmethod
    def __new__(cls, *args, **kwargs):
        return super(TrechoRede, cls).__new__(cls)        
        
    @classmethod
    def ListaDiametros(cls, *args, **kwargs):        
        DIC_DIAMETROS = cls.DIC_DIAMETROS
        return sorted(DIC_DIAMETROS, key=DIC_DIAMETROS.__getitem__)
        
    @classmethod
    def ListaTextosDiamentros(cls, *args, **kwargs):
        """ Retorna um dicionario com os textos do diametro pelo valor do
            diametro, para ser procurado pelo diametro definido (float)
        """
        DIC_DIAMETROS = cls.DIC_DIAMETROS
        TextosDiametros = {}
        for chave_original, valores in DIC_DIAMETROS.items():
            TextosDiametros[valores] = chave_original
        return TextosDiametros
        
    @classmethod
    def StatusModificar(cls, *args, **kwargs):
        """ Retorna uma lista com os STATUS das variaveis de controle de
            modificacao dos TUBOS, para verificar se algum TUBO esta sendo
            modificado por meio de MOVER, ROTACIONAR, LABEL_ARRASTAS, TICK_TOP
        """        
        return [cls.TUBOTick_inicio_top, cls.TUBOTick_inicio_bottom, cls.TUBOTick_middle,
                cls.TUBOTick_final_top, cls.TUBOTick_final_bottom]
    
    @classmethod
    def LimpaStatus(cls, *args, **kwargs):
        """ Seta como False todos os Ticks
        """
        cls.TUBOTick_inicio_top = False
        cls.TUBOTick_inicio_bottom = False
        cls.TUBOTick_middle = False
        cls.TUBOTick_final_top = False
        cls.TUBOTick_final_bottom = False
    
    
    def __init__(self, pvs, nome, T_ini=0.0, T_fin=0.0, T_infil=0.0):
        self.visivel = True
        self.PV1 = pvs[0]
        self.PV2 = pvs[1]
        
        self.PVmontante = self.PV1
        self.PVjusante = self.PV2
        
        self.numero = None
        self.nomeTrecho = nome
        
        self.QentradaInicial = None
        self.QentradaFinal = None
        self._QsaidaInicial = None
        self._QsaidaFinal = None
        
        self.TaxaInicial = 0.0019175270847562 #T_ini
        self.TaxaFinal = 0.00228077752333507 #T_fin
        self.TaxaInfiltracao = 0.001#T_infil        
        
        self.D = 0.150        
        self.EspessuraTubo = 0.00      
        self.coefManning = 0.013
        
        self.comprimentoAuto = True
        self.Ldefinido = 1.0
        
        self._L = None
        self._Iminima = None
        self._Imaxima = None
        self._Iterreno = None        
        self._PmInicial = None
        self._PmFinal = None
        self._AmInicial = None
        self._AmFinal = None
        self._RHinicial = None
        self._RHfinal = None
        self._Vinicial = None
        self._Vfinal = None
        self._TensaoTrativa = None
        
        self._Qpontual = 0.0
        self._Qinicial = None 
        self._Qfinal = None
        
        self._ContribTotalInicio = None
        self._ContribTotalFinal = None
        
        #Metodo de Calculo pelas Planilhas
        self._V0 = None
        self._Q0 = None
        self._Q_Q0_inicial = None
        self._Q_Q0_final = None
        self._V_V0_inicial = None
        self._V_V0_final = None
        self._Vi = None
        self._Vf = None
        self._Rh_D_inicial = None
        self._Rh_D_final = None
        self._Rhidraulico_inicial = None
        self._Rhidraulico_final = None
        self._Vcritica_inicial = None
        self._Vcritica_final = None
        self._StatusVcritica_inicial = None
        self._StatusVcritica_final = None
        self._h_D_inicial = None
        self._h_D_final = None        
        self._Lamina_inicial = None
        self._Lamina_final = None
        self._CotaLaminaMontante = None
        self._CotaLaminaJusante = None
        self._Remanso = None
        self._StatusRemanso = None
        
        self.alturaInicioTrecho = 0.0
        self.alturaFinalTrecho = 0.0        
        self.CGII = self.PV1.CotaFundo + self.alturaInicioTrecho
        self.CGIF = self.PV2.CotaFundo + self.alturaFinalTrecho
        self.CGSI = self.PV1.CotaFundo + self.alturaInicioTrecho + self.D
        self.CGSF = self.PV2.CotaFundo + self.alturaFinalTrecho + self.D
        self.coberturaInicioTrecho = (self.PV1.CotaTerreno - self.CGSI - 2*self.EspessuraTubo)
        self.coberturaFinalTrecho = (self.PV2.CotaTerreno - self.CGSF - 2*self.EspessuraTubo)
        
        ######################################################################
        ######  VERIFICAR ESTA PARTE DO CODIGO, POIS ESTA MUITO CONFUSA ######
        ######  PARA INICIAR COM A DECLIVIDADE ADOTADA                  ######
        ######################################################################
        if ((self.CGII - self.CGIF)/self.L) > 0:
            self._Iadotada = ((self.CGII - self.CGIF)/self.L)
        else:
            self._Iadotada = ((self.CGIF - self.CGII)/self.L)
        ######################################################################
        ######################################################################

        self.Desnivel = (self.L *  (self.Iadotada))
        
        self.cotaMinLaminaMontante = 0
        self.cotaMinLaminaJusante = 0
      
    @property
    def L(self):
        try:
            if self.comprimentoAuto == True: 
                return sqrt((self.PV2.pos[0] - self.PV1.pos[0])**2 +
                                    (self.PV2.pos[1] - self.PV1.pos[1])**2)/100
            else:
                return self.Ldefinido                
        except Exception as e:
            try_Except(e)

    @L.setter
    def L(self, L):
        try:
            self._L = L
        except Exception as e:
            try_Except(e)
            
    @property
    def Iminima(self):
        """Declividade minima da tubulacao para n=0.013 e trativa de 1 Pa.
           Se ainda naoa estiver sido calculado a vazao no trecho, adota
           1.5 l/s para o calculo, pois e a vazao minima
        """
        
        try:
            if (self.QsaidaInicial)>=1.5:
                return (0.0055 * pow(self.QsaidaInicial, -0.47))*100
            else:
                return (0.0055 * pow(1.5, -0.47))*100
        except Exception as e:
            try_Except(e)
            
    @Iminima.setter
    def Iminima(self, Iminima):
        try:
            self._Iminima = Iminima
        except Exception as e:
            try_Except(e)
            
    @property
    def Imaxima(self):
        """Declividade maxima da tubulacao para n=0.013 e velocidade de 5m/s"""
        try:
            return 4.65 * pow(self.Qfinal, -0.67)
        except Exception as e:
            try_Except(e)
            
    @Imaxima.setter
    def Imaxima(self, Imaxima):
        try:
            self._Imaxima = Imaxima
        except Exception as e:
            try_Except(e)

    @property
    def Iterreno(self):
        """Declividade do terreno, calculada pelas cotas do terreno na posicao
           dos Pvs 1 e 2"""
        try:                                    #*100 por causa da porcentagem
            return ((self.PV1.CotaTerreno - self.PV2.CotaTerreno)/self.L)*100
        except Exception as e:
            try_Except(e)
            
    @Iterreno.setter
    def Iterreno(self, Iterreno):
        try:
            self._Iterreno = Iterreno
        except Exception as e:
            try_Except(e)

    @property    
    def Iadotada(self):
        """Declividade adotada para o trecho entre os Pvs 1 e 2"""        
        return self._Iadotada        
        
    @Iadotada.setter    
    def Iadotada(self, Iadotada):
        try:
#            if Iadotada < 0:
#                self.InverteDirecaoTubo()
#                self._Iadotada = abs(Iadotada)
#            else:
            self._Iadotada = Iadotada
            
        except Exception as e:
            try_Except(e)
     
    @property
    def PmInicial(self):
        """Perimetro molhado do tubo em relacao a situacao inicial"""
        try:
            n = self.coefManning
            D = self.D
            I = self.Iadotada
            Q = self.QsaidaInicial/1000
            
            k = Q*n*pow(D,-8/3)*pow(I,-1/2)
            try:
                a = ((3*pi)/2)*sqrt(1-sqrt(1-sqrt(pi*k)))
            except:
                a = 2*pi
            
            print ("---- a ---- %s" %a)
            Pm = (D/2)*a       
    
            return Pm
        except Exception as e:
            try_Except(e)

    @PmInicial.setter
    def PmInicial(self, PmInicial):
        try:
            self._PmInicial = PmInicial
        except Exception as e:
            try_Except(e)

    @property
    def PmFinal(self):
        """Perimetro molhado do tubo em relacao a situacao finall"""
        try:
            n = self.coefManning
            D = self.D
            I = self.Iadotada
            Q = self.QsaidaFinal/1000
            
            k = Q*n*pow(D,-8/3)*pow(I,-1/2)     
            a = ((3*pi)/2)*sqrt(1-sqrt(1-sqrt(pi*k)))
            
            Pm = (D/2)*a       
    
            return Pm
        except Exception as e:
            try_Except(e)

    @PmFinal.setter
    def PmFinal(self, PmFinal):
        try:
            self._PmFinal = PmFinal
        except Exception as e:
            try_Except(e)

    @property
    def AmInicial(self):
        """Area molhada do tubo em relacao a situacao inicial"""
        try:
            n = self.coefManning
            D = self.D
            I = self.Iadotada
            Q = self.QsaidaInicial/1000
            
            k = Q*n*pow(D,-8/3)*pow(I,-1/2)
            try:
                a = ((3*pi)/2)*sqrt(1-sqrt(1-sqrt(pi*k)))
            except:
                a = 2*pi
            
            Am = (pow(D,2)*(a-sin(a)))/8
    
            return Am
        except Exception as e:
            try_Except(e)

    @AmInicial.setter
    def AmInicial(self, AmInicial):
        try:
            self._AmInicial = AmInicial
        except Exception as e:
            try_Except(e)

    @property
    def AmFinal(self):
        """Area molhada do tubo em relacao a situacao final"""
        try:
            n = self.coefManning
            D = self.D
            I = self.Iadotada
            Q = self.QsaidaFinal/1000
            
            k = Q*n*pow(D,-8/3)*pow(I,-1/2)     
            a = ((3*pi)/2)*sqrt(1-sqrt(1-sqrt(pi*k)))
            
            Am = (pow(D,2)*(a-sin(a)))/8
    
            return Am
        except Exception as e:
            try_Except(e)

    @AmFinal.setter
    def AmFinal(self, AmFinal):
        try:
            self._AmFinal = AmFinal
        except Exception as e:
            try_Except(e)

    @property
    def RHinicial(self):
        """Raio Hidraulico do tubo em relacao a situacao inicial"""
        try:
            if self.MODELO_CALCULO == "TABELA":
                return (self.Rh_D_inicial*self.D)
            else:
                n = self.coefManning # adimensional
                D = self.D # metros
                I = self.Iadotada # metro/metro
                Q = self.QsaidaInicial/1000 # M3/segundos 
                
                k = Q*n*pow(D,-8/3)*pow(I,-1/2)
                
                a = ((3*pi)/2)*sqrt(1-sqrt(1-sqrt(pi*k)))
                Am = (pow(D,2)*(a-sin(a)))/8 
                Pm = (D/2)*a            
                RH = Am/Pm
                
                hD = (1/2)*(1-cos(a/2))
                v = (1/n)*(RH**(2/3))*(I**(1/2))        

                return RH
        except Exception as e:
            try_Except(e)

    @RHinicial.setter
    def RHinicial(self, RHinicial):
        try:
            self._RHinicial = RHinicial
        except Exception as e:
            try_Except(e)

    @property
    def RHfinal(self):
        """Raio Hidraulico do tubo em relacao a situacao final"""
        try:
            if self.MODELO_CALCULO == "TABELA":
                return (self.Rh_D_final*self.D)
            else:
                n = self.coefManning
                D = self.D
                I = self.Iadotada
                Q = self.QsaidaFinal/1000
                
                k = Q*n*pow(D,-8/3)*pow(I,-1/2)        
                a = ((3*pi)/2)*sqrt(1-sqrt(1-sqrt(pi*k)))        
                Am = (pow(D,2)*(a-sin(a)))/8        
                Pm = (D/2)*a
                
                RH = Am/Pm
                
                hD = (1/2)*(1-cos(a/2))
                v = (1/n)*(RH**(2/3))*(I**(1/2))
                
                return RH
        except Exception as e:
            try_Except(e)

    @RHfinal.setter
    def RHfinal(self, RHfinal):
        try:
            self._RHfinal = RHfinal
        except Exception as e:
            try_Except(e)

    @property
    def Vinicial(self):
        """Calcula a velocidade inicial do trecho, referente a declividade
           utilizada para a tubulacao"""
        try:
            n = self.coefManning
            RH = self.RHinicial
            I = self.Iadotada
            
            return (1/n)*(RH**(2/3))*(I**(1/2))      
        except Exception as e:
            try_Except(e)

    @Vinicial.setter
    def Vinicial(self, Vinicial):
        try:
            self._Vinicial = Vinicial
        except Exception as e:
            try_Except(e)

    @property
    def Vfinal(self):
        """Calcula a velocidade final do trecho, referente a declividade
           utilizada para a tubulacao"""
        try:
            n = self.coefManning
            RH = self.RHfinal
            I = self.Iadotada
            
            return (1/n)*(RH**(2/3))*(I**(1/2))      
        except Exception as e:
            try_Except(e)

    @Vinicial.setter
    def Vinicial(self, Vinicial):
        try:
            self._Vinicial = Vinicial
        except Exception as e:
            try_Except(e)

    @property
    def TensaoTrativa(self):
        """Calcula a tensao trativa minima --> situacao inicial"""
        try:
            return self.GamaEsgoto*self.RHinicial*self.Iadotada      
        except Exception as e:
            try_Except(e)

    @TensaoTrativa.setter
    def TensaoTrativa(self, TensaoTrativa):
        try:
            self._TensaoTrativa = TensaoTrativa
        except Exception as e:
            try_Except(e)

    @property
    def Qpontual(self):
        try:
            return self._Qpontual
        except Exception as e:
            try_Except(e)

    @Qpontual.setter
    def Qpontual(self, Qpontual):
        try:
            self._Qpontual = Qpontual
        except Exception as e:
            try_Except(e)

    @property
    def Qinicial(self):
        try:
            return (self.TaxaInicial+self.TaxaInfiltracao)*self.L
        except Exception as e:
            try_Except(e)

    @Qinicial.setter
    def Qinicial(self, Qinicial):
        try:
            self._Qinicial = Qinicial
        except Exception as e:
            try_Except(e)

    @property
    def Qfinal(self):
        try:
            return (self.TaxaFinal+self.TaxaInfiltracao)*self.L
        except Exception as e:
            try_Except(e)

    @Qfinal.setter
    def Qfinal(self, Qfinal):
        try:
            self._Qfinal = Qfinal
        except Exception as e:
            try_Except(e)

    @property
    def ContribTotalInicio(self):
        try:
            return ((self.TaxaInicial+self.TaxaInfiltracao)*self.L)+self.Qpontual
        except Exception as e:
            try_Except(e)

    @ContribTotalInicio.setter
    def ContribTotalInicio(self, ContribTotalInicio):
        try:
            self._ContribTotalInicio = ContribTotalInicio
        except Exception as e:
            try_Except(e)

    @property
    def ContribTotalFinal(self):
        try:
            return ((self.TaxaFinal+self.TaxaInfiltracao)*self.L)+self.Qpontual
        except Exception as e:
            try_Except(e)

    @ContribTotalFinal.setter
    def ContribTotalFinal(self, ContribTotalFinal):
        try:
            self._ContribTotalFinal = ContribTotalFinal
        except Exception as e:
            try_Except(e)

    @property
    def QsaidaInicial(self):
        try:            
            QtotalInicial = self.QentradaInicial+self.ContribTotalInicio
            if QtotalInicial < 1.50:
                return 1.50
            else:
                return QtotalInicial
        except Exception as e:
            try_Except(e)
            
    @QsaidaInicial.setter
    def QsaidaInicial(self, QsaidaInicial):
        try:
            self._QsaidaInicial = QsaidaInicial        
        except Exception as e:
            try_Except(e)            
            
    @property
    def QsaidaFinal(self):
        try:
            QtotalFinal = self.QentradaFinal+self.ContribTotalFinal
            if QtotalFinal < 1.50:
                return 1.50
            else:
                return QtotalFinal
        except Exception as e:
            try_Except(e)
            
    @QsaidaFinal.setter
    def QsaidaFinal(self, QsaidaFinal):
        try:
            self._QsaidaFinal = QsaidaFinal        
        except Exception as e:
            try_Except(e)
            
 #######################################################################       
        
    @property
    def V0(self): 
        """Retorna o valor da velocidade a secao plena em m/s"""
        try:
            if self.Iadotada > 0:            
                return (pow(0.0375,(2/3)) * (pow(self.Iadotada,1/2))/(self.coefManning))
            else:
                return -(pow(0.0375,(2/3)) * (pow(-self.Iadotada,1/2))/(self.coefManning))
        except Exception as e:
            try_Except(e)
            
    @V0.setter
    def V0(self, V0):
        try:
            self._V0 = V0
        except Exception as e:
            try_Except(e)
            
    @property
    def Q0(self):
        "Retorna o valor da vazao a secao plena em m3/s"        
        try:
            return (self.V0*(pi*(pow(self.D,2)/4)))      
        except Exception as e:
            try_Except(e)
            
    @Q0.setter
    def Q0(self, Q0):
        try:
            self._Q0 = Q0
        except Exception as e:
            try_Except(e)            
            
    @property
    def Q_Q0_inicial(self):        
        try:
            return ((self.QsaidaInicial/1000)/self.Q0)     
        except Exception as e:
            try_Except(e)            
            
    @Q_Q0_inicial.setter
    def Q_Q0_inicial(self, Q_Q0_inicial):
        try:
            self._Q_Q0_inicial = Q_Q0_inicial
        except Exception as e:
            try_Except(e)            
            
    @property
    def Q_Q0_final(self):        
        try:            
            return ((self.QsaidaFinal/1000)/self.Q0)     
        except Exception as e:
            try_Except(e)
            
    @Q_Q0_final.setter
    def Q_Q0_final(self, Q_Q0_final):
        try:
            self._Q_Q0_final = Q_Q0_final
        except Exception as e:
            try_Except(e)
            
    @property
    def V_V0_inicial(self):
        try:
            i = bisect.bisect_left(self.TABELA_Qh_QD, self.Q_Q0_inicial)
            return float(self.TABELA_INDICES[i][6])  
                    
        except Exception as e:
            try_Except(e)            
            
    @V_V0_inicial.setter
    def V_V0_inicial(self, V_V0_inicial):
        try:
            self._V_V0_inicial = V_V0_inicial
        except Exception as e:
            try_Except(e)
            
    @property
    def V_V0_final(self):        
        try:
            i = bisect.bisect_left(self.TABELA_Qh_QD, self.Q_Q0_final)
            return float(self.TABELA_INDICES[i][6])  
        except Exception as e:
            try_Except(e)            
            
    @V_V0_final.setter
    def V_V0_final(self, V_V0_final):
        try:
            self._V_V0_final = V_V0_final
        except Exception as e:
            try_Except(e)
            
    @property
    def Vi(self):
        """Calcula a velocidade real para inicio de plano por meio da TABELA
        """
        try:
            return (self.V0*self.V_V0_inicial)
        except Exception as e:
            try_Except(e)            
            
    @Vi.setter
    def Vi(self, Vi):
        try:
            self._Vi = Vi
        except Exception as e:
            try_Except(e)            
            
    @property
    def Vf(self):
        try:
            return (self.V0*self.V_V0_final)    
        except Exception as e:
            try_Except(e)            
            
    @Vf.setter
    def Vf(self, Vf):
        try:
            self._Vf = Vf
        except Exception as e:
            try_Except(e)            
            
    @property
    def Rh_D_inicial(self):
        try:
            i = bisect.bisect_left(self.TABELA_Qh_QD, self.Q_Q0_inicial)
            return float(self.TABELA_INDICES[i][3])
        except Exception as e:
            try_Except(e)
            
    @Rh_D_inicial.setter
    def Rh_D_inicial(self, Rh_D_inicial):
        try:
            self._Rh_D_inicial = Rh_D_inicial
        except Exception as e:
            try_Except(e)
            
    @property
    def Rh_D_final(self):
        try:
            i = bisect.bisect_left(self.TABELA_Qh_QD, self.Q_Q0_final)
            return float(self.TABELA_INDICES[i][3])
        except Exception as e:
            try_Except(e)
            
    @Rh_D_final.setter
    def Rh_D_final(self, Rh_D_final):
       try:
           self._Rh_D_final = Rh_D_final
       except Exception as e:
           try_Except(e)           
            
    @property
    def Rhidraulico_inicial(self):        
        try:
            return (self.D*self.Rh_D_inicial)
        except Exception as e:
            try_Except(e)
            
    @Rhidraulico_inicial.setter
    def Rhidraulico_inicial(self, Rhidraulico_inicial):
        try:
            self._Rhidraulico_inicial = Rhidraulico_inicial
        except Exception as e:
            try_Except(e)
            
    @property
    def Rhidraulico_final(self):        
        try:
            return (self.D*self.Rh_D_final)
        except Exception as e:
            try_Except(e)
            
    @Rhidraulico_final.setter
    def Rhidraulico_final(self, Rhidraulico_final):
        try:
            self._Rhidraulico_final = Rhidraulico_final
        except Exception as e:
            try_Except(e)
            
    @property
    def Vcritica_inicial(self):        
        try:
            return 6*(pow(9.81*self.RHinicial,0.5))
        except Exception as e:
            try_Except(e)
            
    @Vcritica_inicial.setter
    def Vcritica_inicial(self, Vcritica_inicial):
        try:
            self._Vcritica_inicial = Vcritica_inicial
        except Exception as e:
            try_Except(e)
            
    @property
    def Vcritica_final(self):        
        try:
            return 6*(pow(9.81*self.RHfinal,0.5))
        except Exception as e:
            try_Except(e)
                        
    @Vcritica_final.setter
    def Vcritica_final(self, Vcritica_final):
        try:
            self._Vcritica_final = Vcritica_final
        except Exception as e:
            try_Except(e)
            
    @property
    def StatusVcritica_inicial(self):        
        try:
            if self.Vcritica_inicial > self.Vinicial:
                return u"OK"
            else:
                return u"NAO"
        except Exception as e:
            try_Except(e)
            
    @StatusVcritica_inicial.setter
    def StatusVcritica_inicial(self, StatusVcritica_inicial):
        try:
            self._StatusVcritica_inicial = StatusVcritica_inicial
        except Exception as e:
            try_Except(e)
            
    @property
    def StatusVcritica_final(self):        
        try:
            if self.Vcritica_final > self.Vfinal:
                return u"OK"
            else:
                return "NAO"         
        except Exception as e:
            try_Except(e)
            
    @StatusVcritica_final.setter
    def StatusVcritica_final(self, StatusVcritica_final):
        try:
            self._StatusVcritica_final = StatusVcritica_final
        except Exception as e:
            try_Except(e)
            
    @property
    def h_D_inicial(self):
        try:
            i = bisect.bisect_left(self.TABELA_Qh_QD, self.Q_Q0_inicial)
            return float(self.TABELA_INDICES[i][0])                
        except Exception as e:
            print ("Erro no trecho %s" %self.numero)
            print ("Nao foi possivel achar na tabela 'Qh/QD'")
            try_Except(e)
            
    @h_D_inicial.setter
    def h_D_inicial(self, h_D_inicial):
        try:
            self._h_D_inicial = h_D_inicial
        except Exception as e:
            try_Except(e)
            
    @property
    def h_D_final(self):        
        try:
            i = bisect.bisect_left(self.TABELA_Qh_QD, self.Q_Q0_final)
            return float(self.TABELA_INDICES[i][0])
        except Exception as e:
            try_Except(e)
            
    @h_D_final.setter
    def h_D_final(self, h_D_final):
        try:
            self._h_D_final = h_D_final
        except Exception as e:
            try_Except(e)
            
    @property
    def Lamina_inicial(self):
        try:
            return (self.h_D_inicial*self.D)
        except Exception as e:
            print ("Erro no trecho %s" %self.numero)
            print ("Nao foi possivel retornar o 'h/D inicial'")
            try_Except(e)
            
    @Lamina_inicial.setter
    def Lamina_inicial(self, Lamina_inicial):
        try:
            self.Lamina_inicial = Lamina_inicial
        except Exception as e:            
            try_Except(e)
            
    @property
    def Lamina_final(self):
        try:
            return (self.h_D_final*self.D)
        except Exception as e:
            try_Except(e)
            
    @Lamina_inicial.setter
    def Lamina_inicial(self, Lamina_inicial):
        try:
            self.Lamina_inicial = Lamina_inicial
        except Exception as e:
            print ("Erro no trecho %s" %self.numero)
            print ("Nao foi possivel retornar a 'Lamina_inicial'")
            try_Except(e)
            
    @property
    def CotaLaminaMontante(self):
        try:
            return (self.CGII+self.Lamina_inicial)
        except Exception as e:
            try_Except(e)
            
    @CotaLaminaMontante.setter
    def CotaLaminaMontante(self, value):
        try:
            self._CotaLaminaMontante = value
        except Exception as e:
            try_Except(e)
            
    @property
    def CotaLaminaJusante(self):
        try:
            return (self.CGIF+self.Lamina_final)
        except Exception as e:
            try_Except(e)
            
    @CotaLaminaJusante.setter
    def CotaLaminaJusante(self, value):
        try:
            self._CotaLaminaJusante = value
        except Exception as e:
            try_Except(e)
            
    @property
    def Remanso(self):
        try:
            if (self.CotaLaminaMontante-self.cotaMinLaminaJusante)>=0:
                return round((0.0),4)
            else:
                return round((self.CotaLaminaMontante-self.cotaMinLaminaJusante),4)                
            
        except Exception as e:
            try_Except(e)
            
    @Remanso.setter
    def Remanso(self, value):
        try:
            self._Remanso = value
        except Exception as e:
            try_Except(e)
            
    @property
    def StatusRemanso(self):
        try:
            if (self.CotaLaminaMontante-self.cotaMinLaminaJusante)>0:
                return "OK"
            else:
                return "NAO"                
            
        except Exception as e:
            try_Except(e)
            
    @StatusRemanso.setter
    def StatusRemanso(self, StatusRemanso):
        try:
            self._StatusRemanso = StatusRemanso
        except Exception as e:
            try_Except(e)
    
    def SetDiametroTrecho(self, diametro):
        """Seta o Diametro do Trecho (m) """        
        self.D = diametro
        
        self.CGSI = (self.CGII + self.D)
        self.CGSF = (self.CGIF + self.D)
        self.coberturaInicioTrecho = (self.PV1.CotaTerreno - self.CGSI - 2*self.EspessuraTubo)
        self.coberturaFinalTrecho = (self.PV2.CotaTerreno - self.CGSF - 2*self.EspessuraTubo)        
        
    def SetCGII(self, cotaGeratriz):
        """Seta a Cota da Geratriz Inferior do Tubo no Inicio do Trecho """
        self.CGII = cotaGeratriz
        
        self.CGSI = (self.CGII + self.D)        
        self.Desnivel = (self.CGII - self.CGIF)
        self.Iadotada = (self.Desnivel/self.L)
        self.alturaInicioTrecho = (self.CGII - self.PV1.CotaFundo)
        self.coberturaInicioTrecho = (self.PV1.CotaTerreno - self.CGSI - 2*self.EspessuraTubo)
        
        
    def SetCGIF(self, cotaGeratriz):
        """Seta a Cota da Geratriz Inferior do Tubo no Final do Trecho """
        self.CGIF = cotaGeratriz
        
        self.CGSF = (self.CGIF + self.D)        
        self.Desnivel = (self.CGII - self.CGIF)
        self.Iadotada = (self.Desnivel/self.L)
        self.alturaFinalTrecho = (self.CGIF - self.PV2.CotaFundo)
        self.coberturaFinalTrecho = (self.PV2.CotaTerreno - self.CGSI - 2*self.EspessuraTubo)
        
    def SetCGSI(self, cotaGeratriz):
        """Seta a Cota da Geratriz Superior do Tubo no Inicio do Trecho """
        self.CGSI = cotaGeratriz
        
        self.CGII = (self.CGSI - self.D)        
        self.Desnivel = (self.CGII - self.CGIF)
        self.Iadotada = (self.Desnivel/self.L)
        self.alturaInicioTrecho = (self.CGII - self.PV1.CotaFundo)
        self.coberturaInicioTrecho = (self.PV1.CotaTerreno - self.CGSI - 2*self.EspessuraTubo)
    
    def SetCGSF(self, cotaGeratriz):
        """Seta a Cota da Geratriz Superior do Tubo no Final do Trecho """
        self.CGSF = cotaGeratriz
        
        self.CGIF = (self.CGSF - self.D)        
        self.Desnivel = (self.CGII - self.CGIF)
        self.Iadotada = (self.Desnivel/self.L)
        self.alturaFinalTrecho = (self.CGIF - self.PV2.CotaFundo)
        self.coberturaFinalTrecho = (self.PV2.CotaTerreno - self.CGSF - 2*self.EspessuraTubo)
        
    def SetCMEIO(self, cotaMEIO):
        """Seta a Cota GERAL do Tubo do Trecho, altera todos as alturas
           no inicio e final do trecho, pela cota do meio do tubo"""
        
        _cotaMeioAtual = ((self.CGSI + self.CGIF)/2)
        
        diferenca = (cotaMEIO - _cotaMeioAtual)
        
        cgsi = self.CGSI+diferenca
        cgsf = self.CGSF+diferenca        
        
        self.SetCGSI(cgsi)
        self.SetCGSF(cgsf)        
        
    
    def SetDeclividade(self, decliv):
        """Seta a Declividade do Trecho em m/m"""
        self.Iadotada = decliv
        
        self.Desnivel = round(self.L * self.Iadotada , 3)       
        self.CGIF = round(self.CGII - self.Desnivel, 3)
        self.CGSF = round(self.CGIF + self.D, 3)
        self.alturaFinalTrecho = round(self.CGIF - self.PV2.CotaFundo, 3)
        self.coberturaFinalTrecho = round(self.PV2.CotaTerreno - self.CGSF - 2*self.EspessuraTubo, 3)
        
    def SetDesnivel(self, desnivel):
        """Seta a Declividade do Trecho em m/m"""
        self.Desnivel = round(desnivel, 3)
        #self.Iadotada = Declividade(self.L, self.Desnivel)
        self.Iadotada = (self.Desnivel/ self.L)
        
        self.CGIF = round(self.CGII - self.Desnivel, 3)
        self.CGSF = round(self.CGIF + self.D, 3)
        self.alturaFinalTrecho = round(self.CGIF - self.PV2.CotaFundo, 3)
        self.coberturaFinalTrecho = round(self.PV2.CotaTerreno - self.CGSF - 2*self.EspessuraTubo, 3)
        
    def SetAlturaInicioTrecho(self, altura):
        """Seta a Altura do Tubo no Inicio do Trecho """
        self.alturaInicioTrecho = altura
        
        self.CGII = (self.PV1.CotaFundo + altura)
        self.CGSI = (self.PV1.CotaFundo + altura + self.D)
        self.Desnivel = (self.CGII - self.CGIF)
        self.Iadotada = (self.Desnivel/self.L)
        self.coberturaInicioTrecho = (self.PV1.CotaTerreno - self.CGSI - 2*self.EspessuraTubo)
        
    def SetAlturaFinalTrecho(self, altura):
        """Seta a Altura do Tubo no Final do Trecho """
        self.alturaFinalTrecho = altura
        
        self.CGIF = (self.PV2.CotaFundo + altura)        
        self.CGSF = (self.PV2.CotaFundo + altura + self.D)        
        self.Desnivel = (self.CGII - self.CGIF)        
        self.Iadotada = (self.Desnivel/self.L)
        self.coberturaFinalTrecho = (self.PV2.CotaTerreno - self.CGSF - 2*self.EspessuraTubo)
        
    def SetCoberturaInicioTrecho(self, cobertura):
        """Seta a Cobertura do Tubo no Inicio do Trecho """
        self.coberturaInicioTrecho = cobertura
        
        self.CGII = round(self.PV1.CotaTerreno - cobertura - self.D, 3)
        self.CGSI = round(self.PV1.CotaTerreno - cobertura, 3)        
        self.alturaInicioTrecho = round(self.CGII - self.PV1.CotaFundo, 3)                
        self.Desnivel = round(self.CGII - self.CGIF, 3)        
        self.Iadotada = round(self.Desnivel/self.L, 4)
        
    def SetCoberturaFinalTrecho(self, cobertura):
        """Seta a Cobertura do Tubo no Final do Trecho """
        self.coberturaFinalTrecho = cobertura
        
        self.CGIF = round(self.PV2.CotaTerreno - cobertura - self.D, 3)
        self.CGSF = round(self.PV2.CotaTerreno - cobertura, 3)        
        self.alturaFinalTrecho = round(self.CGIF - self.PV2.CotaFundo, 3)                
        self.Desnivel = round(self.CGII - self.CGIF, 3)        
        self.Iadotada = round(self.Desnivel/self.L, 4)
        
    def GetalturaInicioTrecho(self):
        """Retorna o valor da alura do tubo em relacao ao fundo do PV inicial
        """
        return (self.CGII - self.PV1.CotaFundo)
        
    def GetalturaFinalTrecho(self):
        """Retorna o valor da alura do tubo em relacao ao fundo do PV final
        """
        return (self.CGIF - self.PV2.CotaFundo)
    
    def GetCompAutoTrecho(self):
        """Retorna o Comprimento automatico do trecho, apenas para fins de
           representacao, esta funcao nao esta envolvida nos calculas.
           
           Para os calculos, usar a property "self.L" ela esta ligadas a todos
           os calulos desta classe.           
            
        """
        return sqrt((self.PV2.pos[0] - self.PV1.pos[0])**2 +
                                    (self.PV2.pos[1] - self.PV1.pos[1])**2)/100
    
    def GetTextoDiamentro(self, flag=None):
        """Retorna o texto do diamentro do trecho.
        """
        for k, v in self.DIC_DIAMETROS.items():
            if self.D == v:
                if flag == "NUM":
                    return k[:-2]
                else:
                    return k
    
    def GetTextoDeclividade(self):
        return truncaNumero(self.Iadotada, 4)+"m/m"
    
    def GetTextoComprimento(self):
        return truncaNumero(self.L, 2)+"m"
    
    def GetListaDregraus(self, listaTrechos):
        """Retorna a altura de queda em relacao ao fundo do tubo a jusante ate
           o fundo do PV a jusante do trecho.
        """
        listaDegraus = []
        
        for i, trecho in enumerate(listaTrechos):
            if i == 0:
                listaDegraus.append(trecho.alturaInicioTrecho)
                listaDegraus.append(trecho.alturaFinalTrecho)
            else:
                listaDegraus.append(trecho.alturaFinalTrecho)
                
        return listaDegraus
    
    def GetAngleDirection(self):
        x = (((self.PV2.pos[0]/100 - self.PV1.pos[0]/100)/self.L))
        y = (((self.PV2.pos[1]/100 - self.PV1.pos[1]/100)/self.L))
        
        alpha = atan2(y,x)*180/pi
        
        return alpha
    
    def GetMatrixRotation(self):
        x = (((self.PV2.pos[0]/100 - self.PV1.pos[0]/100)/self.L))
        y = (((self.PV2.pos[1]/100 - self.PV1.pos[1]/100)/self.L))
        
        alpha = -atan2(y,x)
        matriz = np.matrix([[cos(alpha), -sin(alpha)],
                         [sin(alpha), cos(alpha)]])
        
        return matriz
    
    def GetMiddliPosition(self):
        xi, yi, zi = self.PV1.pos
        xj, yj, zj = self.PV2.pos
        
        x = ((xi+xj)/2)/100
        y = ((yi+yj)/2)/100            
        z = ((zi+zj)/2)/100            
            
        return [x, y, z]

    def Get_1_4_Position(self):
        v1 = np.array(self.PV1.pos)/100
        v2 = np.array(self.PV2.pos)/100
        v = v2-v1
        
        return v/4 + v1
    
    def Get_3_4_Position(self):
        v1 = np.array(self.PV1.pos)/100
        v2 = np.array(self.PV2.pos)/100
        v = v2-v1
        
        return ((v/4)*3) + v1
        
         
     
     
if __name__ == "__main__":
    pv1 = PV_Retangular([83057.0, 31463.9, 0], 29.45)
    pv2 = PV_Retangular([75536.9, 33126.8, 0], 28.89)
    
    pv1.CotaTerreno = 29.45
    pv2.CotaTerreno = 28.89
    
    trecho1 = TrechoRede([pv1, pv2], 0.0000606490063573679, 0.0000989451728440602, 0.0)
    trecho1.Iadotada = 0.008271
    
    print ("Comprimento do Trecho = %s" %trecho1.L)
    print ("Vazao Inicial = %s" %trecho1.Qinicial)
    print ("Vazao Final = %s" %trecho1.Qfinal)
    print ("Cota M = %s" %trecho1.PV1.pos[2])
    print ("Cota J = %s" %trecho1.PV2.pos[2])
    print ("Declividade Minima = %s" %trecho1.Iminima)
    print ("Declividade Terreno = %s" %trecho1.Iterreno)
    print ("Declividade Adotada = %s" %trecho1.Iadotada)
    print ("Desnivel = %s" %trecho1.Desnivel)
    print ("Diametro Tubulacao = %s" %trecho1.D)
    print ("Espessura Tubulacao = %s" %trecho1.EspessuraTubo)
    print ("Velocidade Inicial = %s" %trecho1.Vinicial)
    print ("Velocidade Final = %s" %trecho1.Vfinal)
    
    print ("RH = %s" %trecho1.RHinicial)
    print ("RH = %s" %trecho1.RHfinal)
    print ("TensaoTrativa = %s" %trecho1.TensaoTrativa)
    print ("V0 = %s" %trecho1.V0)
    print ("Q0 = %s" %trecho1.Q0)
    print ("Q_Q0_inicial = %s" %trecho1.Q_Q0_inicial)
    print ("Q_Q0_final = %s" %trecho1.Q_Q0_final)
    print ("V_V0_inicial = %s" %trecho1.V_V0_inicial)
    print ("V_V0_inicial = %s" %trecho1.V_V0_final)
    print ("Vi = %s" %trecho1.Vi)
    print ("Vf = %s" %trecho1.Vf)
    print ("Rh_D_inicial = %s" %trecho1.Rh_D_inicial)
    print ("Rh_D_final = %s" %trecho1.Rh_D_final)
    print ("Rhidraulico_inicial = %s" %trecho1.Rhidraulico_inicial)
    print ("Rhidraulico_final = %s" %trecho1.Rhidraulico_final)
    print ("Vcritica_inicial = %s" %trecho1.Vcritica_inicial)
    print ("Vcritica_final = %s" %trecho1.Vcritica_final)
    print ("h_D_inicial = %s" %trecho1.h_D_inicial)
    print ("h_D_final = %s" %trecho1.h_D_final)
    print ("Lamina_inicial = %s" %trecho1.Lamina_inicial)
    print ("Lamina_final = %s" %trecho1.Lamina_final)
    
    
    
