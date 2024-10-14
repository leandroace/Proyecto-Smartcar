import pygame
import os
import time

class SearchGUI:
    # Clase que se encarga de la interfaz gráfica de búsqueda
    # Atributos:
    # path (str): La ruta del archivo de prueba.
    # search_results: Una lista que contiene los resultados de la búsqueda.
    # Los resultados deben estar en el siguiente orden:
    # - car_moves (list): Lista de movimientos del SmartCar.
    # - tree_nodes (int): Número de nodos del árbol de búsqueda.
    # - expanded_nodes (int): Número de nodos expandidos durante la búsqueda.
    # - depth (int): Profundidad de la solución encontrada.
    # - computation_time (float): Tiempo de cómputo de la búsqueda.
    # - cost (int): Costo de la solución encontrada.
    # algorithm (str): El algoritmo de búsqueda utilizado ('bfs', 'ucs','dfs', 'greedy'. 'astar').
    
        
    def __init__(self, path, search_results, algorithm):

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.empty = pygame.transform.scale(pygame.image.load('./images/empty.png'), (40, 40))
        self.wall = pygame.transform.scale(pygame.image.load('./images/wall.png'), (40, 40))
        self.passenger = pygame.transform.scale(pygame.image.load('./images/passenger.png'), (40, 40))
        self.car = pygame.transform.scale(pygame.image.load('./images/car.png'), (40, 40))
        self.destination = pygame.transform.scale(pygame.image.load('./images/destination.png'), (40, 40))
        self.traffic_medium = pygame.transform.scale(pygame.image.load('./images/traffic_medium.png'), (40, 40))
        self.traffic_heavy = pygame.transform.scale(pygame.image.load('./images/traffic_heavy.png'), (40, 40))
        self.background = pygame.image.load('./images/search_background.png')
        self.screen = pygame.display.set_mode((800, 400))
        self.screen.fill((255, 255, 255))

        # Cargar el archivo de mundo y actualizar la matriz 'tablero'
        with open(path, 'r') as file:
            self.tablero = [list(map(int, line.split())) for line in file.readlines()]

        self.car_moves, self.tree_nodes, self.expanded_nodes, self.depth, self.computation_time, self.cost = search_results

    def draw(self):
        pygame.display.set_caption("Smart Car Search Visualization")
        
        # Definir nuevas fuentes estilizadas
        title_font = pygame.font.SysFont('Verdana', 28, bold=True)  # Fuente para el título
        info_font = pygame.font.SysFont('Verdana', 22)  # Fuente para la información
        
        # Definir nuevos colores
        title_color = (0, 128, 255)  # Azul brillante para el título
        info_color = (34, 139, 34)   # Verde oscuro para la información
        
        # Renderizar los textos con nuevas fuentes y colores
        title = title_font.render('Smart Car Search', True, title_color)
        tree = info_font.render(f'Tree Nodes: {self.tree_nodes}', True, info_color)
        expanded = info_font.render(f'Expanded Nodes: {self.expanded_nodes}', True, info_color)
        depth_title = info_font.render(f'Depth: {self.depth}', True, info_color)
        compute_time_title = info_font.render(f'Computation Time: {round(self.computation_time, 4)}s', True, info_color)
        cost = info_font.render(f'Cost: {self.cost}', True, info_color)
        
        move_index = 0
        velocity = 0.5
        passenger_picked_up = False  # Variable para saber si el pasajero ha sido recogido

        # Variable para controlar si el carro ha llegado a la meta
        car_at_destination = False

        while not car_at_destination:
            self.screen.fill((255, 255, 255))
            for i in range(10):
                for j in range(10):
                    if self.tablero[i][j] == 0:
                        self.screen.blit(self.empty, (j * 40, i * 40))
                    elif self.tablero[i][j] == 1:
                        self.screen.blit(self.wall, (j * 40, i * 40))
                    elif self.tablero[i][j] == 3:
                        self.screen.blit(self.traffic_medium, (j * 40, i * 40))
                    elif self.tablero[i][j] == 4:
                        self.screen.blit(self.traffic_heavy, (j * 40, i * 40))
                    elif self.tablero[i][j] == 5 and not passenger_picked_up:
                        self.screen.blit(self.passenger, (j * 40, i * 40))
                    elif self.tablero[i][j] == 6:
                        self.screen.blit(self.destination, (j * 40, i * 40))

            if move_index < len(self.car_moves):
                move = self.car_moves[move_index]
                self.screen.blit(self.car, (move.column * 40, move.row * 40))

                # Verificar si el carro está en la posición del pasajero
                if self.tablero[move.row][move.column] == 5:
                    passenger_picked_up = True

                # Verificar si el carro ha llegado a la meta
                if self.tablero[move.row][move.column] == 6 and passenger_picked_up:
                    car_at_destination = True  # Detener la animación

                move_index += 1
            else:
                pygame.draw.rect(self.screen, (200, 0, 0), (470, 315, 100, 50))
                pygame.font.SysFont('Arial', 20).render('Back', True, (255, 255, 255))

            self.screen.blit(title, (450, 40))
            self.screen.blit(tree, (450, 100))
            self.screen.blit(expanded, (450, 140))
            self.screen.blit(depth_title, (450, 180))
            self.screen.blit(compute_time_title, (450, 220))
            self.screen.blit(cost, (450, 260))
            pygame.display.flip()
            time.sleep(velocity)

        # Mostrar un mensaje cuando el carro llega al destino
        pygame.display.set_caption("¡El Smart Car ha llegado a su destino!")




