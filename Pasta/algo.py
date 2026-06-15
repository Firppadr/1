import requests 
import os

pasta_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_completo_txt = os.path.join(pasta_do_script, 'armazem.txt')
url = 'https://stoic.tekloon.net/stoic-quote'

response = requests.get(url)
response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
data = response.json()  # Converte a resposta para JSON
quote = str(data['data']['quote'])  # Obtém a citação do JSON
print(f"Citação estoica: {quote}") 
with open(caminho_completo_txt, 'a', encoding='utf-8') as file:
    file.write(f'{quote}' + '\n')
    print('Citação salva no arquivo armazem.txt')
