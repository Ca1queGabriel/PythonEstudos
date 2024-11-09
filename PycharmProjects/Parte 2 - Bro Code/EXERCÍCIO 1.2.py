import math

ladoA = float(input("Insira o lado A do triângulo: "))
ladoB = float(input("Insira o lado B do triângulo: "))
hipot = math.sqrt(pow(ladoA, 2) + pow(ladoB, 2))
print(f"Lado C é: {hipot}")