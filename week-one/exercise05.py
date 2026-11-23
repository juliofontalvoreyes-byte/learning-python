def es_primo(n):
    if n < 2: 
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    numero = int(input("Ingrese un número para verificar si es primo: "))
except ValueError:
    print("Entrada inválida. Por favor, debes ingresar un número entero.")
else:
    
    if es_primo(numero):
        print(f"El número {numero} es primo.")
    else: 
        print(f"El número {numero} no es primo.")

print("\nPrimos del 1 al 100:")

for num in range(1, 101):
    if es_primo(num):
        print(f"El numero {num} es primo.")


