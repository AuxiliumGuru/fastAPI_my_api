from fastapi.testclient import TestClient
from app.main import app  # Adjust the import based on your project structure

client = TestClient(app)

def test_add_task_success():
    response = client.post("/todos/add_task", json={"task": "New Task"})
    assert response.status_code == 200
    assert response.json() == {"message": "Task added successfully"}

def test_add_task_missing_key():
    response = client.post("/todos/add_task", json={})
    assert response.status_code == 400
    assert response.json() == {"detail": "Missing 'task' key in request body"}

def test_add_task_empty_task():
    response = client.post("/todos/add_task", json={"task": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Task cannot be empty"}

def test_get_all_tasks_success():
    response = client.get("/todos/get_all_tasks")
    assert response.status_code == 200
    assert "tasks" in response.json()

if __name__ == "__main__":
    test_add_task_success()
    test_add_task_missing_key()
    test_add_task_empty_task()
    test_get_all_tasks_success()