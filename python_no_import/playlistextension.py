class clip:
	def play(self):
		print("clip playback started")


class playlistextension:
	"""
	playlistextension description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.clips = [clip() for _ in range(10)]
		self.name = 'Playlist 1'

	def Load(self):
		print(f"Playlist {self.name} loaded")

	@property
	def Clips(self):
		return self.clips
		
