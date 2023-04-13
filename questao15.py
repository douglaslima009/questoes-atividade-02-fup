num = int(input("Digite um número de quatro dígitos: "))
milhares = num // 1000
centenas = (num // 100) % 10
dezenas = (num // 10) % 10
unidades = num % 10

print(milhares)
print(centenas)
print(dezenas)
print(unidades)