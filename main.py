import speech_recognition as sr
from src.gemini_call import call_gemini
from src.gemini_tts import gemini_speak_text  

def main():
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio_text = r.listen(source)
            print("wait...")

            try:
                transcript = r.recognize_google(audio_text)
                print("Himu: " + transcript)
                result = call_gemini(transcript)
                if result:
                    reply = result['candidates'][0]['content']['parts'][0]['text']
                    print("Rupa: " + reply)
                    gemini_speak_text(reply) 
                    
            except Exception as e:
                print("Sorry, I did not get that:", str(e))

        if transcript.lower() == "goodbye" or transcript.lower() == "bye":
            print("Sayonara!")
            break



if __name__ == "__main__":
    main()
