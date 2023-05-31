# inicio da variavel global
lista_pecas = []

codigo_produto = 0


# fim da variavel global

# Início da Funçao de cadastro


def cadastrar_peca():
    global codigo_produto
    while True:
        try:
            codigo_produto += 1
            print("-------------CADASTRAR PEÇA-------------")
            print(f"Código do produto:{codigo_produto}")
            nome_peca = input('DIGITE O NOME DA PEÇA: ')
            fabricante_peca = input("DIGITE O NOME DO FABRICANTE: ")
            valor_peca = float(input("PREÇO: (R$) "))
            dicionario_peca = {
                'codigo': codigo_produto,
                'nome': nome_peca,
                'fabricante': fabricante_peca,
                'preco': valor_peca}
            lista_pecas.append(dicionario_peca.copy())
            print("PEÇA CADASTRADA COM SUCESSO!\n")
            op = input("Deseja realizar outro cadastro?(S/N)").upper()
            if op == 'S':
                return cadastrar_peca()
            elif op == 'N':
                print("Voltando ao Menu Principal")
                return main()
            else:
                print("Opção inválida")
                continue

        except ValueError:
            print("Por favor digite uma valor válido!!")
            continue


# fim da função de cadastro


# Inicio da funçao de consultar peças
def consulta_peca():
    while True:
        print("CONSULTAR PEÇAS")
        try:
            opcao = int(input("[1] - CONSULTAR TODAS AS PEÇAS\n"
                              "[2] - CONSuLTAR PEÇAS POR CÓDIGO\n"
                              "[3] - CONSULTAR PEÇAS POR FABRICANTE\n"
                              "[4] - VOLTAR AO MENU PRINCIPAL\n >>> "))
            if opcao == 1:
                print("Lista de todas as peças cadastradas\n")
                if len(lista_pecas) == 0:  # se nao houver nada no dicionário exibe a mensagem de nehuma peça cadastrada
                    print("Nenhuma peça cadastrada\n")
                    continue  # volta ao menu
                else:  # se houver alguma peça no dicionário,faz a varredura e exibe na tela
                    for peca in lista_pecas:  # Varre o dicionário
                        for key, value in peca.items():
                            print(f"{key}: {value}")
                break  # encerra a operação

                # buscar peça por código
            elif opcao == 2:
                cod = int(input("POR FAVOR DIGITE O CÓDIGO DA PEÇA QUE DESEJA BUSCAR:\n>>> "))
                peca_encontrada = False  # verificador,falso por padrao
                for peca in lista_pecas:  # varre o dicionário em busca de itens
                    if peca['codigo'] == cod:  # se o valor digitado for corespondente com oque há no dicionário
                        print("Peça encontrada")
                        for key, value in peca.items():  # verifica a chave e o valor e imprime na tela
                            print(f"{key}: {value}")
                        peca_encontrada = True  # o verificador se torna verdadeiro caso a condição seja atendida
                        break
                if not peca_encontrada:  # se nao for atendida a condição  exibe a mensagem na tela
                    print("Nenhuma peça com este código\n"
                          "Por favor digite um código válido")
                    continue
            # Fim da operação buscar peças por código

            # Buscar peças por fabricantes em comum
            elif opcao == 3:
                fab = (input("POR FAVOR DIGITE O FABRICANTE DA PEÇA QUE DESEJA BUSCAR:\n>>> "))
                fab_encontrado = []  # lista para armazenar os fabricantes em comum
                for peca in lista_pecas:  # varre o dicionário em busca de itens
                    if peca['fabricante'] == fab:  # se o valor digitado for corespondente com oque há no dicionário
                        fab_encontrado.append(peca)  # adiciona a lista todos os fabricantes em comum
                if len(fab_encontrado) > 0:  # caso a lista seja maior que 0,exibe a mensagem
                    print("Peças encontradas")
                    for peca in fab_encontrado:  # varre a lista nova e exibe nao tela
                        for key, value in peca.items():  # verifica a chave e o valor e imprime na tela
                            print(f"{key}: {value}")
                else:
                    print("nenhuma peça encontrada deste fabricante")
                    continue

            # Fim da operação Buscar peças por fabricante

            elif opcao == 4:
                return  # retorna oa menu principal
        except ValueError:
            print("opção inválida")

    # inicio  função remove peças
def remove_peca():
    while True:
        try:
            print("----------REMOVER PEÇAS----------")
            cod = int(input("DIGITE O CÓDIGO DO PRODUTO A SER REMOVIDO:\n>>> "))
            peca_encontrada = False  # verificador,falso por padrao
            for peca in lista_pecas:  # varre o dicionário em busca de itens
                if peca['codigo'] == cod:  # se o valor digitado for corespondente com oque há no dicionário
                    lista_pecas.remove(peca) # usa o valor digita e remove da lista
                    print("Produto removido\n")
                    return  # retorna ao menu principal
            if not peca_encontrada:  # se nao for atendida a condição  exibe a mensagem na tela
                print("Nenhuma peça com este código\n"
                      "Por favor digite um código válido")
                return  # retorna ao menu principal
        except ValueError: # tratamento de erro para caracteres inválidos
            print("Valor inválido digite apenas números")
            return  # retorna ao menu principal
#fima da funão remeove peças

def main():
    print("Bem vindo ao Controle de Estoque da  Bicicletaria de Marcos Paulo Alves de Souza\n"
          "RU 943522 ")
    while True:
        try:
            print('-------------------------MENU PRINCIPAL------------------------------')
            opcao = int(input("Por Favor selecione a opção desejada\n"
                              "[1] - CADASTRAR PEÇAS\n"
                              "[2] - CONSULTAR PEÇAS\n"
                              "[3] - REMOVER PEÇAS\n"
                              "[4] - SAIR\n >>> "))
            # cada opção é chamada uma função onde inicia um novo menu
            if opcao == 1:
                cadastrar_peca()
            elif opcao == 2:
                consulta_peca()
            elif opcao == 3:
                remove_peca()
            elif opcao == 4:  # esta opção encerra o programa
                print("SAINDO.....\n"
                      "OBRIGADO POR USAR NOSSO SISTEMA!!")
                break
            else:  # caso nehuma condição seja atendida volta ao inicio do loop
                print("Valor inválido")
                continue
        except ValueError:  # tratamento de erro para caracteres inválidos
            print("Por favor digite uma opção válida digite apenas números\n")
            continue  # colta ao inicio do looping


if __name__ == '__main__':  # declara a função main como inicial,para que o programa sempre inicie a apartir dele
    main()
