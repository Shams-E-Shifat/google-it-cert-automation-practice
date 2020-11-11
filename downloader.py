import youtube_dl
import sys
import os



ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'webm',
        'preferredquality': '392',
    }],
}


if __name__ == "__main__":
    try:
	    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	        filenames = sys.argv[1:]
	        ydl.download(filenames)

    except:
    	filename = filenames[0]
    	filename = filename[filename.find("?")+3 : ]
    	file = [x for x in os.listdir() if filename in x][0]

    	os.rename(file, file.replace('.webm','.mp3').replace('-'+filename,''))
