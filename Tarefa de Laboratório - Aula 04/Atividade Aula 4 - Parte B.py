n = int(input("Notas lançadas"))
notas = []
soma = 0
media = int

for m in range(1, n+1):
    x = int(input("Digite a nota:"))
    notas.append(x)
    soma = soma+x
media = soma/n

print(notas)

print(media)
