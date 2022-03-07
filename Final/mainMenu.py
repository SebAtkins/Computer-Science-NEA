import os

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from render import show
from generate import runGen
from image import prodImg
from image import showImg

class mainMenu:
    def genTerrain(self):
        self.window.withdraw()
        genTerrainGUI = genTerrainMenu(self.window)
        genTerrainGUI.menu()

    def genHeightmap(self):
        self.window.withdraw()
        genHmapGUI = genHmapMenu(self.window)
        genHmapGUI.menu()

    def ldHeightmap(self):
        self.window.withdraw()
        ldHmapGUI = ldHmapMenu(self.window)
        ldHmapGUI.loadHeightmap()

    def createMenu(self):
        self.window = tk.Tk()

        self.window.geometry("450x420")
        self.window.configure(bg = "#c0fffb")
        canvas = tk.Canvas(
            self.window,
            bg = "#c0fffb",
            height = 420,
            width = 450,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = tk.PhotoImage(file = f"Final/assets/terrainGeneratorBackground.png")
        background = canvas.create_image(
            225.0, 75.0,
            image=background_img)

        img0 = tk.PhotoImage(file = f"Final/assets/genTerrBut.png")
        b0 = tk.Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.genTerrain,
            relief = "flat")

        b0.place(
            x = 25, y = 150,
            width = 400,
            height = 65)

        img1 = tk.PhotoImage(file = f"Final/assets/genHmapBut.png")
        b1 = tk.Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.genHeightmap,
            relief = "flat")

        b1.place(
            x = 25, y = 240,
            width = 400,
            height = 65)

        img2 = tk.PhotoImage(file = f"Final/assets/ldHmapBut.png")
        b2 = tk.Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.ldHeightmap,
            relief = "flat")

        b2.place(
            x = 25, y = 330,
            width = 400,
            height = 65)

        self.window.resizable(False, False)
        self.window.mainloop()

