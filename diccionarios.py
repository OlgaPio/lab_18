# Crear un diccionario con información de una persona
dicci = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Bogotá",
    "profesion": "Ingeniero"
}

# Acceder y modificar valores
print("Diccionario original:", dicci)
dicci["edad"] = 32  # Modificar la edad
print("Diccionario modificado:", dicci)

# Agregar un nuevo par clave-valor
dicci["correo"] = "juan@email.com"
print("Diccionario después de agregar correo:", dicci)
