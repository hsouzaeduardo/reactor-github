import openai

class AzureOpenAIService:
    def __init__(self, api_key: str, endpoint: str, deployment: str):
        self.api_key = api_key
        self.endpoint = endpoint.rstrip('/')
        self.deployment = deployment
        # Configure the openai library for Azure
        openai.api_type = "azure"
        openai.api_key = self.api_key
        openai.api_base = self.endpoint
        openai.api_version = "2022-12-01"

    def send_query(self, prompt: str) -> str:
        try:
            result = openai.Completion.create(
                engine=self.deployment,
                prompt=prompt,
                max_tokens=150
            )
            return result['choices'][0]['text'].strip()
        except Exception as e:
            raise Exception(f"Error: {e}")