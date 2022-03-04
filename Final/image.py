import colorsys

from PIL import Image
from PIL import ImageDraw

from noiseGenerator import noiseFactory

def showImg(file):
	img = Image.open(file)
	img.show()

def getVal(x, y, file):
	image = Image.open(file)

	#Get the RGB value of the pixel
	r, g, b = image.getpixel((x, y))
	#Translate the RGB to HSV in order to get opacity
	h, s, v = colorsys.rgb_to_hsv(r, g, b)

	return v / 10

def prodImg(scale, file, seed, octaves, bias, smooth, xchunk = 0, ychunk = 0):
	noiseGenerator = noiseFactory()

	img = Image.new("HSV", (scale,scale), "white")
	draw = ImageDraw.Draw(img)

	noiseGenerator.makeOctaveList(scale, scale, seed, smooth, octaves, bias, xchunk, ychunk) 

	values = noiseGenerator.list

	minVal = min(values)
	tempList = [x - minVal for x in values]

	maxVal = max(tempList)
	values = [x / maxVal * 100 for x in tempList]

	for x in range (scale):
		for y in range(scale):
			draw.rectangle([x,y,x+1,y+1], fill = (0,0, int(values[y * scale + x])))

	rgbImg = img.convert(mode="RGB")
	rgbImg.save(file)