
class SmartCar:
    def __init__(self, world, parent, operator, depth, cost, heuristic):
        self.world = world
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost
        self.current_position = world.start_position
        self.passenger_picked_up = False

    def move(self, new_position):
        self.current_position = new_position
        if self.world.is_passenger(new_position):
            self.pick_up_passenger()

    def pick_up_passenger(self):
        self.passenger_picked_up = True

    def move_up(self):
        return self.current_position.move_up()

    def move_down(self):
        return self.current_position.move_down()

    def move_left(self):
        return self.current_position.move_left()

    def move_right(self):
        return self.current_position.move_right()

    def expand(self, strategy):
        moves = []
        directions = [(self.move_up, 'up'), (self.move_down, 'down'), 
                  (self.move_left, 'left'), (self.move_right, 'right')]
        for move_func, direction in directions:
            new_position = move_func()
            if self.world.is_within_bounds(new_position) and not self.world.is_wall(new_position):
                # Crear un nuevo nodo del carro
                new_smart_car = SmartCar(self.world, self, direction, self.depth + 1, self.cost, None)
                new_smart_car.current_position = new_position

                # Preservar el estado de si el pasajero ha sido recogido
                new_smart_car.passenger_picked_up = self.passenger_picked_up
            
                # Verificar si el nuevo nodo está en la posición del pasajero y recogerlo si es necesario
                if self.world.is_passenger(new_position):
                    new_smart_car.pick_up_passenger()
            
                # Ajustar el costo acumulado dependiendo del tipo de tráfico
                if self.world.is_traffic_medium(new_position):
                    new_smart_car.cost += 4  # Costo de tráfico medio
                elif self.world.is_traffic_heavy(new_position):
                    new_smart_car.cost += 7  # Costo de tráfico pesado
                else:
                    new_smart_car.cost += 1  # Costo de tráfico liviano

                moves.append(new_smart_car)
        return moves





    def heuristic(self):
        if not self.passenger_picked_up:
            # Calculate the Manhattan distance to the passenger
            return self.current_position.manhattan_distance(self.world.passenger_position)
        else:
            # Calculate the Manhattan distance to the destination
            return self.current_position.manhattan_distance(self.world.destination_position)


    def is_at_destination(self):
        return self.passenger_picked_up and self.current_position == self.world.destination_position


    def solution(self):
        path = []
        current = self
        while current.parent is not None:
            path.append(current.current_position)
            current = current.parent
        path.append(current.current_position)
        path.reverse()
        return path

    def __eq__(self, other):
        return isinstance(other, SmartCar) and self.current_position == other.current_position and self.passenger_picked_up == other.passenger_picked_up

    def __hash__(self):
        return hash((self.current_position, self.passenger_picked_up))
