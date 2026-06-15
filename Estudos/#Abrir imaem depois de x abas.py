#Abrir imaem depois de x abas
from tkinter import *




porta = Tk()
porta.title('ola')
porta.resizable(width=True,height=True)
porta.geometry('300x300')


label = Label(porta,
        font=('Arial','10','bold'),)
label.config(text='Insira',)
label.pack()


#entrars = Entry(
        #width=10,
            #font=('Arial','10','bold'),)
#entrars.grid(row=0,column=2)


contador = 0
def click(): 
    global contador,imagestrado  
    contador+=1
    print(contador)
    if contador >= 5:
            
            mamo = Toplevel()
            mamo.geometry('1600x900')
            mamo.title('Tatu')
            img = PhotoImage(file='C:\\Users\\felip\\.vscode\\Images\\roberto.png')
            abel = Label(mamo,image=img)
            abel.img = img
            abel.pack()
          
         

def combine_funcs(*funcs):
    def combined_func(*click, **oloc):
        for f in funcs:
            f(*click, **oloc)
    return combined_func   

    
    

def oloc():
        porta2 = Toplevel()
        porta2.title('ola')
        porta2.resizable(width=True,height=True)
        porta2.geometry('300x300')

        bota2 = Button(porta2,
                       text='Clica-me!')
        bota2.config(command= combine_funcs(click,oloc),
            width=15,)
        bota2.pack()
        porta2.mainloop()

bota = Button(text='Clock')
bota.config(command=oloc,
            width=15,)
bota.pack()
 

porta.mainloop()
