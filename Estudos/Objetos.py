from tkinter import *


class Chave:
    def __init__(self):
        
        J2 = Toplevel()
        J2.title('Titulo')
        J2.resizable(width=True,height=True)
        J2.geometry('300x300')

        bota = Button(J2,
            command=Chave,
            padx=10,
            pady=10,
        ).place(x=130,y=130) 
        
        J2.mainloop()

class chave2(Chave):
    
    Label(relief='solid',
          text=('Inventário: '
            ),bd=0
          ).place(x=75,y=75)


chave2()
            