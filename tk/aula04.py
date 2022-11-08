from tkinter import *

class Tela:
    def __init__(self, master):
        self.nossaTela = master

        self.fr1 = Frame(self.nossaTela)
        self.fr1.pack()
        self.fr2 = Frame(self.nossaTela)
        self.fr2.pack()
        self.fr3 = Frame(self.nossaTela)
        self.fr3.pack()

        self.btn1 = Button(self.fr1, text="1", width=2, height=2)
        self.btn1.pack()

        self.btn2 = Button(self.fr2, text="2", width=2, height=2)
        self.btn2.pack(side=LEFT)
        self.btn3 = Button(self.fr2, text="3", width=2, height=2)
        self.btn3.pack(side=LEFT)

        self.btn4 = Button(self.fr3, text="4", width=2, height=2)
        self.btn4.pack(side=LEFT)
        self.btn5 = Button(self.fr3, text="5", width=2, height=2)
        self.btn5.pack(side=LEFT)
        self.btn6 = Button(self.fr3, text="6", width=2, height=2)
        self.btn6.pack(side=LEFT)

janelaRaiz = Tk()
Tela(janelaRaiz)

janelaRaiz.mainloop()
