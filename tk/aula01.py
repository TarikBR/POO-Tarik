from tkinter import *
from tkinter.ttk import Treeview
import pymongo
import random

master = Tk()
master.title("Aula 01")

master.geometry("700x400")
master.resizable(width=False, height=False)
master.grid_columnconfigure(0, weight=1)
master.grid_columnconfigure(1, weight=1)

master.config(bg="#BCCEF8")
master.iconphoto(False, PhotoImage(file='./assets/icon.png'))

dbClient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = dbClient["aula01"]
mycol = mydb["products"]

idValue = StringVar()

productsList = []

def exit():
    master.quit()

# Labels
input_frame = LabelFrame(master, text='Valores', bg="lightgray", font=('Consolas', 14))
input_frame.grid(row=0, column=0, columnspan=2)

cod = Label(input_frame, text="Código:", font=("Arial 15"), bg="lightgray")
cod.grid(row=0, column=0, pady=5, padx=5)
name = Label(input_frame, text="Nome do produto:", font=("Arial 15"), bg="lightgray")
name.grid(row=1, column=0, pady=5, padx=5)
valor = Label(input_frame, text="Valor:", font=("Arial 15"), bg="lightgray")
valor.grid(row=2, column=0, pady=5, padx=5)
validade = Label(input_frame, text="Validade:", font=("Arial 15"), bg="lightgray")
validade.grid(row=0, column=2, pady=5, padx=5)
origem = Label(input_frame, text="Origem:", font=("Arial 15"), bg="lightgray")
origem.grid(row=1, column=2, pady=5, padx=5)

# Entrys
codEntry = Label(input_frame, textvariable=str(idValue), relief="ridge", height=1, width=20)
codEntry.grid(row=0, column=1, pady=5, padx=5)
nameEntry = Entry(input_frame)
nameEntry.grid(row=1, column=1, pady=5, padx=5)
valorEntry = Entry(input_frame)
valorEntry.grid(row=2, column=1, pady=5, padx=5)
validadeEntry = Entry(input_frame)
validadeEntry.grid(row=0, column=3, pady=5, padx=5)
origemEntry = Entry(input_frame)
origemEntry.grid(row=1, column=3, pady=5, padx=5)

# Treeview
view = Treeview(master, columns=(1,2,3,4,5), height="8", show="headings")
view.grid(row=2, column=0, columnspan=2)

view.heading(1, text="Código", anchor="center")
view.heading(2, text="Nome", anchor="center")
view.heading(3, text="Valor", anchor="center")
view.heading(4, text="Validade", anchor="center")
view.heading(5, text="Origem", anchor="center")

view.column("#1", anchor="center", width=120, stretch=False)
view.column("#2", anchor="center", width=120, stretch=False)
view.column("#3", anchor="center", width=120, stretch=False)
view.column("#4", anchor="center", width=120, stretch=False)
view.column("#5", anchor="center", width=120, stretch=True)

vsb = Scrollbar(view, orient="vertical", command=view.yview)
vsb.place(x=(120*5)-9.5, height=185, relwidth=0.02)
view.configure(yscrollcommand=vsb.set)


# Functions
def generateNewID():
    while True:
        newID = random.randint(1000000000, 9999999999)
        idCheck = mycol.find({"_id": str(newID)})
        dataList = [i for i in idCheck]
        if len(dataList) == 0:
            codEntry.configure(text="")
            idValue.set(str(newID))
            break

def addEntry():
    productCode = idValue.get()
    productName = nameEntry.get()
    productPrice = valorEntry.get()
    productValidate = validadeEntry.get()
    productOrig = origemEntry.get()

    global productsList
    productsList.append({"_id": productCode, "data":{"name":productName, "price":productPrice, "validate":productValidate, "orig":productOrig}})

    view.insert("", index="end", values=(productCode, productName, productPrice, productValidate, productOrig))

    mycol.insert_one({"_id": productCode, "data":{"name":productName, "price":productPrice, "validate":productValidate, "orig":productOrig}})

    clearEntrys()

def deleteEntry():
    mycol.delete_one({"_id":idValue.get()})

    generateNewID()
    clearEntrys()
    loadView()


def clearEntrys():
    nameEntry.delete(0, END)
    valorEntry.delete(0, END)
    validadeEntry.delete(0, END)
    origemEntry.delete(0, END)
    generateNewID()

def loadView():
    for item in view.get_children():
        view.delete(item)

    global productsList
    productsList.clear()
    for x in mycol.find():
        productsList.append(x)

    for key in productsList:
        view.insert("", index="end",
            values=(key["_id"], key["data"]["name"], key["data"]["price"], key["data"]["validate"], key["data"]["orig"]))

def load_edit_field_with_row_data(_tuple):
    if len(_tuple) == 0:
        return

    idValue.set(_tuple[0])
    nameEntry.delete(0, END)
    nameEntry.insert(0, _tuple[1])
    valorEntry.delete(0, END)
    valorEntry.insert(0, _tuple[2])
    validadeEntry.delete(0, END)
    validadeEntry.insert(0, _tuple[3])
    origemEntry.delete(0, END)
    origemEntry.insert(0, _tuple[4])

def MouseButtonUpCallBack(event):
    if len(view.selection()) != 0:
        currentRowIndex = view.selection()[0]
        lastTuple = (view.item(currentRowIndex, 'values'))
        load_edit_field_with_row_data(lastTuple)
view.bind("<ButtonRelease>", MouseButtonUpCallBack)


# Buttons
frameButton = LabelFrame(master, text="", bg="lightgray")
frameButton.grid(row=1, column=0, columnspan=2)

saveButton = Button(frameButton, text="Salvar", command=addEntry)
saveButton.grid(row=5, column=0, pady=10)
deleteButton = Button(frameButton, text="Deletar", command=deleteEntry)
deleteButton.grid(row=5, column=1, pady=10)
deleteButton = Button(frameButton, text="Limpar", command=clearEntrys)
deleteButton.grid(row=5, column=2, pady=10)
exitButton = Button(frameButton, text="Sair", command=exit)
exitButton.grid(row=5, column=3, pady=10)

generateNewID()
loadView()
master.mainloop()
