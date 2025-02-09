# Voice Chatbot Application

This project is a voice chatbot application built using Streamlit, Azure Speech Service, and Azure OpenAI. The application allows users to interact with a chatbot using voice commands, providing a seamless and engaging user experience.

## Project Structure

```
voice-chatbot-app
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   ├── components
│   │   └── chat_interface.py  # Manages the chat UI and microphone functionality
│   ├── services
│   │   ├── azure_speech.py    # Handles interactions with Azure Speech Service
│   │   └── azure_openai.py     # Interacts with Azure OpenAI API
├── requirements.txt           # Lists project dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd voice-chatbot-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Azure credentials for the Speech Service and OpenAI API. Ensure you have the necessary keys and endpoints.

## Usage Guidelines

1. Run the application:
   ```
   streamlit run src/app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the chatbot interface.

3. Use the microphone button to speak your queries and receive responses from the chatbot.

## Features

- Voice input through a microphone button.
- Real-time speech-to-text conversion using Azure Speech Service.
- Interaction with Azure OpenAI for generating responses.
- Clean and user-friendly chat interface.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.