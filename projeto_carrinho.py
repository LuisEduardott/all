print("=== Bem-vindo ao Carrinho de Compras! ===")
carrinho = []
total = 0

while True:
    produto = input("\nDigite o nome do produto (ou 'sair' para finalizar): ")
    
    if produto.lower() == 'sair':
        break
    
    preco = float(input("Digite o preço do produto: "))
    carrinho.append((produto, preco))
    total += preco
    print(f"Produto '{produto}' adicionado ao carrinho. Preço: R${preco:.2f}")
    
print("\n=== Resumo do Carrinho ===")
for item in carrinho:  
    print(f"{item[0]} - R${item[1]:.2f}")
print(f"Total a pagar: R${total:.2f}")

