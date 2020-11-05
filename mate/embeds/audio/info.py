
from mate.core.embed import Embed
from mate.meta.audio import AudioInfoMeta


class AudioInfoEmbed(Embed):

    def __init__(self):
        super().__init__(
            title=AudioInfoMeta.EMBED_TITLE,
            color=AudioInfoMeta.EMBED_COLOR,
            description=AudioInfoMeta.EMBED_DESC)

        self.set_thumbnail(
            url=AudioInfoMeta.EMBED_THUMBNAIL)

        self.set_footer(
            text=AudioInfoMeta.EMBED_FOOTER_NAME)
