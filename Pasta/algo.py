import requests 

url = 'https://stoic.tekloon.net/stoic-quote'

response = requests.get(url)
response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
data = response.json()  # Converte a resposta para JSON
quote = str(data['data']['quote'])  # Obtém a citação do JSON
print(f"Citação estoica: {quote}") 
with open('armazem.txt', 'a', encoding='utf-8') as file:
    file.write(f'{quote}' + '\n')
    print('Citação salva no arquivo armazem.txt')
