import speech_recognition as sr
recognizer_instance = sr.Recognizer()

#wav = sr.AudioFile("D:/tonyo/Desktop/SpeechToTextProject/Vai_avanti.wav")    #Get audio from a wav file
availableLanguages = ["it-IT","en-US"]   #List of all available languages
currentLanguage = availableLanguages[0]  #Choosen language

isListening = True
phraseTimeLimit = 4.0

while(isListening):   #listening loop
    #with wav as source:    #use audio as source
    with sr.Microphone() as source: #use Microphone as source
        #recognizer_instance.pause_threshold = 3.0  #stop listening if pause is >= threshold
        recognizer_instance.adjust_for_ambient_noise(source)    #get audio from mic while noise is detected
        if currentLanguage == "it-IT":
            print("In ascolto...")
            audio = recognizer_instance.listen(source,5,phraseTimeLimit)
            print("Elaborazione...")
        elif (currentLanguage == "en-US"):
            print("Listening...")
            audio = recognizer_instance.listen(source,5,phraseTimeLimit)
            print("Elaboration...")
    try:
        text = recognizer_instance.recognize_google(audio, language=currentLanguage)
        if currentLanguage == "it-IT":
            print("Testo in uscita:", text)
        elif currentLanguage == "en-US":
            print("Output text:", text)
    except BaseException as e:
        if currentLanguage == "it-IT":
            print(e,"Audio vuoto.", sep='')
        elif currentLanguage == "en-US":
            print(e, "Blank audio.", sep='')