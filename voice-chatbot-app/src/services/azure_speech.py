from azure.cognitiveservices.speech import AudioConfig, SpeechRecognizer

class AzureSpeechService:
    def __init__(self, subscription_key, region):
        self.subscription_key = subscription_key
        self.region = region
        self.speech_config = self.create_speech_config()

    def create_speech_config(self):
        from azure.cognitiveservices.speech import SpeechConfig
        return SpeechConfig(subscription=self.subscription_key, region=self.region)

    def speech_to_text(self):
        # Configurar o AudioConfig para usar o microfone padrão
        audio_config = AudioConfig(use_default_microphone=True)  # Usar o microfone padrão

        # Criar o reconhecedor de fala
        recognizer = SpeechRecognizer(speech_config=self.speech_config, audio_config=audio_config)

        # Realizar o reconhecimento de fala
        result = recognizer.recognize_once()  # Reconhecer uma única vez

        if result.reason == result.Reason.RecognizedSpeech:
            return result.text  # Retorna o texto reconhecido
        elif result.reason == result.Reason.NoMatch:
            return "No speech could be recognized."
        elif result.reason == result.Reason.Canceled:
            cancellation_details = result.cancellation_details
            return f"Speech recognition canceled: {cancellation_details.reason}"
    