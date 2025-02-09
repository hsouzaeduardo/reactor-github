import streamlit as st

class ChatInterface:
    def __init__(self, speech_service, openai_service):
        self.speech_service = speech_service
        self.openai_service = openai_service
        self.messages = []

    def render_chat(self):
        # Renderiza as mensagens na interface (exemplo básico com Streamlit)
        for message in self.messages:
            if message['sender'] == 'user':
                st.write(f"**Você**: {message['text']}")
            else:
                st.write(f"**Bot**: {message['text']}")

    def add_message(self, message, sender='user'):
        self.messages.append({"text": message, "sender": sender})
        self.render_chat()

    def microphone_button(self):
        # Exemplo básico de implementação do botão de microfone com Streamlit
        if st.button("Gravar áudio"):
            st.write("Gravando...")
            speech_to_text = self.speech_service.speech_to_text()
            self.add_message(speech_to_text, sender='user')
            st.write(f"Você disse: {speech_to_text}")
            
            # Aqui você poderia também integrar a resposta do modelo OpenAI
            #response = self.openai_service.get_response(speech_to_text)  # Supondo que o serviço OpenAI tenha esse método
            #self.add_message(response, sender='bot')

    def render(self):
        # Renderiza o chat completo e o botão do microfone
        self.render_chat()
        self.microphone_button()
