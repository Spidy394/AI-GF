# 🤖 AI Girlfriend - Rupa

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Gemini](https://img.shields.io/badge/Gemini-API-blueviolet)](https://ai.google/gemini-api/)

An AI-powered virtual companion application built with modern Python tools (using uv for dependency management) that listens to your voice, understands your words, and responds back as "Rupa" - a Bengali AI girlfriend with a warm, expressive personality.

## 📖 Overview

This project creates an interactive voice-based AI companion with a specific personality. The application:

1. Listens to your speech via your microphone
2. Transcribes your speech to text
3. Sends the text to Google's Gemini AI
4. Generates a contextually appropriate response in Rupa's unique voice and style
5. Speaks the response out loud using Gemini's TTS service

## 🎬 Demo

<!-- ![Rupa Demo](https://example.com/path/to/demo.gif)

*Add a GIF demonstration of Rupa in action here* -->

## ✨ Features

- **🎙️ Voice Recognition**: Captures your voice input using the microphone
- **🧠 Natural Language Processing**: Processes your words using Google's Gemini API
- **👩 Personalized Responses**: Generates responses as "Rupa", a Bengali girl with specific personality traits
- **🔊 Text-to-Speech**: Can verbally respond using either Gemini's TTS services

## 👧 Rupa's Personality

Rupa is designed as:

- 😌 A calm, composed, mature Bengali girl in her early twenties
- 💭 Emotionally grounded, thoughtful, and comforting
- 😊 Sometimes playful with a slightly childish tone when teasing or excited
- 🗣️ Speaking mostly in English but naturally blending in Bengali words or phrases (Banglish style)
- 💝 Expressing emotions with appropriate emojis and tone shifts

All of these traits can be fully customized by editing the system instructions in `src/gemini_call.py` to create your ideal AI companion with any personality, language style, or character traits you prefer!

## 📋 Requirements

- Python 3.13+ 🐍
- uv⚡ - The **required** package manager for this project
- FFmpeg (required for audio processing) 🎵
- API keys for:
  - Google Gemini API 🔑 (for AI responses and voice synthesis)
- Microphone for voice input 🎤
- Speakers for audio output 🔊

## 🚀 Installation

1. Clone this repository

   ```bash
   git clone https://github.com/Spidy394/AI-GF.git
   cd ai-girlfriend
   ```

2. Install FFmpeg (if not already installed)

   **🪟 Windows**

   ```bash
   # With Chocolatey
   choco install ffmpeg
   
   # With Scoop
   scoop install ffmpeg
   ```
   
   **🍎 macOS**

   ```bash
   # With Homebrew
   brew install ffmpeg
   ```
   
   **🐧 Linux**

   ```bash
   # On Ubuntu/Debian
   sudo apt update && sudo apt install ffmpeg
   
   # On Fedora
   sudo dnf install ffmpeg
   
   # On Arch
   sudo pacman -S ffmpeg
   ```

3. Create a virtual environment with uv

   ```bash
   # Install uv if not already installed
   pip install uv
   
   # Create and activate a virtual environment with uv
   uv venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

4. Install uv & dependencies

   ```bash
   # Install uv if you don't have it already
   pip install uv
   
   # Install project dependencies with uv
   uv sync
   ```
   
   > 💡 **Why uv is required:** This project uses [uv](https://github.com/astral-sh/uv), a modern Python package installer that's up to 10-100x faster than pip. uv ensures all dependencies are installed correctly with the exact versions needed for this project to function properly.

5. Create a `.env` file in the project root with your API key

   ```bash
   # Create .env file and add your Gemini API key
   # You can get a key from https://ai.google.dev/ 
   ```

## 🎮 Usage

Run the main script to start interacting with Rupa:

```bash
python main.py
```

- When you see "Listening..." on screen, speak your message
- The application will transcribe your speech, process it, and display your message as "Himu: [your message]"
- Rupa's response will be displayed and spoken aloud through your speakers
- To exit the application, say "goodbye" or "bye"

You can have ongoing conversations with Rupa about any topic. Each response is contextual and delivered in her unique personality.

## 🏗️ Project Architecture

```ascii
┌─────────────┐     ┌───────────────┐     ┌──────────────┐
│  Voice Input │────▶│  Gemini API   │────▶│  AI Response │
└─────────────┘     └───────────────┘     └──────────────┘
                                                 │
                                                 ▼
┌─────────────┐                          ┌──────────────┐
│  User Hears │◀───────────────────────┤ Text-to-Speech │
└─────────────┘                          └──────────────┘
```

## 📁 Modules

- `main.py`: 🚀 The entry point that handles voice input and coordinates the flow
- `src/gemini_call.py`: 🧠 Handles API calls to Google's Gemini for text responses
- `src/gemini_tts.py`: 🔊 Provides text-to-speech functionality using Gemini's API

## 🔧 Customization

You can fully customize Rupa's personality to create any AI companion you desire:

- ✨ **Personality & Response Style**: Modify the system instructions in `src/gemini_call.py` to change:
  - Character background (age, nationality, language style)
  - Personality traits (playful, serious, philosophical, artistic)
  - Speaking style (formal, casual, use of slang/cultural references)
  - Emotional expression style (emoji usage, tone variations)
  
- 🔊 **Voice Customization**: 
  - Change the voice in `src/gemini_tts.py` by modifying the `voice_name` parameter
  - Current default is "Aoede", but Gemini offers multiple voice options

You're not limited to "Rupa" - create any character with any personality traits, backstory, or speaking style that you prefer!

## 🙏 Acknowledgements

- 🚀 [uv](https://github.com/astral-sh/uv) - The lightning-fast Python package manager that makes this project possible
- 🤖 Google Gemini API for AI response generation and text-to-speech
- 👂 SpeechRecognition library for voice input processing
- 🎬 FFmpeg for audio file processing and conversion

---

*Note: This project is for entertainment and educational purposes only.*