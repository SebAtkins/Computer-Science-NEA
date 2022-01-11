import os

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import render as r
import newObjGen as g 
import readImg as read

#Default Functions
def genTerrain(xScale, yScale, image, seed, octaves, bias, normals, outFile, smooth = 25, xchunk = 0, ychunk = 0):
	g.makeImg(xScale, image + ".png", seed, octaves, bias, smooth, xchunk, ychunk)
	g.imgGen(xScale, yScale, image + ".png", normals, outFile)

	r.show(outFile + ".obj")

def genHeightmap(hScale, outFile, seed, octaves, bias):
	g.makeImg(hScale, outFile + ".png", seed, octaves, bias)

	read.showImg(outFile + ".png")

def loadHeightmap(xScale, yScale, image, normals, outFile):
	g.imgGen(xScale, yScale, image + ".png", normals, outFile)

	r.show(outFile + ".obj")

#Menu Functions
def runLoadHeight():
	"""
	This is the handler for loadHeightmap()
	This function performs simple checks on data inputted from selectHeightTerrain()
	Returns an error if the desired size is larger than the input image
	"""
	global x, y, normal

	try:
		xd = int(x.get())
		yd = int(y.get())
		nd = bool(normal.get())

		image = os.path.splitext(tk.filedialog.askopenfilename())[0]
		output = tk.filedialog.asksaveasfilename()

		try:
			loadHeightmap(xd, yd, image, nd, output)
		except:
			messagebox.showerror(title="Error", message="Terrain size larger than image")
	except:
		messagebox.showerror(title="Error", message="Please ensure all data is legal")

def runGenHeight():
	"""
	This is the handler for genHeightmap()
	This function performs simple checks on data inputted from selectGenImg()
	Also returns errors if octaves is too high
	"""
	global seed, scale, octaves, bias

	try:
		s = int(seed.get())
		sc = int(scale.get())
		o = int(octaves.get())
		b = float(bias.get())

		name = tk.filedialog.asksaveasfilename()

		try:
			genHeightmap(sc, name, s, o, b)
		except:
			messagebox.showerror(title="Error", message="Octaves too high")

	except:
		messagebox.showerror(title="Error", message="Please ensure all data is legal")

def runGenTerrain():
	"""
	This is the handler for genTerrain()
	This function performs simple checks on data inputted from selectTerrain()
	Also returns errors if octaves is too high
	"""
	global smooth, xScale, yScale, seed, octaves, bias, normals

	try:
		sm = int(smooth.get())
		x = int(xScale.get())
		y = int(yScale.get())
		s = int(seed.get())
		o = int(octaves.get())
		b = float(bias.get())
		n = bool(normals.get())

		name = tk.filedialog.asksaveasfilename()

		try:
			genTerrain(x, y, "temp", s, o, b, n, name, sm)
		except:
			messagebox.showerror(title="Error", message="Octaves too high")
	except:
		messagebox.showerror(title="Error", message="Please ensure all data is legal")

#Root Functions
def selectTerrain():
	"""
	This function creates the UI for generating terrain from a seed.
	"""
	global smooth, xScale, yScale, seed, bias, octaves, normals, menu

	rootS.withdraw()
	menu = tk.Toplevel(root)

	#Labels
	tk.Label(menu, text="Seed", width = 10, height = 3).grid(row=0)
	tk.Label(menu, text="X Scale", width = 10, height = 3).grid(row=1)
	tk.Label(menu, text="Y Scale", width = 10, height = 3).grid(row=2)
	tk.Label(menu, text="Smoothness", width = 10, height = 3).grid(row=3)
	tk.Label(menu, text="Octaves", width = 15, height = 3).grid(row=4)
	tk.Label(menu, text="Bias", width = 15, height = 3).grid(row=5)
	tk.Label(menu, text="Generate Normals", width = 15, height = 3).grid(row=6)

	#Data Entry Bits
	seed=tk.Entry(menu, width=30)
	seed.grid(row=0,column=1)
	seed.insert(10,"123456")

	xScale=tk.Entry(menu, width=30)
	xScale.grid(row=1,column=1)
	xScale.insert(10,"64")

	yScale=tk.Entry(menu, width=30)
	yScale.grid(row=2,column=1)
	yScale.insert(10,"64")

	smooth=tk.Entry(menu, width=30)
	smooth.grid(row=3,column=1)
	smooth.insert(10,"25")

	octaves=tk.Entry(menu, width=30)
	octaves.grid(row=4,column=1)
	octaves.insert(10,"3")

	bias=tk.Entry(menu, width=30)
	bias.grid(row=5,column=1)
	bias.insert(10,"0.8")

	normals=tk.Entry(menu, width=30)
	normals.grid(row=6,column=1)
	normals.insert(10,"False")

	#Buttons
	quit = tk.Button(menu, text="Back", command=lambda:[menu.destroy(), rootS.deiconify()], width = 25, height = 3)
	quit.grid(row=7, column = 1)

	gen = tk.Button(menu, text="Generate Terrain", command=runGenTerrain, width = 25, height = 3)
	gen.grid(row=7, column = 0)

