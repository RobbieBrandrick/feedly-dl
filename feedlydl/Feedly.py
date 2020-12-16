from feedly.api_client.session import FeedlySession

class Feedly:

    def __init__(self, token):
        self.token = token

    def mark_entry_as_read(self, entryId):
        
        with FeedlySession(self.token) as sess:

            request =  {
                "action": "markAsRead",
                "type": "entries",
                "entryIds": [
                entryId
                ]
            }

            sess.do_api_request('/v3/markers', data=request)

    def get_entries(self, category):
    
        entries = []

        with FeedlySession(self.token) as sess:
            for entry in sess.user.get_category(category).stream_contents():

                entries.append(entry.json)
        
        return entries