from gtts import gTTS
message = "rosa es mi favorito"
tts= gTTS(message)
tts.save("audio.mp3")