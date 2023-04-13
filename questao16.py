segundos = int(input("Digite um valor inteiro positivo em segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = (segundos % 3600) % 60

print(f"{horas}h {minutos}min {segundos}s")