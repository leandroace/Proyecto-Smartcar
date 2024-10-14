import pygame
import os
import time

class SearchGUI:
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

        # Ajustar el tamaño de la pantalla al tamaño del tablero
        self.screen = pygame.display.set_mode((400, 400))  # Cambia el tamaño según sea necesario
        self.screen.fill((200, 200, 200))  # Color de fondo gris claro

        # Cargar el archivo de mundo y actualizar la matriz 'tablero'
        with open(path, 'r') as file:
            self.tablero = [list(map(int, line.split())) for line in file.readlines()]

        self.car_moves, self.tree_nodes, self.expanded_nodes, self.depth, self.computation_time, self.cost = search_results
        self.algorithm = algorithm

        # Inicializar fuentes y colores
        self.font = pygame.font.SysFont('Arial', 20)
        self.text_color = (0, 0, 0)

#Renderiza el texto en la pantalla en la posición dada.
#Args:
#text (str): El texto a mostrar.
#position (tuple): La posición (x, y) en la pantalla.
    def render_text(self, text, position):

        text_surface = self.font.render(text, True, self.text_color)
        self.screen.blit(text_surface, position)


# Muestra los resultados finales de la búsqueda en la pantalla.
    def display_final_results(self):
        self.screen.fill((255, 255, 255))
        self.render_text(f"Algorithm: {self.algorithm}", (10, 10))
        self.render_text(f"Tree Nodes: {self.tree_nodes}", (10, 40))
        self.render_text(f"Expanded Nodes: {self.expanded_nodes}", (10, 70))
        self.render_text(f"Depth: {self.depth}", (10, 100))
        self.render_text(f"Computation Time: {self.computation_time:.2f} s", (10, 130))
        self.render_text(f"Cost: {self.cost}", (10, 160))
        pygame.display.flip()

    def draw(self):
        pygame.display.set_caption("Smart Car Search Visualization")

        move_index = 0
        velocity = 0.5
        passenger_picked_up = False  # Variable para saber si el pasajero ha sido recogido
        car_at_destination = False  # Variable para controlar si el carro ha llegado a la meta

        while not car_at_destination:
            self.screen.fill((200, 200, 200))  # Rellenar el fondo con un color gris claro
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
                self.render_text('Back', (490, 330))

            pygame.display.flip()
            time.sleep(velocity)

        # Mostrar la pantalla final con los resultados
        self.display_final_results()

        # Esperar a que el usuario cierre la ventana
        self.wait_for_quit()

    def wait_for_quit(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
