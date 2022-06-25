import os
import sys

'''indicando um diretório ou um arquivo específico. O
sistema também deve efetuar a busca de documentos
a partir de uma palavra (termo), indicando todos os
documentos que contêm aquela palavra e quantas
vezes a palavra ocorre no documento, além de
informar a quantidade de documentos encontrados.
'''
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

def indexinvertido(termo,diretorio):
    dicio = {}
    dicio[termo] = {}
    diretoriosencontrados = []
    for diretorio in dirs:
        counter = 0
        #contador de vezes que a palavra ocorre
        with open(diretorio, 'r', encoding="utf8") as arquivo:
            for linha in arquivo:
                linhalower = linha.lower()
                if termo in linhalower:
                    counter += linhalower.count(termo)
                    diretoriosencontrados.append(diretorio)
                    basename = os.path.basename(diretorio)
                    dicio[termo].update({basename: counter})
    return dicio

def visualizarIndex(diretorio):
    if os.path.isfile(diretorio) == True:
        dicio = {}
        for linha in diretorio:
            # linha = linha.strip()
            linha = linha.lower()
            palavras = linha.split(" ")
            for word in palavras:
                if word in dicio:
                    dicio[word] += 1
                else:
                    dicio[word] = 1
        return dicio


pasta = input('digita o dir: ')
#lista de diretórios
dirs = percorrerArquivos(pasta)
viewindex = visualizarIndex(pasta)
print(viewindex)
print(dirs)
# dicio = {'termo': {'filename.txt': 'quantpalavras'  } }

# for x in dirs:
#     print(x)

termo = input('digite o termo a ser buscado:').lower()
dicion = indexinvertido(termo, dirs)
for i in dicion:
    print(f'Termo buscado: {i}')
    #sorted(iterable, key=key(parametro de comparação), reverse=reverse)
    #lambda = função anônima 
    for j in sorted(dicion[i].items(), key=lambda dicio: dicio[1], reverse=True):
        print(f'Filename: {j[0]} | Ocorrências: {j[1]}')
