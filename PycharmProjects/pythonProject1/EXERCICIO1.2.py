#objetivo: criar um carrinho de mercado
nomedoproduto = input("Insira o nome do produto: ")
precoproduto = float(input("Insira o preço do produto: "))
qtdprodutos = int(input("Insira a quantidade do produto: "))
valorTotal = qtdprodutos * precoproduto
print(f"O valor total de produtos do tipo {nomedoproduto}/s será de: R${valorTotal}")