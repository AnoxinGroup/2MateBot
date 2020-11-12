
from discord import Embed


class YoutubePlayEmbed(Embed):

    def __init__(self, audio_data):
        super().__init__(
            title=audio_data.title)

        self.set_thumbnail(
            url=audio_data.thumbnail)
