import requests
import json
from tkinter import *


repeat = True

master = Tk()
master.title("Teste")
master.geometry("150x130")

master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

coinsPrice = Label(master, text="")
coinsPrice.grid(row=0, column=0)

def exit():
    master.quit()

stopButton = Button(master, text="Sair", command=exit)
stopButton.grid(row=1, column=0)

def getCot():
    if repeat:
        data = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL")
        jsonData = json.loads(data.content)
        
        text = ""
        for coin in jsonData:
            #print(f"{jsonData[coin]['code']}: {jsonData[coin]['bid']}")
            text += f"{jsonData[coin]['code']}: {jsonData[coin]['bid']} {jsonData[coin]['pctChange']}%\n"

        coinsPrice["text"] = text
        master.after(1000, getCot)

getCot()

master.mainloop()
