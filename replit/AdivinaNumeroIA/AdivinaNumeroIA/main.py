#!/usr/bin/env python3
"""
Adivina el Número – IA Edition
Un juego interactivo de consola donde el jugador debe adivinar un número secreto.

Autor: Replit Agent
Fecha: 2025
"""

from game_logic import JuegoAdivinaNumero
from utils import obtener_numero_usuario, confirmar_accion, limpiar_pantalla


def mostrar_bienvenida():
    """
    Muestra el mensaje de bienvenida y las instrucciones del juego.
    """
    print("=" * 60)
    print(" " * 15 + "🎮 ADIVINA EL NÚMERO – IA EDITION 🎮")
    print("=" * 60)
    print()
    print("📋 INSTRUCCIONES:")
    print("   • Adivina el número secreto entre 1 y 100")
    print("   • Recibirás pistas después de cada intento")
    print("   • Menos intentos = Mayor puntaje")
    print()
    print("💡 PISTAS:")
    print("   • 'Muy alto' o 'Muy bajo': dirección del número")
    print("   • 'Cerca' (±10): estás cerca del número")
    print("   • 'Lejos': estás lejos del número")
    print()
    print("=" * 60)
    print()


def mostrar_resultado_intento(resultado, intento_num):
    """
    Muestra el resultado de un intento del jugador.
    
    Args:
        resultado (dict): Resultado del intento
        intento_num (int): Número del intento actual
    """
    if resultado['correcto']:
        print()
        print("🎉" * 20)
        print(f"   {resultado['pista']}")
        print("🎉" * 20)
        print()
    else:
        print(f"\n🔍 Intento #{intento_num}: {resultado['pista']}")
        print()


def mostrar_estadisticas_finales(juego):
    """
    Muestra las estadísticas finales del juego.
    
    Args:
        juego (JuegoAdivinaNumero): Instancia del juego
    """
    stats = juego.obtener_estadisticas()
    
    print()
    print("=" * 60)
    print(" " * 20 + "📊 ESTADÍSTICAS FINALES")
    print("=" * 60)
    print(f"🎯 Número secreto: {stats['numero_secreto']}")
    print(f"🔢 Intentos realizados: {stats['intentos']}")
    print(f"⭐ Puntaje obtenido: {stats['puntaje']} / 1000")
    print(f"🏅 Calificación: {stats['calificacion']}")
    print()
    
    if len(stats['historial']) > 1:
        print(f"📝 Historial de intentos: {', '.join(map(str, stats['historial']))}")
        print()
    
    print("=" * 60)
    print()


def jugar_partida():
    """
    Ejecuta una partida completa del juego.
    
    Returns:
        bool: True si el jugador quiere jugar otra vez, False en caso contrario
    """
    # Crear nueva instancia del juego
    juego = JuegoAdivinaNumero(minimo=1, maximo=100)
    
    print("🚀 ¡El juego ha comenzado! He pensado en un número entre 1 y 100.")
    print()
    
    # Bucle principal del juego
    while not juego.juego_terminado:
        # Obtener el número del usuario
        numero = obtener_numero_usuario(
            f"Intento #{juego.intentos + 1} - Ingresa tu número: ",
            juego.minimo,
            juego.maximo
        )
        
        # Evaluar el intento
        resultado = juego.evaluar_intento(numero)
        
        # Mostrar resultado
        mostrar_resultado_intento(resultado, juego.intentos)
    
    # Mostrar estadísticas finales
    mostrar_estadisticas_finales(juego)
    
    # Preguntar si quiere jugar otra vez
    return confirmar_accion("¿Quieres jugar otra vez?")


def main():
    """
    Función principal que controla el flujo del programa.
    """
    # Mostrar mensaje de bienvenida
    mostrar_bienvenida()
    
    # Preguntar si está listo para comenzar
    if not confirmar_accion("¿Estás listo para comenzar?"):
        print("\n👋 ¡Hasta luego! Vuelve cuando quieras jugar.\n")
        return
    
    print()
    limpiar_pantalla()
    
    # Bucle principal de partidas
    jugar_otra_vez = True
    
    while jugar_otra_vez:
        jugar_otra_vez = jugar_partida()
        
        if jugar_otra_vez:
            print()
            limpiar_pantalla()
            print("🎮 ¡Nueva partida!\n")
    
    # Mensaje de despedida
    print()
    print("=" * 60)
    print(" " * 15 + "👋 ¡Gracias por jugar!")
    print(" " * 10 + "Creado con ❤️  por Replit Agent")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
