from gtts import gTTS #module for text to speech conversion

text = "Hello everyone, thank you for viewing this code !" #text to be converted

language = 'en' #English Language

obj = gTTS(text = text, lang = language, slow = False)

obj.save("sample.mp3")
