import requests

BASE_URL = "http://localhost:8000"

print("GET /tasks")
response = requests.get(f"{BASE_URL}/tasks")
print(response.json())

print("\nPOST /tasks")
response = requests.post(f"{BASE_URL}/tasks", params={"description": "Testar API"})
task_id = response.json().get("id")
print(response.json())

print(f"\nPUT /tasks/{task_id}/complete")
response = requests.put(f"{BASE_URL}/tasks/{task_id}/complete")
print(response.json())

print(f"\nDELETE /tasks/{task_id}")
response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
print(response.json())

print("\nGET /tasks")
response = requests.get(f"{BASE_URL}/tasks")
print(response.json())