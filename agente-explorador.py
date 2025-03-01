import random
import time

class Mapa:
    def __init__(self, tamaño=5):
        self.tamaño = tamaño
        self.matriz = [['.' for _ in range(tamaño)] for _ in range(tamaño)]

    def mostrar(self, agente_pos):
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                if (i, j) == agente_pos:
                    print("A", end=" ")
                else:
                    print(self.matriz[i][j], end=" ")
            print()
        print("-" * 10)

class AgenteExplorador:
    def __init__(self, mapa):
        self.mapa = mapa
        self.pos = (0, 0)  # Empieza en la esquina superior izquierda
        self.visitados = set()  # Guarda lugares visitados

    def obtener_movimientos(self):
        x, y = self.pos
        posibles = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [(nx, ny) for nx, ny in posibles if 0 <= nx < self.mapa.tamaño and 0 <= ny < self.mapa.tamaño and (nx, ny) not in self.visitados]

    def mover(self):
        self.visitados.add(self.pos)
        movimientos = self.obtener_movimientos()

        if movimientos:
            self.pos = random.choice(movimientos)  # Moverse a un lugar no visitado

    def explorar(self, pasos=10):
        for _ in range(pasos):
            self.mapa.mostrar(self.pos)
            self.mover()
            time.sleep(0.5)

# Ejecutar exploración
mapa = Mapa()    
agente = AgenteExplorador(mapa)
agente.explorar()
