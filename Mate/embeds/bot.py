
from Mate.meta import BotEmbedMeta

from Mate.core.embed import Embed


class BotEmbed(Embed):

    def __init__(self):
        super(BotEmbed, self).__init__(
            title=BotEmbedMeta.TITLE,
            color=BotEmbedMeta.COLOR,
            description=BotEmbedMeta.DESC)
