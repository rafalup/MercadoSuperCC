#criação da classe que define os atributos dos produtos
class mercadoria:
    codigoProduto = 0
    nomeMercadoria = ''
    precoMercadoria = 0.00
    codigoMercadoria = 0
    quantidadeEstoque = 0

#cadastro de novos produtos no sistema do mercado
def cadastroMercadoria(idProduto):
    print("\t\t\tCADASTRAR PRODUTO\n")
    produto=mercadoria()
    produto.codigoProduto = idProduto
    produto.nomeMercadoria=input("Nome do Produto: ")
    produto.precoMercadoria=float(input("Preço do Produto: "))
    produto.codigoMercadoria=int(input("Código de Barras do Produto: "))
    produto.quantidadeEstoque=int(input("Quantidade em Estoque: "))
    print("\n")
    return produto

def atualizaProduto(mercado, cod):
    if len(mercado) == 0:
        print("Produto não Cadastrado!\n")
    print("\t\t\tO QUE DESEJA ATUALIZAR?\n")
    print("[6] Preço")
    print("[7] Estoque")
    print("[8] Preço e estoque")
    atualiza=int(input("\nEscolha uma opção: "))
    #return atualiza
    print("\n")

    if atualiza == 6:
        for i in range(len(mercado)):
            if cod == mercado[i].codigoProduto:
                print("Preço atual: ", mercado[i].precoMercadoria)
                mercado[i].precoMercadoria=float(input("Novo preço: "))
                print("\n")
    
    elif atualiza == 7:
        for i in range(len(mercado)):
            if cod == mercado[i].codigoProduto:
                print("Estoque atual: ", mercado[i].quantidadeEstoque)
                mercado[i].quantidadeEstoque=int(input("Nova quantidade em estoque: "))
                print("\n")

    elif atualiza == 8:
        for i in range(len(mercado)):
            if cod == mercado[i].codigoProduto:
                print("Preço atual: ", mercado[i].precoMercadoria)
                print("Estoque atual: ", mercado[i].quantidadeEstoque)
                print("\n")
                mercado[i].precoMercadoria=float(input("Novo preço: "))
                mercado[i].quantidadeEstoque=int(input("Nova quantidade em estoque: "))
                print("\n")
    else:
        print("Opção Inválida!")
        atualizaProduto(mercado, cod)



def printaProduto(mercado, cod):
    if cod == 0:
        print("\t\t\tPRODUTOS LISTADOS\n")
        for i in range(len(mercado)):
            print("ID do Produto: ", mercado[i].codigoProduto)
            print("Nome do Produto: ", mercado[i].nomeMercadoria)
            print("Preço: ", mercado[i].precoMercadoria)
            print("Código de Barras: ", mercado[i].codigoMercadoria)
            print("Quantidade: ", mercado[i].quantidadeEstoque)
            print("\n")
    else:
        print("\t\t\tINFORMAÇÕES DO PRODUTO\n")
        if len(mercado) == 0:
            print("Produto não Cadastrado!\n")
            return
        for i in range(len(mercado)):
            if cod == mercado[i].codigoProduto:
                print("ID do Produto: ", mercado[i].codigoProduto)
                print("Nome do Produto: ", mercado[i].nomeMercadoria)
                print("Preço: ", mercado[i].precoMercadoria)
                print("Código de Barras: ", mercado[i].codigoMercadoria)
                print("Quantidade: ", mercado[i].quantidadeEstoque)
                print("\n")
            else:
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


mercado=[]
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
        cod=int(input("\nID do Produto: "))
        print("\n")
        for i in range(len(mercado)):
            if cod == mercado[i].codigoProduto:
                atualizaProduto(mercado, cod)
            else:
                print("Produto não Cadastrado!\n")

    elif op == 3:
        novoProduto=cadastroMercadoria()
        mercado.append(novoProduto)

    elif op == 4:
        cod=int(input("\nID do Produto: "))
        print("\n")
        printaProduto(mercado, cod)

    elif op== 5:
        printaProduto(mercado, 0)
    else:
        print("Opção Inválida!")
        menu()