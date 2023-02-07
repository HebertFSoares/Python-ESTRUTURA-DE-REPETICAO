a = int(input("Digite um Numero: "))
p = 0

for c in range(2,a):
    if a % c == 0:
        print("Multiplo de", a)
        p += 1
if(p == 0):
    print("É primo")
else:
    print("Tem",p," múltiplos acima de 2 e abaixo de",a)