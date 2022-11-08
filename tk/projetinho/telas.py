from tkinter import *

class Principal:
    def __init__(self, master):
        self.master = master

        self.master.title("Principal")
        self.img = PhotoImage(file="assets/icon2.png")

        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        self.menu.add_command(label="Arquivo")
        self.menu.add_command(label="Cadastro", command=self.openCadastro)
        self.menu.add_command(label="Help", command=self.openHelp)

        self.label = Label(self.master, image=self.img)
        self.label.pack()


    def openHelp(self):
        self.newWindow = Toplevel()
        Help(self.newWindow)

    def openCadastro(self):
        self.newWindow = Toplevel()
        Cadastrar(self.newWindow)

class Cadastrar:
    def __init__(self, screen):
        self.screen = screen
        self.screen.title("Cadastro Funcionário")

        self.inputFrame = LabelFrame(self.screen, text="Dados", bg="lightgray")
        self.inputFrame.grid(row=0, column=0, columnspan=2)

        self.cod = Label(self.inputFrame, text="Código:", font=("Arial 15"), bg="lightgray")
        self.cod.grid(row=0, column=0, pady=5, padx=5)
        self.name = Label(self.inputFrame, text="Nome do produto:", font=("Arial 15"), bg="lightgray")
        self.name.grid(row=1, column=0, pady=5, padx=5)
        self.cpf = Label(self.inputFrame, text="CPF:", font=("Arial 15"), bg="lightgray")
        self.cpf.grid(row=2, column=0, pady=5, padx=5)
        self.fone = Label(self.inputFrame, text="Fone:", font=("Arial 15"), bg="lightgray")
        self.fone.grid(row=3, column=0, pady=5, padx=5)
        self.end = Label(self.inputFrame, text="Endereço:", font=("Arial 15"), bg="lightgray")
        self.end.grid(row=4, column=0, pady=5, padx=5)
        self.cidade = Label(self.inputFrame, text="Cidade:", font=("Arial 15"), bg="lightgray")
        self.cidade.grid(row=5, column=0, pady=5, padx=5)

        self.codEntry = Label(self.inputFrame, relief="ridge", height=1, width=20)
        self.codEntry.grid(row=0, column=1, pady=5, padx=5)
        self.nameEntry = Entry(self.inputFrame)
        self.nameEntry.grid(row=1, column=1, pady=5, padx=5)
        self.cpfEntry = Entry(self.inputFrame)
        self.cpfEntry.grid(row=2, column=1, pady=5, padx=5)
        self.foneEntry = Entry(self.inputFrame)
        self.foneEntry.grid(row=3, column=1, pady=5, padx=5)
        self.endEntry = Entry(self.inputFrame)
        self.endEntry.grid(row=4, column=1, pady=5, padx=5)
        self.cidadeEntry = Entry(self.inputFrame)
        self.cidadeEntry.grid(row=5, column=1, pady=5, padx=5)

        self.frameButton = LabelFrame(self.screen, text="", bg="lightgray")
        self.frameButton.grid(row=1, column=0, columnspan=2)

        self.saveButton = Button(self.frameButton, text="Salvar")
        self.saveButton.grid(row=5, column=0, pady=10)
        self.deleteButton = Button(self.frameButton, text="Deletar")
        self.deleteButton.grid(row=5, column=1, pady=10)
        self.exitButton = Button(self.frameButton, text="Sair", command=self.screen.destroy)
        self.exitButton.grid(row=5, column=2, pady=10)

class Help:
    def __init__(self, screen):
        self.screen = screen
        self.screen.title("Help")

        self.text = Label(self.screen, text="Informações do sistema.\nLinha1\nLinha2\n\n\nLinha...")
        self.text.pack()

        self.button = Button(self.screen, text="Sair", command=self.screen.destroy)
        self.button.pack(side=RIGHT)

    def exit(self):
        self.screen.quit()