
from .SmartCarPosition import Position

class World:
    #Clase que representa el mundo en el que se mueve el carro.
    #Atributos:
    # - matrix (list): Una matriz que representa el mundo.
    # - dimension (tuple): Una tupla que representa las dimensiones de la matriz (filas, columnas).
    # - start_position (Position): La posición de inicio en el mundo.
    # - passenger_position (Position): La posición del pasajero en el mundo.
    # - destination_position (Position): La posición del destino en el mundo.
    # - traffic_medium (list): Una lista de posiciones con tráfico medio en el mundo.
    # - traffic_heavy (list): Una lista de posiciones con tráfico pesado en el mundo.
    
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

# Devuelve el valor de la casilla en la posición dada.
# Parámetros:
# - position: Posición en el mundo.
# Retorna:
# - El valor de la casilla en la posición dada.
    def get_tile(self, position):
        return self.matrix[position.row][position.column]
    
    

# Verifica si la casilla en la posición dada está vacía (tráfico liviano).
# Parámetros:
# - position: Posición en el mundo.
# Retorna:
# - True si la casilla está vacía, False de lo contrario.
    def is_empty(self, position):
        return self.get_tile(position) == 0



# Verifica si la posición dada contiene al pasajero.
# Parámetros:
# - position: Posición en el mundo.
# Retorna:
# - True si la posición contiene al pasajero, False de lo contrario.
    def is_passenger(self, position):
        return position == self.passenger_position



# Verifica si la posición dada contiene el destino.
# Parámetros:
# - position: Posición en el mundo.
# Retorna:
# - True si la posición contiene el destino, False de lo contrario.
    def is_destination(self, position):
        return position == self.destination_position



# Verifica si la casilla en la posición dada tiene tráfico medio.
# Parámetros:
# - position: Posición en el mundo.
# Retorna:
# - True si la casilla tiene tráfico medio, False de lo contrario.
    def is_traffic_medium(self, position):
        return position in self.traffic_medium



# Verifica si la casilla en la posición dada tiene tráfico pesado.
# Parámetros:
# - position: Posición en el mundo.
# Retorna:
# - True si la casilla tiene tráfico pesado, False de lo contrario.

    def is_traffic_heavy(self, position):
        return position in self.traffic_heavy



# Verifica si la casilla en la posición dada es una pared.
# Parámetros:
# - position: Posición en el mundo.
# Retorna:
# - True si la casilla es una pared, False de lo contrario.
    def is_wall(self, position):

        return self.get_tile(position) == 1


# Verifica si la posición dada está dentro de los límites del mundo.
# Parámetros:
# - position: Posición en el mundo.
# Retorna:
# - True si la posición está dentro de los límites del mundo, False de lo contrario.
    def is_within_bounds(self, position):
        return position.is_within(self.dimension)
