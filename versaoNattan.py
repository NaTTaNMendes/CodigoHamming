binario = "01100010"
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
    print(matriz)
    conjuntos.append(matriz)
    inicio = fim
    fim += 11
'''

FALTA OTIMIZAR ESSA PARTE DO CODIGO E COLOCAR DENTRO DE UM WHILE

y = 0
parq11 = 0
imparq11 = 0
parq12 = 0
imparq12 = 0
while (y < 16):
    if (matriz[y] != "x"):
        if (y % 2 == 0):   
            if (int(matriz[y]) % 2 == 0):
                parq11 += 1
            else:
                imparq11 += 1
        else:
            if (int(matriz[y]) % 2 == 0):
                parq12 += 1
            else:
                imparq12 += 1 
    y += 1
if (parq11 > imparq11):
    matriz [2] = 0
else:
    matriz [2] = 1
if (parq12 > imparq12):
    matriz [1] = 0
else:
    matriz[1] = 1
'''