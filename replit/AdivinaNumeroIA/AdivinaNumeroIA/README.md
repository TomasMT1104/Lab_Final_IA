# 🎮 Adivina el Número – IA Edition

Un juego interactivo de consola donde debes adivinar un número secreto entre 1 y 100. Recibe pistas inteligentes después de cada intento y compite por el mejor puntaje.

## 📋 Descripción del Proyecto

Este es un microproyecto educativo desarrollado en Python que implementa el clásico juego de adivinar números con características modernas:

- **Sistema de pistas inteligentes**: Recibe orientación sobre qué tan cerca estás del número secreto
- **Sistema de puntuación**: Obtén puntos según tu eficiencia (menos intentos = más puntos)
- **Código modular**: Estructura organizada en módulos separados para facilitar el mantenimiento
- **Validación robusta**: Manejo de errores y validación de entrada del usuario

## 🎯 Características

### Pistas del Juego

El juego proporciona pistas combinadas después de cada intento:

- **Dirección**: "Muy alto" o "Muy bajo"
- **Proximidad**:
  - 🔥 "¡Muy cerca!" (diferencia ≤ 3)
  - 👍 "Cerca" (diferencia ≤ 5)
  - "Relativamente cerca" (diferencia ≤ 10)
  - "Lejos" (diferencia ≤ 20)
  - ❄️ "Muy lejos" (diferencia > 20)

### Sistema de Puntaje

| Intentos | Puntaje | Calificación |
|----------|---------|--------------|
| 1 | 1000 | ¡EXTRAORDINARIO! 🏆 |
| 2-3 | 900 | ¡Excelente! 🌟 |
| 4-5 | 800 | ¡Muy bien! 👏 |
| 6-7 | 700 | ¡Bien hecho! 👍 |
| 8-10 | 600 | Buen trabajo 😊 |
| 11-15 | 500 | No está mal 🙂 |
| 16-20 | 400 | Puedes mejorar 💪 |
| 20+ | 100-390 | Sigue intentando |

## 🗂️ Estructura del Proyecto

```
adivina-numero/
│
├── main.py           # Punto de entrada del juego
├── game_logic.py     # Lógica principal del juego
├── utils.py          # Funciones de utilidad y validación
└── README.md         # Este archivo
```

### Descripción de Módulos

#### `main.py`
Punto de entrada de la aplicación. Maneja:
- Interfaz de usuario
- Flujo del juego
- Mensajes y presentación

#### `game_logic.py`
Contiene la clase `JuegoAdivinaNumero` que gestiona:
- Generación del número secreto
- Evaluación de intentos
- Cálculo de pistas
- Sistema de puntuación
- Estadísticas del juego

#### `utils.py`
Funciones de utilidad que incluyen:
- Validación de entrada del usuario
- Obtención segura de números
- Confirmación de acciones
- Utilidades de consola

## 🚀 Cómo Ejecutar

### Requisitos Previos

- Python 3.6 o superior
- No se requieren dependencias externas (solo biblioteca estándar)

### Instalación y Ejecución

1. **Clona o descarga el proyecto**

2. **Navega al directorio del proyecto**
   ```bash
   cd adivina-numero
   ```

3. **Ejecuta el juego**
   ```bash
   python main.py
   ```
   
   O en sistemas Unix/Linux/Mac:
   ```bash
   python3 main.py
   ```

   O marca el archivo como ejecutable:
   ```bash
   chmod +x main.py
   ./main.py
   ```

## 🎮 Cómo Jugar

1. **Inicio del juego**: Al ejecutar, verás las instrucciones y deberás confirmar que estás listo para comenzar.

2. **Adivina el número**: 
   - Ingresa un número entre 1 y 100
   - Recibirás una pista después de cada intento
   - Continúa hasta adivinar el número correcto

3. **Visualiza tus estadísticas**:
   - Número de intentos
   - Puntaje obtenido
   - Calificación de desempeño
   - Historial de tus intentos

4. **Juega nuevamente**: Puedes jugar tantas veces como quieras

### Ejemplo de Partida

```
🚀 ¡El juego ha comenzado! He pensado en un número entre 1 y 100.

Intento #1 - Ingresa tu número: 50
🔍 Intento #1: Muy alto - Lejos

Intento #2 - Ingresa tu número: 25
🔍 Intento #2: Muy bajo - Relativamente cerca

Intento #3 - Ingresa tu número: 35
🔍 Intento #3: Muy alto - ¡Muy cerca! 🔥

Intento #4 - Ingresa tu número: 33
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
   ¡Correcto! 🎉
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉

📊 ESTADÍSTICAS FINALES
🎯 Número secreto: 33
🔢 Intentos realizados: 4
⭐ Puntaje obtenido: 800 / 1000
🏅 Calificación: ¡Muy bien! 👏
```

## 💻 Características Técnicas

- **Lenguaje**: Python 3
- **Paradigma**: Orientado a Objetos
- **Módulos estándar utilizados**:
  - `random`: Generación de números aleatorios
  - `sys`: Funcionalidades del sistema

## 🧪 Validación de Entrada

El juego incluye validación robusta que maneja:

- ✅ Números fuera del rango (1-100)
- ✅ Entrada no numérica (texto, caracteres especiales)
- ✅ Entrada vacía
- ✅ Confirmaciones de acciones (s/n)

## 🎓 Conceptos de Programación Demostrados

Este proyecto es excelente para aprender:

- Programación orientada a objetos en Python
- Modularización y separación de responsabilidades
- Validación de entrada del usuario
- Manejo de excepciones
- Generación de números aleatorios
- Lógica de juegos
- Documentación de código (docstrings)
- Buenas prácticas de programación

## 🔮 Posibles Mejoras Futuras

- [ ] Agregar niveles de dificultad (fácil, medio, difícil)
- [ ] Implementar tabla de récords persistente
- [ ] Modo multijugador por turnos
- [ ] Interfaz gráfica con Tkinter
- [ ] Sistema de logros y medallas
- [ ] Estadísticas acumuladas del jugador
- [ ] Temporizador para añadir desafío adicional
- [ ] Modo "contra la IA" (la IA también adivina)

## 📝 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

## 👨‍💻 Autor

Creado con ❤️ por Replit Agent

---

**¡Disfruta el juego y que tengas suerte adivinando! 🎲**
