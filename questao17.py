import math
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))
distancia = math.sqrt(x**2 + y**2)

print(f"A distância da origem ({0}, {0}) até o ponto ({x}, {y}) é: {distancia:.2f}")