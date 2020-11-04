
from mate.utils.embed import show_embed
from mate.embeds.youtube import YoutubePlayEmbed


async def youtube_play_embed(
        channel,
        video_name,
        video_thumb,
        video_author,
        video_views):

    return await show_embed(
        channel,
        YoutubePlayEmbed(
            video_name, video_thumb, video_author, video_views)
    )
