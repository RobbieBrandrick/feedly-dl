class FeedlyDlOptions:

    def __init__(self, options):
        self.token = options["token"]
        self.directory = options["directory"]
        self.category = options["category"]
        self.markDownloadedAsRead = options["markDownloadedAsRead"]
        self.onlyDownloadUnread = options["onlyDownloadUnread"]
        self.youtubedlOptions = options['youtubedlOptions']