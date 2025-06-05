from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import uvicorn
import os

app = FastAPI()

# Configuração de templates HTML
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Lista de tarefas em memória
class Task(BaseModel):
    id: int
    description: str
    completed: bool = False

tasks: List[Task] = []

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/add")
async def add_task(description: str = Form(...)):
    task_id = len(tasks) + 1
    new_task = Task(id=task_id, description=description)
    tasks.append(new_task)
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete")
async def delete_task(task_id: int = Form(...)):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return RedirectResponse(url="/", status_code=303)

@app.post("/complete")
async def complete_task(task_id: int = Form(...)):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return RedirectResponse(url="/", status_code=303)
    raise HTTPException(status_code=404, detail="Task not found")
