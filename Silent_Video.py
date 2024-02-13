from moviepy.editor import VideoFileClip

def create_silent_video(input_path):
    video = VideoFileClip(input_path)
    video = video.set_audio(None)
    return video

# Example usage:
input_video_path = "/content/result_voice (27).mp4"
silent_video = create_silent_video(input_video_path)
