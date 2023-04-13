premio = float(input("Digite o valor total do prêmio em R$: "))
gan1 = premio * 0.46
gan2 = premio * 0.32
gan3 = premio - gan1 - gan2

print(f"O primeiro ganhador receberá R$ {gan1:.2f}.")
print(f"O segundo ganhador receberá R$ {gan2:.2f}.")
print(f"O terceiro ganhador receberá R$ {gan3:.2f}.")