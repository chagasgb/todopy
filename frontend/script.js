document.addEventListener("DOMContentLoaded", function () {
  const todoForm = document.getElementById("todoForm");
  const taskInput = document.getElementById("taskInput");
  const todoList = document.getElementById("todoList");
  const taskModal = new bootstrap.Modal(document.getElementById("taskModal"));
  const editTaskName = document.getElementById("editTaskName");
  const editTaskDescription = document.getElementById("editTaskDescription");
  let editTaskId = null;

  todoForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const taskName = taskInput.value.trim();
    if (taskName) {
      addTask(taskName);
      taskInput.value = "";
    }
  });

  function addTask(name) {
    const taskId = Date.now();
    const li = document.createElement("li");
    li.className = "todo-item";
    li.id = taskId;
    li.innerHTML = `
      <span onclick="toggleCompletion(${taskId})">${name}</span>
      <div>
        <button class="btn btn-edit btn-sm" onclick="editTask(${taskId})">Editar tarefa</button>
        <button class="btn btn-danger btn-sm" onclick="removeTask(${taskId})">Remover</button>
      </div>
    `;
    todoList.appendChild(li);
  }

  window.toggleCompletion = function (id) {
    const task = document.getElementById(id);
    const taskName = task.querySelector("span");
    taskName.classList.toggle("completed");
  };

  window.editTask = function (id) {
    const task = document.getElementById(id);
    const taskName = task.querySelector("span").textContent;
    editTaskId = id;
    editTaskName.value = taskName;
    taskModal.show();
  };

  document.getElementById("saveTaskChanges").addEventListener("click", function () {
    const updatedTaskName = editTaskName.value.trim();
    if (updatedTaskName) {
      const task = document.getElementById(editTaskId);
      task.querySelector("span").textContent = updatedTaskName;
      taskModal.hide();
      editTaskId = null;
    }
  });

  window.removeTask = function (id) {
    const task = document.getElementById(id);
    task.remove();
  };
});
