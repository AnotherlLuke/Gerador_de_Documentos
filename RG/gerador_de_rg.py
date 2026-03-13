# Gerador de RGs SP

import os
import time
import random

def limpar_tela():
    os.system('cls') if os.name == 'nt' else 'clear'

# Gerar RG
def gerar_rg():
    base_rg = ''
    for _ in range(8):
        base_rg += str(random.randint(0, 9))
    rg_gerado = concatenar_rg(base_rg)
    print(f'RG Gerado: {rg_gerado[0:2]}.{rg_gerado[2:5]}.{rg_gerado[5:8]}-{rg_gerado[-1]}')

    return rg_gerado

def concatenar_rg(base_rg):
    resultado = 0
    ordem = 2
    for _ in base_rg:
        multiplicar = int(_) * ordem
        resultado += multiplicar
        ordem += 1

    digito = 11 - (resultado % 11)
    digito = digito if digito <= 9 else 0           

    rg = base_rg + str(digito)

    return rg

# Validar RG
def validar_rg():
    while True:
        rg_validar = input('Digite o RG para validá-lo: ').replace('.','').replace('-','').upper()
        if rg_validar == 'S':
            break
        try:
            int(rg_validar)
            if len(rg_validar) != 9:
                print('Seu RG deve conter 9 digítos. | Ex: 11.222.333-4')
                time.sleep(1)
                limpar_tela()
                continue
            rg_validado = concatenar_rg(rg_validar[0:8])
            if rg_validar == rg_validado:
                print('RG Válido.')
                break
            else:
                print('RG Inválido.')
                break
        except ValueError:
            print('O RG não pode conter letras, sendo composto de números.')

# Execução:
print('Opcões Disponíveis: [G]Gerar RG | [V]Validar RG |[R]Rever Opções | [S]Sair do progama.')
opcoes_validas = 'G', 'V', 'R', 'S'
while True:
    opcao = input('Digite a opção Desejada: ').upper()

    if opcao in opcoes_validas:
        if opcao == 'G':
            limpar_tela()
            rg_gerado = gerar_rg()

        if opcao == 'V':
            validar_rg()

        if opcao == 'R':
            limpar_tela()
            print('Opcões Disponíveis: [G]Gerar CPF | [M]Gerar Múltiplos CPFs | [V]Validar CPF | [R]Rever Opções | [S]Sair do progama.')

        if opcao == 'S':
            limpar_tela()
            print('Interrompendo o progama.')
            break
    else:
        print('Escolha uma das opções listadas.')


# Num geral a lógica é a mesma do Gerador de CPFs com algumas diferenças.

