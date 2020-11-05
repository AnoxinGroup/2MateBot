
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

        self.add_field(
            name=YoutubePlayMeta.AUTHOR_FIELD_NAME,
            value=video_author)

        self.add_field(
            name=YoutubePlayMeta.VIEWS_FIELD_NAME,
            value=video_views_count)

        self.set_thumbnail(
            url=video_thumb)

        self.set_author(
            name="Youtube",
            icon_url=YoutubePlayMeta.EMBED_AUTHOR_IMAGE)
