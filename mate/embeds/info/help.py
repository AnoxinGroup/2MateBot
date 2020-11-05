
from mate.core.embed import Embed
from mate.meta.info import BotHelpMeta


class BotHelpEmbed(Embed):

    def __init__(self):
        super().__init__(
            title=BotHelpMeta.EMBED_TITLE,
            color=BotHelpMeta.EMBED_COLOR,
            description=BotHelpMeta.EMBED_DESC)

        self.set_thumbnail(
            url=BotHelpMeta.EMBED_THUMBNAIL)

        self.set_footer(
            text=BotHelpMeta.EMBED_FOOTER_NAME)
