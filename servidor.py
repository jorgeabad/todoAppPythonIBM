from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults
import json
import os
from gestorTareas import ListaTareas

class AppWeb:

    def __init__(self, miLista: ListaTareas):
        self.miLista = miLista

    def rest(self, environ, start_response):
        setup_testing_defaults(environ)
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']

        response_body = b""
        status = '200 OK'
        headers = []

        try:
            if path == '/tareas' and method == 'GET':
                response_body = json.dumps(self.miLista.mostrar_tareas()).encode('utf-8')
                headers = [('Content-type', 'application/json')]
            elif path == '/tareas' and method == 'POST':
                content_length = int(environ.get('CONTENT_LENGTH', 0))
                request_body = environ['wsgi.input'].read(content_length)
                miTarea = json.loads(request_body).get('task')
                if miTarea:
                    message = self.miLista.nueva_tarea(miTarea)
                    response_body = json.dumps({'message': message}).encode('utf-8')
                    status = '201 Created'
                else:
                    response_body = json.dumps({'message': 'Se requiere un nombre para la tarea'}).encode('utf-8')
                    status = '400 Bad Request'
                headers = [('Content-type', 'application/json')]
            elif path.startswith('/tareas/') and method == 'DELETE':
                task_id_str = path.split('/')[-1]
                if task_id_str == 'todas':
                    message = self.miLista.vaciar_lista()
                    response_body = json.dumps({'message': message}).encode('utf-8')
                    status = '200 OK'
                elif task_id_str == 'completas':
                    message = self.miLista.eliminar_tareas_completas()
                    response_body = json.dumps({'message': message}).encode('utf-8')
                    status = '200 OK'
                else:
                    try:
                        task_id = int(task_id_str) - 1
                        message = self.miLista.eliminar_tarea(task_id)
                        response_body = json.dumps({'message': message}).encode('utf-8')
                        status = '200 OK' if "eliminada" in message else '400 Bad Request'
                    except ValueError:
                        response_body = json.dumps({'message': 'Error: Invalid task ID'}).encode('utf-8')
                        status = '400 Bad Request'
                headers = [('Content-type', 'application/json')]
            elif path.startswith('/tareas/') and method == 'PUT':
                try:
                    task_id = int(path.split('/')[-1]) - 1
                    message = self.miLista.cambiar_estado_tarea(task_id)
                    response_body = json.dumps({'message': message}).encode('utf-8')
                    status = '200 OK' if "Completada" or "Pendiente" in message else '400 Bad Request'
                except ValueError:
                    response_body = json.dumps({'message': 'Error: Invalid task ID'}).encode('utf-8')
                    status = '400 Bad Request'
                headers = [('Content-type', 'application/json')]
            else:
                if path == '/':
                    path = '/index.html'
                file_path = 'public' + path
                if os.path.exists(file_path) and os.path.isfile(file_path):
                    with open(file_path, 'rb') as file:
                        response_body = file.read()
                    if path.endswith('.html'):
                        headers = [('Content-type', 'text/html')]
                    elif path.endswith('.css'):
                        headers = [('Content-type', 'text/css')]
                    elif path.endswith('.js'):
                        headers = [('Content-type', 'application/javascript')]
                    else:
                        headers = [('Content-type', 'application/octet-stream')]
                    status = '200 OK'
                else:
                    response_body = b'File not found'
                    status = '404 Not Found'
                    headers = [('Content-type', 'text/plain')]
        except Exception as e:
            response_body = json.dumps({'message': str(e)}).encode('utf-8')
            status = '500 Internal Server Error'
            headers = [('Content-type', 'application/json')]

        start_response(status, headers)
        return [response_body]

def main():
    """
    Función principal que ejecuta el programa de gestión de tareas.
    """
    nuevaLista = ListaTareas()
    nuevaLista.nueva_tarea("Aprender HTML")
    nuevaLista.cambiar_estado_tarea(0)
    nuevaLista.nueva_tarea("Aprender CSS")
    nuevaLista.nueva_tarea("Aprender JavaScript")
    nuevaLista.nueva_tarea("Aprender Python")
    nuevaLista.nueva_tarea("Aprender GIT")
    app = AppWeb(nuevaLista)
    port = 8000
    httpd = make_server('', port, app.rest)
                
    print(f"Serving on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    main()
