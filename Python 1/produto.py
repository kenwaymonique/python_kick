codigo = input("Digite o código do produto: ")
nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
preco = int(input("Digite o preço do produto: "))

total = (quantidade)*(preco)

print(codigo + " " + nome)
print(quantidade + preco)
print(total)