from Common import *

class FirstCalc(HasTraits):

    # Add Traits objects
    option = Bool(True)
    rangex = Range(1,10,5)
    yval = Float()
    listoptions = Enum(['Option 1', 'Option 2','Option 2'])
    stringopt = Str("Default string which can also be empty.")
    stringoptread = Str("Default string which can also be empty [read-only version].")
    masterpath = Directory(os.getcwd())
    button1 = Button("Button 1 Name")
    floatval = Float()
    changedcount = Int()
    plotbutton = Button("Plot Me!")
    yintcept = Range(0.0,5.,10.)
    gradient = Range(0.0,5.0,10.)

    #Construct the view

    view = View(
                Item(name='rangex',label='X-Value'),
                Item(name='yval',style='readonly',label='1/x',format_str='%.2e'),
                Item(name='listoptions',label='list of options'),
                Item(name='stringopt'),
                Item(name='stringoptread',style='readonly'),
                Item(name='masterpath',label='Directory'),
                Group(Item(name='button1',show_label=False)),
                Group(Item(name='option',label='Boolean Option')
                     ,enabled_when='floatval < 0.5',label='Enabled Area Upon Random Value < 0.5',show_border=True
                     ),
                Item(name='changedcount',style='readonly',label='Attempts'),
                Item(name='floatval',label='random generated'),
                Group(Item(name='gradient',label='gradient'),
                      Item(name='yintcept',label='y-intercept'),
                      Item(name='plotbutton',show_label=False),show_border=True,label='Plotting Area')
                )

    def _gradient_changed(self):
        y = self.gradient * np.array(range(10)) + self.yintcept

        figure = self.main.display
        figure.clear()
        ax = figure.add_subplot(111)
        ax = self.main.display.axes[0]
        ax.plot(np.array(range(10)),y,color=self.main.markercolor,
                marker=self.main.markerstyle,
                markersize=self.main.markersize,
                markeredgewidth=0.0,
                linestyle='-')
        wx.CallAfter(self.main.display.canvas.draw)

    def _yintcept_changed(self):
        y = self.gradient * np.array(range(10)) + self.yintcept

        figure = self.main.display
        figure.clear()
        ax = figure.add_subplot(111)
        ax = self.main.display.axes[0]
        ax.plot(np.array(range(10)),y,color=self.main.markercolor,
                marker=self.main.markerstyle,
                markersize=self.main.markersize,
                markeredgewidth=0.0,
                linestyle='-')
        wx.CallAfter(self.main.display.canvas.draw)

    def _rangeplotx_changed(self):
        figure.clear()
        y 
        ax = figure.add_subplot(111)
        ax = self.main.display.axes[0]
        ax.plot(xtmp,ytmp,color=self.main.markercolor,
                marker=self.main.markerstyle,
                markersize=self.main.markersize,
                markeredgewidth=0.0,
                linestyle='None')
        wx.CallAfter(self.main.display.canvas.draw)

    def _rangex_changed(self):
        self.yval = 1./self.rangex

    def _button1_fired(self):
        self.changedcount += 1
        self.floatval = random.random()

    def _floatval_changed(self):
        self.stringopt = "Hey, you changed the integer value!"

    def __init__(self, main, **kwargs):
        HasTraits.__init__(self)
        self.main = main
        
    
