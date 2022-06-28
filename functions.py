import os
import sys


def showHelp(command):
    if command == '/help':
        print('''A lista de comandos é:

    /listdir [Lista todos os diretórios e arquivos no diretório principal]
        |------> /listdir -files [Lista todos os arquivos no diretório principal]

    /addindex  [Adiciona o diretório principal]
        |------> /addindex <index> [Adiciona o índice indicado]

    /removeindex <index> [Remove o índice indicado]

    /search <term> [Busca a ocorrência]

    /viewindex <path> [Visualiza o índice adicionado]

    /updateindex <path>
        ''')

def percorrerArquivos(path):
    indexdirs = []
    filesdirs= []
    for dirs in os.walk(path):
        '''RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR '''
        if dirs[0].startswith('C:\\Users\\Keven\\Desktop\\FOOCUS P\\pbl - mi 3\\.git'):    
             pass
        else:
            indexdirs.append(dirs[0])       
    for diretorio, subpastas, arquivos in os.walk(path):
        for arquivo in arquivos:
            if arquivo.endswith('.txt') == True:
                filesdirs.append(os.path.join(diretorio, arquivo))
    return filesdirs

def indexinvertido(termo,dictdir):
    dicio = {}
    dicio[termo] = {}
    diretoriosencontrados = []
    for diretorio in dictdir:
        counter = 0
        #contador de vezes que a palavra ocorre
        with open(diretorio, 'r', encoding="utf8") as arquivo:
            for linha in arquivo:
                linhalower = linha.lower()
                if termo in linhalower:
                    counter += linhalower.count(termo)
                    diretoriosencontrados.append(diretorio)
                    dicio[termo].update({diretorio: counter})
    return dicio

def listDir(path):
    path = os.listdir()
    print(path)

def visualizarIndex(diretorio,stopwords):
    viewindexdicio = {}
    for fileindex in diretorio:
        if os.path.isfile(fileindex) == True:
            with open(fileindex, 'r', encoding='utf-8') as diret:
                dicio = {}
                for linha in diret:
                    linha = linha.rstrip()
                    linha = linha.lower()
                    palavras = linha.split(" ")
                    for palavra in palavras:
                        word = palavra.strip(",.\\:?!'~];/*$#@\"()[1234567890")
                        if word not in stopwords:
                            if word in dicio:
                                dicio[word] += 1
                            else:
                                dicio[word] = 1             
        viewindexdicio[fileindex] = dicio
    return viewindexdicio    

def generateStopWordsList():
    stopwordslist = []
    with open('stopwords.ignore', 'r') as stopwords:
        for linha in stopwords:
            word = linha.rstrip()
            stopwordslist.append(word)
    return stopwordslist

def getOldIndexUpdate():
    with open('cache.ignore', 'r') as cache:
        directorydict = []
        newindexlist = []
        for line in cache:
        #rstrip retira caracteres de controle
            caminho = line.rstrip()
            directorydict.append(caminho)
        for index in directorydict:
            updatetime = os.path.getmtime(index)
            newindexlist.append(str(updatetime))
        return directorydict, newindexlist

def rewriteIndexUpdate(directorydict, newindexlist):        
    with open('indexupdate.ignore', 'r+') as indexupdate:
        oldindexes = indexupdate.readlines()
        for i in range(len(newindexlist)):
            oldindex = oldindexes[i].rstrip()
            if newindexlist[i] != oldindex:
                indexupdate.write(str(newindexlist[i]))
                indexupdate.write('\n')
                print(f'O índice: {directorydict[i]} sofreu alterações, portanto foi atualizado.')
            else:
                indexupdate.write(oldindex)       
                indexupdate.write('\n')
    print('Índices atualizados!')