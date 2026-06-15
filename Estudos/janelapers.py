
from tkinter import *



image = Tk()
image.geometry('1600x900')
image.resizable(height=True,width=True)
image.config(bg="#D49AFF",
             )
imagesd= PhotoImage(file='C:\\Users\\felip\\.vscode\\Images\\IMG-20260107-WA0000.png')
labe = Label(image,
      image = imagesd)   
Label.config(image,

)

labe.pack()
image.mainloop()

def rob():
    image = Tk()
    image.geometry('400x200')
    image.resizable(height=True,width=True)
    image.config(bg="#D49AFF",
             )

    Label(image,
          )
    Label.pack()
    image.mainloop()

entre = Entry(
        width=20,
            font=('Arial','10','bold'),
            )
entre.grid(row=0,column=1)

def ft_entry():
    result = int(entre.get())
    if result >= 5:
        rob()

bota = Button(text='Clica-me!'

)
bota.config(command=ft_entry,
            width=15,
            bd='10',
            )
bota.grid(row=0,column=2,padx=10)

entre.mainloop()