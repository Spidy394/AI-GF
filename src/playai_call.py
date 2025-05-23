import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("PLAYAI_API_KEY")
user_id = os.getenv("PLAYAI_USER_ID")

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
    'X-USER-ID': user_id
}

json_data = {
    'model': 'PlayDialog',
    'text': "All human wisdom is summed up in these two words: Wait and hope.",
    'voice': 's3://voice-cloning-zero-shot/baf1ef41-36b6-428c-9bdf-50ba54682bd8/original/manifest.json',
    'outputFormat': 'wav'
}

response = requests.post('https://api.play.ai/api/v1/tts/stream',
                       headers=headers,
                       json=json_data)

if response.status_code == 200:
    with open('dialogue.wav', 'wb') as f:
        f.write(response.content)
    print("Audio file saved as dialogue.wav")
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")