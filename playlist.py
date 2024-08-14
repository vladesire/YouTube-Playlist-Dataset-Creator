class Playlist:
    def __init__(self, title, category, label, language, count, playlist_id, channel_title = ''):
        # Channel title is for clarity only, as it is retrieved from API query.
        self.title = title
        self.category = category
        self.label = label
        self.language = language
        self.count = count
        self.playlist_id = playlist_id
        self.channel_title = channel_title


    '''
        api is youtube api object
        on_video_loaded callback accepts a string with video data
    '''
    def load(self, api, on_video_loaded):
        next_page = ""

        while True:
            body = {
                'part': 'snippet',
                'playlistId': self.playlist_id,
                'maxResults': 50
            }

            if next_page != "":
                body['pageToken'] = next_page

            response = api.playlistItems().list(**body).execute()

            for item in response['items']:
                try:
                    snippet = item['snippet']
                    
                    video_title = snippet['title'].replace("\"", "\'")
                    video_id = snippet['resourceId']['videoId']
                    channel_title = snippet['videoOwnerChannelTitle'].replace("\"", "\'")
                    channel_id = snippet['videoOwnerChannelId']

                    on_video_loaded(f'"{video_title}","{channel_title}","{self.title}","{self.category}",{self.label},"{self.language}","{video_id}","{channel_id}","{self.playlist_id}"\n')

                except Exception as ex:
                    print(f'Error: {ex}')


            if 'nextPageToken' in response:
                next_page = response['nextPageToken']
            else:
                break