pt = ['Bebo','Bebe','Bebe','Bebeis','Bebem',"Trabalho",
    "Tempo",
    "Desafio",
    "Sucesso",
    "Aprendizado",
    "Mudança",
    "Objetivo",
    "Conhecimento",
    "Criatividade",
    "Desenvolvimento",
    "Equilíbrio",
    "Futuro",
    "Inovação",
    "Perspectiva",
    "Solução"]

En = ['Drank','Drinks','Drunk','Drank','Drank',"Work",
    "Time",
    "Challenge",
    "Success",
    "Learning",
    "Change",
    "Goal",
    "Knowledge",
    "Creativity",
    "Development",
    "Balance",
    "Future",
    "Innovation",
    "Perspective",
    "Solution"]

def traduzir(palavra):
    if palavra in pt:
        mediante = pt.index(f'{palavra}')
        traduzido = En.__getitem__(int(mediante))
        print(f'Em Ingles a palavra é {traduzido}')
    elif palavra in En:
        mediante = En.index(f'{palavra}')
        traduzido = pt.__getitem__(int(mediante))
        print(f'Em Portugues a palavra é {traduzido}')
    else:
        print('Palavra não encontrada')
        
print(f'Palavras atualmente disponiveis: {pt}')
print(f'Words currently available: {En}')

debivi = 'Sim'
while debivi == 'Sim':
    palavra = input('Escreva a palavra a ser traduzida: ').capitalize()
    traduzir(palavra)
    debivi = input('Deseja traduzir outra palavra? ').capitalize()