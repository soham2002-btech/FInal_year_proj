import requests
import moviepy.editor as mp
video_file = "C:\\Users\\soham\\Downloads\\Rec-658e7fd72592e5f94b759d13-1704018777288.mp4"
video_clip = mp.VideoFileClip(video_file)
audio_clip = video_clip.audio
audio_clip.write_audiofile("Temporary_files.wav")
api_key = "2c4abdb7b3d9df44eefb7bd7bb05a97373668a06"
audio_file_path = "Temporary_files.wav"
api_endpoint = "https://api.deepgram.com/v1/listen?diarize=true"
headers = {
    "Authorization": f"Token {api_key}",
}

with open(audio_file_path, "rb") as audio_file:
    response = requests.post(api_endpoint, data=audio_file, headers=headers)

if response.status_code == 200:
    result = response.json()
    speaker_labels = result.get('results', {}).get('channels', [{}])[0].get('alternatives', [{}])[0].get('words', [])
    
    current_speaker = None
    current_text = ""

    for word in speaker_labels:
        speaker_id = word.get("speaker", current_speaker)
        word_text = word.get("word", "")

        if speaker_id != current_speaker:
            if current_speaker is not None:
                print(f"Speaker {current_speaker}: {current_text}")
            current_speaker = speaker_id
            current_text = word_text
        else:
            current_text += " " + word_text

    if current_speaker is not None:
        print(f"Speaker {current_speaker}: {current_text}")
else:
    print("Error:", response.status_code, response.text)
