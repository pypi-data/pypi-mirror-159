from json import tool
from tkinter import Button
from matplotlib.pyplot import axes, show
import wx
import wx.lib.agw.aui as aui
import wx.lib.mixins.inspection as wit

from matplotlib import figure as mplfig
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas, NavigationToolbar2WxAgg as NavigationToolbar

from .PyCrosssections import profile
from .PyTranslate import _
from .PyVertex import getIfromRGB,getRGBfromI

class PlotPanel(wx.Panel):
    '''
    Un seul Panneau du notebook
    
    Plusieurs sizers : 
        - sizerfig (horizontal) avec la figure en premier élément --> l'ajout se place à droite
        - sizer    (vertical) avec comme éléments sizerfig et la barre d'outils Matplotlib --> l'ajout se place en dessous
    '''

    figure:mplfig.Figure

    def __init__(self, parent, id=-1, dpi=None,toolbar=True, **kwargs):
        super().__init__(parent, id=id, **kwargs)
        self.figure = mplfig.Figure(dpi=dpi, figsize=(2,2))    #Création d'une figure Matplotlib

        self.canvas = FigureCanvas(self, -1, self.figure)       #Création d'un Canvas wx pour contenir le dessin de la figure Matplotlib

        self.sizerfig = wx.BoxSizer(wx.HORIZONTAL)                        #ajout d'un sizer pour placer la figure et la barre d'outils l'une au-dessus de l'autre
        self.sizer = wx.BoxSizer(wx.VERTICAL)                        #ajout d'un sizer pour placer la figure et la barre d'outils l'une au-dessus de l'autre

        self.sizerfig.Add(self.canvas, 1, wx.EXPAND)                    #ajout du canvas
        self.sizer.Add(self.sizerfig, 1, wx.EXPAND)                    #ajout du canvas

        if toolbar:
            self.toolbar = NavigationToolbar(self.canvas)           #Ajout d'une barre d'outils pour la figure courante
            self.toolbar.Realize()
            self.sizer.Add(self.toolbar, 0, wx.LEFT| wx.EXPAND)         #ajout de la barre
            
        self.SetSizer(self.sizer)                                    #application du sizer
        
        self.myax=None
    
    def add_ax(self):
        if self.myax is None:
            self.myax = self.figure.add_subplot()
        return self.myax
    
    def get_fig_ax(self):
        if self.myax is None:
            self.myax = self.figure.add_subplot()
        return self.figure,self.myax

