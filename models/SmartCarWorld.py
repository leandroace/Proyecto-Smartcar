
from .SmartCarPosition import Position

class World:
    def __init__(self, file):
        """
        Inicializa una instancia de la clase World.

        Parámetros:
        - file: Ruta del archivo que contiene la matriz del mundo.

        Atributos:
        - matrix: Matriz que representa el mundo.
        - dimension: Tupla que indica las dimensiones de la matriz (filas, columnas).
        - start_position: Posición de inicio en el mundo.
        - passenger_position: Posición del pasajero en el mundo.
        - destination_position: Posición del destino en el mundo.
        - traffic_medium: Lista de posiciones con tráfico medio en el mundo.
        - traffic_heavy: Lista de posiciones con tráfico pesado en el mundo.
        """
        self.matrix = None
        self.dimension = (0, 0)
        self.start_position = None
        self.passenger_position = None
        self.destination_position = None
        self.traffic_medium = []
        self.traffic_heavy = []

        with open(file, 'r') as f:
            self.matrix = [[int(num) for num in line.split()] for line in f.readlines()]
            self.dimension = (len(self.matrix), len(self.matrix[0]))
            for i in range(self.dimension[0]):
                for j in range(self.dimension[1]):
                    if self.matrix[i][j] == 2:
                        self.start_position = Position(i, j)
                    elif self.matrix[i][j] == 3:
                        self.traffic_medium.append(Position(i, j))
                    elif self.matrix[i][j] == 4:
                        self.traffic_heavy.append(Position(i, j))
                    elif self.matrix[i][j] == 5:
                        self.passenger_position = Position(i, j)
                    elif self.matrix[i][j] == 6:
                        self.destination_position = Position(i, j)

    def get_tile(self, position):
        """
        Devuelve el valor de la casilla en la posición dada.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - El valor de la casilla en la posición dada.
        """
        return self.matrix[position.row][position.column]

    def is_empty(self, position):
        """
        Verifica si la casilla en la posición dada está vacía (tráfico liviano).

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - True si la casilla está vacía, False de lo contrario.
        """
        return self.get_tile(position) == 0

    def is_passenger(self, position):
        """
        Verifica si la posición dada contiene al pasajero.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - True si la posición contiene al pasajero, False de lo contrario.
        """
        return position == self.passenger_position

    def is_destination(self, position):
        """
        Verifica si la posición dada contiene el destino.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - True si la posición contiene el destino, False de lo contrario.
        """
        return position == self.destination_position

    def is_traffic_medium(self, position):
        """
        Verifica si la casilla en la posición dada tiene tráfico medio.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - True si la casilla tiene tráfico medio, False de lo contrario.
        """
        return position in self.traffic_medium

    def is_traffic_heavy(self, position):
        """
        Verifica si la casilla en la posición dada tiene tráfico pesado.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - True si la casilla tiene tráfico pesado, False de lo contrario.
        """
        return position in self.traffic_heavy

    def is_wall(self, position):
        """
        Verifica si la casilla en la posición dada es una pared.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - True si la casilla es una pared, False de lo contrario.
        """
        return self.get_tile(position) == 1

    def is_within_bounds(self, position):
        """
        Verifica si la posición dada está dentro de los límites del mundo.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - True si la posición está dentro de los límites del mundo, False de lo contrario.
        """
        return position.is_within(self.dimension)
