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
    dirs = []
    for diretorio, arquivos in os.walk(path):
        for arquivo in arquivos:
            if arquivo.endswith('.txt') == True: 
                # print(os.path.join(diretorio, arquivo))
                dirs.append(os.path.join(os.path.realpath(diretorio), arquivo))
    return dirs

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


pasta = input('digita o dir: ')
#lista de diretórios
dirs = percorrerArquivos(pasta)
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
