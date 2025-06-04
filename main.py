# Importa as dependências necessárias do FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    description: str
    completed: bool = False

tasks: List[Task] = []

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
async def create_task(description: str):
    task_id = len(tasks) + 1
    new_task = Task(id=task_id, description=description)
    tasks.append(new_task)
    return new_task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": f"Task {task_id} deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}/complete")
async def complete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return task
    raise HTTPException(status_code=404, detail="Task not found")