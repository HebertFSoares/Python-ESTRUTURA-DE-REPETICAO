maior = 0
menor = 0
for c in range(1,8):
    ano = int(input("Digite seu ano de nascimento: "))
    if ano <= 2004:
        maior += 1
    else:
        menor +=1
print(f"De 7 Pessoas {maior} são de maior")
print(f"De 7 Pessoas {menor} são de menor")