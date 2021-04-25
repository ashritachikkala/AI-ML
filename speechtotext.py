# Python program to translate speech to text and text to speech
import speech_recognition as sr
# Initialize the recognizer
r = sr.Recognizer()
# Reading Audio file as source listening the audio file and store in audio_text variable
with sr.Microphone() as source:
    print('Speak anything')
    audio = r.listen(source)

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio)
        print('you said:{}'.format(text))
    except:
        print('sorry cant recognize')