def selectHeightImg():
	"""
	This function creates the UI for generating a heightmap.
	"""
	#Admin-y bits
	global seed, scale, octaves, bias, menu

	rootS.withdraw()
	menu = tk.Toplevel(root)

	#Label-y bits
	tk.Label(menu, text="Seed", width = 10, height = 3).grid(row=0)
	tk.Label(menu, text="Scale", width = 10, height = 3).grid(row=1)
	tk.Label(menu, text="Octaves", width = 10, height = 3).grid(row=2)
	tk.Label(menu, text="Bias", width = 10, height = 3).grid(row=3)

	#Input-y bits
	seed=tk.Entry(menu, width=30)
	seed.grid(row=0,column=1)
	seed.insert(10,"123456")

	scale=tk.Entry(menu, width=30)
	scale.grid(row=1,column=1)
	scale.insert(10,"128")

	octaves=tk.Entry(menu, width=30)
	octaves.grid(row=2,column=1)
	octaves.insert(10,"5")

	bias=tk.Entry(menu, width=30)
	bias.grid(row=3,column=1)
	bias.insert(10, "0.8")

	#Button-y bits
	quit = tk.Button(menu, text="Back", command=lambda:[menu.destroy(), rootS.deiconify()], width = 25, height = 3)
	quit.grid(row=4, column = 1)

	gen = tk.Button(menu, text="Generate Heightmap", command=runGenHeight, width = 25, height = 3)
	gen.grid(row=4, column = 0)

def selectHeightTerrain():
	"""
	This function creates the UI for generating terrain from a heightmap.
	"""
	#Admin-y bits
	global x, y, normal, menu

	rootS.withdraw()
	menu = tk.Toplevel(root)

	#Label-y bits
	tk.Label(menu, text="X Scale", width = 10, height = 3).grid(row=0)
	tk.Label(menu, text="Y Scale", width = 10, height = 3).grid(row=1)
	tk.Label(menu, text="Generate Normals", width = 15, height = 3).grid(row=2)

	#Data-entry-y bits
	x = tk.Entry(menu, width = 30)
	x.grid(row=0, column = 1)
	x.insert(10, "64")

	y = tk.Entry(menu, width = 30)
	y.grid(row=1, column = 1)
	y.insert(10, "64")

	normal = tk.Entry(menu, width = 30)
	normal.grid(row=2, column = 1)
	normal.insert(10, "False")

	#Button-y bits
	quit = tk.Button(menu, text="Back", command=lambda:[menu.destroy(), rootS.deiconify()], width = 25, height = 3)
	quit.grid(row=3, column = 1)

	gen = tk.Button(menu, text="Generate Terrain", command=runLoadHeight, width = 25, height = 3)
	gen.grid(row=3, column = 0)

#Silly tkinter stuff
rootS = tk.Tk()
rootS.title("Terrain Generator 0.2.0")

root = tk.Frame(rootS, borderwidth=1, bg="black")
root.pack(fill="both", expand=True)

selTer = tk.Button(root, text="Generate Terrain", command=selectTerrain, width = 50, height = 3)
selHImg = tk.Button(root, text="Generate Heightmap", command=selectHeightImg, width = 50, height = 3)
selHTer = tk.Button(root, text="Import Heightmap", command=selectHeightTerrain, width = 50, height = 3)
quit = tk.Button(root, text="Quit", command=root.quit, width = 50, height = 3)

selTer.pack()
selHImg.pack()
selHTer.pack()

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x')

quit.pack()

root.mainloop()