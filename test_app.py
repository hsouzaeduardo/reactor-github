from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_chat_endpoint():
  # Test payload
  test_message = {
    "user": "TestUser",
    "message": "Hello World"
  }
  
  # Make POST request to /chat endpoint
  response = client.post("/chat", json=test_message)
  
  # Assert response status code is 200
  assert response.status_code == 200
  
  # Assert response content is correct
  expected_response = {
    "response": f"Olá, {test_message['user']}! Você disse: {test_message['message']}"
  }
  assert response.json() == expected_response

def test_chat_endpoint_invalid_payload():
  # Test with invalid payload
  invalid_message = {
    "invalid_field": "test"
  }
  
  # Make POST request with invalid data
  response = client.post("/chat", json=invalid_message)
  
  # Assert response status code is 422 (Unprocessable Entity)
  assert response.status_code == 422