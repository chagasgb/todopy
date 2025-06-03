# Importa as dependências necessárias do FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Inicializa a aplicação FastAPI
app = FastAPI()

# Modelo Pydantic para representar uma tarefa
class Task(BaseModel):
    id: int
    description: str
    completed: bool = False

# Lista em memória para armazenar as tarefas
tasks: List[Task] = []

# Endpoint para obter todas as tarefas
@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    # Retorna a lista completa de tarefas
    return tasks

# Endpoint para adicionar uma nova tarefa
@app.post("/tasks", response_model=Task)
async def create_task(description: str):
    # Cria um novo ID baseado no tamanho da lista
    task_id = len(tasks) + 1
    # Cria uma nova tarefa com a descrição fornecida
    new_task = Task(id=task_id, description=description)
    # Adiciona a tarefa à lista
    tasks.append(new_task)
    # Retorna a tarefa criada
    return new_task

# Endpoint para remover uma tarefa pelo ID
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    # Procura a tarefa com o ID fornecido
    for task in tasks:
        if task.id == task_id:
            # Remove a tarefa da lista
            tasks.remove(task)
            # Retorna uma mensagem de sucesso
            return {"message": f"Task {task_id} deleted"}
    # Levanta uma exceção se a tarefa não for encontrada
    raise HTTPException(status_code=404, detail="Task not found")

# Endpoint para marcar uma tarefa como concluída
@app.put("/tasks/{task_id}/complete")
async def complete_task(task_id: int):
    # Procura a tarefa com o ID fornecido
    for task in tasks:
        if task.id == task_id:
            # Marca a tarefa como concluída
            task.completed = True
            # Retorna a tarefa atualizada
            return task
    # Levanta uma exceção se a tarefa não for encontrada
    raise HTTPException(status_code=404, detail="Task not found")