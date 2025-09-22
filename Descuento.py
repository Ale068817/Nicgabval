def calcular_descuento(total_compra, descuento = 25):
    total_descuento = total_compra * (descuento/100)
    valor_a_pagar = (total_compra - total_descuento)
    return (total_descuento, valor_a_pagar)

print("COMPRA DE PRODUCTOS")
total_compra = int(input("Ingrese el total de la compra:  "))
if(total_compra >= 100):
    total_descuento, valor_a_pagar = calcular_descuento(int(total_compra), 25)
    print(f"descuento: {int(total_descuento)}")
    print(f"valor a Pagar: {int(valor_a_pagar)}")

else:
    print(f"Total a Pagar: {total_compra}")


