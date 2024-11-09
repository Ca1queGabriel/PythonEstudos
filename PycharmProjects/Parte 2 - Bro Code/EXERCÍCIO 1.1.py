#objetivo, calcular área de um círculo
import math

raio = float(input("Insira o raio do círculo que você gostaria de calcular a área: "))
area = math.pi*pow(raio,2)
print(f"A área de um círculo de um raio {raio} é igual a {round(area,2)}cm² ")