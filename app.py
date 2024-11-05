"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import random
gerador_cpf = ''
for i in range(9):
    gerador_cpf += str(random.randint(0, 9))
    
# variavel cpf
cpf = '746.824.890-70'

# tranformar o cpf num inteiro sem caractere especial
cpf_numeros = cpf.replace(".", "").replace("-", "")
cpf_enviado_cliente = int(cpf_numeros)

'''Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10'''

soma_1 = 0
for i in range(9):
    digito = int(cpf_numeros[i])
    multiplicador = 10 - i
    soma_1 += digito * multiplicador * 10

'''Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7'''

resto_divisao_1 = soma_1 % 11

'''Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7'''

if resto_divisao_1> 9:
    print('resultado é 0')

else:
    ...

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
soma_2 = 0

for i in range(10):
    digito = int(cpf_numeros[i])
    multiplicador = 11 - i
    soma_2 += digito * multiplicador * 10
    
'''Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0'''
resto_divisao_2 = soma_2 % 11

'''Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0'''

if resto_divisao_2 > 9:
    print('o resultado é 0')
else:
    ...

# contagem dos 9 primeiros digitos
for nove_digitos in cpf_numeros:
    nove_digitos = cpf_numeros[0:9]

# calculando cpf

cpf_gerado_pelo_calculo = f'{nove_digitos}{resto_divisao_1}{resto_divisao_2}'

# validando cpf

if cpf_gerado_pelo_calculo == cpf_numeros:
    print(f'o CPF:{cpf_enviado_cliente} é valido')
else:
    print('CPF invalido')

          