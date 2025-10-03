from decimal import Decimal

def calcular_subtotal(precio_unitario, cantidad):
    return precio_unitario * cantidad

def aplicar_descuento(subtotal, descuento_percent):
    descuento_valor = subtotal * (descuento_percent / Decimal('100'))
    return descuento_valor, subtotal - descuento_valor

def calcular_iva_y_total(base_gravable, iva_percent):
    iva_valor = base_gravable * (iva_percent / Decimal('100'))
    total_linea = base_gravable + iva_valor
    return iva_valor, total_linea

productos = [
    {"precio": Decimal('100.00'), "cantidad": 2, "iva": Decimal('19'), "descuento": Decimal('10')},
    {"precio": Decimal('50.00'), "cantidad": 1, "iva": Decimal('5'), "descuento": Decimal('0')}
]

subtotal_total = Decimal('0.00')
iva_total = Decimal('0.00')
total_total = Decimal('0.00')

for p in productos:
    subtotal = calcular_subtotal(p["precio"], p["cantidad"])
    descuento_valor, base_gravable = aplicar_descuento(subtotal, p["descuento"])
    iva_valor, total_linea = calcular_iva_y_total(base_gravable, p["iva"])
    
    print(f"Producto: {p}")
    print(f"Subtotal: {subtotal}, Descuento: {descuento_valor}, Base: {base_gravable}, IVA: {iva_valor}, Total línea: {total_linea}")
    print("-----")
    
    subtotal_total += subtotal
    iva_total += iva_valor
    total_total += total_linea

print("==== VENTA FINAL ====")
print("Subtotal:", subtotal_total)
print("IVA total:", iva_total)
print("Total final:", total_total)
