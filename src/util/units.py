"""This module stores basic unit conversion factors. Base units for the
program are km, s, kg. The convention is to store the conversion factor
from unit A to the base unit in a variable named after unit A. 

For example, 1 meter is 1/1000 kilometers, so m = 1/1000. If you have a length 
of 500 m you want to label with the variable name x, you would declare it as 
such:
    x = 500 *m. x would then equal 500/1000 = 0.5. 
To use the module in this manner, declare:
    from units import *
"""

nm = 1e-12
um = 1e-9
mm = 1e-6
cm = 1e-5
m = 1e-3
km = 1
AU = 149597870.7

ns = 1e-9
us = 1e-6
ms = 1e-3
s = 1

mg = 1e-6
g = 1e-3
kg = 1