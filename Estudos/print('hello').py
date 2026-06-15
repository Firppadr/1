from tkinter import *
# widgets = Gui elements: buttons, textboxes, labels, images
#windows = serves as a contier to hod or contain these widgets

window = Tk() #instalamos uma instancia de janela
window.title('Foda')
window.geometry('')
window.config(background='#D5AAFF')
icon = PhotoImage(file='istockphoto-175539755-612x612-removebg-preview.png')
window.iconphoto(True,icon)

label = Label(window,
              text='Olá mundo',
              font=('Arial',10,'bold'),
              fg="#1A381A",
              bg="#FFFFFF",
              relief=SUNKEN,
              bd=10,
              padx=10,
              pady=10,
              image=icon,
              compound='bottom')
            
label.pack()

def abre():
    print('Olá')
button = Button(window,text='Clica-me!1!')
button.config(command=abre)
button.pack()
window.mainloop() #abre uma janela no computador, escutando eventos




