
from mate.core.embed import Embed
from mate.meta.info import BotTextMeta


class BotTextEmbed(Embed):

    def __init__(self):
        super().__init__(
            title=BotTextMeta.EMBED_TITLE,
            color=BotTextMeta.EMBED_COLOR,
            description=BotTextMeta.EMBED_DESC)

        self.set_thumbnail(
            url=BotTextMeta.EMBED_THUMBNAIL)

        self.set_footer(
            text=BotTextMeta.EMBED_FOOTER_NAME)
