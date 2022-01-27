from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("450x420")
window.configure(bg = "#c0fffb")
canvas = Canvas(
    window,
    bg = "#c0fffb",
    height = 420,
    width = 450,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    225.0, 75.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:[print("Hi"), print("Swag")],
    relief = "flat")

b0.place(
    x = 25, y = 150,
    width = 400,
    height = 65)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 25, y = 240,
    width = 400,
    height = 65)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 25, y = 330,
    width = 400,
    height = 65)

window.resizable(False, False)
window.mainloop()
