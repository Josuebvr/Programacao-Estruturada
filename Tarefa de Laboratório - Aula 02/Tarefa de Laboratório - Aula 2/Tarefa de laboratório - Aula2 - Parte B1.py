a = float(input("Digite a medida do lado a: "))
b = float(input("Digite a medida do lado b: "))
c = float(input("Digite a medida do lado c: "))

# Valores inválidos na entrada
if a == 0 or b == 0 or c == 0 and a >= b+c or b >= a+c or c >= b+a:
    print("Valores inválidos na entrada.")

# Triângulo Equilátero
if a == b and a == c and c == b:
    print("É um Triângulo Equilátero.")

# Triângulo Isósceles
elif a == b or a == c or c == b:
    print("É um Triângulo Isósceles.")

# Triângulo Escaleno
if a != b and a != c and c != b and a*b > 0 and b*c > 0 and c*a > 0:
    print("É um Triângulo Escaleno.")

# Triângulo Acutângulo
if a == b * c / 2 and a*b != 0 and b*c != 0 and c*a != 0:
    print("É um Triângulo Acutângulo.")

# Triângulo Retângulo
if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
    print("É um Triângulo Retângulo.")

# Triângulo Obtusângulo
if a*a > b*b + c*c and a*b != 0 and b*c != 0 and c*a != 0:
    print("É um Triângulo Obtusângulo.")
