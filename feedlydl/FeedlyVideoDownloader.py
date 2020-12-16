import os 

from .VideoDownloader import VideoDownloader
from .Feedly import Feedly
from .FeedlyEntryVideoDetailsParser import FeedlyEntryVideoDetailsParser

class FeedlyVideoDownloader:

    def __init__(self, feedlyToken, videoDownloaderOptions, rootDirectory):
        self.videoDownloaderOptions = videoDownloaderOptions
        self.Downloader = VideoDownloader()
        self.Feedly = Feedly(feedlyToken)
        self.rootDirectory = rootDirectory

    def download_category(self, category):

        if os.path.isdir(self.rootDirectory) == False:
            os.mkdir(self.rootDirectory)

        entries = self.Feedly.get_entries(category)
        videos = FeedlyEntryVideoDetailsParser.parse(entries)
        
        for video in videos:

            if video.viewed == False:
                continue

            directory = self.rootDirectory +  "/" + video.author

            if os.path.isdir(directory) == False:
                os.mkdir(directory)

            fileLocation = directory + "/" + video.title + ".%(ext)s"

            self.videoDownloaderOptions["outtmpl"] = fileLocation
            self.Downloader.download(video.url, self.videoDownloaderOptions)
            self.Feedly.mark_entry_as_read(video.entryId)
    