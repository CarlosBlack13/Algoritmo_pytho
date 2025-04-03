
def calcular_area_quadrado(lado):
    area = lado ** 2
    return area


lado = float(input("Digite o valor do lado do quadrado: "))


area = calcular_area_quadrado(lado)


dobro_area = area * 2


print(f"A área do quadrado é: {area} unidades quadradas.")
print(f"O dobro da área do quadrado é: {dobro_area} unidades quadradas.")
