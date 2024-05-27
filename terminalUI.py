import os
import sys
import time
import subprocess
from gestorTareas import ListaTareas

# Define una clase para la interfaz de usuario del administrador de tareas
class administradorTareasUI:
    # Inicializa la clase con un objeto de la clase ListaTareas
    def __init__(self, manager: ListaTareas):
        self.manager = manager

    # Método para limpiar la pantalla de la terminal
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # Método para mostrar un mensaje cuando no hay tareas
    def display_noHayTareas(self):
        print("\033[95mNo hay tareas en la lista.\033[0m")

    # Método para mostrar un mensaje en verde
    def display_mensaje(self, mensaje):
        print(f"\033[92m{mensaje}\033[0m")

    # Método para mostrar un mensaje de error en rojo
    def display_mensaje_error(self, mensaje):
        print(f"\033[91m{mensaje}\033[0m")

    # Método para mostrar las tareas actuales
    def display_tasks(self):
        print("\033[96m" + "====================================")
        print("          LISTA DE TAREAS           ")
        print("====================================\n"+"\033[0m")
        tasks = self.manager.mostrar_tareas()
        if self.manager.es_Vacia():
            print("\033[95mNo hay tareas en la lista.\033[0m")
        else:
            for idx, task in enumerate(tasks):
                name = task.split(" - ")[0]
                status = task.split(" - ")[1]
                icon = "\033[92m✓ Completada" if status=='Completada' else '\033[91m✗ Pendiente'
                print(f"{idx+1}- {name} - {icon} \033[0m")
        print("\033[96m" + "\n====================================\n"+ "\033[0m")

    # Método para mostrar el menú de opciones
    def display_menu(self):
        print("************************************")
        print("         MENÚ DE OPCIONES           ")
        print("************************************\n")
        print("1. Agregar una nueva tarea")
        print("2. Cambiar estado de una tarea")
        print("3. Eliminar una tarea")
        print("4. Eliminar las tareas completadas")
        print("5. Eliminar todas las tareas")
        print("6. Ejecutar version web")
        print("7. Salir")
        print("*************************************\n")

    # Método principal que ejecuta el programa
    def run(self):
        while True:
            self.clear_screen()
            self.display_tasks()
            self.display_menu()
            try:
                opcion = int(input("\nSelecciona una opción: "))
                if opcion == 1:
                    task_name = input("\033[93mIngresa el nombre de la nueva tarea: \033[0m")
                    print(self.manager.nueva_tarea(task_name))
                elif opcion in {2, 3, 4}:
                    if self.manager.es_Vacia():
                        self.display_noHayTareas()
                    else:
                        if opcion == 2:
                            task_index = int(input("\033[93mIngresa el número de la tarea: \033[0m")) - 1
                            self.display_mensaje(self.manager.cambiar_estado_tarea(task_index))
                        elif opcion == 3:
                            task_index = int(input("\033[93mIngresa el número de la tarea: \033[0m")) - 1
                            self.display_mensaje(self.manager.eliminar_tarea(task_index))
                        elif opcion == 4:
                            if not self.manager.hay_tareas_completas():
                                self.display_mensaje_error("No hay tareas completadas.")
                            else:
                                self.display_mensaje(self.manager.eliminar_tareas_completas())
                elif opcion == 5:
                    self.display_mensaje(self.manager.vaciar_lista())
                elif opcion == 6:
                    self.run_web_version()
                elif opcion == 7:
                    print("Saliendo...")
                    break
                else:
                    self.display_mensaje_error('Opción no válida. Por favor, selecciona una opción del 1 al 5')
            except ValueError:
                self.display_mensaje_error('Entrada no válida. Por favor, ingresa un número')
            time.sleep(1)

    # Método para ejecutar la versión web de la aplicación
    def run_web_version(self):
        """Ejecuta la versión web de la aplicación."""
        if sys.platform == "win32":
                os.startfile('servidor.py')
        else:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(current_dir, 'servidor.py')
            command = f'cd "{current_dir}" && python3 "{script_path}"'
            escaped_command = command.replace('"', '\\"')

            if sys.platform.startswith('linux'):
                subprocess.Popen(['gnome-terminal', '--', 'python3', script_path],
                start_new_session=True,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL)
            elif sys.platform == "darwin":
                osascript_command = f'''
                tell application "Terminal"
                activate
                do script "{escaped_command}"
                end tell
                '''
                subprocess.call(['osascript', '-e', osascript_command])

# Función principal que inicializa y ejecuta la interfaz de usuario
def main():
    """Inicializa y ejecuta la interfaz de usuario."""
    manager = ListaTareas()
    initial_tasks = [
        "Aprender HTML", "Aprender CSS", "Aprender JavaScript",
        "Aprender Python", "Aprender GIT", "Aprender Java", "Aprender Linux"
    ]
    for tarea in initial_tasks:
        manager.nueva_tarea(tarea)
    # Cambiar el estado de algunas tareas como ejemplo
    for idx in [3, 6, 2, 4]:
        manager.cambiar_estado_tarea(idx - 1)
    ui = administradorTareasUI(manager)
    ui.run()

# Comprueba si el script se está ejecutando directamente y, en caso afirmativo, llama a la función main
if __name__ == "__main__":
    main()