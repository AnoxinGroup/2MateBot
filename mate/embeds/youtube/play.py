
from mate.core.embed import Embed
from mate.meta.youtube import YoutubePlayMeta


class YoutubePlayEmbed(Embed):

    def __init__(
            self,
            video_name,
            video_thumb,
            video_author,
            video_views_count):

        super().__init__(
            title=video_name,
            color=YoutubePlayMeta.COLOR
        )

        self.set_thumbnail(
            url=video_thumb)

        self.set_footer(
            text=YoutubePlayMeta.EMBED_FOOTER_TEXT,
            icon_url=YoutubePlayMeta.EMBED_FOOTER_IMAGE)
