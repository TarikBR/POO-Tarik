from tkinter import *

class Tela:
    def __init__(self, master):
        self.nossaTela = master

        self.texto1 = Label(self.nossaTela, text="Insira seu nome")
        self.texto1.pack(side=TOP)

        self.entrada = Entry(self.nossaTela)
        self.entrada.pack(side=TOP)

        self.btn = Button(self.nossaTela, text="Continuar", command=self.mostrarNome)
        self.btn.pack(side=TOP, padx=10)

    def mostrarNome(self):
        self.textoNome = Label(self.nossaTela, text=f"Olá: {self.entrada.get()}")
        self.textoNome.pack(side=BOTTOM)

janelaRaiz = Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()