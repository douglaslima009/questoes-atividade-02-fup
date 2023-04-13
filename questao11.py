valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))
soma_quadrados = valor1 ** 2 + valor2 ** 2 + valor3 ** 2
quadrado_soma = (valor1 + valor2 + valor3) ** 2

print(f"A soma dos quadrados dos três valores é {soma_quadrados:.2f}.")
print(f"O quadrado da soma dos três valores é {quadrado_soma:.2f}.")
