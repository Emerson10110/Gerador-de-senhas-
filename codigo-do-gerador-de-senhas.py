# importação das bibliotecas

import secrets
import random

# sorteamento  das letras

letras = 'adDeEfFgGhHiIjJkKlLMmNnoOPpQqRrSsTtUuvVWwxXyYZzZ'
letra_sorteada = random.sample(letras, 6)
resultado = ''.join(letra_sorteada)

# sorteamento dos numeros 

numeros = '1234567890'
numeros_sorteado = random.sample(numeros, 4)
resultadonumero = ''.join(numeros_sorteado)

# sorteamento dos caracteres

caracteres = '!@#$%^&*?~'
caracteres_sorteado = random.sample(caracteres, 4)
resultado_caracteres = ''.join(caracteres_sorteado)
print(resultado + resultadonumero + resultado_caracteres)





