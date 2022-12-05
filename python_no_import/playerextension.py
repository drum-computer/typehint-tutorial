class playerextension:
	"""
	playerextension description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.playlistComp = op('../playlist')

	def LoadPlaylist(self):
		self.playlistComp.Load()

	def PlayClip(self, index):
		self.playlistComp.Clips[index].play()
