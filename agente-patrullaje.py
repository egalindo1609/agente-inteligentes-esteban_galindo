import random
import time

# Definir el entorno
class Entorno:
    def __init__(self, tamaño=10, obstáculos=3):
        self.tamaño = tamaño
        self.ruta = [(i, tamaño // 2) for i in range(tamaño)]  # Ruta central
        self.obstáculos = set(random.sample(self.ruta, obstáculos))  # Colocar obstáculos aleatorios

    def mostrar(self, agente_pos):
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                if (i, j) == agente_pos:
                    print("A", end=" ")  # Agente
                elif (i, j) in self.obstáculos:
                    print("X", end=" ")  # Obstáculo
                else:
                    print(".", end=" ")  # Espacio vacío
            print()
        print("-" * 20)

# Definir el agente reflejo
class AgentePatrulla:
    def __init__(self, entorno):
        self.entorno = entorno
        self.pos = self.entorno.ruta[0]  # Posición inicial
        self.dirección = (1, 0)  # Movimiento hacia abajo

    def mover(self):
        nueva_pos = (self.pos[0] + self.dirección[0], self.pos[1] + self.dirección[1])

        # Si hay obstáculo, cambiar dirección aleatoriamente
        if nueva_pos in self.entorno.obstáculos or nueva_pos[0] >= self.entorno.tamaño:
            self.dirección = random.choice([(-1, 0), (1, 0)])  # Arriba o abajo
        else:
            self.pos = nueva_pos  # Moverse normalmente

    def patrullar(self, pasos=10):
        for _ in range(pasos):
            self.entorno.mostrar(self.pos)
            self.mover()
            time.sleep(0.5)

# Ejecutar simulación
entorno = Entorno()
agente = AgentePatrulla(entorno)
agente.patrullar()
