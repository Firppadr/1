#Deletar arquivos

import os
import shutil

path = 'projetos\\23423'

try:
    #os.remove(path) #deleta um arquivo
    os.rmdir(path) #deleta uma pasta
    #shutil.rmtree(path) #deleta pasta e seus arquivos

except FileExistsError:
    print('Aquivo não encontrado')
except PermissionError:
    print('Não tens o que é necessário')
except OSError:
    print('Não podes deletar usando essa função')
else:
    print(path+' foi removido')