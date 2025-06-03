# Importa o TestClient para testar endpoints da API
from fastapi.testclient import TestClient

# Importa o app FastAPI que será testado
from main import app  # Altere 'main' se o nome do arquivo for diferente

# Cria o cliente de testes
client = TestClient(app)

# Testa o endpoint GET /tasks quando a lista está vazia
def test_get_empty_tasks():
    # Envia uma requisição GET para /tasks
    response = client.get("/tasks")
    # Verifica se o status HTTP é 200 (OK)
    assert response.status_code == 200
    # Verifica se o corpo da resposta é uma lista vazia
    assert response.json() == []

# Testa o endpoint POST /tasks para criar uma nova tarefa
def test_create_task():
    # Envia uma requisição POST com a descrição como parâmetro de query
    response = client.post("/tasks?description=Estudar FastAPI")
    # Verifica se o status HTTP é 200 (OK)
    assert response.status_code == 200
    # Extrai o JSON da resposta
    data = response.json()
    # Verifica se a descrição está correta
    assert data["description"] == "Estudar FastAPI"
    # Verifica se o campo completed está como False
    assert data["completed"] is False
    # Verifica se o id foi atribuído corretamente (deve ser 1 neste teste isolado)
    assert data["id"] == 1

# Testa o endpoint PUT /tasks/{id}/complete para marcar como concluída
def test_complete_task():
    # Marca a tarefa de ID 1 como concluída
    response = client.put("/tasks/1/complete")
    # Verifica se o status é 200
    assert response.status_code == 200
    # Verifica se o campo completed foi atualizado
    assert response.json()["completed"] is True

# Testa o endpoint DELETE /tasks/{id} para deletar a tarefa
def test_delete_task():
    # Deleta a tarefa com ID 1
    response = client.delete("/tasks/1")
    # Verifica se o status é 200
    assert response.status_code == 200
    # Verifica a mensagem de retorno
    assert response.json() == {"message": "Task 1 deleted"}

# Testa o DELETE para uma tarefa que não existe (erro esperado)
def test_delete_nonexistent_task():
    # Tenta deletar tarefa com ID inexistente (ex: 999)
    response = client.delete("/tasks/999")
    # Espera um erro 404
    assert response.status_code == 404
    # Verifica a mensagem de erro
    assert response.json()["detail"] == "Task not found"
