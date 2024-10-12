
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from models.SmartCarWorld import World
from models.SmartCarSearchGUI import SearchGUI
from models.SmartCarUninformedSearch import *
from models.SmartCarInformedSearch import *
import os

class GUI:
    """
    Clase que representa la interfaz gráfica de usuario (GUI) para la aplicación Smart Car.

    Args:
        master: La ventana principal de la GUI.

    Methods:
        __init__: Inicializa la GUI.
        load_world: Abre un cuadro de diálogo para cargar un archivo de mundo.
        show_algorithm_options: Muestra las opciones de algoritmos según el tipo de búsqueda seleccionado.
        run_algorithm: Ejecuta el algoritmo de búsqueda seleccionado.
    """
    def __init__(self, master):
        """
        Inicializa la GUI.

        Args:
            master: La ventana principal de la GUI.
        """
        # Configurar ventana principal
        self.master = master
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = 1280
        window_height = 720
        self.master.title("Smart Car")
        self.master.geometry(f"{window_width}x{window_height}")
        self.master.maxsize(window_width, window_height)
        self.master.minsize(window_width, window_height)
        self.master.resizable(False, False)
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Cargar imagen de fondo
        self.background_image = Image.open("images/background.png")
        self.background_image = self.background_image.resize((window_width, window_height), Image.BICUBIC)
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(master, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Inicializar variables
        self.world = None
        self.search_algorithm = None

        # Crear botones
        self.btn_load_world = tk.Button(master, text="Cargar Archivo de Mundo", command=self.load_world)
        self.btn_load_world.place(x=200, y=250)

        self.lbl_file_name = tk.Label(master, text="", font=("Arial", 12))
        self.lbl_file_name.place(x=410, y=255)

        self.algorithm_var = tk.StringVar(master)
        self.algorithm_var.set("Seleccionar Tipo de Búsqueda")

        self.algorithm_menu = tk.OptionMenu(master, self.algorithm_var, "No Informada", "Informada", command=self.show_algorithm_options)
        self.algorithm_menu.place(x=200, y=325)
        self.algorithm_menu.config(state=tk.DISABLED)

        self.algorithm_options_var = tk.StringVar(master)
        self.algorithm_options_var.set("Seleccionar Algoritmo")
        self.algorithm_options_menu = tk.OptionMenu(master, self.algorithm_options_var, "", "")
        self.algorithm_options_menu.place(x=200, y=400)
        self.algorithm_options_menu.config(state=tk.DISABLED)

        self.btn_run_algorithm = tk.Button(master, text="Ejecutar Búsqueda", command=self.run_algorithm)
        self.btn_run_algorithm.place(x=200, y=475)
        self.btn_run_algorithm.config(state=tk.DISABLED)

    def load_world(self):
        """
        Abre un cuadro de diálogo para cargar un archivo de mundo.
        """
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")], title="Seleccionar Archivo de Mundo", initialdir="./test")
        if file_path:
            relative_path = os.path.relpath(file_path)
            self.lbl_file_name.config(text=relative_path)
            self.algorithm_menu.config(state=tk.NORMAL)
            
    def show_algorithm_options(self, selection):
        """
        Muestra las opciones de algoritmos según el tipo de búsqueda seleccionado.

        Args:
            selection: El tipo de búsqueda seleccionado.
        """
        if selection == "No Informada":
            algorithms = ["Amplitud", "Costo Uniforme", "Profundidad Evitando Ciclos"]
        elif selection == "Informada":
            algorithms = ["Avara", "A*"]
        else:
            algorithms = []

        # Actualizar las opciones del menú desplegable de algoritmos
        self.algorithm_options_var.set(algorithms[0])  # Establecer el primer algoritmo como predeterminado
        self.algorithm_options_menu["menu"].delete(0, "end")  # Limpiar las opciones actuales
        for algorithm in algorithms:
            self.algorithm_options_menu["menu"].add_command(label=algorithm, command=tk._setit(self.algorithm_options_var, algorithm))

        # Habilitar el menú desplegable de algoritmos y las opciones correspondientes
        self.algorithm_options_menu.config(state=tk.NORMAL)

        # Habilitar el botón de ejecución de algoritmo
        self.btn_run_algorithm.config(state=tk.NORMAL)

    def run_algorithm(self):
        """
        Ejecuta el algoritmo de búsqueda seleccionado.
        """
        selected_algorithm = self.algorithm_options_var.get()
        try:
            self.world = World(self.lbl_file_name.cget("text"))
        except Exception as e:
            tk.messagebox.showerror("Error", "Archivo de Mundo Inválido")
            return
        if selected_algorithm == "Amplitud":
            search_results = BreadthFirstSearch(self.world)
        elif selected_algorithm == "Costo Uniforme":
            search_results = UniformCostSearch(self.world)
        elif selected_algorithm == "Profundidad Evitando Ciclos":
            search_results = DepthFirstSearch(self.world)
        elif selected_algorithm == "Avara":
            search_results = GreedySearch(self.world)
        elif selected_algorithm == "A*":
            search_results = AStarSearch(self.world)
        search = SearchGUI(self.lbl_file_name.cget("text"), search_results, selected_algorithm)
        self.master.withdraw()
        search.draw()
        self.master.deiconify()

def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
