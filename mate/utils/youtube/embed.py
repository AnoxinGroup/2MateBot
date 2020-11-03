
from mate.embeds.youtube import YoutubePlayEmbed


async def youtube_play_embed(
        channel, video_name, video_thumb, video_author, video_views):
    await channel.send(
        embed=YoutubePlayEmbed(
            video_name, video_thumb, video_author, video_views))
