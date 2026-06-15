#Abrir aquivos
try:
    with open('C:\\Users\\felip\\OneDrive\\Desktop\\teste.txt') as file:
        print(file.read())
except FileNotFoundError:print('Este aquivo nao existe')