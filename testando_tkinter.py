import tkinter as tk
import requests

base_url = "https://pokeapi.co/api/v2/"
def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
informações_poke = []
pokemon_name = str(input('Digite o nome do pokémon: '))
pokemon_info = get_pokemon_info(pokemon_name)
if pokemon_info:
    print(f"Nome: {pokemon_info["name"].capitalize()}")
    pk_ifo_name = str(pokemon_info['name'])
    informações_poke.append('Nome: ' + pk_ifo_name)
    
    print(f'Id: {pokemon_info['id']}')
    poke_info_ID = str(pokemon_info['id'])
    informações_poke.append('Id:' + poke_info_ID)
    
    print(f'Peso: {pokemon_info['weight']}')
    poke_info_WEIGHT = str(pokemon_info['weight'])
    informações_poke.append('Peso: ' + poke_info_WEIGHT)    
    
    #pole_info_imag = pokemon_info['sprites']['front_shiny']
    

chamar = str(input('Quer acessar a janela: ')).upper
#with open('C:\\Program Files\\Notepad++\\prjetos\\teste\\itemzados.txt', 'a') as file:
#    file.write('bana' + '\n')
#    file.close()        
#baka= ['mama','dfgdgr','vbvb','5555','123','sa']

def jan(altura,comprimento):
        root = tk.Tk()
        root.geometry(f"{altura}x{comprimento}")
       
        label = tk.Label(root,).grid(padx=110,pady=40)
        
        items = informações_poke
        var = tk.StringVar()
        var.set(items)
        listbox = tk.Listbox(root,height=10,width=30, listvariable=var).grid(padx=110,pady=0)

        root.mainloop()

def entrar():
    print('Aperte Enter duas vezes para resolucao padrao')
    altura = input('Altura da sessao(em pixeis): ')
    comprimento = input('Comprimento da sessao(em pixeis): ')
    
    while altura and comprimento == '':
        altura = input('Altura da janela: ')
        comprimento = input('Comprimento da jabela: ')

    if altura and comprimento != '':
        try:
            jan(altura,comprimento)

        except ValueError:
            print('Só numeros')
    else:
        jan(400,400)      
if chamar == 'Y' or 'YES':
    entrar()