class PlotCS(PlotPanel):
    '''
    Panels de traçage des sections en travers
    @author Pierre Archambeau
    '''
    
    def __init__(self, parent, id=-1, dpi=None, mycs=None, **kwargs):
        
        super().__init__(parent, id, dpi, **kwargs)
        
        self.mycs:profile
        self.mycs = mycs
        self.ls = None
        self.length = 100.

        self.second_fig = None
        self.second_ax = None
        
        self.sizernextprev = wx.BoxSizer(wx.HORIZONTAL)                        #ajout d'un sizer pour placer la figure et la barre d'outils l'une au-dessus de l'autre
        self.sizerposbank = wx.BoxSizer(wx.HORIZONTAL)                        #ajout d'un sizer pour placer la figure et la barre d'outils l'une au-dessus de l'autre
        
        self.sizer.Add(self.sizernextprev,0,wx.EXPAND)
        self.sizer.Add(self.sizerposbank,0,wx.EXPAND)

        self.ButPrev = wx.Button(self,label=_("Previous"))
        self.ButNext = wx.Button(self,label=_("Next"))

        curs=5000
        self.slidergenhor = wx.Slider(self, wx.ID_ANY, curs, 0, 10000, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL,name='sliderhor' )
        self.slidergenver = wx.Slider(self, wx.ID_ANY, curs, 0, 10000, wx.DefaultPosition, wx.DefaultSize, wx.SL_VERTICAL,name='sliderver' )
        self.sizer.Add(self.slidergenhor,0,wx.EXPAND)
        self.sizerfig.Add(self.slidergenver,0,wx.EXPAND)
        
        self.sizernextprev.Add(self.ButPrev,1,wx.LEFT| wx.EXPAND)
        self.sizernextprev.Add(self.ButNext,1,wx.LEFT| wx.EXPAND)
        
        self.sizerslider1 = wx.BoxSizer(wx.VERTICAL)
        curs = 0.
        self.sliderleft = wx.Slider(self, wx.ID_ANY, curs, 0, 10000, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL,name='sliderleft' )
        self.txtleft = wx.TextCtrl( self, wx.ID_ANY, str(curs), wx.DefaultPosition, wx.DefaultSize, style=wx.TE_CENTER|wx.TE_PROCESS_ENTER,name='textleft' )
        self.sizerslider1.Add( self.sliderleft, 1, wx.EXPAND)
        self.sizerslider1.Add( self.txtleft, 0, wx.EXPAND)
        self.sizerposbank.Add(self.sizerslider1,1,wx.EXPAND)

        self.sizerslider2 = wx.BoxSizer(wx.VERTICAL)
        curs = 0.
        self.sliderbed = wx.Slider(self, wx.ID_ANY, curs, 0, 10000, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL,name='sliderbed' )
        self.txtbed = wx.TextCtrl( self, wx.ID_ANY, str(curs), wx.DefaultPosition, wx.DefaultSize, style=wx.TE_CENTER|wx.TE_PROCESS_ENTER,name='textbed' )
        self.sizerslider2.Add( self.sliderbed, 1, wx.EXPAND)
        self.sizerslider2.Add( self.txtbed, 0, wx.EXPAND)
        self.sizerposbank.Add(self.sizerslider2, 1, wx.EXPAND)
        
        self.sizerslider3 = wx.BoxSizer(wx.VERTICAL)
        curs = 0.
        self.sliderright = wx.Slider(self, wx.ID_ANY, curs, 0, 10000, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL,name='sliderright' )
        self.txtright = wx.TextCtrl( self, wx.ID_ANY, str(curs), wx.DefaultPosition, wx.DefaultSize, style=wx.TE_CENTER|wx.TE_PROCESS_ENTER,name='textright' )
        self.sizerslider3.Add( self.sliderright, 1, wx.EXPAND)
        self.sizerslider3.Add( self.txtright, 0, wx.EXPAND)
        self.sizerposbank.Add(self.sizerslider3, 1, wx.EXPAND)
        
        self.txtbed.Bind(wx.EVT_TEXT_ENTER,self.movebanksslider)
        self.txtleft.Bind(wx.EVT_TEXT_ENTER,self.movebanksslider)
        self.txtright.Bind(wx.EVT_TEXT_ENTER,self.movebanksslider)

        self.sliderleft.Bind(wx.EVT_SLIDER,self.movebanksslider)
        self.sliderbed.Bind(wx.EVT_SLIDER,self.movebanksslider)
        self.sliderright.Bind(wx.EVT_SLIDER,self.movebanksslider)

        self.slidergenhor.Bind(wx.EVT_SLIDER,self.movegenslider)
        self.slidergenver.Bind(wx.EVT_SLIDER,self.movegenslider)

    def set_cs(self,mycs:profile):
        
        self.mycs=mycs
        self.ls = self.mycs.asshapely_ls()
        self.length = self.ls.length

        curs = self.ls.project(self.mycs.bankleft.as_shapelypoint())
        self.sliderleft.SetValue(curs)
        self.txtleft.SetLabelText(str(curs))

        curs = self.ls.project(self.mycs.bed.as_shapelypoint())
        self.sliderbed.SetValue(curs)
        self.txtbed.SetLabelText(str(curs))
        
        curs = self.ls.project(self.mycs.bankleft.as_shapelypoint())
        self.sliderright.SetValue(curs)
        self.txtright.SetLabelText(str(curs))

    def movegenslider(self,event):
        if self.mycs is None:
            return
        
        id = event.GetEventObject().GetName()
        cs:profile = self.mycs

        if id=='sliderhor':
            cs.sdatum = float(self.slidergenhor.Value-5000)/10000.*self.length
            cs.add_sdatum=True
        elif id=='sliderver':
            cs.zdatum = -float(self.slidergenver.Value-5000)/1000.
            cs.add_zdatum=True
            
        self.plot_cs()
        self.ls=self.mycs.asshapely_ls()
        
    def movebanksslider(self,event:wx.Event):
        if self.mycs is None:
            return
        
        id = event.GetEventObject().GetName()
        cs:profile = self.mycs

        if id=='sliderleft':
            curs=float(self.sliderleft.Value)/10000.*self.length
            self.txtleft.SetValue("{0:.2f}".format(curs))
            cs.movebankbedslider('left',self.ls.interpolate(curs))
        elif id=='sliderright':
            curs=float(self.sliderright.Value)/10000.*self.length
            self.txtright.SetValue("{0:.2f}".format(curs))
            cs.movebankbedslider('right',self.ls.interpolate(curs))
        elif id=='sliderbed':
            curs=float(self.sliderbed.Value)/10000.*self.length
            self.txtbed.SetValue("{0:.2f}".format(curs))
            cs.movebankbedslider('bed',self.ls.interpolate(curs))
        elif id=='textleft':
            curs=float(self.txtleft.Value)
            if curs<0.:
                self.txtleft.SetValue('0.')
                curs=0.
            elif curs>self.length:
                self.txtleft.SetValue(str(self.length))
                curs=self.length
            curslider = int(curs/self.length*10000.)
            self.sliderleft.SetValue(curslider)
            cs.movebankbedslider('left',self.ls.interpolate(curs))
        elif id=='textright':
            curs=float(self.txtright.Value)
            if curs<0.:
                self.txtright.SetValue('0.')
                curs=0.
            elif curs>self.length:
                curs=self.length
                self.txtright.SetValue(str(self.length))
            curslider = int(curs/self.length*10000.)
            self.sliderright.SetValue(curslider)
            cs.movebankbedslider('right',self.ls.interpolate(curs))
        elif id=='textbed':
            curs=float(self.txtbed.Value)
            if curs<0.:
                self.txtbed.SetValue('0.')
                curs=0.
            elif curs>self.length:
                self.txtbed.SetValue(str(self.length))
                curs=self.length
            curslider = int(curs/self.length*10000.)
            self.sliderbed.SetValue(curslider)
            cs.movebankbedslider('bed',self.ls.interpolate(curs))
        
        self.plot_cs()

    # def movebanks(self,event:wx.Event):
    #     if self.mycs is None:
    #         return
        
    #     '''Mouvement des berges'''
    #     id = event.GetEventObject().GetName()
        
    #     cs:profile = self.mycs
        
    #     if id=="BLLeft":
    #         cs.movebankbed('left','left')
    #     elif id=="BLRight":
    #         cs.movebankbed('left','right')
    #     elif id=="BRLeft":
    #         cs.movebankbed('right','left')
    #     elif id=="BRRight":  
    #         cs.movebankbed('right','right')
    #     elif id=="BedLeft":
    #         cs.movebankbed('bed','left')
    #     elif id=="BedRight":  
    #         cs.movebankbed('bed','right')
            
    #     self.plot_cs()
    
    def plot_cs(self):
        cs:profile = self.mycs
        cs.plot_cs(fig=self.figure,ax=self.myax)
        if self.second_fig is not None:
            cs.plot_cs(fig=self.second_fig,ax=self.second_ax,forceaspect=False)
                            
    def plot_up(self,event):
        
        self.mycs:profile
        
        self.mycs.myprop.width=1
        self.mycs.myprop.color=0

        if self.mycs.up is not None:
            self.set_cs(self.mycs.up)
        
        self.plot_cs()
                
        self.mycs.myprop.width=2
        self.mycs.myprop.color=getIfromRGB([255,0,0])
    
    def plot_down(self,event):
        
        self.mycs.myprop.width=1
        self.mycs.myprop.color=0

        if self.mycs.down is not None:
            self.set_cs(self.mycs.down)
        
        self.plot_cs()
                
        self.mycs.myprop.width=2
        self.mycs.myprop.color=getIfromRGB([255,0,0])

