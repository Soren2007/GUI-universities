from tkinter.messagebox  import showerror
from speech_recognition import Recognizer,Microphone
def start ():
    recogn=Recognizer()
    try:
        with Microphone() as src:
            audio=recogn.listen()
            text=recogn.recognize_google(audio)
            text=text.lower()
            print(text)
    except Exception as error:
        showerror("Error",error)