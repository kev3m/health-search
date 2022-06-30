import os
import sys
from functions import showHelp,percorrerArquivos, indexinvertido, visualizarIndex, generateStopWordsList, getOldIndexUpdate, rewriteIndexUpdate

if len (sys.argv) < 2 :
    print (''' 
Para verificar a lista de comandos digite <nomedoarquivo> /help''')
    sys.exit()
elif len (sys.argv) == 3:
    command2 = sys.argv[2]

command = sys.argv[1]

showHelp(command)

path = os.getcwd()
dirList = os.listdir(path) 

stopwordslist = generateStopWordsList()

if len (sys.argv) == 2:
    if command == '/listdir':
        print("Arquivos e diretórios em '", path, "' :")  
        print(dirList) 
    elif command == '/addindex':
        print('Adicione o index utilizando /addindex <path>')
    elif command == '/search':
        print('Efetue a busca utilizando /search <termo>')
    elif command == '/removeindex':
         print('Efetue a remocão do índice utilizando /removeindex <path')
    elif command == '/viewindex':
        with open('cache.ignore', 'r') as cache:
            directorydict = []
            for line in cache:
                #rstrip retira caracteres de controle
                caminho = line.rstrip()
                directorydict.append(caminho)
        viewindex = visualizarIndex(directorydict,stopwordslist)
        for chave in viewindex.keys():
            print(f'Visualizando o índice: {chave}')
            for j in sorted(viewindex[chave].items(), key=lambda dicio: dicio[1], reverse=True):
                print(f'Palavra: {j[0]} | Ocorrências: {j[1]}')
            print('\n')
    elif command == '/updateindex':
        directorylist, modificationsTimeList = getOldIndexUpdate()
        rewriteIndexUpdate(directorylist, modificationsTimeList)
elif len (sys.argv) == 3: 
    if command == '/listdir' and command2 == '-files':
        print(f'Os arquivos de texto presentes no diretório {path}:')
        for i in dirList:
            if i.endswith(".txt") == True:
                print(i)
    elif command == '/addindex' and command2 != None:
        with open('cache.ignore', 'w') as cache, open('indexupdate.ignore', 'r+') as indexupdate:
            if os.path.isfile(command2) == True:
                cache.write(command2)
                print(f'O indíce de arquivo {command2} foi adicionado!')
                indexupdate.write(str(os.path.getmtime(command2)))
            else: 
                dicio = percorrerArquivos(command2)
                print(f'O indíce de diretório {command2} foi adicionado!')
                for index in dicio:
                    cache.write(index)
                    cache.write('\n')
                    indexupdate.write(str(os.path.getmtime(index)))
                    indexupdate.write('\n')
    elif command == '/search' and command2 != None:
        with open('cache.ignore', 'r') as cache:
            directorydict = []
            for line in cache:
                #rstrip retira caracteres de controle
                caminho = line.rstrip()
                directorydict.append(caminho)
            dicion = indexinvertido(command2, directorydict)
            for i in dicion:
                print(f'Termo buscado: {i}')
                print(f'Quantidade de arquivos encontrados: {len(dicion[command2])}')
                #sorted(iterable, key=key(parametro de comparação), reverse=reverse)
                #lambda = função anônima 
                for j in sorted(dicion[i].items(), key=lambda dicio: dicio[1], reverse=True):
                    print(f'Caminho do arquivo: {j[0]} | Ocorrências: {j[1]}')
    elif command == '/removeindex' and command2 != None:
        try:
            with open('cache.ignore', 'r') as cacheread:
                cacheindexes = cacheread.readlines()
            with open('cache.ignore', 'w') as cache:    
                for linha in cacheindexes:     
                    if linha.startswith(command2) == True:
                        removedaux = True
                    else:
                        cache.write(linha)
            if removedaux == True:
                print(f'O índice {command2} foi removido com sucesso!')
                directorylist, modificationsTimeList = getOldIndexUpdate()
                with open('indexupdate.ignore', 'w+') as indexupdate:
                    indexupdate.write("\n".join(modificationsTimeList))
        except:
            print('Houve um erro! Não foi possivel localizar e remover o índice')        
        #verificar se é um caminho válido

         
        

