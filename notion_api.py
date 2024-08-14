import requests
from playlist import Playlist

def label_to_number(label):
    if label == 'Non-demanding':
        return 1
    elif label == 'Moderately demanding':
        return 2
    else: 
        return 3


class NotionApi:
    def __init__(self, database_id, token):
        self.database_id = database_id
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2022-06-28", 
            "Content-Type": "application/json"
        }

    def fetch_playlists(self) -> list[Playlist]:
        playlists = []

        has_more = True

        while has_more: 
            r = requests.post(
                url = f"https://api.notion.com/v1/databases/{self.database_id}/query",
                headers = self.headers,
                json = {"page_size": 100}
            )  

            if r.status_code == 200:
                response = r.json()
                pages = response['results']

                for page in pages: 
                    properties = page['properties']

                    channel_title = properties['channel']['rich_text'][0]['plain_text']
                    category = properties['category']['select']['name']
                    count = properties['count']['number']
                    label = label_to_number(properties['label']['select']['name'])
                    language = properties['language']['select']['name']
                    playlist_title = properties['name']['title'][0]['plain_text']
                    playlist_id = properties['id']['rich_text'][0]['plain_text']

                    playlists.append(Playlist(playlist_title, category, label, language, count, playlist_id, channel_title))

                has_more = response['has_more']

                if has_more: 
                    json['start_cursor'] = response['next_cursor']

            else:
                raise Exception(f"Something went wrong with Notion API: {r.json()}")

        return playlists