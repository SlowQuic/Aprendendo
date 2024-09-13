import math
def raiz_quadrada(numero):
    try:
        resultado = math.sqrt(numero)
        return resultado
    except ValueError:
        return "Não é possivel"  

numero = int(input()) 

resultado = raiz_quadrada(numero)
print(resultado)