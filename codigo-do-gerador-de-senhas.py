# importação das bibliotecas

import secrets
import random

# sorteamento  das letras

letras = 'adDeEfFgGhHiIjJkKlLMmNnoOPpQqRrSsTtUuvVWwxXyYZzZ'
letra_sorteada = random.sample(letras, 7)
resultado = ''.join(letra_sorteada)

# sorteamento dos numeros 

numeros = '1234567890'
numeros_sorteado = random.sample(numeros, 6 )
resultadonumero = ''.join(numeros_sorteado)

# sorteamento dos caracteres

caracteres = '!@#$%^&*?~'
caracteres_sorteado = random.sample(caracteres, 5)
resultado_caracteres = ''.join(caracteres_sorteado)

#Criando a variavel senha

senha = resultado + resultadonumero + resultado_caracteres
print(senha)


