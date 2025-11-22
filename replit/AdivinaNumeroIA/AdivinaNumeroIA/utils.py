"""
Módulo de utilidades para el juego "Adivina el Número".
Contiene funciones de validación de entrada del usuario.
"""

def validar_numero(entrada, minimo=1, maximo=100):
    """
    Valida que la entrada del usuario sea un número entero dentro del rango especificado.
    
    Args:
        entrada (str): La entrada del usuario como cadena de texto
        minimo (int): El valor mínimo permitido (por defecto 1)
        maximo (int): El valor máximo permitido (por defecto 100)
    
    Returns:
        tuple: (bool, int o None, str) 
               - True/False indicando si es válido
               - El número convertido o None si es inválido
               - Mensaje de error si aplica
    
    Ejemplos:
        >>> validar_numero("50", 1, 100)
        (True, 50, "")
        >>> validar_numero("abc", 1, 100)
        (False, None, "Por favor, ingresa un número válido.")
    """
    try:
        numero = int(entrada)
        
        if numero < minimo or numero > maximo:
            return (False, None, f"El número debe estar entre {minimo} y {maximo}.")
        
        return (True, numero, "")
    
    except ValueError:
        return (False, None, "Por favor, ingresa un número válido.")


def obtener_numero_usuario(mensaje, minimo=1, maximo=100):
    """
    Solicita un número al usuario y valida la entrada.
    Continúa solicitando hasta obtener un número válido.
    
    Args:
        mensaje (str): El mensaje a mostrar al usuario
        minimo (int): El valor mínimo permitido (por defecto 1)
        maximo (int): El valor máximo permitido (por defecto 100)
    
    Returns:
        int: El número válido ingresado por el usuario
    """
    while True:
        entrada = input(mensaje)
        valido, numero, error = validar_numero(entrada, minimo, maximo)
        
        if valido:
            return numero
        else:
            print(f"❌ {error}")


def confirmar_accion(mensaje):
    """
    Solicita confirmación del usuario para una acción.
    
    Args:
        mensaje (str): El mensaje de confirmación a mostrar
    
    Returns:
        bool: True si el usuario confirma (s/S), False en caso contrario
    """
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        
        if respuesta in ['s', 'si', 'sí', 'yes', 'y']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print("Por favor, responde 's' para sí o 'n' para no.")


def limpiar_pantalla():
    """
    Imprime líneas en blanco para simular limpieza de pantalla.
    Compatible con todos los sistemas operativos.
    """
    print("\n" * 50)
