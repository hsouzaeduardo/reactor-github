import os
import streamlit as st
from components.chat_interface import ChatInterface
from services.azure_speech import AzureSpeechService
from services.azure_openai import AzureOpenAIService
from azure.cognitiveservices.speech import SpeechConfig
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

def main():
    st.title("Voice Chatbot")
    
    # Fetch environment variables for Azure OpenAI
    AZURE_OPENAI_KEY = os.environ.get("AZURE_OPENAI_KEY")
    AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_DEPLOYMENT = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
    AZURE_SPEECH_KEY = os.environ.get("AZURE_SPEECH_KEY")
    AZURE_SPEECH_REGION = os.environ.get("AZURE_SPEECH_REGION")
    
    print(AZURE_SPEECH_KEY)

    
    # Initialize services
    speech_service = AzureSpeechService(
        subscription_key=AZURE_SPEECH_KEY,
        region=AZURE_SPEECH_REGION
    )

    openai_service = AzureOpenAIService(
        api_key=AZURE_OPENAI_KEY, 
        endpoint=AZURE_OPENAI_ENDPOINT, 
        deployment=AZURE_OPENAI_DEPLOYMENT
    )
    
    #Create chat interface
    chat_interface = ChatInterface(speech_service, openai_service)
    
    #Render chat interface
    chat_interface.render()

if __name__ == "__main__":
    main()