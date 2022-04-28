def converterEmHamming(binario): #Retorna uma string binaria convertida com o algoritmo de hamming (input: string binaria)
    print("Binário informado:", binario)
    qtdBits = len(binario)

    if (qtdBits % 11 != 0): #transforma o código número em múltiplo de 11
        x = 0                                                                                   
        while True: #coleta o primeiro multiplo de 11 acima da do tamanho do binário        
            if (x > qtdBits):                                                               
                break                                                                       
            x += 11                                                                         
        zeros = x - qtdBits                                                                                                                                                         
        x = 0                                                                               
        saida = ""                                                                          
        while True: #adiciona os 0 para que o binário se torne multiplo de 11               
            if (x == zeros):                                                                
                break                                                                       
            saida = "0" + saida                                                             
            x += 1
        binario = saida + binario

    inicio = 0
    fim = 11
    conjuntos = []
    while True: 
        if (fim > len(binario)):
            break
        divisao = binario[inicio : fim]
        matriz = "xxx" + divisao[0] + "x" + divisao[1:4] + "x" + divisao[4:11]
        conjuntos.append(matriz)
        inicio = fim
        fim += 11

    def criarQ1(binario): #verifica o bit necessário para as colunas 2 e 4
        y = 1
        um = 0
        while (y < 16):
            if (binario[y] != "x"):  
                if (binario[y] == "1"):
                    um += 1
            y += 2
        if (um % 2 == 1):
            return 1
        else:
            return 0

    def criarQ2(binario): #verifica o bit necessário para as colunas 3 e 4
        y = 2
        um = 0
        while (y < 16): 
            if (binario[y] != "x"):  
                if (binario[y] == "1"):
                    um += 1
            if (y % 2 == 0):
                y += 1
            else:
                y += 3
        if (um % 2 == 1):
            return 1
        else:
            return 0

    def criarQ3(binario): #verifica o bit necessário para as linhas 2 e 4
        y = 4
        um = 0
        while (y < 16):
            if (binario[y] != "x"):  
                if (binario[y] == "1"):
                    um += 1
            if (y == 7):
                y = 12
            else:
                y += 1
        if (um % 2 == 1):
            return 1
        else:
            return 0

    def criarQ4(binario): #verifica o bit necessário para as linhas 3 e 4
        y = 8
        um = 0
        while (y < 16):
            if (binario[y] != "x"):
                if (binario[y] == "1"):
                    um += 1
            y += 1
        if (um % 2 == 1):
            return 1
        else:
            return 0

    def criarQ0(binario): #verifica o bit necessário para todas as linhas
        y = 1
        um = 0
        while (y < 16): 
            if (binario[y] == "1"):
                um += 1
            y += 1
        if (um % 2 == 1):
            return 1
        else:
            return 0

    x = 0 
    for saida in conjuntos:    
        lista = list(saida)
        lista[1] = str(criarQ1(saida))
        lista[2] = str(criarQ2(saida))
        lista[4] = str(criarQ3(saida))
        lista[8] = str(criarQ4(saida))
        lista[0] = str(criarQ0("".join(lista)))
        saida = "".join(lista)
        conjuntos[x] = saida
        x += 1

    return (conjuntos)

def verificaHamming(valoresConvertidos):
    binarios = valoresConvertidos

    def verificaQ1(binario):
        x = 1
        um = 0
        while x < 16:
            if (binario[x] == "1"):
                um += 1
            x += 2
        if (um % 2 == 0):
            return 0
        else:
            return 1

    def verificaQ2(binario):
        x = 2
        um = 0
        while x < 16:
            if (binario[x] == "1"):
                um += 1
            if (x % 2 == 1):
                x += 3
            else:
                x+= 1
        if (x % 2 == 1):
            return 1
        else:
            return 0

    def verificaQ3(binario):
        x = 4
        um = 0
        while x < 16:
            if (binario[x] == "1"):
                um += 1
            if (x == 7):
                x = 12
            else: 
                x += 1
        if (x % 2 == 1):
            return 1
        else:
            return 0

    def verificaQ4(binario):
        x = 8
        um = 0
        while x < 16:
            if (binario[x] == "1"):
                um += 1
            x+= 1
        if (x % 2 == 1):
            return 1
        else:
            return 0

    verificacao = ""
    for binario in binarios:
        verificacao = ""
        verificacao += str(verificaQ4(binario))
        verificacao += str(verificaQ3(binario))
        verificacao += str(verificaQ2(binario))
        verificacao += str(verificaQ1(binario))
        if (verificacao != "0000"):
            total = 0
            i = 0
            while (i < 4):
                total += int(verificacao[i]) * (2 ** (4 - i -1))
                i += 1
            if (binario[0] == "0"):
                print("Mais de um erro entre as posições", ((binarios.index(binario) + 1) * 16), " e ", ((binarios.index(binario) + 1) * 16) + 16)
            else:
                print("Erro na posição", total * ((binarios.index(binario) + 1) * 16))

valoresConvertidos = converterEmHamming("010011100110000101110100011101000110000101101110")
comHamming = ""
for valor in valoresConvertidos:
    comHamming += valor
print("Binário com Hamming aplicado:",comHamming)
print()

for valor in valoresConvertidos:
    print(valor)

maximo = len(valoresConvertidos) -1

while True:
    bloco = input("Informe o bloco que deseja alterar (0 a %.0d): " % maximo)

    if (bloco == ""):
        break

    bloco = int(bloco)

verificaHamming(valoresConvertidos)