tempo_caracol = []
valor = 0

while True:
    valor = int(input("Digite o tempo: "))
    if valor == -1:
        break
    else:

        tempo_caracol.append(valor)
    n0 = 0
    n1 = 0
    n2 = 0
    soma = 0
    qtd = 0
    vmin = 0
    vmx = 0

    for t in tempo_caracol:
        soma = soma+t
        qtd = qtd+1

        if vmin == 0 and vmx == 0:
            vmin = t
            vmx = t

        if t < vmin:
            vmin = t
            if t > vmx:
                vmx = t

            if t < 180:
                n0 = n0+1
            elif t > 180 and t < 240:
                n1 = n1+1
            elif t > 240:
                n2 = n2+1

media = soma/qtd
media = round(media, 2)
print('caracois com nivel 0', n0)
print('caracois com nivel 1', n1)
print('caracois com nivel 2', n2)
print('caracois média:', media)
print('caracois minimo:', vmin)
print('caracois maximo:', vmx)
