from functools import reduce

def hamming_syndrome(bits):
    return reduce(
    lambda x, y: x ^ y,
    [i for (i, b) in enumerate(bits) if b]
    )

def converter(arquivo):
    with open(arquivo,'rb') as file:
        string = file.read()
        hex = bytes.hex(string)
        binario = bin(int(hex,base=16))
        binarioCorreto = binario[0] + binario[2:]
        return binarioCorreto

x = 1
um = 0
zero = 0
binario = converter("bla")
print(binario)
while True:
    if (x == len(binario)):
        break
    if (binario[x] == "1"):
        um += 1
    else:
        zero += 1
    x += 1

teste = 0
if (um > zero):
    teste = 1

verificacao = False
if (int(binario[0]) == teste):
    verificacao = True

ls = []
for i in binario:
    ls.append(i)

erroLocalizado = hamming_syndrome(ls)

if (erroLocalizado == 0 and verificacao == False):
    print("Tem mais de um erro")
elif(erroLocalizado == 0 and verificacao == True):
    print("Tudo correto")
else:
    print("Erro na posição:", erroLocalizado)