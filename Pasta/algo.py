import requests 
import json

url = 'https://stoic.tekloon.net/stoic-quote'
try:
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
    data = response.json()  # Converte a resposta para JSON
    quote = str(data['data']['quote'])  # Obtém a citação do JSON
    print(f"Citação estoica: {quote}") 
    with open('..\\armazem.txt', 'a') as file:
        file.write(f'{quote}' + '\n')

except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer a requisição: {e}")
