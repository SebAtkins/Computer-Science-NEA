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

def prodImg(xScale, yScale, file, seed, octaves, bias, smooth, xchunk = 0, ychunk = 0):
	noiseGenerator = noiseFactory()

	img = Image.new("HSV", (xScale,yScale), "white")
	draw = ImageDraw.Draw(img)

	noiseGenerator.makeOctaveList(xScale, yScale, seed, smooth, octaves, bias, xchunk, ychunk) 

	values = noiseGenerator.list

	minVal = min(values)
	tempList = [x - minVal for x in values]

	maxVal = max(tempList)
	values = [x / maxVal * 100 for x in tempList]

	for x in range (xScale):
		for y in range(yScale):
			draw.rectangle([x,y,x+1,y+1], fill = (0,0, int(values[y * xScale + x])))

	rgbImg = img.convert(mode="RGB")
	rgbImg.save(file)

prodImg(160, 100, "Final/swag.png", 12345, 4, 0.67, 25)