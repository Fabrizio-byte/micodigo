# Abrimos el archivo en modo escritura para crear uno nuevo o sobreescribir uno existente
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de texto en el archivo
    file.write("Esta es mi primera nota.\n")
    file.write("Aquí va la segunda nota.\n")
    file.write("Y esta es la tercera nota.\n")

print("¡Notas guardadas con éxito!")

# Abrimos el archivo en modo lectura
with open('my_notes.txt', 'r') as file:
    print("Contenido del archivo my_notes.txt:")
    # Leemos el archivo línea por línea
    for line in file:
        # Imprimimos cada línea en la consola
        print(line.rstrip())  # rstrip() elimina los espacios en blanco al final de la línea

print("¡Lectura completada!")