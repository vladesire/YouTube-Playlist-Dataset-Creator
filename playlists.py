class Playlist:
	def __init__(self, title, category, label, language, count, playlist_id, channel_title = ''):
		self.title = title
		self.category = category
		self.label = label
		self.language = language
		self.count = count
		self.playlist_id = playlist_id
		self.channel_title = channel_title

		# Channel title is for clarity only, as it is retrieved from API query.

playlists = [
	Playlist('Editor\'s Picks', 'discussion', 3, 'en', 156, 'PLsRNoUx8w3rOERmePNyC2hAONG9tL2ZYx', 'TEDx Talks'),
	Playlist('Shorts', 'discussion', 3, 'en', 387, 'PLu15HihogYiAebBvpC2NMa71LvOi--sBX', 'Robert Greene'),
	Playlist('Tutorials', 'programming', 3, 'en', 174, 'PLWKjhJtqVAbmDGFE_pZ-PDJ1GWe3KtT-M', 'freeCodeCamp.org'),
	Playlist('The Dr. Jordan B. Peterson Podcast', 'discussion', 2, 'en', 295, 'PL22J3VaeABQAbEeT04p5VmAOBmqw2kmxj', 'Jordan B Peterson'),
]
