# Proyecto de Integracion: Precios y Descuentos

Este proyecto muestra una integracion simple entre dos modulos de negocio:

- `descuentos.py`: define el porcentaje de descuento por tipo de cliente.
- `precios.py`: calcula el precio final aplicando el descuento correspondiente.

Incluye pruebas de integracion con `pytest` para validar los flujos principales y casos de error.

## Funcionalidad

### Tipos de cliente soportados

- `regular`: 0% de descuento
- `premium`: 10% de descuento
- `vip`: 20% de descuento

### Regla de calculo

Precio final:

```text
precio_final = round(precio_base * (1 - descuento), 2)
```

Validaciones:

- Si `precio_base` es negativo, se lanza `ValueError`.
- Si `tipo_cliente` no existe, se lanza `ValueError`.

## Estructura del proyecto

```text
proyecto_integracion/
|-- pytest.ini
|-- requirements.txt
|-- src/
|   |-- __init__.py
|   |-- descuentos.py
|   `-- precios.py
`-- tests/
    |-- __init__.py
    `-- test_integracion.py
```

## Requisitos

- Python 3.10 o superior
- pip

Dependencias del proyecto:

- `pytest==8.1.1`
- `pytest-cov==5.0.0`

## Instalacion

Desde la raiz del proyecto:

```bash
python -m venv .venv
```

Activar entorno virtual:

```bash
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar pruebas

El archivo `pytest.ini` ya configura:

- `testpaths = tests`
- `pythonpath = src`
- `addopts = -v --tb=short`

Para correr las pruebas:

```bash
pytest
```

Con cobertura:

```bash
pytest --cov=src --cov-report=term-missing
python -m pytest --cov=src --cov-report=term-missing
```
Opción 2 — panel visual de Testing en VS Code
1. Ctrl+Shift+P → "Python: Configure Tests"
2. Selecciona "pytest"
3. Selecciona la carpeta raíz del proyecto
4. Clic en el ícono de matraz (Testing) en la barra lateral
5. En todas las pruebas listadas —>  clic en ▶ para correr

## Ejemplo de uso

Opcion 1: ejecutar desde la carpeta `src`.

```bash
cd src
python -c "from precios import calcular_precio_final; print(calcular_precio_final(200.0, 'premium'))"
```

Salida esperada:

```text
180.0
```

Opcion 2: desde la raiz, agregando `src` al `PYTHONPATH`.

```bash
# Windows PowerShell
$env:PYTHONPATH = "src"
python -c "from precios import calcular_precio_final; print(calcular_precio_final(50.0, 'vip'))"
```

## Casos cubiertos por las pruebas

- Cliente regular sin descuento
- Cliente premium con 10%
- Cliente vip con 20%
- Precio base cero
- Tipo de cliente invalido
- Precio negativo
- Redondeo a 2 decimales

## Proposito

Este repositorio sirve como ejemplo de integracion entre modulos Python y como base para practicar pruebas automatizadas en escenarios de negocio simples.
