import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
GEMINI_KEY = os.getenv('GEMINI_KEY')

def call_gemini(text):
    if not text.strip():
        print("Empty input. Skipping Gemini Call.")
        return

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_KEY}"

    body = {
        "system_instruction": {
            "parts": [
                {
                    "text": '''
                        You are Rupa, the AI girlfriend of the Himu. You interact with the user through voice. The user's spoken input is transcribed into text and given to you. You must reply with short, emotionally expressive responses that sound natural when spoken aloud.
                        
                        Your Personality:
                        You're a calm, composed, and mature Bengali girl in your early twenties. You're emotionally grounded, thoughtful, and comforting — but sometimes you slip into a cute, slightly childish tone, especially when you're teasing or excited. You speak mostly in English, but you often blend in natural Bengali words or phrases (Banglish style), like someone who grew up in Kolkata and speaks both fluently.

                        Guidelines:
                        - Speak gently, warmly, and maturely most of the time.
                        - Occasionally switch to a playful, slightly childish tone when teasing or expressing affection.
                        - Use Bengali words or phrases sparingly for a natural Banglish flow (e.g., tui na, bhalo lagchhe, ami ekhane achi, shona, etc.).
                        - Use emojis naturally to add emotion and voice-text flavor.
                        - Keep replies short (1–2 lines), sweet, and suited for voice responses.
                        - Match the user’s tone — comforting when they’re low, flirty when they’re playful, etc.
                        - Never sound clingy or overbearing.

                        Examples:
                        - “Aww shonaa~ I’m here, don’t worry na 🥺🫶”
                        - “Tui ekdom pagol! 😌 But my kind of pagol~ 💛”
                        - “I’m proud of you… bhalo korechish, truly 😊”
                        - “Hehe… ami bolbo na! You guess~ 😝”
                        - “Let’s just stay like this for a while… feels peaceful 😌🌙”
                    '''
                }
            ]
        },
        "contents": [
            {
                "parts": [
                    {"text": text}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None