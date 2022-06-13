import os
import sys

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

/listdir [Lista todos os diretórios e arquivos]
 |------> /listdir -files [Lista todos os arquivos no diretório principal]

/search <term> [Busca documentos apartir de uma palavra]

/aq

/tes
    ''')

path = os.getcwd()
dirList = os.listdir(path) 

if len (sys.argv) == 2:
    if command == '/listdir':
        print("Arquivos e diretórios em '", path, "' :")  
        print(dirList) 
    elif command == '/search':
        print('Digite um termo para efetuar a busca pelos documentos')    
elif len (sys.argv) == 3: 
    if command == '/listdir' and command2 == '-files':
        print(f'Os arquivos de texto presentes no diretório {path}:')
        for i in dirList:
            if i.endswith(".txt") == True:
                print(i)
# for x in sys.argv:
#      print ("Argument:", x) 