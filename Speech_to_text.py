import speech_recognition as sr
from mp3_to_wav import mp3_to_wav
def speech_to_text(input_audio_path):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    # Load audio file
    with sr.AudioFile(input_audio_path) as source:
        audio_data = recognizer.record(source)

    # Recognize speech using Google Speech Recognition
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

# Example usage:
input_audio_path = "output_file.wav"
recognized_text = speech_to_text(input_audio_path)
if recognized_text:
    print("Recognized text:", recognized_text)
