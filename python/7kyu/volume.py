"""
Find the volume of a cone whose radius and height are provided as parameters to the function volume. Use the value of PI provided by your language (for example: Math.PI in JS, math.pi in Python or Math::PI in Ruby) and round down the volume to an Interger.
"""

import math
def volume(r,h):
    return int(1/3*math.pi*r*r*h)
