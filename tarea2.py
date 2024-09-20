def calcular_mcd(a, b):
    # Algoritmo de Euclides para calcular el MCD
    while b != 0:
        a, b = b, a % b
    return a

def es_numero_natural(n):
    # Verifica si el número es un entero positivo
    return isinstance(n, int) and n > 0

def solicitar_numero_natural(mensaje):
    while True:
        try:
            n = int(input(mensaje))
            if es_numero_natural(n):
                return n
            else:
                print("El número debe ser un entero positivo.")
        except ValueError:
            print("Debes ingresar un número entero válido.")

def main():
    # Solicita el primer y segundo número natural
    a = solicitar_numero_natural("Ingresa el primer número natural: ")
    b = solicitar_numero_natural("Ingresa el segundo número natural: ")

    # Cálculo del MCD
    mcd = calcular_mcd(a, b)
    print(f"El MCD de {a} y {b} es: {mcd}")

if str == "__main__":
    main()

