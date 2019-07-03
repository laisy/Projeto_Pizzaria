import os
import os.path

def espaco():
    print(20*"=")

#Funcoes Genericas

def criarArquivo(nomeArq):
    try:
        with open('%s.txt' %nomeArq, 'r') as f:     #ja existe o arquivo? retorne
            return

    except IOError:                                 #arquivo nao encontrado? crie
         arq = open('%s.txt' %nomeArq, 'w')
         arq.close()

#OPCOES COM CLIENTE ABAIXO

def cadastrarCliente():
    arq = open('clientes.txt', 'a')

    espaco()
    telefone = raw_input('Informe o telefone do Cliente: ')
    arq.write(str('Telefone: ' + telefone + '\n'))
    nome = raw_input('Informe o nome completo do Cliente: ')
    arq.write(str('Nome: ' + nome + '\n'))
    endereco = raw_input('Informe o endereco do Cliente: ')
    arq.write(str('Endereco: ' + endereco + '\n'))
    codigo = raw_input('Informe o codigo do Cliente: ')
    arq.write(str('Codigo: ' + codigo + '\n'))
    arq.close()
    espaco()
    print('CLIENTE CADASTRADO COM SUCESSO!')
    espaco()

def excluirCliente():
    espaco()
    cod = raw_input('INFORME O CODIGO DO CLIENTE: ')
    confirma = raw_input('CONFIRMA A EXCLUSAO DO CLIENTE? ')
    espaco()

    cod = (str('Codigo: ' + cod + '\n'))
    lista = []
    if (confirma == 'sim'):
        with open('clientes.txt', 'r') as a:
            for linha in a.readlines():
                lista.append(linha)

            if (cod in lista):
                posi = lista.index(cod)

                lista.pop(int(posi))
                lista.pop(int(posi-1))
                lista.pop(int(posi-2))
                lista.pop(int(posi-3))

                arq = open('clientes.txt', 'w')
                arq.writelines(lista)
                arq.close()
                espaco()
                print ('CLIENTE REMOVIDO!')
                espaco()

    elif (confirma == 'nao'):
        return
    else:
        espaco()
        print('OPCAO INVALIDA! ')
        espaco()
        return

def exibirCliente():
    espaco()
    tel = raw_input('INFORME O TELEFONE DO CLIENTE: ')
    nTel = str('Telefone: ' + tel  + '\n')
    espaco()

    listaCliente = []
    lista = []
    try:
        with open( 'clientes.txt', 'r' ) as a:
            for linha in a.readlines():
                lista.append(linha)
            for k in range(0, len(lista), 3):
                flag = nTel in lista[k]
                if (flag == True):
                    if lista[k] == nTel:
                        listaCliente.append(lista[k].rstrip('\n'))      # .rstrip('\n') serve para retirar o \n
                        listaCliente.append(lista[k+1].rstrip('\n'))
                        listaCliente.append(lista[k+2].rstrip('\n'))
                        listaCliente.append(lista[k+3].rstrip('\n'))

                        for k in listaCliente:
                            print(k)

    except IOError:
        criarArquivo(clientes)
        return

def buscaCliente():
    espaco()
    codClien = raw_input('INFORME O CODIGO DO CLIENTE: ')
    nCod = str('Codigo: ' + codClien  + '\n')
    espaco()

    listaCliente = []
    lista = []
    with open( 'clientes.txt', 'r' ) as a:
        for linha in a.readlines():
            lista.append(linha)
        for k in range(len(lista)):
            flag = nCod in lista[k]
            if (flag == True):
                if lista[k] == nCod:
                    listaCliente.append(lista[k].rstrip('\n'))
                    listaCliente.append(lista[k-1].rstrip('\n'))
                    listaCliente.append(lista[k-2].rstrip('\n'))
                    listaCliente.append(lista[k-3].rstrip('\n'))

                    return listaCliente
    return

#OPCOES COM PRODUTOS ABAIXO

