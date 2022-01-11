import os

from PIL import Image
from PIL import ImageDraw
from PIL import *

import perlinWIP

from random import randint
import colorsys

swag = Image.open("swag.png")

r, g, b = swag.getpixel((7,9))
h, s, v = colorsys.rgb_to_hsv(r, g, b)
print(h, s, v)