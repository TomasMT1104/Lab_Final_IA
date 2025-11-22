"""
Módulo de lógica del juego "Adivina el Número – IA Edition".
Contiene la lógica principal del juego, generación de números y evaluación de intentos.
"""

import random


class JuegoAdivinaNumero:
    """
    Clase que maneja la lógica del juego de adivinar el número.
    """
    
    def __init__(self, minimo=1, maximo=100):
        """
        Inicializa un nuevo juego.
        
        Args:
            minimo (int): Número mínimo del rango (por defecto 1)
            maximo (int): Número máximo del rango (por defecto 100)
        """
        self.minimo = minimo
        self.maximo = maximo
        self.numero_secreto = self.generar_numero_secreto()
        self.intentos = 0
        self.historial = []
        self.juego_terminado = False
    
    def generar_numero_secreto(self):
        """
        Genera un número secreto aleatorio dentro del rango especificado.
        
        Returns:
            int: Número aleatorio entre minimo y maximo (inclusive)
        """
        return random.randint(self.minimo, self.maximo)
    
    def evaluar_intento(self, numero):
        """
        Evalúa el intento del jugador y genera pistas.
        
        Args:
            numero (int): El número que el jugador está adivinando
        
        Returns:
            dict: Diccionario con información sobre el intento:
                - 'correcto': bool, si adivinó el número
                - 'pista': str, la pista generada
                - 'diferencia': int, diferencia absoluta con el número secreto
        """
        self.intentos += 1
        self.historial.append(numero)
        
        diferencia = abs(numero - self.numero_secreto)
        
        if numero == self.numero_secreto:
            self.juego_terminado = True
            return {
                'correcto': True,
                'pista': '¡Correcto! 🎉',
                'diferencia': 0
            }
        
        # Generar pista combinada
        pista = self.generar_pista(numero, diferencia)
        
        return {
            'correcto': False,
            'pista': pista,
            'diferencia': diferencia
        }
    
    def generar_pista(self, numero, diferencia):
        """
        Genera una pista basada en la diferencia entre el número y el secreto.
        
        Args:
            numero (int): El número adivinado
            diferencia (int): Diferencia absoluta con el número secreto
        
        Returns:
            str: La pista generada
        """
        # Determinar si es muy alto o muy bajo
        direccion = "Muy alto" if numero > self.numero_secreto else "Muy bajo"
        
        # Determinar si está cerca o lejos (±10 se considera "cerca")
        proximidad = "Cerca" if diferencia <= 10 else "Lejos"
        
        # Pistas extra para mejorar la experiencia
        if diferencia <= 3:
            proximidad = "¡Muy cerca! 🔥"
        elif diferencia <= 5:
            proximidad = "Cerca 👍"
        elif diferencia <= 10:
            proximidad = "Relativamente cerca"
        elif diferencia <= 20:
            proximidad = "Lejos"
        else:
            proximidad = "Muy lejos ❄️"
        
        return f"{direccion} - {proximidad}"
    
    def calcular_puntaje(self):
        """
        Calcula el puntaje basado en el número de intentos.
        Menos intentos = mayor puntaje.
        
        Returns:
            int: El puntaje obtenido (0-1000)
        """
        if not self.juego_terminado:
            return 0
        
        # Puntaje base de 1000, se reduce según intentos
        if self.intentos == 1:
            return 1000  # Puntaje perfecto
        elif self.intentos <= 3:
            return 900
        elif self.intentos <= 5:
            return 800
        elif self.intentos <= 7:
            return 700
        elif self.intentos <= 10:
            return 600
        elif self.intentos <= 15:
            return 500
        elif self.intentos <= 20:
            return 400
        else:
            # A partir de 20 intentos, se va reduciendo gradualmente
            puntaje = max(100, 400 - (self.intentos - 20) * 10)
            return puntaje
    
    def obtener_calificacion(self):
        """
        Obtiene una calificación cualitativa basada en el puntaje.
        
        Returns:
            str: Calificación del desempeño
        """
        puntaje = self.calcular_puntaje()
        
        if puntaje >= 900:
            return "¡EXTRAORDINARIO! 🏆"
        elif puntaje >= 800:
            return "¡Excelente! 🌟"
        elif puntaje >= 700:
            return "¡Muy bien! 👏"
        elif puntaje >= 600:
            return "¡Bien hecho! 👍"
        elif puntaje >= 500:
            return "Buen trabajo 😊"
        elif puntaje >= 400:
            return "No está mal 🙂"
        else:
            return "Puedes mejorar 💪"
    
    def obtener_estadisticas(self):
        """
        Obtiene las estadísticas del juego actual.
        
        Returns:
            dict: Diccionario con las estadísticas del juego
        """
        return {
            'intentos': self.intentos,
            'puntaje': self.calcular_puntaje(),
            'calificacion': self.obtener_calificacion(),
            'historial': self.historial.copy(),
            'numero_secreto': self.numero_secreto if self.juego_terminado else None
        }
    
    def reiniciar(self):
        """
        Reinicia el juego para una nueva partida.
        """
        self.numero_secreto = self.generar_numero_secreto()
        self.intentos = 0
        self.historial = []
        self.juego_terminado = False