def cadastrarProduto():
    arq = open('produtos.txt', 'a')

    espaco()
    cod = int(input('Informe o codigo do Produto: '))
    arq.write(str('Codigo: ' + str(cod) + '\n'))
    nome = raw_input('Informe o nome do Produto: ')
    arq.write(str('Nome: ' + nome + '\n'))
    tempoMax = raw_input('Informe o tempo maximo de preparo: ')
    arq.write(str('TempoMax: ' + tempoMax + '\n'))
    ativo = raw_input('Informe se produto esta ativo (0 - Ativo ou 1 - Inativo): ')
    arq.write(str('Ativo: ' + ativo + '\n'))
    preco = float(input('Informe o preco do Produto: R$ '))
    arq.write(str('Preco: R$ ' + str(preco) + '\n'))

    arq.close()

    espaco()
    print('PRODUTO CADASTRADO COM SUCESSO!')
    espaco()
    return

def excluirProduto():
        espaco()
        cod = raw_input('INFORME O CODIGO DO PRODUTO: ')
        confirma = raw_input('CONFIRMA A EXCLUSAO DO PRODUTO? ')
        espaco()

        cod = (str('Codigo: ' + cod + '\n'))
        lista = []
        if (confirma == 'sim'):
            with open('produtos.txt', 'r') as a:
                for linha in a.readlines():
                    lista.append(linha)

                if (cod in lista):
                    posi = lista.index(cod)

                    lista.pop(int(posi+9))
                    lista.pop(int(posi+8))
                    lista.pop(int(posi+7))
                    lista.pop(int(posi+6))
                    lista.pop(int(posi+5))
                    lista.pop(int(posi+4))
                    lista.pop(int(posi+3))
                    lista.pop(int(posi+2))
                    lista.pop(int(posi+1))
                    lista.pop(int(posi))

                    arq = open('produtos.txt', 'w')
                    arq.writelines(lista)
                    arq.close()
                    espaco()
                    print ('PRODUTO REMOVIDO!')
                    espaco()

        elif (confirma == 'nao'):
            return
        else:
            espaco()
            print('OPCAO INVALIDA! ')
            espaco()
            return

def buscarProduto():
    espaco()
    cod = int(raw_input('INFORME O CODIGO DO PRODUTO: '))
    nCod = str('Codigo: ' + str(cod)  + '\n')
    espaco()

    listaProduto = []
    lista = []
    try:
        with open( 'produtos.txt', 'r' ) as a:
            for linha in a.readlines():
                lista.append(linha)
            for k in range(0, len(lista), 4):
                flag = nCod in lista[k]
                if (flag == True):
                    if lista[k] == nCod:
                        listaProduto.append(lista[k].rstrip('\n'))
                        listaProduto.append(lista[k+1].rstrip('\n'))
                        listaProduto.append(lista[k+2].rstrip('\n'))
                        listaProduto.append(lista[k+3].rstrip('\n'))
                        listaProduto.append(lista[k+4].rstrip('\n'))

                        return listaProduto
                        for k in listaProduto:
                            print(k)

    except IOError:
        criarArquivo(produtos)
        return

def cardapio():

        listaCard = []
        lista = []

        with open( 'produtos.txt', 'r' ) as a:
            for linha in a.readlines():
                lista.append(linha)
            for k in range(len(lista)):
                if (lista[k] == 'Ativo: 0\n'):
                    listaCard.append(lista[k-3].rstrip('\n'))
                    listaCard.append(lista[k-2].rstrip('\n'))
                    listaCard.append(lista[k+1].rstrip('\n'))

        espaco()
        print ('CARDAPIO')
        espaco()
        for k in listaCard:
            print(k)
        espaco()

#OPCOES COM PEDIDOS ABAIXO

def cadastrarPedido():

        arq = open('pedidos.txt', 'a')

        espaco()
        codPed = int(input('INFORME O CODIGO DO PEDIDO: '))
        arq.write(str('CodigoPedido: ' + str(codPed) + '\n'))

        quantProd = int(input('INFORME A QUANTIDADE DE PRODUTOS: '))
        arq.write(str('QuantidadeProd: ' + str(quantProd) + '\n'))
        if (quantProd == 1):
            arq.write(str(str(buscarProduto()) + '\n'))
            quantDoProd = int(input('INFORME A QUANTIDADE DESSE PRODUTO: '))
            arq.write(str('QuantDoProd: ' + str(quantDoProd) + '\n'))
        else:
            while(quantProd > 0):
                arq.write(str(str(buscarProduto()) + '\n'))
                quantDoProd = int(input('INFORME A QUANTIDADE DESSE PRODUTO: '))
                arq.write(str('QuantDoProd: ' + str(quantDoProd) + '\n'))
                quantProd -= 1

        arq.write(str(str(buscaCliente()) + '\n'))
        data = raw_input('INFORME A DATA (DD/MM) DO PEDIDO: ')
        arq.write(str('Data: ' + data + '\n'))
        hora = raw_input('INFORME A HORA (HH:MM) DO PEDIDO: ')
        arq.write(str('Hora: ' + hora + '\n'))

        arq.write(str(str(horaEnt()) + '\n'))

        arq.close()

        espaco()
        print('PEDIDO CADASTRADO COM SUCESSO!')
        espaco()

