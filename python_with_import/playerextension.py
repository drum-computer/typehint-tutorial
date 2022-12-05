import td
from playlistextension import playlistextension


class playerextension:
    """
    playerextension description
    """
    def __init__(self, ownerComp: td.baseCOMP):
        # The component to which this extension is attached
        self.ownerComp = ownerComp
        self.playlistComp: playlistextension = self.ownerComp.op('../playlist')

    def LoadPlaylist(self):
        self.playlistComp.Load()

    def PlayClip(self, index):
        self.playlistComp.Clips[index].play()
