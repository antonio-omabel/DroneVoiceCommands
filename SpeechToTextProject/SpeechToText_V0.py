import speech_recognition as sr

recognizer = sr.Recognizer()


def Transcript(audio_data, current_language, rate, audio, audio_format):
    try:
        audio_data = sr.AudioData(audio_data, rate, audio.get_sample_size(audio_format))  # Convert audio data
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data, language=current_language)  # Real speech recognition
        print(text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
