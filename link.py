from youtube import youtube_search
import youtube_dl

def lookSong(name):
    id = youtube_search(name)
    ydl_opts = {'format': '140'}
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
         result = ydl.extract_info('https://www.youtube.com/watch?v=X2oPI688EQM', download=False)
    
    x = result['url'],result['duration']
    print x[0], x[1]    
    