class PlotNotebook(wx.Panel):
    '''
    Fenêtre contenant potentiellement plusieurs graphiques Matplotlib
    '''
    
    def __init__(self, parent = None, id=-1,show=True,framesize=(1024,768)):
        '''Initialisation
         Si un parent est fourni, on l'attache, sinon on crée une fenêtre indépendante
        '''
        if parent is None:
            self.frame = wx.Frame(None, -1, 'Plotter',size=framesize)
            super().__init__(self.frame, id=id)
        else:
            self.frame=parent
            super().__init__(parent, id=id)

        self.ntb = aui.AuiNotebook(self)    #ajout du notebook 
        sizer = wx.BoxSizer()               #sizer pour servir de contenant au notebook
        sizer.Add(self.ntb, 1, wx.EXPAND)   #ajout du notebook au sizer et demande d'étendre l'objet en cas de redimensionnement
        self.SetSizer(sizer)                #applique le sizer
        if show:
            self.frame.Show()
            
        self.Bind(wx.EVT_CLOSE , self.OnClose)

    def OnClose(self):
        self.Hide()

    def add(self, name="plot",which=""):
        '''
        Ajout d'un onglet au notebook
        L'onglet contient une Figure Matplotlib
        On retourne la figure du nouvel onglet
        '''
        
        if which=="":
            page = PlotPanel(self.ntb)               #crée un objet Plot
            self.ntb.AddPage(page, name)        #ajout de l'objet Plot au notebook
        elif which=="CS":
            page = PlotCS(self.ntb)               #crée un objet Plot
            page2 = PlotPanel(self.ntb)               #crée un objet Plot
            self.ntb.AddPage(page, name)        #ajout de l'objet Plot au notebook
            self.ntb.AddPage(page2, name+' expand')        #ajout de l'objet Plot au notebook
            
            ax=page.add_ax()
            ax2=page2.add_ax()
            
            page.second_fig = page2.figure
            page.second_ax = ax2
            
        return page                  

    def getfigure(self,index = -1, caption="") -> mplfig.Figure:
        if index!=-1:
            return self.ntb.GetPage(index).figure
        elif caption!="":
            for curpage in range(self.ntb.GetPageCount()):
                if caption==self.ntb.GetPageText(curpage):
                    return self.ntb.GetPage(curpage).figure
            return
        else:
            return

def demo():
    app = wx.App()
    # frame = wx.Frame(None, -1, 'Plotter')
    plotter = PlotNotebook()
    axes1 = plotter.add('figure 1').figure.add_subplot()
    axes1.plot([1, 2, 3], [2, 1, 4])
    # axes2 = plotter.add('figure 2').add_subplot()
    # axes2.plot([1, 2, 3, 4, 5], [2, 1, 4, 2, 3])

    fig=plotter.getfigure(0)
    fig.get_axes()[0].plot([5, 6, 10], [2, 1, 10])
    app.MainLoop()

if __name__ == "__main__":
    demo()