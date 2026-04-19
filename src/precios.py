from descuentos import obtener_descuento

def calcular_precio_final(precio_base: float, tipo_cliente: str) -> float:
    """
    Calcula el precio final aplicando el descuento
    según el tipo de cliente.
    """
    if precio_base < 0:
        raise ValueError("El precio no puede ser negativo")

    descuento = obtener_descuento(tipo_cliente)
    precio_final = precio_base * (1 - descuento)
    return round(precio_final, 2)