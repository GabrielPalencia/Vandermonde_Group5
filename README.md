# Vandermonde Group 5

## Introducción

Este proyecto realiza la interpolación de puntos utilizando el método de la matriz de Vandermonde.

###
Integrantes:
*   Kidman Cabana Perez
*   Nelson Diaz Pizarro
*   Gabriel Palencia Cure
*   Presly Romero Col
*   Jose Ferrer Vidal

## Instalación

En la terminal de comandos donde desee instalarlo ejecutar la siguiente línea:
pip install git+https://github.com/GabrielPalencia/Vandermonde_Group5.git


## Requisitos

- Lista de listas con puntos (x, y)
- Mínimo dos puntos para realizar la interpolación

## Uso

1. Proporcione una lista de puntos en el formato `[[x1, y1], [x2, y2], ...]`.
2. Asegúrese de que la lista contenga al menos dos puntos.
3. Ejecute el script para obtener el polinomio interpolador.

## Ejemplo

```python
from vandermonde_lib import Vandermonde

set_of_points = [
    [1, 2],
    [2, 3],
    [3, 5],
    [4, 8],
    [5, 12]
]
polynomial = Vandermonde(set_of_points)
print(polynomial)

# Código para realizar la interpolación
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue o envíe un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.
