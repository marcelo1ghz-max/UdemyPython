# Exercício 13 - List Comprehension

precos = []
caros = []
com_desconto = []

quantidade = input()

while quantidade != "0":
    novos_precos = [float(x) for x in input("Preço: ").split()]
    
    precos.extend(novos_precos)
    caros.extend([p for p in novos_precos if p > 10])
    com_desconto.extend([round(p * 0.9, 2) for p in novos_precos])
    
    quantidade = input()

print(f"Preços: {precos}")
print(f"Acima de R$ 10: {caros}")
print(f"Com desconto: {com_desconto}")
