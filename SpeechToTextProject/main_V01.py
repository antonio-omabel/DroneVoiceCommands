import speech_recognition as sr
import SocketCommunication as sc

recognizer_instance = sr.Recognizer()

availableLanguages = ["it-IT","en-US"]   #List of all available languages
currentLanguage = availableLanguages[0]  #Choosen language

isListening = True
phraseTimeLimit = 5.0

def AudioRecording():
    with sr.Microphone() as source:     #use Microphone as source
        recognizer_instance.pause_threshold = 1.0               #stop listening if pause is >= threshold
        recognizer_instance.non_speaking_duration = 1.0         #stop listening if not speaking duration is >= threshold
        recognizer_instance.adjust_for_ambient_noise(source)    #get audio from mic while noise is detected
        sc.SendTCPString("HIGH")
        print("Listening...")
        audio = recognizer_instance.listen(source, None, phraseTimeLimit)
        return audio

while(isListening):                     #listening loop
    audio = AudioRecording()
    sc.SendTCPString("LOW")
    print("Elaboration...")
    try:
        text = recognizer_instance.recognize_google(audio, language=currentLanguage)
        print(text)
        sc.SendTCPString(text)
    except BaseException as e:
        print(e, "Blank audio.", sep='')
sc.CloseConnection()