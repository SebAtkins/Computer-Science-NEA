from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("845x420")
window.configure(bg = "#c0fffb")
canvas = Canvas(
    window,
    bg = "#c0fffb",
    height = 420,
    width = 845,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    416.5, 167.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 228, y = 338,
    width = 190,
    height = 65)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 428, y = 338,
    width = 190,
    height = 65)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    120.0, 182.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e1dbbb",
    highlightthickness = 0)

entry0.place(
    x = 57.5, y = 150,
    width = 125.0,
    height = 63)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    320.0, 182.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e1dbbb",
    highlightthickness = 0)

entry1.place(
    x = 257.5, y = 150,
    width = 125.0,
    height = 63)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    620.0, 182.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#e1dbbb",
    highlightthickness = 0)

entry2.place(
    x = 455.0, y = 150,
    width = 330.0,
    height = 63)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    220.0, 267.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#e1dbbb",
    highlightthickness = 0)

entry3.place(
    x = 55.0, y = 235,
    width = 330.0,
    height = 63)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    620.0, 267.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#e1dbbb",
    highlightthickness = 0)

entry4.place(
    x = 455.0, y = 235,
    width = 330.0,
    height = 63)

window.resizable(False, False)
window.mainloop()
