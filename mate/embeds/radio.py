
from discord import Embed


class RadioPlayEmbed(Embed):

    def __init__(self, radio_data):
        super().__init__(
            title=radio_data.title)

        self.set_thumbnail(
            url=radio_data.thumbnail)
