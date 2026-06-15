from tkinter import *
import os
contador = 0
text = input('insira texto: ')



jane = Tk()
jane.title('Porta')
jane.geometry('300x300')
image2 = PhotoImage(file='')
jane.config(background='#D5AAFF',)


def texto():
    jane = Tk()
    jane.title('Porta')
    jane.geometry('300x300')
    image2 = PhotoImage(file='')
    jane.config(background='#D5AAFF',)
        
    botao = Button(jane,
        text='',
            font=('Arial',10,'bold'),
        )
        
    botao.config(command=texto,
        bg='#005523',
        bd='10',
            padx='10',
            pady='10',
            compound='bottom'
            )

    label = Label(jane,
        bd='10',
            font=('Arial','10','bold'),
                compound='top')
    
    label.config(text=text,
                 )

    label.pack()
    botao.pack()

    #with open('Cteste.txt','w') as file:
        #file.write('')
    global contador
    contador+=1
    print(contador)

botao = Button(jane,
    text='',
        font=('Arial',10,'bold'),)

botao.config(command=(texto),
                   
    bg='#005523',
    bd='10',
        padx='10',
        pady='10',)

label = Label(jane,
    bd='10',
        font=('Arial','10','bold'),
            compound='top'        )

label.config(text=text,)

label.pack()
botao.pack()
jane.mainloop()

