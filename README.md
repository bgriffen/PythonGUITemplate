Python GUI Template
=================

A basic template for making a GUI in Python using Traits. It gives you access to a matplotlib canvas object and Mayavi 3D rendering object which can be dynamically updated by adjusting the objects on the right panel. Tabbed viewing is also enabled by default.

## Requirements

There are two options to get you going, either:

* you will need Enthought's EPD distribution (32-bit, **not** 64-bit as it does not include Mayavi) which can be found [here](https://www.enthought.com/repo/epd/installers/). You will need an academic license to access it for free (simply requires a .edu email address). Go to the next step to install EPD if this is your choice (or if you are a beginner).

or,

* if you don't use EPD, you will need to change the `Common.py` file to have the header not use EPD's distribution. Simply replace the following where appropriate (you will need [TraitsUI](https://github.com/enthought/traitsui) **v5.0 or above** however):

```python
from traits.api import *
from traitsui.api import View,UItem, Item, Group, Heading, Label, \
        HSplit, Handler, CheckListEditor, EnumEditor, TableEditor, FileEditor, \
        ListEditor, Tabbed, VGroup, HGroup, RangeEditor, Spring, spring
from traitsui.menu import NoButtons
from traitsui.wx.editor import Editor
from traitsui.wx.basic_editor_factory import BasicEditorFactory
from traitsui.api import ColorTrait
```

If you do not have TraitsUI **v5.0 or above**, then you will get black backgrounds and odd interface errors. This took me quite some time to solve so please heed my advice!

If you are a beginner or new to Python, I suggest you install EPD (pacakge manager for Python and its tools):

`bash epd-7.3-2-rh5-x86.sh` ('rh3' for older operating systems) or just use the `.dmg` image for OSX.

## Running GUI

Run `ipython` then `run main.py` or `python main.py` outright. If you get errors, you will likely also have to install wxpython. Install via `conda install wxpython`. If you are on Mac OSX, you then run via `pythonw main.py`. On Ubuntu you just run `python main.py`.

## Adding your own features.

There is very comprehensive documentation on using Traits [here](http://code.enthought.com/projects/traits/documentation.php) and a lot of [tutorials](http://docs.enthought.com/traitsui/tutorials/index.html). I will be giving a few introductory sessions on my [blog](http://www.brendangriffen.com) as well.

## Screenshots

![Detault view upon launch.](http://www.brendangriffen.com/assets/pythongui/PythonGUIEx7-1024x599.png)

An example of the some of the features within Traits.  
![Example 1](http://www.brendangriffen.com/assets/pythongui/PythonGUIEx4Zoom.png)

Gnarly, dynamic updates!  
![Example 2](http://www.brendangriffen.com/assets/pythongui/PythonGUIEx5.png)

Example of enabling options when particular criteria are met.  
![Example 3](http://www.brendangriffen.com/assets/pythongui/PythonGUIEx6.png)

