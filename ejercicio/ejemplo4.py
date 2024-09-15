import numpy as np

# Define las dimensiones de la matriz
num_ciudades = 3
num_dias = 7
num_semanas = 4

# Crea la matriz 3D con temperaturas aleatorias
temperatures = np.random.randint(10, 35, size=(num_ciudades, num_dias, num_semanas))

# Función para calcular el promedio semanal de una ciudad
def promedio_semanal(ciudad, semana):
    return np.mean(temperatures[ciudad, :, semana])

# Selecciona una ciudad y una semana (índices comienzan desde 0)
ciudad_seleccionada = 2  # Tercera ciudad
semana_seleccionada = 3  # Cuarta semana

# Calcula el promedio de la ciudad y semana seleccionadas
promedio = promedio_semanal(ciudad_seleccionada, semana_seleccionada)
print(f"El promedio de temperaturas de la ciudad {ciudad_seleccionada + 1} en la semana {semana_seleccionada + 1} es: {promedio:.2f}°C")

# Calcula el promedio de todas las ciudades y semanas
promedio_total = np.mean(temperatures)
print(f"El promedio de temperaturas de todas las ciudades y semanas es: {promedio_total:.2f}°C")