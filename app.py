from fastapi import FastAPI
from pydantic import BaseModel

# Criação da instância da API com informações que serão exibidas na documentação Swagger
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
    # Aqui você pode implementar a lógica do chat, interagir com um chatbot ou processar a mensagem
    resposta = f"Olá, {msg.user}! Você disse: {msg.message}"
    return {"response": resposta}

# Caso queira executar o uvicorn diretamente pelo script:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
