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

def BinaryToDecimal(binary):  
    string = int(binary, 2)      
    return string 

st = "P"
binary_converted = ''.join(format(c, 'b') for c in bytearray(st, "utf-8"))
         
print("The binary value is:", binary_converted) 
   
str_data =''
   
for i in range(0, len(binary_converted), 7):   
    temp_data = binary_converted[i:i + 7] 
    decimal_data = BinaryToDecimal(temp_data)
    str_data = str_data + chr(decimal_data)

print("The Binary value after string conversion is:", str_data) 
print(len(binary_converted))

