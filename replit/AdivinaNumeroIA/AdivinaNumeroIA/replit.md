# Overview

Este es un juego interactivo de consola "Adivina el Número – IA Edition" construido en Python. Los jugadores intentan adivinar un número secreto entre 1 y 100, recibiendo pistas inteligentes después de cada intento. El juego cuenta con un sistema de puntuación que premia la eficiencia (menos intentos = mayor puntaje) y proporciona retroalimentación basada en proximidad para guiar a los jugadores hacia la respuesta correcta.

# User Preferences

Estilo de comunicación preferido: Lenguaje simple y cotidiano.

# System Architecture

## Tipo de Aplicación
Aplicación de consola en Python con diseño modular orientado a objetos.

## Patrón de Arquitectura Principal
La aplicación sigue un patrón de **separación de responsabilidades** con tres módulos distintos:

1. **Módulo de Lógica del Juego (`game_logic.py`)**: Encapsula la mecánica central del juego en una clase `JuegoAdivinaNumero`
   - Genera números secretos aleatorios
   - Rastrea el estado del juego (intentos, historial, estado de finalización)
   - Evalúa las suposiciones del jugador y genera pistas contextuales
   - **Razón**: Aislar la lógica del juego facilita las pruebas, modificaciones y posibles adiciones de funcionalidades

2. **Módulo de Utilidades (`utils.py`)**: Maneja la validación de entrada y ayudas de interacción del usuario
   - Valida entrada numérica dentro de rangos especificados
   - Proporciona funciones reutilizables de recolección de entrada
   - **Razón**: Centralizar la lógica de validación previene duplicación de código y asegura manejo consistente de errores

3. **Módulo Principal (`main.py`)**: Orquesta el flujo del juego y la interfaz de usuario
   - Muestra mensajes de bienvenida e instrucciones
   - Gestiona el bucle del juego y las interacciones del usuario
   - Formatea y presenta los resultados del juego
   - **Razón**: Separar la presentación de la lógica permite cambios en la UI sin tocar la funcionalidad central

## Mecánicas del Juego

### Sistema de Pistas
Proporciona retroalimentación bidimensional:
- **Direccional**: "Muy alto" (muy alto) / "Muy bajo" (muy bajo)
- **Basada en proximidad**: Los umbrales de distancia activan diferentes mensajes de proximidad (≤3: "¡Muy cerca!", ≤5: "Cerca", ≤10: "Relativamente cerca", ≤20: "Lejos", >20: "Muy lejos")

### Algoritmo de Puntuación
Inversamente proporcional a los intentos realizados. Los niveles de puntuación van desde 1000 puntos (1 intento) hasta 100-390 puntos (20+ intentos), fomentando las suposiciones estratégicas.

## Flujo de Datos
1. El usuario ingresa una suposición → `utils.obtener_numero_usuario()`
2. Validación → `utils.validar_numero()`
3. Evaluación del juego → `JuegoAdivinaNumero.evaluar_intento()`
4. Visualización del resultado → `main.mostrar_resultado_intento()`

## Decisiones de Diseño

**Solo Biblioteca Estándar de Python**: Usa únicamente módulos integrados (`random` para generación de números). Sin dependencias externas simplifica la implementación y reduce la complejidad para propósitos educativos.

**Estado del Juego Basado en Clases**: La clase `JuegoAdivinaNumero` mantiene un estado encapsulado (número secreto, intentos, historial), facilitando la instanciación de múltiples juegos o la adición de características como niveles de dificultad.

**Separación de Validación**: La validación de entrada devuelve tuplas `(válido, valor, mensaje_de_error)` para manejo explícito de errores, facilitando la depuración y la retroalimentación al usuario.

# Dependencias Externas

## Módulos de la Biblioteca Estándar
- **random**: Genera números aleatorios criptográficamente no seguros para la generación del número secreto del juego

## Sin Servicios Externos
Esta aplicación se ejecuta completamente de forma local sin:
- Conexiones a bases de datos
- Integraciones de API
- Bibliotecas de terceros
- Requisitos de red
- Autenticación externa

La aplicación es completamente autónoma y solo requiere un intérprete de Python 3 para ejecutarse.

# Recent Changes

**2025-11-22**: Proyecto inicial creado con estructura modular completa
- Implementados los módulos `main.py`, `game_logic.py` y `utils.py`
- Creado sistema de pistas con 5 niveles de proximidad
- Implementado sistema de puntuación con 7 rangos diferentes
- Agregado README.md completo con instrucciones de uso
- Configurado workflow de ejecución del juego
- Agregado .gitignore para Python
