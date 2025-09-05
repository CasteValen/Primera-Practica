import random

opciones = ["piedra", "papel", "tijera"]
rondas_totales = 5
puntos_usuario = 0
puntos_pc = 0
ronda = 1

print(f"¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")
print(f"Se jugará hasta {rondas_totales} rondas o hasta que alguien no pueda ser alcanzado.")

while ronda <= rondas_totales:
    print(f"\nRonda {ronda}")
    
    # Pedir jugada del usuario y validar
    jugada_usuario = input("Tu jugada (piedra/papel/tijera): ").strip().lower()
    if jugada_usuario not in opciones:
        print("Entrada no válida. Debe ser piedra, papel o tijera. Intentalo de nuevo.")
        continue  # no contar la ronda si es inválida

    # Jugada de la computadora
    jugada_pc = random.choice(opciones)
    print(f"La computadora eligió: {jugada_pc}")

    # Comparar jugadas
    if jugada_usuario == jugada_pc:
        print("Empate.")
    elif (
        (jugada_usuario == "piedra" and jugada_pc == "tijera") or
        (jugada_usuario == "papel" and jugada_pc == "piedra") or
        (jugada_usuario == "tijera" and jugada_pc == "papel")
    ):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1
    
    ronda += 1

    # Verificar si alguien ya no puede ser alcanzado
    rondas_restantes = rondas_totales - ronda + 1
    if abs(puntos_usuario - puntos_pc) > rondas_restantes:
        print("Alguien ya no puede ser alcanzado. El juego termina.")
        break

# Resultado final
print("\n=== Resultado final ===")
print(f"Tus puntos: {puntos_usuario} | Puntos de la PC: {puntos_pc}")

if puntos_usuario > puntos_pc:
    print("¡Ganaste el juego! 🎉")
elif puntos_usuario < puntos_pc:
    print("La computadora ganó el juego.")
else:
    print("Empate total.")
