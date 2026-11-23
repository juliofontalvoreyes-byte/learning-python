from random import randint

count = 0
num = randint(1, 100)

while True:
    try:
        user_num = int(input("Adivina el numero entre 1 y 100: "))
    except ValueError:
        print("Entrada inválida. Por favor, debes ingresar un número entero.")
    else:
        
        if user_num < 1 or user_num > 100:
            print("El número debe estar entre 1 y 100.")
            continue

        count += 1
        if user_num == num:
            if count == 1:
                print(f"¡Increíble! Lo adivinaste en {count} intento.")
            else:
                print(f"¡Correcto! Lo adivinaste en {count} intentos.")
            break
        elif user_num < num:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")
        