import youtube_dl

class VideoDownloader:

    def download(self, url, options):
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([url])