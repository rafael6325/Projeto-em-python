def calcular_area(base, altura):
    return base * altura

base = float(input("Digite a base do quadrado/retângulo: "))
altura = float(input("Digite a altura do quadrado/retângulo: "))

area = calcular_area(base, altura)

print(f"A área do quadrado/retângulo é: {area}")