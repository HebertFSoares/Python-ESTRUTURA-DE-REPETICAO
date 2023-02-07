n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
op = 0
while op != 5:
    print("**"*30)
    print("[1] SOMAR ")
    print("[2] MULTIPLICAR ")
    print("[3] MAIOR")
    print("[4] NOVOS NÚMEROS")
    print("[5] SAIR DO PROGRAMA")
    op = int(input("Digite a opção: "))
    if op == 1:
        soma = n1 + n2
        print(f"Resultado da sua soma = {soma}")
    elif op == 2:
        mult = n1 * n2
        print(f"Resultado da multiplicação = {mult}")
    elif op == 3:
        if n1 > n2:
            print(f"O maior é {n1}")
        else:
            print(f"O maior é {n2}")
    elif op == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif op == 5:
        print("PROGRAMA FINALIZADO")
        break
    else:
        print("Digito Invalido...")
    