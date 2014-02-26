
from firstcalc import FirstCalc
from secondcalc import SecondCalc

from tvtk.pyface.scene_editor import SceneEditor
from mayavi.tools.mlab_scene_model import MlabSceneModel
from mayavi.core.ui.mayavi_scene import MayaviScene

from Common import *

class ApplicationMain(HasTraits):

    scene = Instance(MlabSceneModel, ())
    
    firstcalc = Instance(FirstCalc)
    secondcalc = Instance(SecondCalc)
    display = Instance(Figure)
    markercolor = ColorTrait
    markerstyle = Enum(['+',',','*','s','p','d','o'])
    markersize = Range(0,10,2)
 
    left_panel  = Tabbed(Group(VGroup(Item('display', editor=MPLFigureEditor(),show_label=False, resizable=True)),
                               HGroup(Item(name='markercolor', label="Color", style="custom",springy=True),
                                      Item(name='markerstyle', label="Marker",springy=True),
                                      Item(name='markersize', label="Size",springy=True)), label='Display'),
                               Item(name='scene',label='Mayavi',editor=SceneEditor(scene_class=MayaviScene)),show_labels=False)

    right_panel = Tabbed(Item('firstcalc', style='custom', label='First Tab',show_label=False),
                         Item('secondcalc', style='custom', label='Second Tab',show_label=False))
    
    view = View(HSplit(left_panel,
                 right_panel),
                width = 1280,
                height = 750,
                resizable = True,
                title="Proving Grounds"
            )

    def _display_default(self):
        """Initialises the display."""
        figure = Figure()
        ax = figure.add_subplot(111)
        ax = figure.axes[0]
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_xlim(0,1)
        ax.set_ylim(0,1)
 
        # Set matplotlib canvas colour to be white
        rect = figure.patch
        rect.set_facecolor('w')
        return figure

    def _firstcalc_default(self):
        # Initialize halos the way we want to.
        # Pass a reference of main (e.g. self) downwards
        return FirstCalc(self)

    def _secondcalc_default(self):
        # Initialize halos the way we want to.
        # Pass a reference of main (e.g. self) downwards
        return SecondCalc(self)

    def _markercolor_changed(self):
        ax = self.display.axes[0]
        if hasattr(self, 'display_points'): 
            self.display_points.set_color(self.markercolor)
            self.display_points.set_markeredgecolor(self.markercolor)
            wx.CallAfter(self.display.canvas.draw)

    def _markerstyle_changed(self):
        ax = self.display.axes[0]
        if hasattr(self, 'display_points'): 
            self.display_points.set_marker(self.markerstyle)
            wx.CallAfter(self.display.canvas.draw)

    def _markersize_changed(self):
        ax = self.display.axes[0]
        if hasattr(self, 'display_points'): 
            self.display_points.set_markersize(self.markersize)
            wx.CallAfter(self.display.canvas.draw)

    def __init__(self, **kwargs):
        self.markercolor = 'blue'
        self.markersize = 2
        self.markerstyle = 'o'

if __name__ == '__main__':
    app = ApplicationMain()
    app.configure_traits()
