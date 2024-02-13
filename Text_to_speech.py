# from gtts import gTTS
# import io,os

# def text_to_speech(text):
#     # Create gTTS object
#     tts = gTTS(text)

#     # Save the audio to an in-memory file (BytesIO)
#     audio_buffer = io.BytesIO()
#     tts.write_to_fp(audio_buffer)
#     audio_buffer.seek(0)

#     return audio_buffer.read()

# # Example usage:
# text = "Hello, how are you?"
# speech = text_to_speech(text)
# os.system(speech)
from gtts import gTTS
import io
import os

def text_to_speech(text, filename='output.mp3'):
    # Create gTTS object
    tts = gTTS(text)

    # Save the audio to a file
    tts.save(filename)

    return filename

# Example usage:
text = "Hello, how are you?"
output_file = text_to_speech(text)
print("Audio file saved as:", output_file)

# Play the audio using the default media player
os.system("start " + output_file)  # for Windows
# os.system("xdg-open " + output_file)  # for Linux
# os.system("open " + output_file)  # for macOS
