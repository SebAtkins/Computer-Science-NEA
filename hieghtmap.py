import os

from PIL import Image
from PIL import ImageDraw

import NewPerlinTest as perl

from random import randint

scale = 128
seed = 9834
smoothness = 25
octaves = 8
persistance = 0.6
xOffset = 1
yOffset = 2

img = Image.new("RGB", (scale, scale), "white")
draw = ImageDraw.Draw(img)

noise = perl.noiseFactory()
noise.makeOctaveList(scale, scale, seed, smoothness, octaves, persistance, yOffset, xOffset)

swag = noise.returnList()

temp = [x - min(swag) for x in swag]
swag = [x / max(temp) * 255 for x in temp]

for x in range (scale):
	for y in range(scale):
		draw.rectangle([x,y,x+1,y+1], fill = ((1 - int(swag[y * scale + x])),0, int(swag[y * scale + x])))

img.show()
img.save("C:/Users/sebat/Desktop/CS NEA/swag.png")
