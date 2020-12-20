import os 

from .VideoDownloader import VideoDownloader
from .Feedly import Feedly
from .FeedlyEntryVideoDetailsParser import FeedlyEntryVideoDetailsParser
from .FeedlyDlOptions import FeedlyDlOptions

class FeedlyVideoDownloader:

    def __init__(self, options):
        self.Options = FeedlyDlOptions(options)
        self.Downloader = VideoDownloader()
        self.Feedly = Feedly(self.Options.token)        

    def download_category(self):

        if os.path.isdir(self.Options.directory) == False:
            os.mkdir(self.Options.directory)

        entries = self.Feedly.get_entries(self.Options.category)
        videos = FeedlyEntryVideoDetailsParser.parse(entries)
        
        for video in videos:

            if self.Options.onlyDownloadUnread == True:
                if video.viewed == False:\
                    continue

            directory = self.Options.directory + "/" + video.author

            if os.path.isdir(directory) == False:
                os.mkdir(directory)

            fileLocation = directory + "/" + video.title + ".%(ext)s"

            self.Options.youtubedlOptions["outtmpl"] = fileLocation
            self.Downloader.download(video.url, self.Options.youtubedlOptions)

            if self.Options.markDownloadedAsRead:
                self.Feedly.mark_entry_as_read(video.entryId)
    