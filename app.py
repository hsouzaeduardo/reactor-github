from fastapi import FastAPI
from pydantic import BaseModel

# Instância da API
app = FastAPI(
    title="Chat API",
    description="API para interface de chat com um endpoint POST para enviar mensagens.",
    version="1.0.0"
)

# Modelo de dados para a mensagem
class Message(BaseModel):
    user: str
    message: str

# Endpoint POST para o chat
@app.post("/chat", summary="Enviar mensagem", response_description="Resposta do chat")
async def chat_interface(msg: Message):
    resposta = f"Olá, {msg.user}! Você disse: {msg.message}"
    return {"response": resposta}

# Execução do Uvicorn para rodar o servidor corretamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
