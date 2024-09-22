def calcular_descuento(monto_total, descuento=10):
  """
  Calcula el descuento en una compra.

  Args:
    monto_total: El monto total de la compra.
    descuento: El porcentaje de descuento (por defecto, 10%).

  Returns:
    El monto del descuento calculado.
  """

  # Calcula el descuento en base al porcentaje y el monto total
  monto_descuento = monto_total * (descuento / 100)
  return monto_descuento

# Ejemplo de uso de la función
monto_compra1 = 100
descuento_compra1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento_compra1
print("Monto total de la compra 1:", monto_compra1)
print("Descuento aplicado:", descuento_compra1)
print("Monto final a pagar:", monto_final1)

monto_compra2 = 200
descuento_compra2 = calcular_descuento(monto_compra2, 15)  # Descuento personalizado
monto_final2 = monto_compra2 - descuento_compra2
print("\nMonto total de la compra 2:", monto_compra2)
print("Descuento aplicado:", descuento_compra2)
print("Monto final a pagar:", monto_final2)