from tkinter import *


class ldHmapMenu:
    def back(self):
        print("Back")
        
    def generate(self):
        print("Generate")

    def loadHeightmap(self):
        windowLoadHeightmap = Tk()

        windowLoadHeightmap.geometry("845x330")
        windowLoadHeightmap.configure(bg = "#c0fffb")
        canvas = Canvas(
            windowLoadHeightmap,
            bg = "#c0fffb",
            height = 330,
            width = 845,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"Final/assets/ldHmapBackground.png")
        background = canvas.create_image(
            451.5, 177.5,
            image=background_img)

        img0 = PhotoImage(file = f"Final/assets/back.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.back,
            relief = "flat")

        b0.place(
            x = 435, y = 247,
            width = 190,
            height = 65)

        img1 = PhotoImage(file = f"Final/assets/generate.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.generate,
            relief = "flat")

        b1.place(
            x = 635, y = 247,
            width = 190,
            height = 65)

        entry0_img = PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry0_bg = canvas.create_image(
            220.0, 269.5,
            image = entry0_img)

        entry0 = Entry(
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        entry0.place(
            x = 55.0, y = 237,
            width = 330.0,
            height = 63)

        entry1_img = PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry1_bg = canvas.create_image(
            220.0, 179.5,
            image = entry1_img)

        entry1 = Entry(
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        entry1.place(
            x = 55.0, y = 147,
            width = 330.0,
            height = 63)

        entry2_img = PhotoImage(file = f"Final/assets/wideTextBox.png")
        entry2_bg = canvas.create_image(
            620.0, 179.5,
            image = entry2_img)

        entry2 = Entry(
            bd = 0,
            bg = "#e1dbbb",
            highlightthickness = 0)

        entry2.place(
            x = 455.0, y = 147,
            width = 330.0,
            height = 63)

        windowLoadHeightmap.resizable(False, False)
        windowLoadHeightmap.mainloop()
