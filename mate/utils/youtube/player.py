
from .url import get_stream_url
from .search import search_video
from .data import load_youtube_data
from .embed import youtube_play_embed
from mate.utils.audio import play_audio


async def play_youtube_audio(ctx, voice_client, url, show_embed=True):
    video_data = load_youtube_data(url)

    if show_embed:
        await youtube_play_embed(
            ctx.channel,
            video_data.title,
            video_data.bigthumbhd,
            video_data.author,
            video_data.viewcount)

    play_audio(
        voice_client, get_stream_url(voice_client.channel.bitrate, video_data))


async def search_and_play(ctx, voice_client, url):
    video_found = search_video(url)

    if not video_found:
        raise Exception("Unable to find the video by this name")

    await play_youtube_audio(
        ctx, voice_client, video_found.id)
