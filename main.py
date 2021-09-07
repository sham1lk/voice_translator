import speech_recognition as sr
from googletrans import Translator
import gtts
from playsound import playsound

r = sr.Recognizer()
mic = sr.Microphone()
translator = Translator()
# language of speech
MY_LANG = 'ru-RU'
# language to translate and output
TRANSLATE_TO = 'en'


# function to listen and translate to text. Listens till pause after words.
def voice_to_text():
    with mic as audio_file:
        print("Speak Please")
        r.adjust_for_ambient_noise(audio_file)
        audio = r.listen(audio_file)
        print("Converting Speech to Text...")
        text = r.recognize_google(audio, language=MY_LANG)
        return text


while True:
    print("press Enter to start recording, stop speaking to end the recording")
    input()
    # get text
    text = voice_to_text()
    print("text to translate: {}".format(text))
    # translate text
    text = translator.translate(text, dest=TRANSLATE_TO).text
    # text to audio
    tts = gtts.gTTS(text)
    tts.save("test.mp3")
    # play sound
    playsound("test.mp3")
