# Dcumentación del gestor de Tareas

## gestorTareas.py

### Clases:

1. **TareaEstado(Enum):**
   - Enumeración para representar el estado de una tarea.
   - **Atributos:**
     - `PENDIENTE`: Representa el estado de una tarea pendiente.
     - `COMPLETADA`: Representa el estado de una tarea completada.

2. **Tarea:**
   - Clase para representar una tarea con su nombre y estado.
   - **Métodos:**
     - `__init__(self, name: str)`: Inicializa una tarea con un nombre y un estado predeterminado de PENDIENTE.
     - `estado(self) -> str`: Devuelve una representación en cadena del estado de la tarea ('Completada' o 'Pendiente').
     - `cambiar_estado(self)`: Cambia el estado de la tarea de pendiente a completada y viceversa.
     - `__str__(self) -> str`: Devuelve una representación en cadena de la tarea, incluyendo su nombre y estado.

3. **ListaTareas:**
   - Clase para gestionar una lista de tareas.
   - **Métodos:**
     - `__init__(self)`: Inicializa una lista de tareas vacía.
     - `es_Vacia(self) -> bool`: Comprueba si la lista de tareas está vacía.
     - `es_posicion_valida(self, index: int) -> bool`: Comprueba si un índice es válido para la lista de tareas.
     - `hay_tareas_pendientes(self) -> bool`: Comprueba si hay tareas pendientes en la lista.
     - `hay_tareas_completas(self) -> bool`: Comprueba si hay tareas completadas en la lista.
     - `nueva_tarea(self, name: str) -> str`: Añade una nueva tarea a la lista.
     - `cambiar_estado_tarea(self, index: int) -> str`: Cambia el estado de una tarea en la lista.
     - `mostrar_tareas(self) -> List[str]`: Devuelve una lista con las tareas y sus estados.
     - `eliminar_tarea(self, index: int) -> str`: Elimina una tarea de la lista.
     - `vaciar_lista(self) -> str`: Elimina todas las tareas de la lista.
     - `eliminar_tareas_completas(self) -> str`: Elimina todas las tareas completadas de la lista.

### Comentarios:

- La clase `Tarea` encapsula la información y el comportamiento de una tarea individual, proporcionando métodos para cambiar su estado y obtener una representación legible en cadena.

- La clase `ListaTareas` gestiona una colección de tareas, proporcionando métodos para agregar, eliminar y modificar tareas, así como para realizar consultas sobre el estado de la lista.

- Se ha utilizado el módulo `enum` para definir el estado de la tarea como una enumeración, lo que mejora la legibilidad y la claridad del código.

## TerminalUI.py

### Clase:

1. **administradorTareasUI:**
   - Clase para la interfaz de usuario del administrador de tareas.
   - **Métodos:**
     - `__init__(self, manager: ListaTareas)`: Inicializa la clase con un objeto de la clase ListaTareas.
     - `clear_screen(self)`: Método para limpiar la pantalla de la terminal.
     - `display_noHayTareas(self)`: Método para mostrar un mensaje cuando no hay tareas.
     - `display_mensaje(self, mensaje)`: Método para mostrar un mensaje en verde.
     - `display_mensaje_error(self, mensaje)`: Método para mostrar un mensaje de error en rojo.
     - `display_tasks(self)`: Método para mostrar las tareas actuales.
     - `display_menu(self)`: Método para mostrar el menú de opciones.
     - `run(self)`: Método principal que ejecuta el programa.
     - `run_web_version(self)`: Método para ejecutar la versión web de la aplicación.

### Comentarios:

- La clase `administradorTareasUI` proporciona una interfaz de línea de comandos para interactuar con la lista de tareas, permitiendo al usuario realizar operaciones como agregar, eliminar y cambiar el estado de las tareas.

- Se han definido métodos para mostrar mensajes de diferentes tipos (normal, éxito, error) y para presentar de manera ordenada las tareas y el menú de opciones.

- El método `run` es el punto de entrada principal para la aplicación de línea de comandos, donde se maneja la lógica de interacción con el usuario y se llama a los métodos correspondientes de la clase `ListaTareas`.

## servidor.py

### Clase:

1. **AppWeb:**
   - Clase para la aplicación web de gestión de tareas.
   - **Métodos:**
     - `__init__(self, miLista: ListaTareas)`: Inicializa la clase con una instancia de ListaTareas.
     - `rest(self, environ, start_response)`: Método principal que maneja las solicitudes HTTP REST.

### Comentarios:

- La clase `AppWeb` implementa una API REST para interactuar con la lista de tareas a través de solicitudes HTTP, utilizando el protocolo WSGI para la comunicación con el servidor web.

- Se han definido rutas y métodos para manejar las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre las tareas, así como para servir archivos estáticos como HTML, CSS y JavaScript.

- Se utiliza la clase `ListaTareas` para gestionar la colección de tareas y realizar las operaciones correspondientes en respuesta a las solicitudes del cliente.


### Endpoints del API REST:

- **GET /tareas:**
  - Descripción: Obtiene la lista de todas las tareas con sus estados.
  - Respuesta: Lista de objetos JSON, donde cada objeto representa una tarea con su nombre y estado.

- **POST /tareas:**
  - Descripción: Crea una nueva tarea con el nombre proporcionado.
  - Cuerpo de la solicitud: Objeto JSON con el nombre de la tarea.
  - Respuesta: Objeto JSON con un mensaje indicando si la tarea fue creada correctamente o si hubo un error.

- **PUT /tareas/id:**
  - Descripción: Cambia el estado de la tarea con el ID proporcionado.
  - Parámetros de la URL: ID de la tarea a modificar.
  - Respuesta: Objeto JSON con un mensaje indicando si el estado de la tarea fue cambiado correctamente o si hubo un error.

- **DELETE /tareas/id:**
  - Descripción: Elimina la tarea con el ID proporcionado.
  - Parámetros de la URL: ID de la tarea a eliminar.
  - Respuesta: Objeto JSON con un mensaje indicando si la tarea fue eliminada correctamente o si hubo un error.

- **DELETE /tareas/todas:**
  - Descripción: Elimina todas las tareas de la lista.
  - Respuesta: Objeto JSON con un mensaje indicando que todas las tareas fueron eliminadas.

- **DELETE /tareas/completas:**
  - Descripción: Elimina todas las tareas completadas de la lista.
  - Respuesta: Objeto JSON con un mensaje indicando que todas las tareas completadas fueron eliminadas.

### Comentarios adicionales:

- Los endpoints están diseñados para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre la lista de tareas, proporcionando una interfaz para interactuar con la aplicación desde un cliente web o móvil.