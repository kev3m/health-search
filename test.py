dicio = {}

dicio['item'] = {'lula': '3'}
dicio['item'].update({'bolso': '5'}) 
dicio['item'].update({'alckmin': '1'}) 
dicio['item'].update({'marina': '4'}) 
for i in dicio:
    print(i)
    for j in sorted(dicio[i].items(), key=lambda item: item[1], reverse=True):
        print(f'Arquivo:{j[0]} | Ocorrências {j[1]}')
