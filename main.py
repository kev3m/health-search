import os
import sys

if len (sys.argv) < 2 :
    print (''' 
Para verificar a lista de comandos digite /help''')
    sys.exit()

command = sys.argv[1]
if command == 'zap':
    print('meu deus meu senhor me ajuda')
    
if command == '/help':
    print('''A lista de comandos é:
/teste
/alo
/aq
/tes
    ''')
    

# for x in sys.argv:
#      print ("Argument:", x) 