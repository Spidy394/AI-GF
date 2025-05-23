# AI Girlfriend - Rupa

An AI-powered virtual companion application that listens to your voice, understands your words, and responds back as "Rupa" - a Bengali AI girlfriend with a warm, expressive personality.

## Overview

This project creates an interactive voice-based AI companion with a specific personality. The application:

1. Listens to your speech via your microphone
2. Transcribes your speech to text
3. Sends the text to AI models (Google Gemini)
4. Generates a contextually appropriate response in Rupa's unique voice and style
5. Optionally speaks the response out loud (using OpenAI TTS or Play.AI)

## Features

- **Voice Recognition**: Captures your voice input using the microphone
- **Natural Language Processing**: Processes your words using Google's Gemini API
- **Personalized Responses**: Generates responses as "Rupa", a Bengali girl with specific personality traits
- **Text-to-Speech**: Can verbally respond using either OpenAI's or Play.AI's TTS services

## Rupa's Personality

Rupa is designed as:

- A calm, composed, mature Bengali girl in her early twenties
- Emotionally grounded, thoughtful, and comforting
- Sometimes playful with a slightly childish tone when teasing or excited
- Speaking mostly in English but naturally blending in Bengali words or phrases (Banglish style)
- Expressing emotions with appropriate emojis and tone shifts

## Requirements

- Python 3.13+
- FFmpeg (required for audio processing)
- API keys for:
  - Google Gemini API
  - OpenAI API (for TTS)
  - Play.AI API (alternative TTS)
- Microphone for voice input
- Speakers for audio output

## Installation

1. Clone this repository

   ```bash
   git clone [repository-url]
   cd ai-girlfriend
   ```

1. Install FFmpeg (if not already installed)

   ```bash
   # On Windows with Chocolatey
   choco install ffmpeg
   
   # On Windows with Scoop
   scoop install ffmpeg
   
   # On macOS with Homebrew
   brew install ffmpeg
   
   # On Ubuntu/Debian
   sudo apt update && sudo apt install ffmpeg
   ```

1. Create a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

1. Install dependencies

   ```bash
   pip install -r requirements.txt
   # Or if using uv (as seen in project files)
   uv pip install -e .
   ```

1. Create a `.env` file in the project root with your API keys:

   ```env
   GEMINI_KEY=your-gemini-api-key
   OPENAI_KEY=your-openai-api-key
   PLAYAI_API_KEY=your-playai-api-key
   PLAYAI_USER_ID=your-playai-user-id
   ```

## Usage

Run the main script to start interacting with Rupa:

```bash
python main.py
```

- When prompted with "Talk", speak your message
- The application will transcribe your speech, process it, and display Rupa's response
- If text-to-speech is enabled (uncomment the relevant code in main.py), Rupa will speak her response

## How It Works

1. **Voice Input**: Uses SpeechRecognition library with Google's speech recognition service
2. **AI Processing**: Sends transcribed text to Google's Gemini API with custom personality instructions
3. **Response Generation**: Receives and processes AI-generated response
4. **Text-to-Speech** (optional): Converts the text response to speech using OpenAI or Play.AI

## Modules

- `main.py`: The entry point that handles voice input and coordinates the flow
- `src/gemini_call.py`: Handles API calls to Google's Gemini
- `src/gpt_call.py`: Provides text-to-speech functionality using OpenAI's API
- `src/playai_call.py`: Alternative text-to-speech using Play.AI's API

## Customization

You can customize Rupa's personality by modifying the system instructions in:

- `src/gemini_call.py` for response generation
- `src/gpt_call.py` for voice characteristics when using OpenAI TTS

## License

[Your chosen license]

## Acknowledgements

- Google Gemini API for AI response generation
- OpenAI API for text-to-speech capabilities
- Play.AI for alternative voice synthesis
- SpeechRecognition library for voice input processing
- FFmpeg for audio file processing and conversion

---

*Note: This project is for entertainment and educational purposes only.*