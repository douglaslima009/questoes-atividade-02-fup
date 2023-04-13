taxa_de_cambio = 3.92

valor_em_dolares = float(input("Digite o valor em dólares: "))

valor_em_reais = valor_em_dolares * taxa_de_cambio

print(f"US${valor_em_dolares:.2f} equivalem a R${valor_em_reais:.2f}.")
