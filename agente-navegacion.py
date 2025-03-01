from collections import deque

class AgenteNavegacion:
    def __init__(self, laberinto, inicio, meta):
        self.laberinto = laberinto
        self.inicio = inicio
        self.meta = meta
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])

    def encontrar_ruta(self):
        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha
        visitado = set()
        cola = deque([(self.inicio, [self.inicio])])  # (posición actual, camino recorrido)

        while cola:
            (x, y), camino = cola.popleft()

            if (x, y) == self.meta:
                return camino  # Ruta más corta encontrada

            for dx, dy in movimientos:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.filas and 0 <= ny < self.columnas and self.laberinto[nx][ny] == 0:
                    if (nx, ny) not in visitado:
                        visitado.add((nx, ny))
                        cola.append(((nx, ny), camino + [(nx, ny)]))

        return None  # No hay ruta a la meta

    def mostrar_ruta(self):
        ruta = self.encontrar_ruta()
        if ruta:
            print("🚀 Ruta más corta encontrada:")
            for paso in ruta:
                print(f"➡ {paso}")
        else:
            print("❌ No se encontró una ruta.")

# Definir el laberinto (5x5)
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]     
]

inicio = (0, 0)
meta = (4, 4)

agente = AgenteNavegacion(laberinto, inicio, meta)
agente.mostrar_ruta()
