import youtube_dl
import ffmpeg
def downloader():
    url=input('Enter youtube url: ')
    vid_info = youtube_dl.YoutubeDL().extract_info(url=url,download=False)
    fname = f"{vid_info['title']}.mp3"
    options= {'format':'bestaudio/best','keepvideo':False,'outtmpl':fname,'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]}
    
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([vid_info['webpage_url']])

    print('Download Complete')
    
if __name__=='__main__':
    downloader()


def downloaderUI(url):
    vid_info = youtube_dl.YoutubeDL().extract_info(url=url,download=False)
    fname = f"{vid_info['title']}.mp3"
    options= {'format':'bestaudio/best','keepvideo':False,'outtmpl':fname,'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]}
    
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([vid_info['webpage_url']])

    print('Download Complete')
