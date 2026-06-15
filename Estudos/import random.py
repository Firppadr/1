def novo_():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questoes:
        print('-----------------')
        print(key)
        for i in respostas[question_num-1]:
            print(i)
        guess = input('Insira resposta (A,B,C,D): ')
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_resp(questoes.get(key),guess)
        question_num +=1
    display_score(correct_guesses, guesses)


#-------------------------#

def check_resp(respostass, guess):
    if respostass == guess:
        print('Correto!')
        return 1
    else:
        print('Errado!')
    return 0

#-------------------------#

def display_score(correct_guesses, guesses):
    print('------------')
    print('Resutados!')
    print('------------')
    print('Respostas: ',end=' ')
    for i in questoes:
        print(questoes.get(i),end=' ')
    print()

    for i in guesses:
        print(i,end=' ')
    print()

    score = int((correct_guesses/len(questoes))*100)
    print('Sua pontuação é: '+str(score)+'%')

#-------------------------#

def dnv():

    response = input('Jogar denovo?(s/n): ')
    response = response.upper()

    if response == 'S':
        return True
    else:
        return False

#-------------------------#

questoes = {
    'Em que ano estamos?: ':'A',
    'Qual foi o ano passado?: ':'C',
    'quantos anões cabem numa bacia?:':'D'
}

respostas = [['A. 2026','B. 2025','C. 2020','D. 2023'],
             ['A. 2020','B. 2026','C. 2025','D. 2029'],
             ['A. 55','B. 23','C. 21','D. Muitos']]

novo_()
while (
        dnv() == True):
    novo_()
print('Tchauuu!!')