'''
파이썬의 pytube 기능에 대해서 프로그램을 통해 기능을 설명해 본다.
'''

from pytube import YouTube
import sys

def progress_func(stream, chunk, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    sys.stdout.write("\r[{}{}] ".format('=' * done, ' ' * (50-done)) )
    sys.stdout.flush()

ytv = YouTube("https://www.youtube.com/watch?v=_0Uifu9APfc", on_progress_callback=True )
ytv.register_on_progress_callback(progress_func)
print(ytv.title)
# ytv.streams.filter(file_extension='mp4')
# down = ytv.streams.get_audio_only(subtype='mp4')
# down.download('d:/')
'''
Youtube 의 동영상에는 여러종류의 파일이 존재하며, 이를 filtering 하는 기능을 제공 
'''
print(ytv.length.bit_length())
print(ytv.streams.filter(progressive=True))
print(ytv.streams.filter(adaptive=True))
print(ytv.streams.filter(only_audio=True))
print(ytv.streams.filter(file_extension='mp4'))
'''
Youtube 의 하나의 동영상에는 여러 동영상 및 파일 형식이 있으며 이는 itag 라는 id 로 구분되어있다.
Pytube 는 파일을 itag 별로 다운받을 수 있는 기능을 제공한다.
get_by_itag
'''

audio  = ytv.streams.get_by_itag(itag='18')
title = ytv.title
audio.download(output_path='d:/', filename= title+'.mp4', )


