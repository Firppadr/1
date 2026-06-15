from tkinter import *
from Objetos import Chave

contador = 0
J1 = Tk()

def conta():
    global contador
    contador+=1
    label.config(text=contador)

J1.title('Titulo')
J1.resizable(width=True,height=True)
J1.geometry('300x300')

label = Label(J1,
              text=contador,
              )

botao = Button(J1,
               command=conta,
                padx=10,
                pady=10,
               ).place(x=130,y=130)
label.pack()
J1.mainloop()