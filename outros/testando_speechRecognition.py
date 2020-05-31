import speech_recognition as sr


microfone = sr.Recognizer()
def ouvir_microfone():
    with microfone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)

try:
    frase = microfone.recognize_google(audio, language='pt-BR')
    print('Você disse: ' + frase)
except sr.UnknownValueError:
    print('não entendi')



ouvir_microfone()
