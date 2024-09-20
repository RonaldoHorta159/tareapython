def calcular_mcd(a, b):
    # Algoritmo de Euclides para calcular el MCD
    while b != 0:
        a, b = b, a % b
    return a

def es_numero_natural(n):
    # Verifica si el número es un entero positivo
    return isinstance(n, int) and n > 0

def main():
    try:
        # Ingreso y validación de los datos
        a = int(input("Ingresa el primer número natural: "))
        b = int(input("Ingresa el segundo número natural: "))
        
        if not es_numero_natural(a) or not es_numero_natural(b):
            print("Ambos números deben ser naturales (enteros positivos).")
        else:
            # Cálculo del MCD
            mcd = calcular_mcd(a, b)
            print(f"El MCD de {a} y {b} es: {mcd}")
    
    except ValueError:
        print("Debes ingresar números enteros.")

if __name__ == "__main__":
    main()
