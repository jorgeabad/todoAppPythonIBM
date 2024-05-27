from enum import Enum, auto
from typing import List

class TareaEstado(Enum):
    """
    Enumeración para representar el estado de una tarea.
    """
    PENDIENTE = auto()
    COMPLETADA = auto()

class Tarea:
    def __init__(self, name: str):
        """
        Inicializa una tarea con un nombre y un estado predeterminado de PENDIENTE.

        :param name: Nombre de la tarea.
        """
        self.name = name
        self.status = TareaEstado.PENDIENTE
    
    @property
    def estado(self) -> str:
        """
        Devuelve una representación en cadena del estado de la tarea.

        :return: 'Completada' si la tarea está completada, 'Pendiente' de lo contrario.
        """
        return 'Completada' if self.status == TareaEstado.COMPLETADA else 'Pendiente'

    def cambiar_estado(self):
        """
        Cambia el estado de la tarea. Si está completada, la cambia a pendiente y viceversa.
        """
        self.status = TareaEstado.COMPLETADA if self.status == TareaEstado.PENDIENTE else TareaEstado.PENDIENTE

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena de la tarea, incluyendo su nombre y estado.

        :return: Cadena con el nombre y el estado de la tarea.
        """
        return f'{self.name} - {self.estado}'

class ListaTareas:
    def __init__(self):
        """
        Inicializa una lista de tareas vacía.
        """
        self.tareas: List[Tarea] = []
    
    def es_Vacia(self) -> bool:
        """
        Comprueba si la lista de tareas está vacía.

        :return: True si la lista está vacía, False de lo contrario.
        """
        return len(self.tareas) == 0

    def es_posicion_valida(self, index: int) -> bool:
        """
        Comprueba si un índice es válido para la lista de tareas.

        :param index: Índice a comprobar.
        :return: True si el índice es válido, False de lo contrario.
        """
        return 0 <= index < len(self.tareas)

    def hay_tareas_pendientes(self) -> bool:
        """
        Comprueba si hay tareas pendientes en la lista.

        :return: True si hay al menos una tarea pendiente, False de lo contrario.
        """
        return any(task.status == TareaEstado.PENDIENTE for task in self.tareas)
    
    def hay_tareas_completas(self) -> bool:
        """
        Comprueba si hay tareas completadas en la lista.

        :return: True si hay al menos una tarea completada, False de lo contrario.
        """
        return any(task.status == TareaEstado.COMPLETADA for task in self.tareas)

    def nueva_tarea(self, name: str) -> str:
        """
        Añade una nueva tarea a la lista.

        :param name: Nombre de la nueva tarea.
        :return: Mensaje indicando si la tarea fue agregada o si hubo un error.
        """
        if not name.strip():
            return "Error: El nombre de la tarea no puede estar vacío."
        
        if any(tarea.name == name for tarea in self.tareas):
            return f"Error: Ya existe una tarea con el nombre '{name}'."
        
        tarea = Tarea(name)
        self.tareas.append(tarea)
        return f'Tarea "{name}" agregada.'

    def cambiar_estado_tarea(self, index: int) -> str:
        """
        Cambia el estado de una tarea en la lista.

        :param index: Índice de la tarea cuyo estado se va a cambiar.
        :return: Mensaje indicando si el estado fue cambiado o si hubo un error.
        """
        if self.es_posicion_valida(index):
            tarea = self.tareas[index]
            tarea.cambiar_estado()
            return f'Tarea "{tarea.name}" marcada como "{tarea.estado}".'
        else:
            return f'Error: No existe una tarea en la posición {index + 1}.'

    def mostrar_tareas(self) -> List[str]:
        """
        Devuelve una lista con las tareas y sus estados.

        :return: Lista de cadenas con las tareas y sus estados.
        """
        if not self.tareas:
            return ['No hay tareas en la lista.']
        return [str(task) for task in self.tareas]

    def eliminar_tarea(self, index: int) -> str:
        """
        Elimina una tarea de la lista.

        :param index: Índice de la tarea a eliminar.
        :return: Mensaje indicando si la tarea fue eliminada o si hubo un error.
        """
        if self.es_posicion_valida(index):
            tarea_eliminada = self.tareas.pop(index)
            return f'Tarea "{tarea_eliminada.name}" eliminada.'
        else:
            return f'Error: No existe una tarea en la posición {index + 1}.'
    
    def vaciar_lista(self) -> str:
        """
        Elimina todas las tareas de la lista.

        :return: Mensaje indicando si la lista fue vaciada o si ya estaba vacía.
        """
        if not self.tareas:
            return "No hay tareas en la lista."
        
        self.tareas.clear()
        return "Lista de tareas vaciada."
    
    def eliminar_tareas_completas(self) -> str:
        """
        Elimina todas las tareas completadas de la lista.

        :return: Mensaje indicando que las tareas completadas fueron eliminadas.
        """
        self.tareas = [task for task in self.tareas if task.status != TareaEstado.COMPLETADA]
        return "Tareas completadas eliminadas."
