import math


def calcular_area_circulo(raio):
    area = math.pi * (raio ** 2)  # Fórmula da área: A = π * r²
    return area

raio = float(input("Digite o valor do raio do círculo: "))

area = calcular_area_circulo(raio)

print(f"A área do círculo com raio {raio} é: {area:.2f} unidades quadradas.")
