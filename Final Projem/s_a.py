import google.generativeai as genai
import api
import k
from gtts import gTTS
import os

from playsound import playsound

    
    
# Metni tanımlayın


# gTTS nesnesi oluşturun


genai.configure(api_key=api.api)

model = genai.GenerativeModel('gemini-pro')

def geminiai(mesaj):
    response = model.generate_content(str(mesaj))

    with open("output.txt", "a", encoding="UTF-8") as f:
        for chunk in response:
            f.write(chunk.text) 
    

if __name__=="__main__":
    while True:
        mesaj = k.tr_konusma()
        print(mesaj)
        response = model.generate_content(mesaj)
        for chunk in response:
                geminiai(mesaj)
                tts = gTTS(text=chunk.text, lang='tr')

                # Ses dosyasını kaydedin
                tts.save("merhaba.mp3")
                playsound("merhaba.mp3")
                # Ses dosyasını oynatın
                os.remove("merhaba.mp3")
                
                
                