from pytube import YouTube, Playlist
from moviepy.editor import *

# function to download a single video
def download_video(video_url, convert_to_mp3, quality):
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_by_resolution(quality)
        if video is None:
            print(f"No video found with resolution '{quality}'")
            return
        video_path = video.download()
        if convert_to_mp3:
            mp3_path = video_path.split(".")[0] + ".mp3"
            video_clip = VideoFileClip(video_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(mp3_path)
            audio_clip.close()
            video_clip.close()
            os.remove(video_path)
        print(f"Video downloaded successfully to '{video_path}'")
    except Exception as e:
        print(f"Error occurred while downloading video: {str(e)}")

# function to download all videos in a playlist
def download_playlist(playlist_url, convert_to_mp3, quality):
    try:
        playlist = Playlist(playlist_url)
        for video in playlist.videos:
            video = video.streams.get_by_resolution(quality)
            if video is None:
                print(f"No video found with resolution '{quality}' for video '{video.title}'")
                continue
            video_path = video.download()
            if convert_to_mp3:
                mp3_path = video_path.split(".")[0] + ".mp3"
                video_clip = VideoFileClip(video_path)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(mp3_path)
                audio_clip.close()
                video_clip.close()
                os.remove(video_path)
            print(f"Video '{video.title}' downloaded successfully to '{video_path}'")
    except Exception as e:
        print(f"Error occurred while downloading playlist: {str(e)}")

# prompt user for input (video URL or playlist URL)
url = input("Enter the URL of the video or playlist you want to download: ")

# prompt user whether to convert to MP3
convert_to_mp3 = input("Do you want to convert to MP3? (y/n): ").lower() == "y"

# prompt user to choose quality
quality = input("Enter the video or audio quality you want (e.g. 720p, 128kbps): ")

# determine whether the input is a video or playlist URL
if "playlist" in url:
    download_playlist(url, convert_to_mp3, quality)
else:
    download_video(url, convert_to_mp3, quality)
