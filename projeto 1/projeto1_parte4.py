def convert_cm_m(centimetros):
    return centimetros / 100

centimetros = float(input("Digite o valor em centímetros: "))

metros = convert_cm_m(centimetros)

print(f"{centimetros} centímetros é igual a {metros} metros.")