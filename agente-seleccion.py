import numpy as np    

class AgenteSeleccionRuta:
    def __init__(self, entorno):
        self.entorno = np.array(entorno)  # Matriz de recompensas
        self.filas, self.columnas = self.entorno.shape
        self.posicion_inicial = (0, 0)  # El agente comienza en la esquina superior izquierda
        self.posicion_meta = (self.filas - 1, self.columnas - 1)  # La meta es la esquina inferior derecha

    def encontrar_mejor_ruta(self):
        # Usaremos programación dinámica para encontrar la mejor ruta basada en utilidad
        dp = np.zeros((self.filas, self.columnas))
        ruta = np.full((self.filas, self.columnas), None)

        # Llenamos la matriz de DP con los valores óptimos
        for i in range(self.filas):
            for j in range(self.columnas):
                if i == 0 and j == 0:
                    dp[i][j] = self.entorno[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + self.entorno[i][j]
                    ruta[i][j] = (i, j - 1)
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + self.entorno[i][j]
                    ruta[i][j] = (i - 1, j)
                else:
                    if dp[i - 1][j] > dp[i][j - 1]:
                        dp[i][j] = dp[i - 1][j] + self.entorno[i][j]
                        ruta[i][j] = (i - 1, j)
                    else:
                        dp[i][j] = dp[i][j - 1] + self.entorno[i][j]
                        ruta[i][j] = (i, j - 1)

        # Reconstruimos la mejor ruta desde la meta hasta el inicio
        mejor_camino = []
        actual = self.posicion_meta
        while actual is not None:
            mejor_camino.append(actual)
            actual = ruta[actual]

        mejor_camino.reverse()  # Para que vaya de inicio a meta
        return mejor_camino, dp[-1, -1]

    def mostrar_ruta(self):
        ruta, utilidad = self.encontrar_mejor_ruta()
        print(f"🚀 Mejor ruta encontrada con utilidad total {utilidad}:")
        for paso in ruta:
            print(f"➡ {paso}")


# Ejemplo de entorno con valores de recompensa
entorno = [
    [3, 2, 1, 4],
    [1, 5, 2, 3],
    [4, 2, 8, 1],
    [2, 3, 4, 7]
]

agente = AgenteSeleccionRuta(entorno)
agente.mostrar_ruta()
