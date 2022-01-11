import main
import tkinter as tk
from tkinter import filedialog

#Functions
def generate():
    main.run(str(input.get()),
             str(output.get()),
             int(seed.get()),
             int(xshift.get()),
             int(xshift.get()))

#Creating Tkinter instance
root = tk.Tk()
root.title("Terrain Generator 0.1.6")

#Input file
#Output file
#Seed
#X Shift
#Z Shift

#Text
tk.Label(root, text="Input File").grid(row=0)
tk.Label(root, text="Output File").grid(row=1)
tk.Label(root, text="Seed").grid(row=2)
tk.Label(root, text="X-Shift").grid(row=3)
tk.Label(root, text="Z-Shift").grid(row=4)

#Inputs
input=tk.Entry(root, width=30)
input.grid(row=0,column=1)
input.insert(10,"test.obj")

output=tk.Entry(root, width=30)
output.grid(row=1,column=1)
output.insert(10,"testOut.obj")

seed=tk.Entry(root, width=30)
seed.grid(row=2,column=1)
seed.insert(10,"123456")

xshift=tk.Entry(root, width=30)
xshift.grid(row=3,column=1)
xshift.insert(10,"0")

zshift=tk.Entry(root, width=30)
zshift.grid(row=4,column=1)
zshift.insert(10,"0")

#Buttons
tk.Button(root, text="Quit", command=root.quit).grid(row=0, column=3)
tk.Button(root, text="Generate", command=generate).grid(row=1, column=3)

root.mainloop()
