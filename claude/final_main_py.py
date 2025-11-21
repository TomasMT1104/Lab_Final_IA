"""
Módulo principal del proyecto.

Este módulo procesa una lista de números y calcula sus cuadrados
utilizando operaciones matemáticas del módulo math_operations.
"""

import logging
import sys
from typing import List

from config import DEFAULT_DATA, LOG_FORMAT, LOG_LEVEL
from math_operations import square_number

# Configuración de logging
logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log')
    ]
)

logger = logging.getLogger(__name__)


def process_numbers(data: List[int | float]) -> List[int | float]:
    """
    Procesa una lista de números y calcula sus cuadrados.

    Args:
        data: Lista de números (int o float) a procesar.

    Returns:
        Lista con los cuadrados de los números de entrada.

    Raises:
        ValueError: Si la lista está vacía o contiene valores no numéricos.
        TypeError: Si el argumento no es una lista.

    Examples:
        >>> process_numbers([1, 2, 3])
        [1, 4, 9]
        >>> process_numbers([2.5, 3.5])
        [6.25, 12.25]
    """
    if not isinstance(data, list):
        logger.error(f"Se esperaba una lista, se recibió: {type(data)}")
        raise TypeError("El argumento debe ser una lista")

    if not data:
        logger.warning("La lista de datos está vacía")
        raise ValueError("La lista no puede estar vacía")

    # Validar que todos los elementos sean numéricos
    for i, value in enumerate(data):
        if not isinstance(value, (int, float)):
            logger.error(f"Valor no numérico en índice {i}: {value}")
            raise ValueError(
                f"Todos los elementos deben ser números. "
                f"Valor inválido en índice {i}: {value}"
            )

    logger.info(f"Procesando {len(data)} números")
    
    # List comprehension: más eficiente y pythonic
    result = [square_number(x) for x in data]
    
    logger.info(f"Procesamiento completado exitosamente")
    return result


def main() -> None:
    """
    Función principal del programa.

    Ejecuta el procesamiento de números y muestra los resultados.
    Maneja errores de forma robusta con logging apropiado.
    """
    try:
        logger.info("Iniciando aplicación")
        
        # Usar datos de configuración
        data = DEFAULT_DATA
        logger.debug(f"Datos de entrada: {data}")
        
        # Procesar números
        result = process_numbers(data)
        
        # Mostrar resultados
        print(f"Números originales: {data}")
        print(f"Cuadrados calculados: {result}")
        
        logger.info("Aplicación finalizada exitosamente")
        
    except ValueError as e:
        logger.error(f"Error de validación: {e}")
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
        
    except TypeError as e:
        logger.error(f"Error de tipo: {e}")
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
        
    except Exception as e:
        logger.critical(f"Error inesperado: {e}", exc_info=True)
        print(f"❌ Error crítico: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()