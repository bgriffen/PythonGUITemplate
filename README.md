Python GUI Template
=================

A basic template for making a GUI in Python using Traits. It gives you access to a matplotlib canvas object and Mayavi 3D rendering object which can be dynamically updated by adjusting the objects on the right panel. Tabbed viewing is also enabled by default.

![Detault view upon launch.](http://www.brendangriffen.com/assets/pythongui/PythonGUIEx7-1024x599.png)

An example of the some of the features within Traits.  
![Example 1](http://www.brendangriffen.com/assets/pythongui/PythonGUIEx4Zoom.png)

Gnarly, dynamic updates!  
![Example 2](http://www.brendangriffen.com/assets/pythongui/PythonGUIEx5.png)

Example of enabling options when particular criteria are met.  
![Example 3](http://www.brendangriffen.com/assets/pythongui/PythonGUIEx6.png)

## Requirements

You will need Enthought's EPD distribution (32-bit, **not** 64-bit as it does not include Mayavi) which can be found [here](https://www.enthought.com/repo/epd/installers/). You will need an academic license to access it for free.

## Installing EPD:

`bash epd-7.3-2-rh5-x86.sh` ('rh3' for older operating systems) or just use the `.dmg` image for OSX.

## Running GUI

`ipython` then `run main.py` or `python main.py` outright.

## Adding your own features.

There is very comprehensive documentation on using Traits [here](http://code.enthought.com/projects/traits/documentation.php) and a lot of [tutorials](http://docs.enthought.com/traitsui/tutorials/index.html). I will be giving a few introductory sessions on my [blog](http://www.brendangriffen.com) as well.
