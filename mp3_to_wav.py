from pydub import AudioSegment

def mp3_to_wav(input_mp3_path):
    # Load MP3 audio
    audio = AudioSegment.from_mp3(input_mp3_path)

    # Export audio as WAV
    audio.export(format="wav")

    return audio

# Example usage:
# input_mp3_path = "Outputed_speech.mp3"

# mp3_to_wav(input_mp3_path)
