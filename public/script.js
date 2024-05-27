document.addEventListener('DOMContentLoaded', function() {
    const tareaForm = document.getElementById('tarea-form');
    const tareaInput = document.getElementById('tarea-input');
    const tareaList = document.getElementById('tarea-list');
    const eliminarTodas = document.getElementById('eliminarTodas');
    const eliminarCompletadas = document.getElementById('eliminarCompletadas');


    // Fetch and display tasks
    function cargarTareas() {
        fetch('/tareas')
            .then(response => response.json())
            .then(data => {
                tareaList.innerHTML = '';
                data.forEach((tarea, index) => {
                    const li = document.createElement('li');
                    const completeButton = document.createElement('button');
                    let estado = tarea.split(' - ')[1];
                    if (estado === 'Pendiente') {
                        li.className = 'list-group-item list-group-item-warning';
                        completeButton.className = 'btn btn-success';
                        completeButton.textContent = '✓';
                        li.textContent = tarea + " ❌";
                    } else {
                        li.className = 'list-group-item list-group-item-success';
                        completeButton.className = 'btn btn-danger';
                        completeButton.textContent = '✗';
                        li.textContent = tarea + " ✔️";
                    }
                    if (estado){
                        completeButton.onclick = () => cambiarEstado(index + 1);
                        const deleteButton = document.createElement('button');
                        deleteButton.className = 'btn';
                        deleteButton.textContent = 'Eliminar';
                        deleteButton.onclick = () => eliminarTarea(index + 1);
                        const actions = document.createElement('div');
                        actions.className = 'tarea-actions';
                        actions.appendChild(completeButton);
                        actions.appendChild(deleteButton);
                        li.appendChild(actions);
                        tareaList.appendChild(li);
                    }else{
                        const actions = document.createElement('div');
                        actions.className = 'tarea-actions';
                        li.textContent = tarea;
                        li.appendChild(actions);
                        tareaList.appendChild(li);
                    }
  
                });
            })
            .catch(error => console.error('Error fetching tasks:', error));
    }

    // Add a new task
    tareaForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const nuevaTarea = tareaInput.value.trim();
        if (nuevaTarea) {
            fetch('/tareas', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ task: nuevaTarea })
            }).then(response => {
                if (response.ok) {
                    tareaInput.value = '';
                    cargarTareas();
                }
            }).catch(error => console.error('Error añadiendo tarea:', error));
        }
    });


    // Complete a task
    function cambiarEstado(tareaId) {
        fetch(`/tareas/${tareaId}`, {
            method: 'PUT'
        }).then(response => {
            if (response.ok) {
                cargarTareas();
            }
        }).catch(error => console.error('Error al cambiar la tarea:', error));
    }

    // Delete a task
    function eliminarTarea(taskId) {
        fetch(`/tareas/${taskId}`, {
            method: 'DELETE'
        }).then(response => {
            if (response.ok) {
                cargarTareas();
            }
        }).catch(error => console.error('Error deleting task:', error));
    }

    // Delete all tasks
    function eliminarTodasTareas() {
        fetch('/tareas/todas', {
            method: 'DELETE'
        }).then(response => {
            if (response.ok) {
                cargarTareas();
            }
        }).catch(error => console.error('Error deleting all tasks:', error));
    }

    // Delete completed tasks
    function eliminarTareasCompletas() {
        fetch('/tareas/completas', {
            method: 'DELETE'
        }).then(response => {
            if (response.ok) {
                cargarTareas();
            }
        }).catch(error => console.error('Error deleting completed tasks:', error));
    }

    eliminarTodas.addEventListener('click', function(event) {
        event.preventDefault();
        eliminarTodasTareas();
    });

    eliminarCompletadas.addEventListener('click', function(event) {
        event.preventDefault();
        eliminarTareasCompletas();
    });
    // Initial load of tasks
    cargarTareas();
});
