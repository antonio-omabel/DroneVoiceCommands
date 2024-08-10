import speech_recognition as sr


def transcript_audio(audio_data, current_language, rate_times_channels, sample_size):
    recognizer = sr.Recognizer()
    try:
        audio_data = sr.AudioData(audio_data, rate_times_channels, sample_size)  # Convert audio data
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data, language=current_language)  # Real speech recognition
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Could not request results")
