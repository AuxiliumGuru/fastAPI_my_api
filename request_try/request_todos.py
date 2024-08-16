import requests

# Base URL of the API
base_url = "http://127.0.0.1:8000"

def add_task(task):
    response = requests.post(f"{base_url}/todos/add_task", json={"task": task})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def get_all_tasks():
    response = requests.get(f"{base_url}/todos/get_all_tasks")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    # Test add_task with a valid task
    print("Testing add_task with 'New Task'")
    add_task("New Task")

    # Test add_task with a missing key
    print("\nTesting add_task with missing key")
    response = requests.post(f"{base_url}/todos/add_task", json={})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    # Test add_task with an empty task
    print("\nTesting add_task with an empty task")
    add_task("")

    # Test get_all_tasks
    print("\nTesting get_all_tasks")
    get_all_tasks()