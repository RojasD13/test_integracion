def obtener_descuento(tipo_cliente: str) -> float:
    "Devuelve el porcentaje de descuento según el tipo de cliente."
    descuentos = {
        "regular": 0.0,
        "premium": 0.10,
        "vip": 0.20,
    }
    if tipo_cliente not in descuentos:
        raise ValueError(f"Tipo de cliente desconocido: {tipo_cliente}")
    return descuentos[tipo_cliente]