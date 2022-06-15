import os
import sys
from testinvert import percorrerArquivos, indexinvertido

def listDir(path):
    path = os.listdir()
    print(path)

if len (sys.argv) < 2 :
    print (''' 
Para verificar a lista de comandos digite <nomedoarquivo> /help''')
    sys.exit()
elif len (sys.argv) == 3:
    command2 = sys.argv[2]
    print(command2)

command = sys.argv[1]
print(command)

if command == '/help':
    print('''A lista de comandos é:

/listdir [Lista todos os diretórios e arquivos no diretório principal]
 |------> /listdir -files [Lista todos os arquivos no diretório principal]

/addindex  [Adiciona o diretório principal]
 |------> /addindex <diretorio> [Adiciona o diretório indicado]

/search <term> [Busca documentos apartir de uma palavra]

/tes
    ''')

path = os.getcwd()
dirList = os.listdir(path) 

if len (sys.argv) == 2:
    if command == '/listdir':
        print("Arquivos e diretórios em '", path, "' :")  
        print(dirList) 
    elif command == '/addindex':
        path = os.getcwd()
        print('O diretório principal foi adiconado.')
    elif command == '/search':
        print('Efetue a busca utilizando /search <termo>')    
elif len (sys.argv) == 3: 
    if command == '/listdir' and command2 == '-files':
        print(f'Os arquivos de texto presentes no diretório {path}:')
        for i in dirList:
            if i.endswith(".txt") == True:
                print(i)


