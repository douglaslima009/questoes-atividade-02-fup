apostador1 = float(input("Digite o valor investido pelo primeiro apostador: "))
apostador2 = float(input("Digite o valor investido pelo segundo apostador: "))
apostador3 = float(input("Digite o valor investido pelo terceiro apostador: "))
premio = float(input("Digite o valor do prêmio: "))

total_investido = apostador1 + apostador2 + apostador3
proporcao1 = apostador1 / total_investido
proporcao2 = apostador2 / total_investido
proporcao3 = apostador3 / total_investido
valor1 = proporcao1 * premio
valor2 = proporcao2 * premio
valor3 = proporcao3 * premio

print(f"O primeiro apostador receberá R$ {valor1:.2f}")
print(f"O segundo apostador receberá R$ {valor2:.2f}")
print(f"O terceiro apostador receberá R$ {valor3:.2f}")