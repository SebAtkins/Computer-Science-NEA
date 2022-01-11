import os
import colorsys

from PIL import Image
from PIL import ImageDraw

import NewPerlinTest as perl 

def showImg(file="swag.png"):
	img = Image.open(file)
	img.show()

def getVal(x, y, file="swag.png"):
	swag = Image.open(file)

	#Get the RGB value of the pixel
	r, g, b = swag.getpixel((x, y))
	#Translate the RGB to HSV in order to get opacity
	h, s, v = colorsys.rgb_to_hsv(r, g, b)

	return v / 10

def prodImg(scale=16, file="swag.png", seed=123, octaves=3, bias=0.8, smooth = 25, xchunk = 0, ychunk = 0):
	testPerl = perl.noiseFactory()

	img = Image.new("HSV", (scale,scale), "white")
	draw = ImageDraw.Draw(img)

	testPerl.makeOctaveList(scale, scale, seed, smooth, octaves, bias, xchunk, ychunk) # Add x-offset and y-offset

	swag = testPerl.list

	temp = [x - min(swag) for x in swag]
	swag = [x / max(temp) * 100 for x in temp]

	for x in range (scale):
		for y in range(scale):
			draw.rectangle([x,y,x+1,y+1], fill = (0,0, int(swag[y * scale + x])))

	rgbImg = img.convert(mode="RGB")
	rgbImg.save(file)