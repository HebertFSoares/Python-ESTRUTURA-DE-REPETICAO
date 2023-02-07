sexo = str(input("Digite seu Sexo [M/F] ")).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input("Dados invalidos. Digite seu sexo novamente: ")).strip().upper()[0]
print(f"Sexo {sexo} foi registrado.")