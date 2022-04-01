#criação da classe que define os atributos dos produtos
from turtle import goto


class mercadoria:
    codigoProduto = 0
    nomeMercadoria = ''
    precoMercadoria = 0.00
    #codigoMercadoria = 0
    quantidadeEstoque = 0

class compra:
    codigoProd = 0
    quantidadeProd = 0
    nomeProd = ''
    total = 0.00

#cadastro de novos produtos no sistema do mercado
def cadastroMercadoria(idProduto):
    print("\t\t\tCADASTRAR PRODUTO\n")
    produto=mercadoria()
    produto.codigoProduto = idProduto
    produto.nomeMercadoria=input("Nome do Produto: ")
    produto.precoMercadoria=float(input("Preço do Produto: "))
    #produto.codigoMercadoria=int(input("Código de Barras do Produto: "))
    produto.quantidadeEstoque=int(input("Quantidade em Estoque: "))
    print("\n")
    return produto

def atualizaProduto(mercado, cod):
    existe = 0
    for i in range(len(mercado)):
        if cod == mercado[i].codigoProduto:
            existe = 1
            print("\t\t\tO QUE DESEJA ATUALIZAR?\n")
            print("[6] Preço")
            print("[7] Estoque")
            print("[8] Preço e estoque")
            print("[9] Voltar")
            atualiza=int(input("\nEscolha uma opção: "))
            #return atualiza
            print("\n")

            if atualiza == 6:
                print("Preço atual: ", mercado[i].precoMercadoria)
                mercado[i].precoMercadoria=float(input("Novo preço: "))
                print("\n")
                break
            
            elif atualiza == 7:
                print("Estoque atual: ", mercado[i].quantidadeEstoque)
                mercado[i].quantidadeEstoque=int(input("Nova quantidade em estoque: "))
                print("\n")
                break

            elif atualiza == 8:
                print("Preço atual: ", mercado[i].precoMercadoria)
                print("Estoque atual: ", mercado[i].quantidadeEstoque)
                print("\n")
                mercado[i].precoMercadoria=float(input("Novo preço: "))
                mercado[i].quantidadeEstoque=int(input("Nova quantidade em estoque: "))
                print("\n")
                break
            elif atualiza == 9:
                break
            else:
                print("Opção Inválida!")
                atualizaProduto(mercado, cod)

    if existe == 0:
        print("Produto não Cadastrado!\n")


def registraCompra(mercado, cod):
    
    regComp=compra()
    for i in range(len(mercado)):
            if cod == mercado[i].codigoProduto:
                print("Nome do Produto: ", mercado[i].nomeMercadoria)
                print("\n")

                qtd=int(input("Quantidade: "))
                if qtd > mercado[i].quantidadeEstoque:
                    print("Quantidade superior ao estoque!")
                    print("Quantidade em estoque: ", mercado[i].quantidadeEstoque)
                    print("Compra não realizada!\n")
                else:
                    mercado[i].quantidadeEstoque = mercado[i].quantidadeEstoque - qtd
                    regComp.codigoProd = mercado[i].codigoProduto
                    regComp.nomeProd = mercado[i].nomeMercadoria
                    regComp.quantidadeProd = qtd
                    regComp.total = mercado[i].precoMercadoria * qtd
                    print("Compra adicionada!\n")
                    return regComp
        

def chamaCompra(mercado):
    comp = []
    totalPagar = 0.0
    print("\t\t\tCOMPRA\n")
    print("Digite 0 no ID do Produto para encerrar compra\n")

    while True:
        cod=int(input("\nID do Produto: "))
        if cod != 0:
            existe = 0
            for i in range(len(mercado)):
                if cod == mercado[i].codigoProduto:
                    existe = 1
                    novaCompra=registraCompra(mercado, cod)
                    comp.append(novaCompra)
                    break
            if existe == 0:
                print("Produto não Cadastrado!\n")

        else:
            print("\nCompra Encerrada!")
            print("\n")
            break

    print("\t------------------------------------------------------------------")
    print("\t\t\t\tCUPOM FISCAL")
    print("\t------------------------------------------------------------------")
    print("\tCódigo\t\tProduto\t\tQuantidade\t\tPreço")
    for i in range(len(comp)):
        print("\t", comp[i].codigoProd, "\t\t", comp[i].nomeProd, "   \t", comp[i].quantidadeProd, "   \t\t\t", comp[i].total)
        totalPagar = totalPagar + comp[i].total

    print("\t\t\t\t\t\t\t Total: ", totalPagar)
    print("\t------------------------------------------------------------------")
    print("\n")

    


def printaProduto(mercado, cod):
    if cod == 0:
        print("\t\t\tPRODUTOS LISTADOS\n")
        for i in range(len(mercado)):
            print("ID do Produto: ", mercado[i].codigoProduto)
            print("Nome do Produto: ", mercado[i].nomeMercadoria)
            print("Preço: ", mercado[i].precoMercadoria)
            #print("Código de Barras: ", mercado[i].codigoMercadoria)
            print("Quantidade: ", mercado[i].quantidadeEstoque)
            print("\n")
    else:
        existe = 0
        print("\t\t\tINFORMAÇÕES DO PRODUTO\n")
        for i in range(len(mercado)):
            if cod == mercado[i].codigoProduto:
                existe = 1
                print("ID do Produto: ", mercado[i].codigoProduto)
                print("Nome do Produto: ", mercado[i].nomeMercadoria)
                print("Preço: ", mercado[i].precoMercadoria)
                #print("Código de Barras: ", mercado[i].codigoMercadoria)
                print("Quantidade: ", mercado[i].quantidadeEstoque)
                print("\n")
                break
        if existe == 0:
            print("Produto não Cadastrado!\n")




#escolha das ações a serem realizadas pelo operador do caixa
def menu():
    print("\t\t\tMENU\n")
    print("[1] Cadastrar Novo Produto")
    print("[2] Atualizar Produto")
    print("[3] Realizar Compra")
    print("[4] Consultar Informações de um Produto")
    print("[5] Listar Produtos Cadastrados")
    print("[0] Sair do Programa")
    #print("\nEscolha uma opção: ")
    opcoes=int(input("\nEscolha uma opção: "))
    print("\n")
    return opcoes


mercado = []
idProduto=1

while True:
    op=menu()
    if op == 0:
        break
    elif op == 1:
        novoProduto=cadastroMercadoria(idProduto)
        mercado.append(novoProduto)
        idProduto += 1

    elif op == 2:
        if len(mercado) == 0:
            print("Nenhum produto cadastrado!\n")
        else:
            cod=int(input("\nID do Produto: "))
            print("\n")
            atualizaProduto(mercado, cod)

    elif op == 3:
        if len(mercado) == 0:
            print("Nenhum produto cadastrado!\n")
        else:
            chamaCompra(mercado)

    elif op == 4:
        if len(mercado) == 0:
            print("Nenhum produto cadastrado!\n")
        else:
            cod=int(input("\nID do Produto: "))
            print("\n")
            printaProduto(mercado, cod)

    elif op== 5:
        if len(mercado) == 0:
            print("Nenhum produto cadastrado!\n")
        else:
            printaProduto(mercado, 0)
    else:
        print("Opção Inválida!")