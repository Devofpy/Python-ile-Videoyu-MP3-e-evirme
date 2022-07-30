#Gerekli kütüphaneler 
import moviepy.editor as mp

def video_to_mp3(video_path, audio_path):
    clip = my.VideoFileClip(video_path)

clip.audio.write_audiofile(audio_path)
clip.close()