class genHmapMenu:
    def __init__(self, root):
        self.root = root

    def exit_function(self):
        self.root.destroy()
    
    def back(self):
        self.root.deiconify()
        self.window.destroy()

    def generate(self):
        try:
            xSize = int(self.xSize.get())
            ySize = int(self.ySize.get())
            seed = int(self.seed.get())
            bias = float(self.bias.get())
            smoothing = int(self.smoothing.get())

            output = tk.filedialog.asksaveasfilename()

            try:
                prodImg(xSize, ySize, output, seed, smoothing, bias, 25)
                showImg(output)
            except:
                messagebox.showerror(title="Error", 
                                     message="Please ensure valid file")
        except:
            messagebox.showerror(title="Error", 
                                 message="Please ensure all data is the correct type")

    def menu(self):
        self.window = tk.Toplevel(self.root)

        self.window.protocol('WM_DELETE_WINDOW', self.exit_function)

        self.window.geometry("845x420")
        self.window.configure(bg = "#c0fffb")
        canvas = tk.Canvas(
            self.window,
            bg = "#c0fffb",
            height = 420,
            width = 845,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = tk.PhotoImage(file = f"Final/assets/genHmapBackground.png")
        background = canvas.create_image(
            416.5, 167.0,
            image=background_img)

        img0 = tk.PhotoImage(file = f"Final/assets/back.png")
        b0 = tk.Button(
            self.window,
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.back,
            relief = "flat")

        b0.place(
            x = 228, y = 338,
            width = 190,
            height = 65)

        img1 = tk.PhotoImage(file = f"Final/assets/generate.png")
        b1 = tk.Button(
            self.window,
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.generate,
            relief = "flat")

        b1.place(
            x = 428, y = 338,
            width = 190,
            height = 65)

        entry0_img = tk.PhotoImage(file = f"Final/assets/thinTextBox.png")
        entry0_bg = canvas.create_image(
            120.0, 182.5,
            image = entry0_img)

        self.xSize = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.xSize.place(
            x = 57.5, y = 150,
            width = 125.0,
            height = 63)

        entry1_img = tk.PhotoImage(file = f"Final/assets/thinTextBox.png")
        entry1_bg = canvas.create_image(
            320.0, 182.5,
            image = entry1_img)

        self.ySize = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.ySize.place(
            x = 257.5, y = 150,
            width = 125.0,
            height = 63)

        entry2_img = tk.PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry2_bg = canvas.create_image(
            620.0, 182.5,
            image = entry2_img)

        self.seed = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.seed.place(
            x = 455.0, y = 150,
            width = 330.0,
            height = 63)

        entry3_img = tk.PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry3_bg = canvas.create_image(
            220.0, 267.5,
            image = entry3_img)

        self.bias = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.bias.place(
            x = 55.0, y = 235,
            width = 330.0,
            height = 63)

        entry4_img = tk.PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry4_bg = canvas.create_image(
            620.0, 267.5,
            image = entry4_img)

        self.smoothing = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.smoothing.place(
            x = 455.0, y = 235,
            width = 330.0,
            height = 63)

        self.window.resizable(False, False)
        self.window.mainloop()


class genTerrainMenu:
    def __init__(self, root):
        self.root = root

    def back(self):
        self.root.deiconify()
        self.window.destroy()

    def exit_function(self):
        self.root.destroy()
    
    def generate(self):
        try:
            xSize = int(self.xSize.get())
            ySize = int(self.ySize.get())
            bias = float(self.bias.get())
            smoothing = int(self.smoothing.get())
            seed = int(self.seed.get())
            genNormals = bool(self.genNormals.get())

            output = tk.filedialog.asksaveasfilename()

            try:
                prodImg(xSize, ySize, "temp.png", seed, smoothing, bias, 25)
                runGen(xSize, ySize, output, "temp.png", genNormals)
                show(output)
            except:
                messagebox.showerror(title="Error", 
                                     message="Please ensure valid file")

        except:
            messagebox.showerror(title="Error", 
                                 message="Please ensure all data is the correct type")


    def menu(self):
        self.window = tk.Toplevel(self.root)

        self.window.protocol('WM_DELETE_WINDOW', self.exit_function)

        self.window.geometry("845x420")
        self.window.configure(bg = "#c0fffb")
        canvas = tk.Canvas(
            self.window,
            bg = "#c0fffb",
            height = 420,
            width = 845,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = tk.PhotoImage(file = f"Final/assets/genTerrBackground.png")
        background = canvas.create_image(
            448.0, 222.0,
            image=background_img)

        img0 = tk.PhotoImage(file = f"Final/assets/back.png")
        b0 = tk.Button(
            self.window,
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.back,
            relief = "flat")

        b0.place(
            x = 435, y = 335,
            width = 190,
            height = 65)

        img1 = tk.PhotoImage(file = f"Final/assets/generate.png")
        b1 = tk.Button(
            self.window,
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.generate,
            relief = "flat")

        b1.place(
            x = 635, y = 335,
            width = 190,
            height = 65)

        entry0_img = tk.PhotoImage(file = f"Final/assets/thinTextBox.png")
        entry0_bg = canvas.create_image(
            120.0, 182.5,
            image = entry0_img)

        self.xSize = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.xSize.place(
            x = 57.5, y = 150,
            width = 125.0,
            height = 63)

        entry1_img = tk.PhotoImage(file = f"Final/assets/thinTextBox.png")
        entry1_bg = canvas.create_image(
            320.0, 182.5,
            image = entry1_img)

        self.ySize = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.ySize.place(
            x = 257.5, y = 150,
            width = 125.0,
            height = 63)

        entry2_img = tk.PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry2_bg = canvas.create_image(
            620.0, 182.5,
            image = entry2_img)

        self.seed = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.seed.place(
            x = 455.0, y = 150,
            width = 330.0,
            height = 63)

        entry3_img = tk.PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry3_bg = canvas.create_image(
            220.0, 357.5,
            image = entry3_img)

        self.genNormals = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.genNormals.place(
            x = 55.0, y = 325,
            width = 330.0,
            height = 63)

        entry4_img = tk.PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry4_bg = canvas.create_image(
            220.0, 267.5,
            image = entry4_img)

        self.bias = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.bias.place(
            x = 55.0, y = 235,
            width = 330.0,
            height = 63)

        entry5_img = tk.PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry5_bg = canvas.create_image(
            620.0, 267.5,
            image = entry5_img)

        self.smoothing = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.smoothing.place(
            x = 455.0, y = 235,
            width = 330.0,
            height = 63)

        self.window.resizable(False, False)
        self.window.mainloop()

class ldHmapMenu:
    def __init__(self, root):
        self.root = root

    #Tkinter Handling Bits
    def back(self):
        self.root.deiconify()
        self.window.destroy()
        
    def generate(self):
        try:
            xSize = int(self.xSize.get())
            ySize = int(self.ySize.get())
            genNormals = bool(self.genNormals.get())

            image = os.path.splitext(tk.filedialog.askopenfilename())[0]
            output = tk.filedialog.asksaveasfilename()

            try:
                runGen(xSize, ySize, output, image + ".png", genNormals)
                show(output)
            except:
                messagebox.showerror(title="Error", 
                                     message="Please ensure size is smaller than image")
        except:
            messagebox.showerror(title="Error", 
                                 message="Please ensure all data is the correct type")

    def exit_function(self):
        self.root.destroy()

    def loadHeightmap(self):
        self.window = tk.Toplevel(self.root)

        self.window.protocol('WM_DELETE_WINDOW', self.exit_function)

        self.window.geometry("845x330")
        self.window.configure(bg = "#c0fffb")
        canvas = tk.Canvas(
            self.window,
            bg = "#c0fffb",
            height = 330,
            width = 845,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = tk.PhotoImage(file = f"Final/assets/ldHmapBackground.png")
        background = canvas.create_image(
            451.5, 177.5,
            image=background_img)

        img0 = tk.PhotoImage(file = f"Final/assets/back.png")
        b0 = tk.Button(
            self.window,
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.back,
            relief = "flat")

        b0.place(
            x = 435, y = 247,
            width = 190,
            height = 65)

        img1 = tk.PhotoImage(file = f"Final/assets/generate.png")
        b1 = tk.Button(
            self.window,
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.generate,
            relief = "flat")

        b1.place(
            x = 635, y = 247,
            width = 190,
            height = 65)

        entry0_img = tk.PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry0_bg = canvas.create_image(
            220.0, 269.5,
            image = entry0_img)

        self.genNormals = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.genNormals.place(
            x = 55.0, y = 237,
            width = 330.0,
            height = 63)

        entry1_img = tk.PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry1_bg = canvas.create_image(
            220.0, 179.5,
            image = entry1_img)

        self.xSize = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.xSize.place(
            x = 55.0, y = 147,
            width = 330.0,
            height = 63)

        entry2_img = tk.PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry2_bg = canvas.create_image(
            620.0, 179.5,
            image = entry2_img)

        self.ySize = tk.Entry(
            self.window,
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        self.ySize.place(
            x = 455.0, y = 147,
            width = 330.0,
            height = 63)

        self.window.resizable(False, False)
        self.window.mainloop()

mainGUI = mainMenu()
mainGUI.createMenu()