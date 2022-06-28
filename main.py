import os
import sys
from functions import percorrerArquivos, indexinvertido, listDir, visualizarIndex


if len (sys.argv) < 2 :
    print (''' 
Para verificar a lista de comandos digite <nomedoarquivo> /help''')
    sys.exit()
elif len (sys.argv) == 3:
    command2 = sys.argv[2]


command = sys.argv[1]


if command == '/help':
    print('''A lista de comandos é:

/listdir [Lista todos os diretórios e arquivos no diretório principal]
 |------> /listdir -files [Lista todos os arquivos no diretório principal]

/addindex  [Adiciona o diretório principal]
 |------> /addindex <index> [Adiciona o índice indicado]

/removeindex <index> [Remove o índice indicado]

/search <term> [Busca a ocorrência]

/viewindex <path>

/updateindex <path>
    ''')

path = os.getcwd()
dirList = os.listdir(path) 

stopwordslist = []
with open('stopwords.ignore', 'r') as stopwords:
    for linha in stopwords:
     word = linha.rstrip()
     stopwordslist.append(word)

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
        with open('cache.ignore', 'r') as cache:
            directorydict = []
            newindexlist = []
            for line in cache:
                #rstrip retira caracteres de controle
                caminho = line.rstrip()
                directorydict.append(caminho)
            for index in directorydict:
                updatetime = os.path.getmtime(index)
                newindexlist.append(updatetime)
            with open('indexupdate.ignore', 'r+') as indexupdate:
                oldindexes = indexupdate.readlines()
                for i in range(len(newindexlist)):
                    oldindex = oldindexes[i].rstrip()
                    if newindexlist[i] != oldindex:
                        indexupdate.write(str(newindexlist[i]))
                        print(f'O índice {directorydict[i]} sofreu alterações, portanto foi atualizado.')
                    else:
                        indexupdate.write(oldindex)
            print('Índices atualizados!')
elif len (sys.argv) == 3: 
    if command == '/listdir' and command2 == '-files':
        print(f'Os arquivos de texto presentes no diretório {path}:')
        for i in dirList:
            if i.endswith(".txt") == True:
                print(i)
    elif command == '/addindex' and command2 != None:
        with open('cache.ignore', 'w') as cache, open('indexupdate.ignore', 'w') as indexupdate:
            if os.path.isfile(command2) == True:
                cache.write(command2)
                print(f'O indíce de arquivo {command2} foi adicionado!')
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
        except:
            print('Houve um erro! Não foi possivel localizar e remover o índice')        




        #verificar se é um caminho válido

         
        

