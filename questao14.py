num = int(input("Digite um número de três dígitos: "))
centenas = num // 100
dezenas = (num // 10) % 10
unidades = num % 10
novo_num = unidades * 100 + dezenas * 10 + centenas

print(f"O número invertido é {novo_num}.")