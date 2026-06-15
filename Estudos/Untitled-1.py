from tkinter import * 

window = Tk() #instalamos uma instancia de janela
window.title('Foda')
window.geometry('420x420')
window.config(background='#D5AAFF')

icon = PhotoImage(file='')
def abre():
    window = Tk() #instalamos uma instancia de janela
    window.title('Foda')
    window.geometry('')
    window.config(background='#D5AAFF')
    butão = Button(window,text='Clica=me',font=('Arial',10,'bold'))
    butão.config(command=abre)
    butão.pack()


butão = Button(window,
               text='Clica=me',
                font=('Arial',10,'bold'),
                image=icon,   )
butão.config(command=abre,
             bg='#D55AA0',
                fg="#FFD900",
                    activebackground="#FFA600",
                    activeforeground="#FF0000",
                    bd='10',
                        padx='10',
                        pady='10',
             image=icon,
             compound=('bottom'),
                )

butão.pack()
window.mainloop()
