from tkinter import *

class Tela:
    def __init__(self, master):
        self.nossaTela = master

        self.l1 = Label(self.nossaTela, text="label 1")
        self.l1.pack()

        self.l2 = Label(self.nossaTela, text="label 2")
        self.l2.pack(side=BOTTOM)

        self.l3 = Label(self.nossaTela, text="label 3")
        self.l3.pack(side=LEFT)

        self.l4 = Label(self.nossaTela, text="label 4")
        self.l4.pack(side=RIGHT)

janelaRaiz = Tk()
janelaRaiz.geometry("125x100")

Tela(janelaRaiz)

janelaRaiz.mainloop()