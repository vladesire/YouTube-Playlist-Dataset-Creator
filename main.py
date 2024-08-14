from googleapiclient.discovery import build
from playlists import playlists

with open('.token', 'r') as token_file:
	API_KEY = token_file.read()

OUT_FILE = 'datasets/youtube-videos.csv'

youtube = build('youtube', 'v3', developerKey = API_KEY)

'''
	on_video_loaded callback accepts a string with video data
'''
def playlist_loader(
	playlist_title: str, 
	playlist_id: str, 
	language: str,
	category: str, 
	label: int,
	on_video_loaded
):
	next_page = ""

	while True:
		body = {
			'part': 'snippet',
			'playlistId': playlist_id,
			'maxResults': 50
		}

		if next_page != "":
			body['pageToken'] = next_page

		response = youtube.playlistItems().list(**body).execute()

		for item in response['items']:
			try:
				snippet = item['snippet']

				video_title = snippet['title'].replace("\"", "\'")
				video_id = snippet['resourceId']['videoId']
				channel_title = snippet['videoOwnerChannelTitle'].replace("\"", "\'")
				channel_id = snippet['videoOwnerChannelId']

				on_video_loaded(f'"{video_title}","{channel_title}","{playlist_title}","{category}",{label},"{language}","{video_id}","{channel_id}","{playlist_id}"\n')

			except Exception as ex:
				print(f'Error: {ex}')


		if 'nextPageToken' in response:
			next_page = response['nextPageToken']
		else:
			break


with open(OUT_FILE, 'w') as out:
	out.write('VideoTitle,ChannelTitle,PlaylistTitle,Category,Label,Language,VideoId,ChannelId,PlaylistId\n')

	for i, playlist in enumerate(playlists):
		print(f'Loading [{i}]: {playlist.channel_title} -- {playlist.title}')
		playlist_loader(playlist.title, playlist.playlist_id, playlist.language, playlist.category, playlist.label, out.write)