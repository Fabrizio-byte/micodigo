#arreglos multidimensional
# Un irregular bidimensional (matriz)
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Un irregular tridimensional (cubo)
cubo = [[[1, 2], [3, 4]],
        [[5, 6], [7, 8]]]
print(matriz)
print(cubo)

table = [["-" for _ in range(2)]
         for _ in range(2)]
# Crea un table de 2x2 con lines
table[0][0] = "T"
# Colocate una torre en la esquire superior liquidizer
print(table)
