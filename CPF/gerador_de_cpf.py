from funcoes_cpf import limpar_tela, gerar_cpf, validar_cpf 

# Execução:
print('Opcões Disponíveis: [G]Gerar CPF | [M]Gerar Múltiplos CPFs | [V]Validar CPF |[R]Rever Opções | [S]Sair do progama.')
opcoes_validas = 'G', 'M', 'V', 'S', 'R'
lista_cpfs = None 

while True:
    opcao = input('Digite a opção Desejada: ').upper()

    if opcao in opcoes_validas:
        if opcao == 'G':
            limpar_tela()
            cpf_gerado = gerar_cpf()
            print(f'CPF Gerado:', cpf_gerado)

        if opcao == 'M':
            limpar_tela()
            multiplos = input('Digite quantos CPFs você precisa: ')
            print('CPFs Gerados: ')
            try:
                lista_cpfs = []
                for _ in range(int(multiplos)):
                    multiplos_cpfs = gerar_cpf()
                    lista_cpfs.append(multiplos_cpfs)
                    print(multiplos_cpfs)
            except ValueError:
                print('Essa operação só pode ser realizada com números.')

        if opcao == 'V':
            validar_cpf()

        if opcao == 'R':
            limpar_tela()
            print('Opcões Disponíveis: [G]Gerar CPF | [M]Gerar Múltiplos CPFs | [V]Validar CPF | [R]Rever Opções | [S]Sair do progama.')

        if opcao == 'S':
            limpar_tela()
            print('Interrompendo o progama.')
            break
    else:
        print('Escolha uma das opções listadas.')


# Pro caso de precissar dos CPFs eles são armazenados em lista automaticamente
# Exemplo

# if lista_cpfs is not None:
#     for i, _ in enumerate(lista_cpfs):
#         print(f'{i}.', _)
# else:
#     print('Lista Vazia.')