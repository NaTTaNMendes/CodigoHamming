import os
from pathlib import Path

'''caminho = input('Primeiro txt: ')
arquivo = open(caminho, 'r').read()

caminho = input('Segundo txt: ')
arquivo2 = open(caminho, 'r').read()

if (arquivo == arquivo2):
    print('igual')
else:
    print('diferente')'''

#os.remove('imagem2.png')

def binarioParaInt(lista):

    # inicialize potência com o 2**8 utilizando operações bit a bit
    pot = (1<<7)
    # criar uma acumulador chamado palavra, afinal um grupo de bytes é uma
    # palavra
    word = 0
    # para cada bit da lista l
    for b in lista:
        b = int(b)
        # guarde o valor do bit vezes a sua potência
        word += b * pot
        # reduza a potência pela divisão por dois usando bit a bit
        pot = pot >> 1
    return word

caminho = 'video.mkv'

st = caminho
binary_converted = ''.join(format(c, 'b').zfill(8) for c in bytearray(st, "utf-8"))
str_data =''
   
for i in range(0, len(binary_converted), 8):   
    temp_data = binary_converted[i:i + 8] 
    decimal_data = binarioParaInt(temp_data)
    str_data = str_data + chr(decimal_data)

print(str_data)
print(binary_converted)

