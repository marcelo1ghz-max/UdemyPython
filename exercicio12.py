# Exercício 12 - While

quantidade = 0
total = 0.0

nome = input()

while nome != "fim":
    preco = float(input())
    quantidade += 1
    total += preco
    print(f"{quantidade}. {nome} - R$ {preco:.2f}")
    nome = input()

print(f"Quantidade de itens: {quantidade}")
print(f"Total: R$ {total:.2f}")