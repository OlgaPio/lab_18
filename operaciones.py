# Capturar dos números y realizar operaciones
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Operaciones matemáticas
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")

# Manejo de división por cero
if num2 != 0:
    print(f"División: {num1 / num2}")
else:
    print("Error: No se puede dividir por cero.")
