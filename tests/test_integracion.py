import pytest
from precios import calcular_precio_final

class TestIntegracionPrecios:
    "Pruebas de integración entre precios y descuentos."

    def test_cliente_regular_sin_descuento(self):
        "Un cliente regular paga el precio completo."
        resultado = calcular_precio_final(100.0, "regular")
        assert resultado == 100.0

    def test_cliente_premium_con_descuento_10(self):
        "Un cliente premium obtiene 10% de descuento."
        resultado = calcular_precio_final(200.0, "premium")
        assert resultado == 180.0

    def test_cliente_vip_con_descuento_20(self):
        "Un cliente VIP obtiene 20% de descuento."
        resultado = calcular_precio_final(50.0, "vip")
        assert resultado == 40.0

    def test_precio_cero_es_valido(self):
        "Un precio de 0 es válido y sigue aplicando descuentos."
        resultado = calcular_precio_final(0.0, "vip")
        assert resultado == 0.0

    def test_cliente_tipo_invalido_lanza_error(self):
        "Un tipo de cliente desconocido debe lanzar ValueError."
        with pytest.raises(ValueError, match="Tipo de cliente desconocido"):
            calcular_precio_final(100.0, "corporativo")

    def test_precio_negativo_lanza_error(self):
        "Un precio negativo debe lanzar ValueError."
        with pytest.raises(ValueError, match="El precio no puede ser negativo"):
            calcular_precio_final(-10.0, "regular")

    def test_resultado_redondeado_a_dos_decimales(self):
        "El resultado debe estar redondeado a 2 decimales."
        resultado = calcular_precio_final(33.33, "premium")
        assert resultado == 30.0