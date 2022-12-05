import td


class clip:
	def play(self) -> None:
		print("clip playback started")


class playlistextension:
	"""
	playlistextension description
	"""
	def __init__(self, ownerComp: td.baseCOMP):
		# The component to which this extension is attached
		self.ownerComp: td.baseCOMP = ownerComp
		self.clips: list[clip] = [clip() for _ in range(10)]
		self.name: str = 'Playlist 1'

	def Load(self) -> None:
		print(f"Playlist {self.name} loaded")

	@property
	def Clips(self) -> list[clip]:
		return self.clips
    
    
		