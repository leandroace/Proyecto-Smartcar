
class Position:
    #Crea una nueva instancia de la clase Position.
    #Args: row (int): La fila de la posición.
    #column (int): La columna de la posición.
    def __init__(self, row, column):
        self.row = row
        self.column = column

    #Mueve la posición hacia arriba.
    #Returns: Position: La nueva posición después de mover hacia arriba.
    def move_up(self):
        return Position(self.row - 1, self.column)

    #Mueve la posición hacia abajo.
    #Returns: Position: La nueva posición después de mover hacia abajo.
    def move_down(self):
        return Position(self.row + 1, self.column)

    #Mueve la posición hacia la izquierda.
    #Returns: Position: La nueva posición después de mover hacia la izquierda.    
    def move_left(self):
        return Position(self.row, self.column - 1)

    #Mueve la posición hacia la derecha.
    #Returns: Position: La nueva posición después de mover hacia la derecha.
    def move_right(self):
        return Position(self.row, self.column + 1)

    #Verifica si la posición está dentro de los límites de una dimensión dada.
    #Args: dimension (tuple): Una tupla que representa las dimensiones (filas, columnas).
    #Returns: bool: True si la posición está dentro de los límites, False de lo contrario.
    
    def is_within(self, dimension):
        filas, columnas = dimension
        return 0 <= self.row < filas and 0 <= self.column < columnas

    #Calcula la distancia de Manhattan entre dos posiciones.
    #Args: other (Position): La otra posición.
    #Returns: int: La distancia de Manhattan entre las dos posiciones.
    def manhattan_distance(self, other):
        return abs(self.row - other.row) + abs(self.column - other.column)
    
    #Verifica si la posición es una pared.
    #Args: world (World): El mundo que contiene las posiciones.
    #Returns: bool: True si es una pared, False en caso contrario.    
    def is_traffic_light(self, world):
        return world.grid[self.row][self.column] == 0

    #Verifica si la posición tiene tráfico ligero.
    #Args: world (World): El mundo que contiene las posiciones.
    #Returns: bool: True si es tráfico ligero, False en caso contrario.
    def is_traffic_medium(self, world):
        return world.grid[self.row][self.column] == 3

    #Verifica si la posición tiene tráfico pesado.
    #Args: world (World): El mundo que contiene las posiciones.
    #Returns: bool: True si es tráfico pesado, False en caso contrario.
    def is_traffic_heavy(self, world):
        return world.grid[self.row][self.column] == 4

    #Verifica si la posición es una pared.
    #Args: world (World): El mundo que contiene las posiciones.
    #Returns: bool: True si es una pared, False en caso contrario.
    def __eq__(self, other):
        return isinstance(other, Position) and self.row == other.row and self.column == other.column
 
    #Calcula el hash de la posición.
    #Returns: int: El hash de la posición. 
    def __hash__(self):
        return hash((self.row, self.column))

    #Devuelve una representación en cadena de la posición.
    #Returns: str: La representación en cadena de la posición
    def __repr__(self):
        return f"({self.row}, {self.column})"
