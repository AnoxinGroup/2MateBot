
from mate.core.embed import Embed
from mate.meta.info import BotInfoMeta


class BotInfoEmbed(Embed):

    def __init__(self):
        super().__init__(
            title=BotInfoMeta.EMBED_TITLE,
            color=BotInfoMeta.EMBED_COLOR,
            description=BotInfoMeta.EMBED_DESC)
