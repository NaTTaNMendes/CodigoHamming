import os
import random
from turtle import st

tamanhoRajada = 2
contadorRajada = 0

corrompeu = False

with open('corrompido.bin', 'wb') as corrompido:
    with open('arquivo.bin', 'rb') as normal:
        while True:
            dados = normal.read(1)
            if str(dados) == "b''":
                break

            if not corrompeu and random.choice([True, False]):
                corrompeu = True
                print("Ta feito chefe :sunglasses:")
            
            if corrompeu and contadorRajada < tamanhoRajada:
                contadorRajada += 1
                dados = int('11111111', base=2).to_bytes(1, 'little')

            corrompido.write(dados)