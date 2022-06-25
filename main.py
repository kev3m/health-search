import os
import sys
# from testinvert import percorrerArquivos

def percorrerArquivos(path):
    indexdirs = []
    filesdirs= []
    for dirs in os.walk(path):
        '''RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR '''
        if dirs[0].startswith('C:\\Users\\Keven\\Desktop\\FOOCUS P\\pbl - mi 3\\.git'):    
             pass
        else:
            print(dirs[0])
            indexdirs.append(dirs[0])
    for index in indexdirs:         
        for diretorio, subpastas, arquivos in os.walk(index):
            for arquivo in arquivos:
                if arquivo.endswith('.txt') == True:
                    print(os.path.join(diretorio, arquivo))
                    filesdirs.append(os.path.join(diretorio, arquivo))
    return filesdirs

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

/viewindex <path>
    ''')

path = os.getcwd()
dirList = os.listdir(path) 

if len (sys.argv) == 2:
    if command == '/listdir':
        print("Arquivos e diretórios em '", path, "' :")  
        print(dirList) 
    elif command == '/addindex':
        path = os.getcwd()
        print(path)
        with open('cache.ignore', 'w') as cache:
            cache.write(path)
        print('O diretório principal foi adicionado.')
    elif command == '/search':
        print('Efetue a busca utilizando /search <termo>')    
elif len (sys.argv) == 3: 
    if command == '/listdir' and command2 == '-files':
        print(f'Os arquivos de texto presentes no diretório {path}:')
        for i in dirList:
            if i.endswith(".txt") == True:
                print(i)
    elif command == '/addindex' and command2 != None:
        with open('cache.ignore', 'w') as cache:
            if os.path.isfile(command2) == True:
                cache.write(command2)
                print(f'O indíce de arquivo {command2} foi adicionado')
            else: 
                dicio = percorrerArquivos(command2)
                print(f'O indíce de diretório {command2} foi adicionado')
                for index in dicio:
                    cache.write(index)
                    cache.write('\n')

        #verificar se é um caminho válido

         
        

