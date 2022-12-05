import td
from playlistextension import playlistextension


class playerextension:
    """
    playerextension description
    """
    def __init__(self, ownerComp: td.baseCOMP):
        # The component to which this extension is attached
        self.ownerComp: td.baseCOMP = ownerComp
        self.playlistComp: playlistextension = self.ownerComp.op('../playlist')

    def LoadPlaylist(self) -> None:
        self.playlistComp.Load()

    def PlayClip(self, index: int) -> None:
        self.playlistComp.Clips[index].play()
