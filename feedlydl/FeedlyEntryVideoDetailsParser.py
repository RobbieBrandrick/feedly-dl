from .VideoDetails import VideoDetails

class FeedlyEntryVideoDetailsParser:

    @staticmethod
    def parse(entries):

        details = []

        for entry in entries:

            if 'video' not in entry['originId']:
                continue

            author = entry["author"]
            title = entry["title"]
            url = entry['alternate'][0]["href"]
            entryId = entry['id']
            viewed = entry['unread']
            originId = entry['originId']
            videoDetails = VideoDetails(entryId, author, title, url, viewed, originId)

            details.append(videoDetails)

        return details