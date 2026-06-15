import random

balanço_inicial = 100
print(f'Você possui {balanço_inicial}')
numaposta = ''
choise = input('Deseja jogar? Y/N: ').upper
quantaposta = ''
def jogar(choise):
    if choise == 'Y' or 'YES':
        return True

while jogar(choise) == True:
    while numaposta == '':
        numaposta = input('Qual número você aposta-rá?: ')
    while quantaposta == '':
        quantaposta = input('Quanto aposta-rá?: ')
    
    x = random.choice([1,1])
    
    if int(numaposta) == x:
        print('você ganhou!')
        balanço_inicial+=int(quantaposta)*2
        print(f'Agora você tem {balanço_inicial} moedas!')
        


