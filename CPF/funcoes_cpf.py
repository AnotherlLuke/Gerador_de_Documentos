import random
import time
import os

def limpar_tela():
    os.system('cls') if os.name == 'nt' else 'clear'

def gerar_cpf():
    nove_digitos = ''
    for _ in range(9):
        nove_digitos += str(random.randint(0, 9))
    cpf_gerado = concatenar_cpf(nove_digitos)
    return cpf_gerado
            
# Cálculo para gerar digitos verificadores
def concatenar_cpf(nove_digitos):
    contador = 10
    for _ in range(2):
        resultado = 0
        for n in nove_digitos:
            multiplicar = int(n) * contador
            resultado = resultado + multiplicar
            contador -= 1
        digito = 11 - (resultado % 11)
        digito = digito if digito <= 9 else 0

        nove_digitos = nove_digitos + str(digito)
        contador = 11 # Reiniciando o loop, contabilizando digito 2

    cpf = f'{nove_digitos[0:3]}.{nove_digitos[3:6]}.{nove_digitos[6:9]}-{nove_digitos[9:11]}'
    return cpf

def validar_cpf():
    while True:
        cpf_validar = input('Digite o CPF para válida-lo: ').replace('.','').replace('-','').upper()
        try:
            if cpf_validar == 'S':
                break
            int(cpf_validar) # Checar try
            if len(cpf_validar) != 11:
                print('Seu CPF deve conter 11 números. Ex: 111.222.333-00')
                time.sleep(1)
                continue
            cpf_validado = concatenar_cpf(cpf_validar[0:9])
            if cpf_validar == cpf_validado.replace('.','').replace('-',''):
                print('CPF Válido.')
                break
            else:
                print('CPF Inválido.')
                break
        except ValueError:
            print('Seu CPF não pode ser composto de letras!')
