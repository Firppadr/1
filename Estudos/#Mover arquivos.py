#Mover arquivos

import os

source = 'copy.txt'
destinatio = 'C:\\Users\\felip\\OneDrive\\Desktop\\copy.txt'

try:
    if os.path.exists(destinatio):
        print('Arquivo já existe')
    else:
        os.replace(source,destinatio)
        print(source+ ' foi movido')



except FileNotFoundError:
    print(source+ 'nao encontrado')

