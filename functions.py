import os

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
                        word = palavra.strip(",.:?!'~;/*$#@\"")
                        if word not in stopwords:
                            if word in dicio:
                                dicio[word] += 1
                            else:
                                dicio[word] = 1             
        viewindexdicio[fileindex] = dicio
    return viewindexdicio    