def horaEnt():

    listaPedido = []
    lista = []
    listaTemps = []

    with open( 'pedidos.txt', 'r' ) as a:
        for linha in a.readlines():
            lista.append(linha)
        for i in range(len(lista)):
            for j in range(i):
                listaTemps.append(lista[i][3])

        return listaTemps

#MENUS ABAIXO

def menuClientes():
    espaco()
    print("MENU CLIENTES")
    espaco()
    print("1 - CADASTRAR CLIENTE")
    print("2 - EXCLUIR CLIENTE")
    print("3 - EXIBIR CLIENTE")
    print("4 - RETORNAR PARA O MENU PRINCIPAL")
    print("5 - ENCERRAR")
    espaco()

    opcaoClientes = int(input())
    while (opcaoClientes != 5):
        nomeArq = 'clientes'
        if (opcaoClientes == 1):
            criarArquivo(nomeArq)               #Conferir se o arquivo ja existe, caso nao criar
            cadastrarCliente()
            return

        if (opcaoClientes == 2):
            criarArquivo(nomeArq)
            excluirCliente()
            return

        if (opcaoClientes == 3):
            criarArquivo(nomeArq)
            exibirCliente()
            return

        if (opcaoClientes == 4):
            return
        opcaoClientes = int(input("DIGITE A OPCAO DESEJADA: "))

    exit(0)

def menuProdutos():
    espaco()
    print("MENU PRODUTOS")
    espaco()
    print("1 - CADASTRAR PRODUTO")
    print("2 - EXCLUIR PRODUTO")
    print("3 - BUSCAR PRODUTO")
    print("4 - RETORNAR PARA O MENU PRINCIPAL")
    print("5 - ENCERRAR")
    espaco()

    opcaoProdutos = int(input())

    while(opcaoProdutos != 5):
        nomeArq = 'produtos'
        if (opcaoProdutos == 1):
            criarArquivo(nomeArq)
            cadastrarProduto()
            return

        if (opcaoProdutos == 2):
            excluirProduto()
            return

        if (opcaoProdutos == 3):
            buscarProduto()
            return

        if (opcaoProdutos == 4):
            return
        opcaoProdutos = int(input("DIGITE A OPCAO DESEJADA: "))

    exit(0)

def menuPedidos():
    espaco()
    print("MENU PEDIDOS")
    espaco()
    print("1 - CADASTRO PEDIDO")
    print("2 - EXCLUIR PEDIDO")
    print("3 - BUSCAR PEDIDO")
    print("4 - RETORNAR PARA O MENU PRINCIPAL")
    print("5 - ENCERRAR")
    espaco()
    opcaoPedidos = int(input())

    while (opcaoPedidos != 5):
        nomeArq = 'pedidos'
        if (opcaoPedidos == 1):
            criarArquivo(nomeArq)
            cadastrarPedido()
            return
        if (opcaoPedidos == 4):
            return
        opcaoPedidos = int(input("DIGITE A OPCAO DESEJADA: "))

    exit(0)

def menuPrincipal():
    espaco()
    print("MENU PRINCIPAL")
    espaco()
    print("1 - OPCOES CLIENTES")
    print("2 - OPCOES PRODUTOS")
    print("3 - OPCOES PEDIDOS")
    print("4 - CARDAPIO")
    print("5 - SAIR DO SISTEMA")
    espaco()
    opcao = int(input("DIGITE A OPCAO DESEJADA: "))
    return opcao

opcao = menuPrincipal()

while (opcao < 5):

    if (opcao == 1):
        menuClientes()

    if (opcao == 2):
        menuProdutos()

    if (opcao == 3):
        menuPedidos()

    if (opcao == 4):
        cardapio()

    opcao = menuPrincipal()
