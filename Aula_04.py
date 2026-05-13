### DESAFIO: Crie um programa que: ###
# 1. Peça o raio de um círculo
# 2. Calcule a área, dica: (π * raio²)
# 3. Calcule a circunferência, dica: (2 * π * raio)
# Use π = 3.14

raio = float(input("Digite o raio do circulo: "))
pi = 3.14

area = pi * raio ** 2
circunferencia = 2 * pi * raio

print(f"a area do circule e: {area}")
print(f"a circuferencia do circulo e: {circunferencia}")