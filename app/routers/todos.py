from fastapi import APIRouter, Request, HTTPException
from app.utility.todo_list.todos import Todos
from pydantic import BaseModel

router = APIRouter()


@router.post("/todos/add_task")
async def add_task(request: Request) -> dict:
    body = await request.json()
    if "task" not in body:
        raise HTTPException(status_code=400, detail="Missing 'task' key in request body")

    task = body["task"]
    if not task:
        raise HTTPException(status_code=400, detail="Task cannot be empty")

    try:
        todos = Todos()
        todos.add_task(task)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    response: dict = {"message": "Task added successfully"}
    return response


@router.get("/todos/get_all_tasks")
def get_tasks() -> dict:
    try:
        todos = Todos()
        tasks = todos.get_all_tasks()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    response: dict = {"tasks": tasks}
    return response
