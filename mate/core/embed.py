
from discord import (
    Embed as _Embed)
from mate.meta.embed import EmbedMeta


class Embed(_Embed):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_footer(
            text=EmbedMeta.EMBED_FOOTER,
            icon_url=EmbedMeta.EMBED_FOOTER_IMAGE)


__all__ = (
    "Embed",
)
