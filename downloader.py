import os
import re
import yt_dlp as youtube_dl
import subprocess

def download_and_convert():
    video_url = input("Please enter the YouTube video URL: ")
    download_type = input("Do you want to download the video or audio? (v/a): ")

    # Set the download options
    if download_type == 'v':
        ydl_opts = {
            'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4][vcodec^=avc1]',
            'outtmpl': 'videos/%(title)s.%(ext)s',
        }
    elif download_type == 'a':
        ydl_opts = {
            'format': 'bestaudio[ext=m4a]/best',
            'outtmpl': 'audios/%(title)s.%(ext)s',
        }
    else:
        print('Invalid download type')
        return

    # Create the "videos" or "audios" folder if it does not already exist
    if download_type == 'v' and not os.path.exists('videos'):
        os.makedirs('videos')
    elif download_type == 'a' and not os.path.exists('audios'):
        os.makedirs('audios')

    # Download the videos or audios from YouTube
    filename = ""
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)    
        filename = ydl.prepare_filename(info_dict)

    # Cleaning the title of the video or audio
    print('Renaming file ...')
    try:
        new_file_name = re.sub(r'[^\w\s\.]', '', filename)
        if download_type == 'v':
            os.rename(filename, 'videos/' + new_file_name)
        elif download_type == 'a':
            os.rename(filename, 'audios/' + new_file_name)
    except Exception as e:
        print('Error renaming the file {}: {}'.format(filename, e))
        return
    

if __name__ == "__main__":
    download_and_convert()
