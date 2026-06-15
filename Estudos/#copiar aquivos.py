#copiar aquivos
#   copyfile() = copia o conteudo de um arquivo
#   copy() = copyfie() + permission mode + destination can be a directory
#   copy2() = copy() + copies metadata (file's creation and modification times)   

import shutil

shutil.copyfile('Cteste.txt','C:\\Users\\felip\\OneDrive\\Desktop\\copy.txt') #dois arguentos: src,dst source and destination