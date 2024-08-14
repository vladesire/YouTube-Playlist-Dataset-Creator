import yaml
from notion_api import NotionApi
from googleapiclient.discovery import build

with open('configuration.yaml', 'r') as configuration_file:
	configuration = yaml.safe_load(configuration_file)

CSV_HEADER = 'VideoTitle,ChannelTitle,PlaylistTitle,Category,Label,Language,VideoId,ChannelId,PlaylistId\n'
OUT_FILE = 'datasets/youtube-videos.csv'
YOUTUBE_API_KEY = configuration['youtube-token']
NOTION_API_KEY = configuration['notion-token']
NOTION_DATABASE_ID = configuration['notion-database-id']

youtube_api = build('youtube', 'v3', developerKey = YOUTUBE_API_KEY)
notion_api = NotionApi(NOTION_DATABASE_ID, NOTION_API_KEY)

playlists = notion_api.fetch_playlists()

with open(OUT_FILE, 'w') as out:
	out.write(CSV_HEADER)
	for i, playlist in enumerate(playlists):
		print(f'Loading [{i}]: {playlist.channel_title} -- {playlist.title}')
		playlist.load(youtube_api, out.write)