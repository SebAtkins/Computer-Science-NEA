import random
import os
import math

from PIL import Image
from PIL import ImageDraw

class perlin:
	seeds = []
	out = []

	def prodImg(self, file="swag.png"):
		img = Image.new("HSV", (int(math.sqrt(len(self.out))),int(math.sqrt(len(self.out)))), "white")
		draw = ImageDraw.Draw(img)
		for x in range (int(math.sqrt(len(self.out)))):
			for y in range(int(math.sqrt(len(self.out)))):
				draw.rectangle([x,y,x+1,y+1], fill = (0,0, int(self.getVal(x, y))))
		rgbImg = img.convert(mode="RGB")
		rgbImg.save(file)

	def getVal(self, x, y, xscale = 1):
		return self.out[y * x * xscale + x] / 50

	def interpolate(self, a, b, f):
		if 0.0 > f:
			return a
		elif 1.0 < f:
			return b
		else:
			return (b-a)*((f*(f* 6.0-15.0)+10.0)*f*f*f)+a

	def gen(self, width, height, change = 123):
		random.seed(change)
		for x in range(width * height):
			self.seeds.append(random.random())
		self.out = [None] * (width * height)

	def noise(self, width, height, change = 123, octaves = 3, bias = 2):
		self.gen(width, height, change)

		largest = 0

		for x in range(width):
			for y in range(height):
				noise = 0
				scaleTot = 0
				scale = 1

				for o in range(octaves):
					pitch = width >> o

					x1 = int(x/pitch) * pitch
					y1 = int(y/pitch) * pitch

					x2 = (x1 + pitch) % width
					y2 = (y1 + pitch) % width

					blendX = (x - x1) / pitch
					blendY = (y - y1) / pitch

					t1 = self.interpolate(self.seeds[y1 * width + x1], self.seeds[y1 * width + x2], blendX)
					t2 = self.interpolate(self.seeds[y2 * width + x1], self.seeds[y2 * width + x2], blendX)

					#t1 = (1 - blendX) * self.seeds[y1 * width + x1] + blendX * self.seeds[y1 * width + x2]
					#t2 = (1 - blendX) * self.seeds[y2 * width + x1] + blendX * self.seeds[y2 * width + x2]

					scaleTot += scale
					noise += (blendY * (t2 - t1) + t1) * scale
					scale = scale / bias

				if noise > largest:
					largest = noise

				self.out[y * width + x] = round(noise * 100 / largest, 5)


"""test = perlin()
test.noise(32, 32, 123, 6)
print(len(test.out), max(test.out), min(test.out))"""