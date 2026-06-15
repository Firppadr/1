#importar os
import os
path = 'C:\\Users\\felip\\OneDrive\\Desktop\\teste.txt'

if os.path.exists(path):
    print('Existe!')
    if os.path.isfile(path):
        print('e É um Aquivo')
    elif os.path.isdir(path):
        print('e é um Diretório')
else:
    print('Se fodeu')