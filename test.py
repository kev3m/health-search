from importlib.metadata import files
import os

# arquivo = os.path.realpath('C:\Users\Keven\Desktop\FOOCUS P\pbl - mi 3\moretrash\Arquivo 5.txt')
# arquivo = os.path.relpath('moretrash\Arquivo 5.txt')
# # filename = os.path.basename(arquivo)

# def visualizarIndex(diretorio):
#     if os.path.isfile(diretorio) == True:
#         dicio = {}
#         with open(diretorio, 'r', encoding='utf8') as diretorio:
#             for linha in diretorio:
#                 linha = linha.strip()
#                 linha = linha.lower()
#                 palavras = linha.split(" ")
#                 print(palavras)
#                 for word in palavras:
#                     if word in dicio:
#                         dicio[word] += 1
#                     else:
#                         dicio[word] = 1
#         return dicio

# print(visualizarIndex(arquivo))
# def percorrerArquivos(path):
#     dirs = []
#     for diretorio, arquivos in os.walk(path):
#         for arquivo in arquivos:
#             if arquivo.endswith('.txt') == True: 
#                 # print(os.path.join(diretorio, arquivo))
#                 dirs.append(os.path.join(os.path.realpath(diretorio), arquivo))
#     return dirs

# command2 = 'C:\Users\Keven\Desktop\FOOCUS P\pbl - mi 3\protocols'
# dicio = percorrerArquivos(command2)

# with open('cache.ignore', 'w') as cache:
#     if os.path.isfile(command2) == True:
#         cache.write(command2)
#         print(f'O indíce de arquivo {command2} foi adicionado')
#     else: 
#         dicio = percorrerArquivos(command2)
#         print(f'O indíce de diretório {command2} foi adicionado')
#         for index in dicio:
#             cache.write(index)
#             cache.write('\n')

# def percorrerArquivos(path):
#     indexdirs = []
#     filesdirs= []
#     if os.path.isfile(path) == True:
#         filesdirs.append(path)
#     else:
#         for dirs in os.walk(path):
#             '''RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR RETIRAR '''
#             if dirs[0].startswith('C:\\Users\\Keven\\Desktop\\FOOCUS P\\pbl - mi 3\\.git'):    
#                 pass
#             else:
#                 print(dirs[0])
#                 indexdirs.append(dirs[0])
#         for index in indexdirs:         
#             for diretorio, subpastas, arquivos in os.walk(index):
#                 for arquivo in arquivos:
#                     if arquivo.endswith('.txt') == True:
#                         print(os.path.join(diretorio, arquivo))
#                         filesdirs.append(os.path.join(diretorio, arquivo))
#     return filesdirs

# path = 'C:\\Users\Keven\Desktop\FOOCUS P\pbl - mi 3\moretrash\Arquivo 2.txt'
# print(percorrerArquivos(path))
# # print(filesdirs)

# dicio = {}
# for chave in dicio.keys():
#     print(f'Visualizando o índice: {chave}')
#     for j in sorted(dicio[chave].items(), key=lambda dicio: dicio[1], reverse=True):
#         print(f'Palavra: {j[0]} | Ocorrências: {j[1]}')
#     print('\n')
# import time 
# path = r"C:\\Users\Keven\Desktop\arquivos\test.txt"
# ti_c = str(os.path.getctime(path))
# ti_m = os.path.getmtime(path) 
# # c_ti = time.ctime(ti_c) 
# # m_ti = time.ctime(ti_m) 
# print(ti_c, ti_m)
  
# print( 
#     f'''The file located at the path {path} 
#     was created at {c_ti} and was last modified at {m_ti}''') 
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