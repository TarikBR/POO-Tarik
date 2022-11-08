from tkinter import *

class Tela:
    def __init__(self, master):
        self.screen = master

        self.frame = Frame(self.screen)
        self.frame.pack(ipadx=30, ipady=30)

        self.label = Label(self.frame, text="Insira os segundos:")
        self.label.pack(side=LEFT)

        self.entry = Entry(self.frame)
        self.entry.pack(side=LEFT, padx=26)

        self.button = Button(self.screen, text="Converter", bg="red", command=self.convert)
        self.button.pack()

        self.exitText = Label(self.screen)
        self.exitText.pack(pady=15)

    def convert(self):
        seconds = int(self.entry.get())
        weeks = str(seconds // (86400 * 7))
        days = str((seconds % (86400 * 7)) // 86400)
        hours = str((seconds % 86400) // 3600)
        minutes = str((seconds % 3600) // 60)
        seconds = str((seconds % 3600) % 60)

        converted = f"{weeks}w {days}d {hours}h {minutes}m {seconds}s"

        self.exitText["text"]= converted

screenMaster = Tk()
Tela(screenMaster)
screenMaster.mainloop()