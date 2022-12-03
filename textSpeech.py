from gtts import gTTS
import os


text = input("enter someting:")
language = "en"
gtts_object = gTTS(text = text, lang= language, slow = False)

gtts_object.save("welcom.mp3")
os.system("welcom.mp3")
